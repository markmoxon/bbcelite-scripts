import re
import os


def make_id(name):
    return "{}".format(
        name.replace("/", "-")
            .replace(" ", "_")
            .replace("(", "")
            .replace(")", "")
            .replace('"', "")
            .replace("'", "")
            .replace(",", "")
            .replace("+", "-plus-")
            .replace("%", "-per-cent")
            .replace("---", "-minus-")
            .replace("ü", "u")
            .replace("!", "")
            .lower()
    )


def sort_by_name(k):
    key_fixed = k["name"].lower()
    key_fixed = re.sub(r"^a ", r"", key_fixed)
    key_fixed = re.sub(r"^an ", r"", key_fixed)
    key_fixed = re.sub(r"^the ", r"", key_fixed)
    return key_fixed


# Environment variables
source_website = os.environ['ELITE_WEBSITE']

if not os.path.isdir("output"):
    os.mkdir("output")

if not os.path.isdir("output/deep_dives"):
    os.mkdir("output/deep_dives")

# Config
deep_dive_index = source_website + "/deep_dives/index.html"
re_deep_dive = re.compile(r'^\t{7}<li><a href="(.+)">(.+)</a> - (.+)</li>\n')
re_category = re.compile(r'<h2 class="articleSubheader">(.+)<br>')

html_prev_next = '''
\t\t\t\t<div class="codeBlockWrapper nav">
\t\t\t\t\t<nav class="codeBlock previousNext"><a class="previous" rel="prev" title="Previous deep dive" href="{}">{}</a><a class="next" rel="next" title="Next deep dive" href="{}">{}</a></nav>
\t\t\t\t</div>
'''
html_prev = '''
\t\t\t\t<div class="codeBlockWrapper nav">
\t\t\t\t\t<nav class="codeBlock previousNext"><a class="previous" rel="prev" title="Previous deep dive" href="{}">{}</a></nav>
\t\t\t\t</div>
'''
html_next = '''
\t\t\t\t<div class="codeBlockWrapper nav">
\t\t\t\t\t<nav class="codeBlock previousNext"><a class="next" rel="next" title="Next deep dive" href="{}">{}</a></nav>
\t\t\t\t</div>
'''
deep_dive_html = '''<?php
include_once("../templates/template_functions.php");
page_header("deep_dives", "{0}", "{1}", "{1}", "A deep dive into {2} in Elite on the BBC Micro", "elite", "deep_dives_{3}", "{4}");
?>
{5}
\t\t\t\t<div class="codeBlockWrapper">
\t\t\t\t\t<div class="codeBlock article">
\t\t\t\t\t\t<h2 class="articleSubheader deepDive">{6}</h2>

\t\t\t\t\t\t<p>This deep dive is being written and will be published in the next few weeks.</p>
\t\t\t\t\t</div>
\t\t\t\t</div>
{5}
\t\t\t</article>

<?php
include_once("../templates_local/navigation.php");

?>
\t\t</div>
\t</body>
</html>
'''
nav_html = '''\t\t\t\t\t\t\t\t\t<li><a id="deep_dives_{0}_{1}" href="/deep_dives/{2}"><span class="menuTitle">{3}</span> <span class="menuSummary">{4}</span></a></li>
'''
category_html_before = '''\t\t\t\t\t\t\t\t</ul>
\t\t\t\t\t\t\t</li>
'''
category_html = '''\t\t\t\t\t\t\t<li id="deep_dives_maths"><span class="menuTitle">{0}</span> <span class="menuSummary menuSummarySubmenu">{1}</span>
\t\t\t\t\t\t\t\t<ul id="submenu_deep_dives_{2}">
\t\t\t\t\t\t\t\t\t<li class="menuItemHeader">{0}</li>
'''
script_html = '''        {0}
            "filename": "deep_dives/{1}",
            "name": "{2}"
        {3},
'''

# Categories
category_summary = {}
category_summary["Buying ships"] = "Elite-A allows you to fly different ships"
category_summary["Charts"] = "Long-range and short-range galactic charts"
category_summary["Copy protection"] = "Hiding the Elite code from prying eyes"
category_summary["Dashboard"] = "The dials, 3D scanner and compass"
category_summary["Demo"] = "Self-playing demos, Star Wars scroll text and more"
category_summary["Drawing circles"] = "Hyperspace tunnels, launch rings and planets"
category_summary["Drawing lines"] = "The core line-drawing routines"
category_summary["Drawing pixels"] = "How to plot pixels in various colours"
category_summary["Drawing planets"] = "Planets with meridians and craters"
category_summary["Drawing ships"] = "The celebrated 3D ship plotting process"
category_summary["Drawing suns"] = "The epic, shimmering Elite sun"
category_summary["Encyclopedia"] = "Elite-A contains the Encyclopedia Galactica"
category_summary["Equipment"] = "Buying and selling weapons and ship upgrades"
category_summary["Flight"] = "Docking, hyperspace, views, shields and more"
category_summary["Keyboard"] = "Processing key presses and joysticks"
category_summary["Loader"] = "The loading screen and system setup"
category_summary["Main loop"] = "The core loop that runs Elite"
category_summary["The main game loop"] = "The core loop that runs Elite"
category_summary["Market"] = "Market prices, selling, buying and inventory"
category_summary["Maths (Arithmetic)"] = "Addition, subtraction, multiplication, division"
category_summary["Maths (Geometry)"] = "Vectors, coordinates, dot products and matrices"
category_summary["Missions"] = "Hunting stolen ships and evading Thargoids"
category_summary["Moving"] = "Moving and rotating ships and planets in space"
category_summary["Save and load"] = "Commander files and competition codes"
category_summary["Ship hangar"] = "The ship hangar that's displayed on docking"
category_summary["Sound"] = "Explosions, laser fire, hyperspace and more"
category_summary["Stardust"] = "Stardust generation and movement"
category_summary["Start and end"] = "The title screen... and the Game Over screen"
category_summary["Status"] = "Showing the commander's status and rank"
category_summary["Tactics"] = "AI tactics for enemy ships and missiles"
category_summary["Text"] = "The game's recursive text tokenisation system"
category_summary["Tube"] = "Communicating with the Second Processor in Elite"
category_summary["Universe"] = "Ship spawning, local bubble, system/market data"
category_summary["Utility routines"] = "Memory/screen clearing, delay routines"
category_summary["Workspaces"] = "Collections of important variables into blocks"
category_summary["Combat demo"] = "Scroll text and training for first-time players"
category_summary["Controllers"] = "Routines for scanning both NES controllers"
category_summary["Drawing sprites"] = "Drawing and hiding sprites"
category_summary["Sprites"] = "Sprites for Trumbles, laser sights and explosions"
category_summary["Drawing the screen"] = "The split-screen mode and different screen views"
category_summary["Icon bar"] = "Processing the NES version's unique icon bar"
category_summary["PPU"] = "Sending data to the Picture Processing Unit (PPU)"
category_summary["Software archaeology"] = "Digging for clues in the original source code"

# Global variables
dive_list = [{"url": "/deep_dives/", "name": "Index of deep dives", "description": ""}]
category = ""
previous_category = ""

with open(deep_dive_index, "r") as index_file:
    for line in index_file.readlines():
        c = re_category.search(line)
        if c:
            category = c.group(1)
        m = re_deep_dive.search(line)
        if m:
            dive_list.append({"url": m.group(1), "name": m.group(2), "description": m.group(3), "category": category})

with open("output/next_prev.html", "w") as next_prev_file:
    with open("output/navigation.html", "w") as nav_file:
        for i, dive in enumerate(dive_list):
            if i == 0:
                next_dive = dive_list[i + 1]
                next_prev = html_next.format(next_dive["url"], next_dive["name"])
            elif i == len(dive_list) - 1:
                previous_dive = dive_list[i - 1]
                next_prev = html_prev.format(previous_dive["url"], previous_dive["name"])
            else:
                previous_dive = dive_list[i - 1]
                next_dive = dive_list[i + 1]
                next_prev = html_prev_next.format(previous_dive["url"], previous_dive["name"], next_dive["url"], next_dive["name"])
            next_prev_file.write(next_prev)

            if dive["url"] != "/deep_dives/":
                if previous_category != dive["category"]:
                    if previous_category != "":
                        nav_file.write(category_html_before)
                    previous_category = dive["category"]
                    if dive["category"] in category_summary:                        
                        nav_file.write(category_html.format(
                            dive["category"],
                            category_summary[dive["category"]],
                            make_id(dive["category"])
                        ))
                    else:
                        nav_file.write(category_html.format(
                            dive["category"],
                            "xxx",
                            make_id(dive["category"])
                        ))

                nav_file.write(nav_html.format(
                    make_id(dive["category"]),
                    dive["url"].replace(".html", ""),
                    dive["url"],
                    dive["name"],
                    dive["description"]
                ))

                with open("output/deep_dives/" + dive["url"], "w") as file:
                    file.write(deep_dive_html.format(
                        dive["url"],
                        dive["name"],
                        dive["name"][0].lower() + dive["name"][1:],
                        make_id(dive["category"]),
                        dive["url"].replace(".html", ""),
                        next_prev,
                        dive["description"]
                    ))
        nav_file.write(category_html_before)

        with open("output/script.py", "w") as script_file:
            for i, dive in enumerate(sorted(dive_list, key=sort_by_name)):
                script_file.write(script_html.format(
                    "{",
                    dive["url"],
                    dive["name"],
                    "}"
                ))
