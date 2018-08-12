<?php
require_once('levels.php');
header('Content-Type: text/javascript');

print("var levels = {\n");
foreach ($levels as $game => $level_list)
{
    print('  "' . $game . '": [' . "\n");
    foreach ($level_list as $level_tuple) {
        print('    ["' . $level_tuple[0] . '", "' . $level_tuple[1] . '"],' . "\n");
    }
    print("  ],\n");
}
print("};\n");
?>

/*
 * Function to toggle the contents of the level-select box
 */
function populateLevelList() {
    var gameList = document.getElementById('game');
    var selectList = document.getElementById('level');
    var game = gameList.options[gameList.selectedIndex].value;

    // Clear out the level list and put an empty option in.
    var i;
    for (i = selectList.options.length - 1 ; i >= 0; i--) {
        selectList.remove(i);
    }
    var option = document.createElement("option");
    option.text = "";
    option.value = "";
    selectList.add(option);

    // Now, if we have levels for the selected game, load them.
    if (game in levels) {

        // Check our querystring to see if one's already selected.
        var urlParams = new URLSearchParams(location.search);
        var selectedLevel = "";
        if (urlParams.has("level")) {
            selectedLevel = urlParams.get("level");
        }

        // Loop through and add
        var levelList = levels[game];
        var tuple;
        for (idx in levelList) {
            tuple = levelList[idx];
            var option = document.createElement("option");
            option.text = tuple[0] + " (" + tuple[1] + ")";
            option.value = tuple[1];
            if (selectedLevel === tuple[1]) {
                option.selected = true;
            }
            selectList.add(option);
        }
    }
}
