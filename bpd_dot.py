#!/usr/bin/env python36
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright (c) 2018, CJ Kucera
# All rights reserved.
#   
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the development team nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL CJ KUCERA BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
import sys
import argparse
from ftexplorer.data import Data

broken_cold_fill = 'red'
event_fill = 'chartreuse2'
event_link_color = 'chartreuse2'

invalid_event_shape = 'ellipse'
invalid_event_fill = 'red'

remote_event_shape = 'ellipse'
remote_event_fill = 'gold1'

def compliment(number):
    """
    Returns a two's-compliment tuple for the given number.
    """
    number = int(number)
    one = (number >> 16)
    two = (number & 0xFF)
    return (one, two)

def follow(link, cold_data, behavior_data, coming_from, seq_idx, cold_followed):
    """
    Follows the given `link` (being a two's-compliment number of the sort
    found in BPDs) through the given `behavior_data`, using `cold_data`
    as the glue.  `coming_from` is the source which we've been linked
    from.  `seq_idx` is our current BPD index
    """
    (link_index, link_length) = compliment(link)
    for (cold_order_idx, cold_index) in enumerate(range(link_index, link_index+link_length)):
        full_cold_index = '{}_{}'.format(seq_idx, cold_index)
        if full_cold_index in cold_followed:
            continue
        else:
            cold_followed.add(full_cold_index)
        try:
            cold = cold_data[cold_index]
        except IndexError:
            broken_id = 'broken_{}_{}'.format(seq_idx, cold_order_idx)
            print('  {} [label=<BROKEN>,style=filled,fillcolor={}];'.format(broken_id, broken_cold_fill))
            print('  {} -> {}'.format(coming_from, broken_id))
            return
        (link_id, bindex) = compliment(cold['LinkIdAndLinkedBehavior'])
        behavior = behavior_data[bindex]
        going_to = 'behavior_{}_{}'.format(seq_idx, bindex)
        delay = round(float(cold['ActivateDelay']), 6)
        if delay == 0:
            delay_extra = ''
        else:
            if int(delay) == delay:
                delay = round(delay)
            delay_extra = '<br/>d{}'.format(delay)
        print('  {} -> {} [taillabel=<{}<br/>[{}]{}>];'.format(coming_from, going_to, cold_order_idx, cold_index, delay_extra))
        follow(behavior['OutputLinks']['ArrayIndexAndLength'],
            cold_data,
            behavior_data,
            going_to,
            seq_idx,
            cold_followed,
            )

def get_var_list(number, cvld_data, clv_data, variable_data):
    (var_index, var_len) = compliment(number)
    var_list = []
    for cvld_idx in range(var_index, var_index+var_len):
        cvld = cvld_data[cvld_idx]
        var_name = cvld['PropertyName']
        var_type_full = cvld['VariableLinkType']
        (link_index, link_len) = compliment(cvld['LinkedVariables']['ArrayIndexAndLength'])
        # This is stupid because our ft-explorer parsing is stupid.  Doesn't really
        # handle lists of numbers too well.  We'll just pretend.
        clv_data_real = [int(p) for p in clv_data.split(',')]

        for link_index_iter in range(link_index, link_index+link_len):

            finalvar_idx = clv_data_real[link_index_iter]
            finalvar = variable_data[finalvar_idx]
            if finalvar['Name'] == '':
                finalvar_name = ''
            else:
                finalvar_name = finalvar['Name']
            if finalvar['Type'].startswith('BVAR_'):
                finalvar_type = finalvar['Type'][5:].lower()
            else:
                raise Exception('Unknown variable type: {}'.format(finalvar['Type']))

            finalvar_desc = '[{}]{}({}) via [{}]{}, [{}]'.format(
                    finalvar_idx,
                    finalvar_name.strip('"'),
                    finalvar_type,
                    cvld_idx,
                    var_name.strip('"'),
                    link_index_iter,
                    )

            if var_type_full == 'BVARLINK_Input':
                var_list.append('In: {}'.format(finalvar_desc))
            elif var_type_full == 'BVARLINK_Output':
                var_list.append('Out: {}'.format(finalvar_desc))
            elif var_type_full == 'BVARLINK_Context':
                var_list.append('Ctx: {}'.format(finalvar_desc))
            else:
                raise Exception('Unknown var type: {}'.format(var_type_full))

    return var_list

def get_var_extra(number, cvld_data, clv_data, variable_data):
    var_list = get_var_list(number, cvld_data, clv_data, variable_data)
    if len(var_list) > 0:
        return '<br/>{}'.format('<br/>'.join(var_list))
    else:
        return ''

def get_rce_bpd(rce):
    """
    Gets the BPD pointed-to by the given RemoteCustomEvent
    """
    string_build = []
    # This is actually a bit weird 'cause the output of these vars uses
    # bracket-based indexes, as if they were top-level vars, but they're
    # not.  So we're doing some special processing on 'em
    pcns = {}
    for (name, value) in rce['ProviderDefinitionPathName'].items():
        if value and value != '':
            if name.startswith('PathComponentNames['):
                pcns[int(name[19:-1])] = value.strip('"')
    for index in sorted(pcns.keys()):
        element = pcns[index]
        if len(string_build) == 0:
            string_build.append(element)
        elif (element.startswith('AIBehaviorProviderDefinition_') or 
                element.startswith('BehaviorProviderDefinition_')):
            string_build.append(':{}'.format(element))
        else:
            string_build.append('.{}'.format(element))
    return ''.join(string_build)

def generate_dot(node, bpd_name):
    """
    Outputs a graphviz dot file from the given node
    """
    bpd_name_lower = bpd_name.lower()
    bpd = node.get_structure()
    cold_followed = set()
    event_map = {}
    print('digraph bpd {')
    print('')
    print('  labelloc = "t";')
    print('  fontsize = 25;')
    print('  label = <{}>;'.format(bpd_name))
    print('  node [shape=box,style=rounded];')
    print('')

    print('  {')
    print('    node [style=filled,fillcolor={}];'.format(event_fill))
    for (seq_idx, seq) in enumerate(bpd['BehaviorSequences']):

        seq_name = seq['BehaviorSequenceName']
        event_data = seq['EventData2']
        behavior_data = seq['BehaviorData2']
        variable_data = seq['VariableData']
        cold_data = seq['ConsolidatedOutputLinkData']
        cvld_data = seq['ConsolidatedVariableLinkData']
        clv_data = seq['ConsolidatedLinkedVariables']

        for (event_idx, event) in enumerate(event_data):
            if event['UserData']['bEnabled'] == 'True':

                var_extra = get_var_extra(event['OutputVariables']['ArrayIndexAndLength'], cvld_data, clv_data, variable_data)
                event_name = event['UserData']['EventName'].strip('"')
                event_name_lower = event_name.lower()
                event_id = 'event_{}_{}'.format(seq_idx, event_idx)
                if event_name_lower not in event_map:
                    event_map[event_name_lower] = []
                event_map[event_name_lower].append(event_id)

                print('    {} [label=<[{}]{}.{}[{}]{}>];'.format(
                    event_id,
                    seq_idx,
                    seq_name.strip('"'),
                    event_name,
                    event_idx,
                    var_extra,
                    ))

        print('')

    print('  }')
    print('')

    event_links = []
    invalid_events = []
    remote_events = []
    for (seq_idx, seq) in enumerate(bpd['BehaviorSequences']):

        seq_name = seq['BehaviorSequenceName']
        event_data = seq['EventData2']
        behavior_data = seq['BehaviorData2']
        variable_data = seq['VariableData']
        cold_data = seq['ConsolidatedOutputLinkData']
        cvld_data = seq['ConsolidatedVariableLinkData']
        clv_data = seq['ConsolidatedLinkedVariables']

        for (behavior_idx, behavior) in enumerate(behavior_data):
            if behavior['Behavior'] != 'None':
                (behavior_type, full_behavior_class, junk) = behavior['Behavior'].split("'", 2)
                if full_behavior_class.lower().startswith(bpd_name_lower):
                    behavior_class = full_behavior_class[len(bpd_name_lower)+1:]
                else:
                    behavior_class = full_behavior_class
            else:
                behavior_type = ''
                behavior_class = 'None'
                full_behavior_class = 'None'

            var_extra = get_var_extra(behavior['LinkedVariables']['ArrayIndexAndLength'], cvld_data, clv_data, variable_data)
            behavior_id = 'behavior_{}_{}'.format(seq_idx, behavior_idx)

            print('  {} [label=<[{}] {}{}>];'.format(
                behavior_id,
                behavior_idx,
                behavior_class,
                var_extra,
                ))

            # We can draw some more links if we're a remotecustomevent
            if behavior_type == 'Behavior_RemoteCustomEvent':
                rce = data.get_struct_by_full_object(full_behavior_class)
                if rce:
                    rce_bpd = get_rce_bpd(rce)
                    event_name = rce['CustomEventName']
                    if rce_bpd.lower() == bpd_name_lower:
                        if event_name.lower() in event_map:
                            for event_id in event_map[event_name.lower()]:
                                event_links.append((behavior_id, event_id))
                        else:
                            invalid_event_name_id = 'invalid_event_{}'.format(len(invalid_events))
                            invalid_events.append((invalid_event_name_id, event_name))
                            event_links.append((behavior_id, invalid_event_name_id))
                    else:
                        really_remote_id = 'really_remote_id_{}'.format(len(remote_events))
                        remote_events.append((really_remote_id, rce_bpd, event_name))
                        event_links.append((behavior_id, really_remote_id))

        print('')

    if len(invalid_events) > 0:
        print('  {')
        print('    node [style=filled,fillcolor={},shape={}];'.format(invalid_event_fill, invalid_event_shape))
        for (node_id, event_name) in invalid_events:
            print('    {} [label=<{} (invalid)>];'.format(node_id, event_name))
        print('  }')
        print('')

    if len(remote_events) > 0:
        print('  {')
        print('    node [style=filled,fillcolor={},shape={}];'.format(remote_event_fill, remote_event_shape))
        for (node_id, remote_bpd, event_name) in remote_events:
            if ':' in remote_bpd:
                (first, second) = remote_bpd.split(':', 2)
                print('    {} [label=<{}:<br/>{}<br/>{}>];'.format(node_id, first, second, event_name))
            else:
                print('    {} [label=<{}<br/>{}>];'.format(node_id, remote_bpd, event_name))
        print('  }')
        print('')

    if len(event_links) > 0:
        print('  {')
        print('    edge [color={}];'.format(event_link_color))
        for (link_from, link_to) in event_links:
            print('    {} -> {};'.format(link_from, link_to))
        print('  }')
        print('')

    for (seq_idx, seq) in enumerate(bpd['BehaviorSequences']):

        seq_name = seq['BehaviorSequenceName']
        event_data = seq['EventData2']
        behavior_data = seq['BehaviorData2']
        variable_data = seq['VariableData']
        cold_data = seq['ConsolidatedOutputLinkData']
        cvld_data = seq['ConsolidatedVariableLinkData']
        clv_data = seq['ConsolidatedLinkedVariables']

        for (event_idx, event) in enumerate(event_data):
            if event['UserData']['bEnabled'] == 'True':
                follow(event['OutputLinks']['ArrayIndexAndLength'],
                        cold_data,
                        behavior_data,
                        'event_{}_{}'.format(seq_idx, event_idx),
                        seq_idx,
                        cold_followed)

        print('')

    print('')
    print('}')

if __name__ == '__main__':

    if 'generate_all_dots' in sys.argv[0]:

        dotdir = 'dotfiles'

        if not os.path.exists(dotdir) and not os.path.isdir(dotdir):
            print('ERROR: "{}" directory must exist, closing.'.format(dotdir))
            sys.exit(1)

        print('About to generate dotfiles for ALL BPDs in both BL2 and TPS.')
        print('Ctrl-C now if that\'s not what you want.')
        print('')
        print('(Hit a key to continue)')
        sys.stdin.readline()

        generated = 0
        for game in ['BL2', 'TPS']:

            data = Data(game)

            objects = []
            objects.extend(data.get_all_by_type('AIBehaviorProviderDefinition'))
            objects.extend(data.get_all_by_type('BehaviorProviderDefinition'))

            max_len_seen = 0
            for bpd_name in sorted(objects):
                with open('{}/{}_{}.dot'.format(dotdir, game, bpd_name), 'w') as df:

                    # Redirect stdout.  This is hokey, but whatever.
                    sys.stdout = df

                    # Figure out out string to report to the user
                    report_str = 'Processing {} {}'.format(game, bpd_name)
                    if len(report_str) > 120:
                        report_str = '{}...'.format(report_str[:117])
                    if len(report_str) > max_len_seen:
                        max_len_seen = len(report_str)
                        spaces = ''
                    else:
                        spaces = ' '*(max_len_seen-len(report_str))
                    sys.stderr.write("{}{}\r".format(report_str, spaces))

                    # Load the node, complaining if we couldn't find it
                    node = data.get_node_by_full_object(bpd_name)
                    if not node:
                        print('', file=sys.stderr)
                        print('ERROR: {} {} not found'.format(game, bpd_name), file=sys.stderr)

                    # aaaand generate.
                    try:
                        generate_dot(node, bpd_name)
                        generated += 1
                    except Exception as e:
                        print('', file=sys.stderr)
                        raise e

        print('', file=sys.stderr)
        print('', file=sys.stderr)
        print('{} dotfiles generated'.format(generated), file=sys.stderr)

    else:

        parser = argparse.ArgumentParser(
            description='Generate a graphviz DOT file showing a borderlands BPD',
            )

        parser.add_argument('game',
            choices=['bl2', 'tps'],
            help='Which game to search',
            )

        parser.add_argument('bpd',
            help='BPD to output',
            )

        args = parser.parse_args()

        game = args.game.upper()
        bpd_name = args.bpd

        data = Data(game)

        node = data.get_node_by_full_object(bpd_name)
        if not node:
            sys.exit(1)

        generate_dot(node, bpd_name)
