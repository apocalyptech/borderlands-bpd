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
from level_sequence_event_names import level_sequence_event_names

###
### Color/shape information
###

style_default = 'shape=box style=rounded'
style_broken_cold = 'style=filled fillcolor=red'
style_event = 'style=filled fillcolor=chartreuse2'
style_event_edge = 'color=chartreuse2'
style_event_invalid = 'style=filled fillcolor=lightpink2 shape=cds margin=0.15'
style_event_remote = 'style=filled fillcolor=gold1 shape=cds margin=0.15'
style_seq_event = 'style=filled fillcolor=deepskyblue1'
style_event_unknown = 'style=filled fillcolor=deepskyblue1'
style_seq_event_edge = 'color=deepskyblue1'

###
### Class for dealing with kismet-style sequence objects.
###

class KismetNode(object):
    """
    A single Kismet sequence object
    """

    def __init__(self, name, node_id, data, prev_node):
        self.name = name
        self.node_id = node_id
        (self.base_class, self.short_name) = name.rsplit('.', 1)
        if prev_node:
            if self.base_class == prev_node.base_class:
                self.change_point = False
            else:
                self.change_point = True
        else:
            self.change_point = True
        self.struct = data.get_struct_by_full_object(name)
        if 'EventName' in self.struct:
            self.event_name = self.struct['EventName']
        else:
            self.event_name = None
        self.behaviors = None
        self.behavior_type_report = None
        if 'Behaviors' in self.struct:
            self.behaviors = []
            behavior_types = []
            for behavior_full in self.struct['Behaviors']:
                if behavior_full and behavior_full != '':
                    (behavior_type, behavior_name, junk2) = behavior_full.split("'")
                    self.behaviors.append(behavior_name)
                    behavior_types.append(behavior_type)
            if len(behavior_types) == 1:
                self.behavior_type_report = behavior_types[0]
            elif len(behavior_types) > 1:
                self.behavior_type_report = '{} +{} more'.format(
                        behavior_types[0],
                        len(behavior_types)-1,
                        )

            # TODO: Read in the behavior data as well
            for (btype, bname) in zip(behavior_types, self.behaviors):
                if btype == 'Behavior_RemoteCustomEvent':
                    pass
                elif btype == 'Behavior_RemoteEvent' or btype == 'Behavior_CustomEvent':
                    pass
        
        # Read out output links (this is our primary treeing method)
        self.output_names = []
        if 'OutputLinks' in self.struct and self.struct['OutputLinks'] != '':
            for outputlink in self.struct['OutputLinks']:
                if 'Links' in outputlink and outputlink['Links'] != '':
                    for link in outputlink['Links']:
                        self.output_names.append(Data.get_struct_attr_obj(link, 'LinkedOp'))

        # Read in variables (not doing anything with this yet, but will
        # hopefully be reporting on them)
        self.variable_names = []
        if 'VariableLinks' in self.struct and self.struct['VariableLinks'] != '':
            for variablelink in self.struct['VariableLinks']:
                if 'LinkedVariables' in variablelink and variablelink['LinkedVariables'] != '':
                    linkvars = variablelink['LinkedVariables']
                    # This processing is due to our data library being a bit stupid about
                    # lists of things.  Have to split on the comma ourselves here.
                    for var in linkvars.split(','):
                        (junk, var_name, junk2) = var.split("'")
                        self.variable_names.append(var_name)

        # Read in any events which get triggered.  This seems reasonably rare.
        # TODO: Not sure exactly what happens here; does it just branch off?
        self.event_names = []
        if 'EventLinks' in self.struct and self.struct['EventLinks'] != '':
            for eventlink in self.struct['EventLinks']:
                if 'LinkedEvents' in eventlink and eventlink['LinkedEvents'] != '':
                    linkevents = eventlink['LinkedEvents']
                    # This processing is due to our data library being a bit stupid about
                    # lists of things.  Have to split on the comma ourselves here.
                    for var in linkevents.split(','):
                        (junk, var_name, junk2) = var.split("'")
                        self.event_names.append(var_name)

    def get_label(self):
        label_list = []
        if self.change_point:
            label_list.append('{}.'.format(self.base_class))
        label_list.append(self.short_name)
        if self.event_name:
            label_list.append('Event "{}"'.format(self.event_name))
        if self.behavior_type_report:
            label_list.append('({})'.format(self.behavior_type_report))
        # TODO: put in variables, etc, here?
        return '<br/>'.join(label_list)

    def get_style(self):
        global style_seq_event
        if self.event_name:
            return '{} '.format(style_seq_event)
        else:
            return ''

class Kismets(object):
    """
    It's a bit stupid that these have their own class where nothing else in
    here does, but that's a side-effect of having this stuff tacked on later,
    when the rest was just procedural
    """

    def __init__(self, data, seq_event_map={}, from_bpd=None,
            follow_to_new_base=False):
        self.data = data
        self.seq_event_map = seq_event_map
        self.from_bpd = from_bpd
        self.follow_to_new_base = follow_to_new_base
        self.entry_points = []
        self.nodes = {}
        self.links = []

    def add_entry(self, from_id, to_name):
        self.entry_points.append((from_id, to_name))

    def follow_entries(self):
        global style_seq_event_edge
        for (idx, (from_id, entry_name)) in enumerate(self.entry_points):
            node = self.follow(entry_name, None, idx)
            if node.event_name:
                style = style_seq_event_edge
            else:
                style = None
            self.links.append((from_id, node.node_id, style, idx))

    def start_path(self, node_name):
        self.follow(node_name, None, 0)

    def follow(self, node_name, prev_node, output_idx):
        global style_seq_event_edge
        if node_name not in self.nodes:
            node = KismetNode(node_name,
                    'kismet_node_{}'.format(len(self.nodes)),
                    self.data, prev_node)
            self.nodes[node_name] = node
            if not prev_node or not node.change_point or self.follow_to_new_base:
                for (idx, output) in enumerate(node.output_names):
                    self.follow(output, node, idx)
        if prev_node:
            if self.nodes[node_name].event_name:
                style = style_seq_event_edge
            else:
                style = None
            self.links.append((prev_node.node_id, self.nodes[node_name].node_id, style, output_idx))
        return self.nodes[node_name]

    def get_nodes(self):
        return self.nodes.values()

    def get_links(self):
        return self.links

###
### Functions
###

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
            print('  {} [label=<BROKEN> {}];'.format(broken_id, style_broken_cold))
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

def generate_dot(node, bpd_name, seq_event_map):
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
    print('  node [{}];'.format(style_default))
    print('')

    # First bit of processing is just if we've been handed a
    # BPD.  This used to be our only mode!  Now we support Kismet
    # stuff, too, though.
    if 'behaviorproviderdefinition' in bpd_name_lower:

        is_bpd = True

        print('  {')
        print('    node [{}];'.format(style_event))
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
        seq_events = []
        unknown_events = []
        seq_event_links = []
        kismets = Kismets(data, seq_event_map=seq_event_map, from_bpd=bpd_name)
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

                # Handle CustomEvents and RemoteEvents.  Functionally these appear to be nearly
                # identical, as far as BL2+TPS's datasets are concerned.  RemoteEvents in our
                # datasets seem to only ever link to seqvar event names, and don't seem to ever
                # link back to BPD event names, whereas CustomEvents can.  Contrariwise,
                # CustomEvents nearly always seem to link to the same BPD or to other BPDs, and
                # rarely to seqvar event names (though it does seem to do that sometimes).
                # Ayway, we may as well just check for both.  Note that currently we don't
                # handle linking to remote BPDs, but if we have a level specified, we may be
                # able to follow into seqvar events.
                elif behavior_type == 'Behavior_CustomEvent' or behavior_type=='Behavior_RemoteEvent':
                    if behavior_type == 'Behavior_CustomEvent':
                        attr_name = 'CustomEventName'
                    else:
                        attr_name = 'EventName'
                    rce = data.get_struct_by_full_object(full_behavior_class)
                    if rce:
                        event_name = rce[attr_name]
                        event_name_lower = event_name.lower()
                        got_a_link = False
                        # First check for any links within the same BPD
                        if event_name_lower in event_map:
                            got_a_link = True
                            for event_id in event_map[event_name_lower]:
                                event_links.append((behavior_id, event_id))
                        # Now for any links outside (will probably never happen)
                        if event_name_lower in seq_event_map:
                            got_a_link = True
                            for seq_obj in seq_event_map[event_name_lower]:
                                #seq_id = 'seq_id_{}'.format(len(seq_events))
                                #seq_events.append((seq_id, seq_obj))
                                #seq_event_links.append((behavior_id, seq_id))
                                kismets.add_entry(behavior_id, seq_obj)
                        # If we haven't found any links, put the event name out there,
                        # at least.
                        if not got_a_link:
                            unknown_event_id = 'unknown_event_id_{}'.format(len(unknown_events))
                            unknown_events.append((unknown_event_id, event_name))
                            seq_event_links.append((behavior_id, unknown_event_id))

            print('')

        # Loop through Kismet sequence data, if we've colleceted any
        kismets.follow_entries()

        if len(invalid_events) > 0:
            print('  {')
            print('    node [{}];'.format(style_event_invalid))
            for (node_id, event_name) in invalid_events:
                print('    {} [label=<{}<br/>(possibly invalid?)>];'.format(node_id, event_name))
            print('  }')
            print('')

        if len(remote_events) > 0:
            print('  {')
            print('    node [{}];'.format(style_event_remote))
            for (node_id, remote_bpd, event_name) in remote_events:
                if ':' in remote_bpd:
                    (first, second) = remote_bpd.split(':', 2)
                    print('    {} [label=<{}:<br/>{}<br/>{}>];'.format(node_id, first, second, event_name))
                else:
                    print('    {} [label=<{}<br/>{}>];'.format(node_id, remote_bpd, event_name))
            print('  }')
            print('')

        if len(unknown_events) > 0:
            print('  {')
            print('    node [{}];'.format(style_event_unknown))
            for (node_id, event_name) in unknown_events:
                if len(seq_event_map) == 0:
                    extra_label = ',<br/>or to an unknown SeqEvent'
                else:
                    extra_label = ''
                print('    {} [label=<{}<br/><i>(Unknown Event,<br/>may call to other BPD{})</i>>];'.format(node_id, event_name, extra_label))
            print('  }')
            print('')

        if len(event_links) > 0:
            print('  {')
            print('    edge [{}];'.format(style_event_edge))
            for (link_from, link_to) in event_links:
                print('    {} -> {};'.format(link_from, link_to))
            print('  }')
            print('')

        if len(seq_event_links) > 0:
            print('  {')
            print('    edge [{}];'.format(style_seq_event_edge))
            for (link_from, link_to) in seq_event_links:
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

    else:

        # Here's our branch if we're just doing a Kismet tree
        is_bpd = False

        kismets = Kismets(data, seq_event_map=seq_event_map)
        kismets.start_path(bpd_name)

    # Kismet stuff gets rendered regardless, since BPDs will be able to
    # recurse into them.

    kismet_nodes = kismets.get_nodes()
    if len(kismet_nodes) > 0:
        for node in kismet_nodes:
            print('  {} [{}label=<{}>];'.format(node.node_id, node.get_style(), node.get_label()))
        print('')

    kismet_links = kismets.get_links()
    if len(kismet_links) > 0:
        for (link_from, link_to, link_style, link_tail) in kismet_links:
            if link_style:
                edge_style = '{} '.format(link_style)
            else:
                edge_style = ''
            print('  {} -> {} [{}taillabel=<{}>];'.format(link_from, link_to, edge_style, link_tail))
        print('')

    print('')
    print('}')

###
### Now process to find out what we're supposed to do
###

if __name__ == '__main__':

    if 'generate_all_dots' in sys.argv[0]:

        ###
        ### Generate all possible graphviz dot files (really only used for
        ### my own debugging)
        ###

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
                        generate_dot(node, bpd_name, {})
                        generated += 1
                    except Exception as e:
                        print('', file=sys.stderr)
                        raise e

        print('', file=sys.stderr)
        print('', file=sys.stderr)
        print('{} dotfiles generated'.format(generated), file=sys.stderr)

    else:

        ###
        ### Main application - generate a single graphviz dot file, to STDOUT.
        ###

        parser = argparse.ArgumentParser(
            description='Generate a graphviz DOT file showing a borderlands BPD',
            )

        parser.add_argument('-l', '--level',
            required=False,
            help="Optional level in which the BPD is running, to link in sequence data too",
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

        seq_event_map = {}
        if args.level and args.level != '':
            if args.level.lower() not in level_sequence_event_names[game]:
                raise argparse.ArgumentTypeError('Level name {} not found in {}'.format(args.level, game))
            seq_event_map = level_sequence_event_names[game][args.level.lower()]

        data = Data(game)

        node = data.get_node_by_full_object(bpd_name)
        if not node:
            sys.exit(1)

        generate_dot(node, bpd_name, seq_event_map)
