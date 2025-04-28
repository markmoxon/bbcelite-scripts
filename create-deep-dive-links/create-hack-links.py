import re
import os


# Environment variables
elite_website = os.environ['ELITE_WEBSITE']

# Config
deep_dive_index = elite_website + "/hacks/index.html"
re_deep_dive = re.compile(r'^\t{7}<li><a href="(.+)">(.+)</a> - (.+)</li>\n')
html_prev_next = '''
\t\t\t\t<div class="codeBlockWrapper nav">
\t\t\t\t\t<nav class="codeBlock previousNext"><a class="previous" rel="prev" title="Previous page" href="{}">{}</a><a class="next" rel="next" title="Next page" href="{}">{}</a></nav>
\t\t\t\t</div>
'''
html_prev = '''
\t\t\t\t<div class="codeBlockWrapper nav">
\t\t\t\t\t<nav class="codeBlock previousNext"><a class="previous" rel="prev" title="Previous page" href="{}">{}</a></nav>
\t\t\t\t</div>
'''
html_next = '''
\t\t\t\t<div class="codeBlockWrapper nav">
\t\t\t\t\t<nav class="codeBlock previousNext"><a class="next" rel="next" title="Next page" href="{}">{}</a></nav>
\t\t\t\t</div>
'''

# Global variables
dive_list = [{"url": "/deep_dives/", "name": "Index of all Elite hacks", "description": ""}]

with open(deep_dive_index, "r") as index_file:
    for line in index_file.readlines():
        m = re_deep_dive.search(line)
        if m:
            dive_list.append({"url": m.group(1), "name": m.group(2), "description": m.group(3)})

for i, dive in enumerate(dive_list):
    print("Code for '{}'".format(dive["name"]))
    if i == 0:
        next_dive = dive_list[i + 1]
        print(html_next.format(next_dive["url"], next_dive["name"]))
    elif i == len(dive_list) - 1:
        previous_dive = dive_list[i - 1]
        print(html_prev.format(previous_dive["url"], previous_dive["name"]))
    else:
        previous_dive = dive_list[i - 1]
        next_dive = dive_list[i + 1]
        print(html_prev_next.format(previous_dive["url"], previous_dive["name"], next_dive["url"], next_dive["name"]))
