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

$errors = array();
$game = 'bl2';
if (array_key_exists('action', $_REQUEST))
{
    if ($_REQUEST['action'] == 'generate')
    {
        $game = $_REQUEST['game'];
        $bpd = trim($_REQUEST['bpd']);
        if ($game == 'tps' or $game == 'bl2')
        {
            if (strlen($bpd) > 0)
            {
                if (preg_match('/^[0-9a-zA-Z:_\.]+$/', $bpd))
                {
                    $cache_filename = 'cache/' . $game . '_' . strtolower(preg_replace('/[^0-9a-zA-Z_]/', '_', $bpd)) . '.png';
                    if (!file_exists($cache_filename))
                    {
                        $output = array();
                        exec("/usr/bin/python36 bpd_dot.py $game $bpd", $output, $return_val);
                        $output_full = implode("\n", $output);
                        if ($return_val == 0)
                        {
                            $descriptors = array(
                               0 => array("pipe", "r"),
                               1 => array("pipe", "w"),
                               2 => array("pipe", "w")
                            );
                            $pipes = array();
                            $process = proc_open('/usr/bin/unflatten -l 10 -c 99 -f | /usr/bin/dot -Tpng', $descriptors, $pipes);

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
                        else
                        {
                            array_push($errors, 'Specified class was not found');
                        }
                    }
                    if (file_exists($cache_filename))
                    {
                        header('Content-Type: image/png');
                        header('Content-Disposition: attachment; filename="bpd_image.png"');
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
$page->set_title('Borderlands 2 / The Pre-Sequel BPD Graphs');
$page->add_changelog('June 19, 2018', 'Initial post');
$page->add_changelog('June 28, 2018', 'Changed to rectangles rather than ellipses for the nodes');
$page->add_changelog('July 2, 2018', array(
    'Use text labels for variables rather than arrows',
    'Added LightChaosman credit for data -- should\'ve had that in for awhile!'
));
$page->add_changelog('July 13, 2018', 'Correctly display delays which aren\'t whole numbers');
$page->apoc_header();
?>

<p>
Just a page to generate graphs from Borderlands 2/TPS BPDs.  If you
don't know what a BPD is, this isn't for you.  Many thanks to LightChaosman
for the data which powers this generator!
</p>

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

<form action="index.php" method="get">
<select name="game" id="game">
<option value="bl2"<?php if ($game == 'bl2') { echo ' selected'; } ?>>Borderlands 2</option>
<option value="tps"<?php if ($game == 'tps') { echo ' selected'; } ?>>The Pre-Sequel</option>
</select>
<input type="text" name="bpd" id="bpd" size=80>
<input type="hidden" name="action" value="generate">
<input type="submit" value="Generate">
</form>

<h2>Output Reference</h2>

<blockquote>

<img src="impact.png?v=2" alt="Graph of base Amp shield BPD">

<p>
Green nodes are the initial Events in <tt>EventData2</tt> which kick off
the BPD trees.  The number in brackets is the index in the
<tt>BehaviorSequences</tt> array which the event lives.  If the main
BehaviorSequence has a name, it will be here.  The Event name itself is
always shown after a period.
</p>

<p>
Other nodes are behaviors from the <tt>BehaviorData2</tt> array.  The
number in brackets is the index of the behavior.
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
to provide the link.  Optionally, a third entry may appear under that, 
prefixed with a lowercase "d", which will specify a delay before triggering
the next behavior.
</p>

</blockquote>

<? $page->apoc_footer(); ?>
