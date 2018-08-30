<?php

/*
 *
 * Copyright (c) 2018, CJ Kucera
 * All rights reserved.
 *   
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *     * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above copyright
 *       notice, this list of conditions and the following disclaimer in the
 *       documentation and/or other materials provided with the distribution.
 *     * Neither the name of the development team nor the
 *       names of its contributors may be used to endorse or promote products
 *       derived from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL CJ KUCERA BE LIABLE FOR ANY
 * DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

require_once('levels.php');

$errors = array();
$game = 'bl2';

// I should really stop nesting gigantic `if` statements.  That stops... NOW.
$filetype = 'svg';
if (array_key_exists('filetype', $_REQUEST))
{
    if ($_REQUEST['filetype'] == 'png')
    {
        $filetype = 'png';
    }
}
$follow_kismet = array_key_exists('follow_kismet', $_REQUEST);

$kismet_vars = true;

// Now back to our historically-deep big ol' gigantic `if` statements.
if (array_key_exists('action', $_REQUEST))
{
    // If the user specifically unchecked vars, keep them unchecked
    if (!array_key_exists('kismet_vars', $_REQUEST))
    {
        $kismet_vars = false;
    }

    // Now continue
    if ($_REQUEST['action'] == 'generate')
    {
        $game = $_REQUEST['game'];
        $bpd = trim($_REQUEST['bpd']);
        if ($game == 'tps' or $game == 'bl2')
        {
            if (strlen($bpd) > 0)
            {
                // Allow passing in a fully-qualified object name
                if (preg_match("/^.*'(.*)'$/", $bpd, $matches))
                {
                    $bpd = $matches[1];
                }
                if (preg_match('/^[0-9a-zA-Z:_\.]+$/', $bpd))
                {
                    $level = trim($_REQUEST['level']);
                    if ($level == '' or array_key_exists($level, $levels_by_id[$game])) {

                        $cmd_args = array();
                        $cache_parts = array();

                        $cache_parts[] = $game;
                        $cache_parts[] = strtolower(preg_replace('/[^0-9a-zA-Z_]/', '_', $bpd));

                        if ($level != '')
                        {
                            $cmd_args[] = '-l ' . $level;
                            $cache_parts[] = strtolower($level);

                            if ($follow_kismet)
                            {
                                $cmd_args[] = '-f';
                                $cache_parts[] = 'follow';
                            }
                        }

                        if ($kismet_vars)
                        {
                            $cmd_args[] = '-v';
                            $cache_parts[] = 'vars';
                        }
                        else
                        {
                            $cache_parts[] = 'novars';
                        }

                        $cmd_args[] = $game;
                        $cmd_args[] = $bpd;

                        $cache_filename = 'cache/' . implode('_', $cache_parts) . '.' . $filetype;
                        if (!file_exists($cache_filename))
                        {
                            $output = array();
                            exec("/usr/bin/python36 bpd_dot.py " . implode(' ', $cmd_args), $output, $return_val);
                            $output_full = implode("\n", $output);
                            if ($return_val == 0)
                            {
                                $descriptors = array(
                                   0 => array("pipe", "r"),
                                   1 => array("pipe", "w"),
                                   2 => array("pipe", "w")
                                );
                                $pipes = array();
                                $process = proc_open('/usr/bin/unflatten -l 10 -c 99 -f | /usr/bin/dot -T' . $filetype, $descriptors, $pipes);

                                if (is_resource($process))
                                {
                                    fwrite($pipes[0], $output_full);
                                    fclose($pipes[0]);
                                    $image = stream_get_contents($pipes[1]);
                                    fclose($pipes[1]);
                                    fclose($pipes[2]);
                                    proc_close($process);

                                    $outfile = fopen($cache_filename, 'wb');
                                    if ($outfile)
                                    {
                                        fwrite($outfile, $image);
                                        fclose($outfile);
                                    }
                                    else
                                    {
                                        array_push($errors, 'Could not open cache for writing');
                                    }
                                }
                                else
                                {
                                    array_push($errors, 'Error generating graph');
                                }
                            }
                            elseif ($return_val == 2)
                            {
                                array_push($errors, 'Specified class was not found');
                            }
                            else
                            {
                                array_push($errors, 'Unknown error encountered when generating graph; probably a code problem.  Let me know what your object name and options were, please!');
                            }
                        }
                        if (file_exists($cache_filename))
                        {
                            if ($filetype == 'svg')
                            {
                                header('Content-Type: image/svg+xml');
                                //header('Content-Disposition: attachment; filename="bpd_graph.svg"');
                            }
                            else
                            {
                                header('Content-Type: image/png');
                                //header('Content-Disposition: attachment; filename="bpd_image.png"');
                            }
                            readfile($cache_filename);
                            exit();
                        }
                        elseif (count($errors) == 0)
                        {
                            array_push($errors, 'Could not write to cache');
                        }
                    }
                    else
                    {
                        array_push($errors, 'Invalid level specified');
                    }
                }
                else
                {
                    array_push($errors, 'Invalid class specified');
                }
            }
            else
            {
                array_push($errors, 'Input a class name');
            }
        }
        else
        {
            $game = 'bl2';
            array_push($errors, 'Error parsing game selection');
        }
    }
}

include('../../inc/apoc.php');
$page->set_title('Borderlands 2 / The Pre-Sequel BPD/Kismet Graphs');
$page->add_js('bpd_js.php');
$page->add_css('bpd.css');
$page->add_onload('populateLevelList();');
$page->add_changelog('June 19, 2018', 'Initial post');
$page->add_changelog('June 28, 2018', 'Changed to rectangles rather than ellipses for the nodes');
$page->add_changelog('July 2, 2018', array(
    'Use text labels for variables rather than arrows',
    'Added LightChaosman credit for data -- should\'ve had that in for awhile!'
));
$page->add_changelog('July 13, 2018', 'Correctly display delays which aren\'t whole numbers');
$page->add_changelog('August 3, 2018', 'Added a link to the freshly-uploaded source at Github');
$page->add_changelog('August 6, 2018', 'Updated TPS BPD data to BLCMM\'s data, rather than my own -- more complete definitions in a variety of cases');
$page->add_changelog('August 10, 2018', array(
    'Added EventData2 index to Event nodes',
    'Link RemoteCustomEvent Behaviors where possible',
    'Updated BL2 BPD data to BLCMM\'s latest -- there were a few things missing, I think'
));
$page->add_changelog('August 13, 2018', array(
    'Allow graphing of Kismet sequences as well',
    'BPDs can link to Kismet sequence events, if a level is chosen to operate in',
));
$page->add_changelog('August 16, 2018', array(
    'Added ability to graph entire Kismet sequence, rather than having to choose a start point',
    'Added PNG/SVG output dropdown',
));
$page->add_changelog('August 17, 2018', array(
    'Allow fully-qualified objects to be passed in as name (with object type and quotes)',
    'Show linked kismet variables as separate nodes',
    'Fix error on full-kismet graphs where nodes could be drawn twice',
));
$page->add_changelog('August 19, 2018', array(
    'Fixed Kismet sequence over-reporting of full classnames, when graphing entire sequence',
    'Default to SVG output',
    'Graphs will open in new tab',
    'Option to not show kismet variables',
));
$page->add_changelog('August 20, 2018', array(
    'Added link to Kismet/BPD Basics Wiki page',
));
$page->add_changelog('August 28, 2018', array(
    'Added VarName reporting for sequence variables',
    'Added data reporting in some BPD behavior nodes: ChangeInstanceDataSwitch, ChangeUsability, Delay, IsSequenceEnabled, and event names',
    'Fixed a bug preventing PNG images from being generated',
));
$page->add_changelog('August 29, 2018', array(
    'Added data reporting in some more BPD behavior nodes: ChangeRemoteBehaviorSequenceState, SimpleAnimPlay, SimpleAnimStop',
    'Show disabled BPD events in graph (only affects ten BPDs across both BL2 and TPS)',
    'Added Link IDs to BPD Links',
));
$page->apoc_header();
?>

<p>
Just a page to generate graphs from Borderlands 2/TPS BPDs and Kismets.  If you
don't know what a BPD or Kismet is, this probably isn't for you, but you can
check out some <a href="https://github.com/BLCM/BLCMods/wiki/Kismet-Sequence-and-BehaviorProviderDefinition-Basics">basic
information at the BLCMods Wiki</a>.  Many thanks to LightChaosman for the data
which powers this generator!
</p>

<h2>Generate A Graph</h2>

<?php
if (count($errors) > 0)
{
    echo "<div class=\"bad\">\n";
    echo "<ul>\n";
    foreach ($errors as $error)
    {
        echo "<li>$error</li>\n";
    }
    echo "</ul>\n";
    echo "</div>\n";
}
?>

<blockquote>
<form action="index.php" method="get" target="_blank">
<p><strong>Note:</strong> PNG graphic output supports a max. width of about 32k pixels.  Graphics
which would be larger than that will scale down, sometimes into illegibility.  Stick with SVG
output for extremely large graphs.</p>
<select name="game" id="game" onChange="populateLevelList();">
<option value="bl2"<?php if ($game == 'bl2') { echo ' selected'; } ?>>Borderlands 2</option>
<option value="tps"<?php if ($game == 'tps') { echo ' selected'; } ?>>The Pre-Sequel</option>
</select>
<input type="text" name="bpd" id="bpd" size="70">
<select name="filetype" id="filetype">
<option value="svg"<?php if ($filetype == 'svg') { echo ' selected'; }?>>SVG</option>
<option value="png"<?php if ($filetype == 'png') { echo ' selected'; }?>>PNG</option>
</select>
<input type="hidden" name="action" value="generate">
<input type="submit" value="Generate">
<div class="bpd_optional">
<p><strong>Optional:</strong></p>
<p>Selecting a level here will allow the tree to follow Kismet sequence
events within the specified level.</p>
<select name="level" id="level">
<?php
// May as well prepopulate this in case someone's got Javascript disabled
foreach ($levels as $game => $level_list)
{
    foreach ($level_list as $level_tuple) {
        echo '<option value="' . $level_tuple[1] . '"';
        if (array_key_exists('level', $_REQUEST))
        {
            if ($_REQUEST['level'] == $level_tuple[1])
            {
                echo ' selected';
            }
        }
        echo '>' . strtoupper($game) . ' - ' . $level_tuple[0] . "</option>\n";
    }
}
?>
</select><br/>
<input type="checkbox" name="follow_kismet" id="follow_kismet"<?php if ($follow_kismet) { echo ' checked'; }?>>
<label for="follow_kismet"><i>Allow following Kismet events through class boundaries</i></label>
</div>
<div class="bpd_optional">
<p><strong>Optional:</strong></p>
<input type="checkbox" name="kismet_vars" id="kismet_vars"<?php if ($kismet_vars) { echo ' checked'; }?>>
<label for="kismet_vars">Include Kismet variables in graphs <i>(can lead to very busy graphs, but is generally useful)</i></label>
</div>
</form>
</blockquote>

<p><span class="bad">Warning:</span> The Kismet graphing abilities seem pretty
solid to me, but I wouldn't be surprised if there are edge cases I've missed.  Please
let me know if any graphs error out, or are doing anything weird!</p>

<h2>Option Reference</h2>

<p>
For the most basic functionality (which is all most people are ever going to
need), simply paste the BPD name into the main textbox, choose the game, and hit
"Generate."  As of August 13, 2018, you can also put in a Kismet sequence start
point to graph those.  For instance, some valid start points:
</p>

<ul>
<li><tt>GD_Shields.Skills.Impact_Shield_Skill:BehaviorProviderDefinition_0</tt></li>
<li><tt>Xmas_Dynamic.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_RemoteEvent_16</tt></li>
</ul>

<p>
The graph should let you know whenever it would "call out" to an external event,
whether it's to another BPD or a Kismet sequence.  In some cases, it can know the
BPD name to display, in which case it will show you (see the screenshot below).
By default, it won't actually "follow" any of these links, though.
</p>

<p>
In order to have the graph follow into event links as much as possible (which will
often be into Kismet sequences), choose a level in which the BPD or Kismet will be
running.  This way, the grapher can know which Kismets are available to link to.
</p>

<p>
Finally, when graphing into Kismets, sometimes the sequence links will take the
grapher out of the class that it started in.  For instance, the graph of
<tt>Distillery_Boss.TheWorld:PersistentLevel.Main_Sequence.SeqEvent_LevelLoaded_1</tt>
starts out in the main class <tt>Distillery_Boss.TheWorld:PersistentLevel.Main_Sequence</tt>.
So long as Rotgut Distillery is chosen as the level to work in, the tree will end
up showing that it branches out to other sequences into classes such as
<tt>Distillery_Mission3.TheWorld:PersistentLevel.Main_Sequence</tt>.  In order to
actually follow those links, rather than just stopping at the class change, check
the "Allow following Kismets through class boundaries" checkbox.
</p>

<h2>Output Reference</h2>

<blockquote>

<img src="impact.png?v=3" alt="Graph of base Amp shield BPD">
<img src="yeti.png?v=1" alt="Graph of a Kismet sequence from the Christmas Headhunter Pack" style="vertical-align: top;">

<p>
Green nodes are the initial Events in <tt>EventData2</tt> which kick off
the BPD trees.  The number in brackets is the index in the
<tt>BehaviorSequences</tt> array which the event lives.  If the main
BehaviorSequence has a name, it will be here.  The Event name itself is
always shown after a period.  The second index in brackets is the
index of the event inside the <tt>EventData2</tt> index.
</p>

<p>
Blue nodes are Kismet sequence objects, and the darker blue, square-corner
ones are Kismet sequence events.  The lighter blue nodes are other sequence
objects.  The event name will be included where relevant.
</p>

<p>
Other nodes are behaviors from the <tt>BehaviorData2</tt> array.  The
number in brackets is the index of the behavior.
</p>

<p>
Inbetween the behavior name and the optional variables (see below), there may 
be some extra data provided, depending on the behavior type.  Most behavior 
types won't report anything special, but a few will.  I am open to suggestions 
as to more data which would be usefully provided in the graph.
</p>

<p>
Variables are inside the nodes, underneath the title of the node.  Output
variables are prefixed by <tt>Out:</tt>, input variables are prefixed
by <tt>In:</tt>, and context variables are prefixed by <tt>Ctx:</tt>.
</p>
<ul>
<li>The left-hand
side of the variable (before "via") is the relevant entry in the
<tt>VariableData</tt> array, with its index in brackets.  If the
<tt>VariableData</tt> entry is named, the name will appear there as well.
The data type is always shown.</li>
<li>The right-hand side of the variable (after "via") is two components:
<ul>
<li>First, the relevant entry in the <tt>ConsolidatedVariableLinkData</tt>
array, with its index in brackets.  The name will always be shown there.</li>
<li>Secondly (after the comma), the index in the
<tt>ConsolidatedLinkedVariables</tt> array which points to the actual
variable.</li>
</ul>
</ul>

<p>
The links between the behaviors will have a few labels attached right
where they leave their parent node.  The first number is the order in
which they are called, starting with zero.  The second number, in brackets,
is the index of the <tt>ConsolidatedOutputLinkData</tt> entry being used
to provide the link.  The third line will be the "Link ID."  Some Behaviors
will require certain IDs for the links to work properly, so this should give
you a feel for what the IDs are.  (See my <a href="../bl-bpdnumbers/">BPD
Number Calculator page</a> for information on how those relate to the values
you'll see in the BPDs themselves.)  Then, an optional fourth entry may appear
under that, prefixed with a lowercase "d", which will specify a delay
before triggering the next behavior.
</p>

<p>
Links which refer back to events will be colored in green if it's heading
towards a BPD Event, or blue if it's heading towards a Kismet sequence event.
If a <tt>RemoteCustomEvent</tt> links to an event name which isn't present in
this BPD, the link will be shown in a node which looks a bit like an
arrow pointing to the right.  Those nodes will be light red for event
names which appear to be invalid generally, and gold for events which
explicitly link to other BPDs.
</p>

</blockquote>

<h2>Sourcecode</h2>

<blockquote>

<p>
The code (and data) for this page exist at github:
<a href="https://github.com/apocalyptech/borderlands-bpd">https://github.com/apocalyptech/borderlands-bpd</a>.
The code is licensed under the <a href="https://opensource.org/licenses/BSD-3-Clause">3-clause BSD license</a>.
Feel free to run it locally yourself, if you like, or even host it
elsewhere.  I intend to keep hosting this on my own site, but should
it ever go dark, having mirrors is always nice.
</p>

</blockquote>

<h2>TODO</h2>

<ul>
<li>Kismet Sequence objects should be able to autodetect what level they're in.</li>
<li>Would be really nice to figure out a way to get graphs to scrunch down to be
    more square, rather than being so wide a lot of the time.</li>
<li>Search/Highlight functionality</li>
<li>Figure out other useful attributes to display in the nodes themselves, based on
    node type (mostly just for Kismets)</li>
<li>Sort level names by DLC</li>
</ul>

<? $page->apoc_footer(); ?>
