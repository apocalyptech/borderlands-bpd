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

import sys
import argparse
from ftexplorer.data import Data

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
bpd_name = args.bpd.lower()

data = Data(game)
cold_followed = set()

def compliment(number):
    """
    Returns a two's-compliment tuple for the given number.
    """
    number = int(number)
    one = (number >> 16)
    two = (number & 0xFF)
    return (one, two)

def follow(link, cold_data, behavior_data, coming_from, seq_idx):
    """
    Follows the given `link` (being a two's-compliment number of the sort
    found in BPDs) through the given `behavior_data`, using `cold_data`
    as the glue.  `coming_from` is the source which we've been linked
    from.  `seq_idx` is our current BPD index
    """
    global cold_followed
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
            print('  {} [label=<BROKEN>,style=filled,fillcolor=red];'.format(broken_id))
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
            )

def get_var_list(number):
    global cvld_data
    global clv_data
    global variable_data
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

def get_var_extra(number):
    var_list = get_var_list(number)
    if len(var_list) > 0:
        return '<br/>{}'.format('<br/>'.join(var_list))
    else:
        return ''

node = data.get_node_by_full_object(bpd_name)
if not node:
    sys.exit(1)

bpd = node.get_structure()
print('digraph bpd {')
print('')
print('  labelloc = "t";')
print('  fontsize = 25;')
print('  label = <{}>;'.format(args.bpd))
print('  node [shape=box,style=rounded];')
print('')

print('  {')
print('    node [style=filled,fillcolor=chartreuse2];')
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

            var_extra = get_var_extra(event['OutputVariables']['ArrayIndexAndLength'])

            print('    event_{}_{} [label=<[{}]{}.{}{}>];'.format(
                seq_idx,
                event_idx,
                seq_idx,
                seq_name.strip('"'),
                event['UserData']['EventName'].strip('"'),
                var_extra,
                ))

    print('')

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

    for (behavior_idx, behavior) in enumerate(behavior_data):
        if behavior['Behavior'] != 'None':
            (behavior_type, behavior_class, junk) = behavior['Behavior'].split("'", 2)
            if behavior_class.lower().startswith(bpd_name.lower()):
                behavior_class = behavior_class[len(bpd_name)+1:]
        else:
            behavior_type = ''
            behavior_class = 'None'

        var_extra = get_var_extra(behavior['LinkedVariables']['ArrayIndexAndLength'])

        print('  behavior_{}_{} [label=<[{}] {}{}>];'.format(
            seq_idx,
            behavior_idx,
            behavior_idx,
            behavior_class,
            var_extra,
            ))
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
                    seq_idx)

    print('')

print('')
print('}')
