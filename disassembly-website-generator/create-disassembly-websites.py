import re
import os
import json
import argparse
import ntpath


# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("platform", help="The platform to generate (e.g. 6502sp or cassette)")
args = parser.parse_args()
print("Extracting platform: {}".format(args.platform), end="", flush=True)

# Environment variables
elite_repositories = os.environ['ELITE_CODE_REPOSITORIES']
library_repository = os.environ['ELITE_LIBRARY_REPOSITORY']
aviator_repository = os.environ['AVIATOR_CODE_REPOSITORY']
revs_repository = os.environ['REVS_CODE_REPOSITORY']
lander_repository = os.environ['LANDER_CODE_REPOSITORY']

# Config
if args.platform == "cassette":
    source_folder = elite_repositories + "/elite-source-code-bbc-micro-cassette/1-source-files/main-sources/"
    elite_loader = source_folder + "elite-loader.asm"
    elite_source = source_folder + "elite-source.asm"
    elite_bcfs = source_folder + "elite-bcfs.asm"
    dest_folder = "websites/elite/"
    content_folder = "cassette/"
    explore_folder = "explore/"
    platform_name = "BBC Micro cassette"
    platform_name_capitalised = "BBC Micro cassette"
    platform_short_name = "BBC Micro cassette"
    platform_id = "cassette_"
    platform_key = "cassette"
    comment_delimiter = "\\"
    re_comment_delimiter = r'\\'
    re_hex_prefix = r'&'

elif args.platform == "disc":
    source_folder = elite_repositories + "/elite-source-code-bbc-micro-disc/1-source-files/main-sources/"
    elite_text_tokens = source_folder + "elite-text-tokens.asm"
    elite_ship_missile = source_folder + "elite-missile.asm"
    elite_loader1 = source_folder + "elite-loader1.asm"
    elite_loader2 = source_folder + "elite-loader2.asm"
    elite_loader3 = source_folder + "elite-loader3.asm"
    elite_loader_sideways_ram = source_folder + "elite-loader-sideways-ram.asm"
    elite_source_docked = source_folder + "elite-source-docked.asm"
    elite_source_flight = source_folder + "elite-source-flight.asm"
    elite_source_ships_a = source_folder + "elite-ships-a.asm"
    elite_source_ships_b = source_folder + "elite-ships-b.asm"
    elite_source_ships_c = source_folder + "elite-ships-c.asm"
    elite_source_ships_d = source_folder + "elite-ships-d.asm"
    elite_source_ships_e = source_folder + "elite-ships-e.asm"
    elite_source_ships_f = source_folder + "elite-ships-f.asm"
    elite_source_ships_g = source_folder + "elite-ships-g.asm"
    elite_source_ships_h = source_folder + "elite-ships-h.asm"
    elite_source_ships_i = source_folder + "elite-ships-i.asm"
    elite_source_ships_j = source_folder + "elite-ships-j.asm"
    elite_source_ships_k = source_folder + "elite-ships-k.asm"
    elite_source_ships_l = source_folder + "elite-ships-l.asm"
    elite_source_ships_m = source_folder + "elite-ships-m.asm"
    elite_source_ships_n = source_folder + "elite-ships-n.asm"
    elite_source_ships_o = source_folder + "elite-ships-o.asm"
    elite_source_ships_p = source_folder + "elite-ships-p.asm"
    dest_folder = "websites/elite/"
    content_folder = "disc/"
    explore_folder = "explore/"
    platform_name = "BBC Micro disc"
    platform_name_capitalised = "BBC Micro disc"
    platform_short_name = "BBC Micro disc"
    platform_id = "disc_"
    platform_key = "disc"
    comment_delimiter = "\\"
    re_comment_delimiter = r'\\'
    re_hex_prefix = r'&'

elif args.platform == "6502sp":
    source_folder = elite_repositories + "/elite-source-code-6502-second-processor/1-source-files/main-sources/"
    elite_loader = source_folder + "elite-loader1.asm"
    elite_loader2 = source_folder + "elite-loader2.asm"
    elite_source = source_folder + "elite-source.asm"
    elite_io = source_folder + "elite-z.asm"
    elite_bcfs = source_folder + "elite-bcfs.asm"
    dest_folder = "websites/elite/"
    content_folder = "6502sp/"
    explore_folder = "explore/"
    platform_name_capitalised = "6502 Second Processor"
    platform_name = "6502 Second Processor"
    platform_short_name = "6502SP"
    platform_id = "sp_"
    platform_key = "6502sp"
    comment_delimiter = "\\"
    re_comment_delimiter = r'\\'
    re_hex_prefix = r'&'

elif args.platform == "c64":
    source_folder = elite_repositories + "/elite-source-code-commodore-64/1-source-files/main-sources/"
    elite_loader1 = source_folder + "elite-firebird.asm"
    elite_loader2 = source_folder + "elite-gma1.asm"
    elite_loader = source_folder + "elite-loader.asm"
    elite_source = source_folder + "elite-source.asm"
    elite_data = source_folder + "elite-data.asm"
    elite_sprites = source_folder + "elite-sprites.asm"
    dest_folder = "websites/elite/"
    content_folder = "c64/"
    explore_folder = "explore/"
    platform_name_capitalised = "Commodore 64"
    platform_name = "Commodore 64"
    platform_short_name = "C64"
    platform_id = "c64_"
    platform_key = "c64"
    comment_delimiter = ";"
    re_comment_delimiter = r';'
    re_hex_prefix = r'\$'

elif args.platform == "apple":
    source_folder = elite_repositories + "/elite-source-code-apple-ii/1-source-files/main-sources/"
    elite_loader = source_folder + "elite-loader.asm"
    elite_source = source_folder + "elite-source.asm"
    elite_data = source_folder + "elite-data.asm"
    elite_bcfs = source_folder + "elite-bcfs.asm"
    elite_transfer = source_folder + "elite-transfer.asm"
    dest_folder = "websites/elite/"
    content_folder = "apple/"
    explore_folder = "explore/"
    platform_name_capitalised = "Apple II"
    platform_name = "Apple II"
    platform_short_name = "Apple"
    platform_id = "apple_"
    platform_key = "apple"
    comment_delimiter = ";"
    re_comment_delimiter = r';'
    re_hex_prefix = r'\$'

elif args.platform == "master":
    source_folder = elite_repositories + "/elite-source-code-bbc-master/1-source-files/main-sources/"
    elite_loader = source_folder + "elite-loader.asm"
    elite_source = source_folder + "elite-source.asm"
    elite_data = source_folder + "elite-data.asm"
    dest_folder = "websites/elite/"
    content_folder = "master/"
    explore_folder = "explore/"
    platform_name_capitalised = "BBC Master"
    platform_name = "BBC Master"
    platform_short_name = "Master"
    platform_id = "master_"
    platform_key = "master"
    comment_delimiter = "\\"
    re_comment_delimiter = r'\\'
    re_hex_prefix = r'&'

elif args.platform == "electron":
    source_folder = elite_repositories + "/elite-source-code-acorn-electron/1-source-files/main-sources/"
    elite_loader = source_folder + "elite-loader.asm"
    elite_source = source_folder + "elite-source.asm"
    elite_bcfs = source_folder + "elite-bcfs.asm"
    dest_folder = "websites/elite/"
    content_folder = "electron/"
    explore_folder = "explore/"
    platform_name = "Acorn Electron"
    platform_name_capitalised = "Acorn Electron"
    platform_short_name = "Electron"
    platform_id = "electron_"
    platform_key = "electron"
    comment_delimiter = "\\"
    re_comment_delimiter = r'\\'
    re_hex_prefix = r'&'

elif args.platform == "elite-a":
    source_folder = elite_repositories + "/elite-a-source-code-bbc-micro/1-source-files/main-sources/"
    elite_text_tokens = source_folder + "elite-text-tokens.asm"
    elite_ship_missile = source_folder + "elite-missile.asm"
    elite_loader = source_folder + "elite-loader.asm"
    elite_source_docked = source_folder + "elite-source-docked.asm"
    elite_source_flight = source_folder + "elite-source-flight.asm"
    elite_source_encyclopedia = source_folder + "elite-source-encyclopedia.asm"
    elite_io = source_folder + "elite-6502sp-io-processor.asm"
    elite_parasite = source_folder + "elite-6502sp-parasite.asm"
    elite_source_ships_a = source_folder + "elite-ships-a.asm"
    elite_source_ships_b = source_folder + "elite-ships-b.asm"
    elite_source_ships_c = source_folder + "elite-ships-c.asm"
    elite_source_ships_d = source_folder + "elite-ships-d.asm"
    elite_source_ships_e = source_folder + "elite-ships-e.asm"
    elite_source_ships_f = source_folder + "elite-ships-f.asm"
    elite_source_ships_g = source_folder + "elite-ships-g.asm"
    elite_source_ships_h = source_folder + "elite-ships-h.asm"
    elite_source_ships_i = source_folder + "elite-ships-i.asm"
    elite_source_ships_j = source_folder + "elite-ships-j.asm"
    elite_source_ships_k = source_folder + "elite-ships-k.asm"
    elite_source_ships_l = source_folder + "elite-ships-l.asm"
    elite_source_ships_m = source_folder + "elite-ships-m.asm"
    elite_source_ships_n = source_folder + "elite-ships-n.asm"
    elite_source_ships_o = source_folder + "elite-ships-o.asm"
    elite_source_ships_p = source_folder + "elite-ships-p.asm"
    elite_source_ships_q = source_folder + "elite-ships-q.asm"
    elite_source_ships_r = source_folder + "elite-ships-r.asm"
    elite_source_ships_s = source_folder + "elite-ships-s.asm"
    elite_source_ships_t = source_folder + "elite-ships-t.asm"
    elite_source_ships_u = source_folder + "elite-ships-u.asm"
    elite_source_ships_v = source_folder + "elite-ships-v.asm"
    elite_source_ships_w = source_folder + "elite-ships-w.asm"
    dest_folder = "websites/elite/"
    content_folder = "elite-a/"
    explore_folder = "explore/"
    platform_name = "Elite-A"
    platform_name_capitalised = "Elite-A"
    platform_short_name = "Elite-A"
    platform_id = "elite-a_"
    platform_key = "elite-a"
    comment_delimiter = "\\"
    re_comment_delimiter = r'\\'
    re_hex_prefix = r'&'

elif args.platform == "nes":
    source_folder = elite_repositories + "/elite-source-code-nes/1-source-files/main-sources/"
    elite_source_common = source_folder + "elite-source-common.asm"
    elite_source_bank_0 = source_folder + "elite-source-bank-0.asm"
    elite_source_bank_1 = source_folder + "elite-source-bank-1.asm"
    elite_source_bank_2 = source_folder + "elite-source-bank-2.asm"
    elite_source_bank_3 = source_folder + "elite-source-bank-3.asm"
    elite_source_bank_4 = source_folder + "elite-source-bank-4.asm"
    elite_source_bank_5 = source_folder + "elite-source-bank-5.asm"
    elite_source_bank_6 = source_folder + "elite-source-bank-6.asm"
    elite_source_bank_7 = source_folder + "elite-source-bank-7.asm"
    elite_source_header = source_folder + "elite-source-header.asm"
    dest_folder = "websites/elite/"
    content_folder = "nes/"
    explore_folder = "explore/"
    platform_name_capitalised = "NES"
    platform_name = "NES"
    platform_short_name = "NES"
    platform_id = "nes_"
    platform_key = "nes"
    comment_delimiter = ";"
    re_comment_delimiter = r';'
    re_hex_prefix = r'\$'

elif args.platform == "aviator":
    source_folder = aviator_repository + "/1-source-files/main-sources/"
    aviator_source = source_folder + "aviator-source.asm"
    dest_folder = "websites/aviator/"
    content_folder = "source/"
    explore_folder = "explore/"
    platform_name = "Aviator"
    platform_name_capitalised = "Aviator"
    platform_short_name = ""
    platform_id = "source_"
    platform_key = "aviator"
    comment_delimiter = "\\"
    re_comment_delimiter = r'\\'
    re_hex_prefix = r'&'

elif args.platform == "revs":
    source_folder = revs_repository + "/1-source-files/main-sources/"
    revs_source = source_folder + "revs-source.asm"
    revs_silverstone = source_folder + "revs-silverstone.asm"
    revs_brands_hatch = source_folder + "revs-brandshatch.asm"
    revs_donington_park = source_folder + "revs-doningtonpark.asm"
    revs_oulton_park = source_folder + "revs-oultonpark.asm"
    revs_snetterton = source_folder + "revs-snetterton.asm"
    revs_nurburgring = source_folder + "revs-nurburgring.asm"
    dest_folder = "websites/revs/"
    content_folder = "source/"
    explore_folder = "explore/"
    platform_name = "Revs"
    platform_name_capitalised = "Revs"
    platform_short_name = ""
    platform_id = "source_"
    platform_key = "revs"
    comment_delimiter = "\\"
    re_comment_delimiter = r'\\'
    re_hex_prefix = r'&'

elif args.platform == "lander":
    source_folder = lander_repository + "/1-source-files/main-sources/"
    lander_source = source_folder + "Lander.arm"
    lander_runimage = source_folder + "RunImage.arm"
    dest_folder = "websites/lander/"
    content_folder = "source/"
    explore_folder = "explore/"
    platform_name = "Lander"
    platform_name_capitalised = "Lander"
    platform_short_name = ""
    platform_id = "source_"
    platform_key = "lander"
    comment_delimiter = "\\"
    re_comment_delimiter = r'\\'
    re_hex_prefix = r'&'

else:
    dest_folder = "websites/elite/"
    content_folder = "compare/"
    platform_short_name = ""
    platform_id = "compare_"
    platform_key = ""
    comment_delimiter = "\\"
    re_comment_delimiter = r'\\'
    re_hex_prefix = r'&'

if args.platform == "aviator":
    game_id = "aviator"
    game_name = "Aviator"
elif args.platform == "revs":
    game_id = "revs"
    game_name = "Revs"
elif args.platform == "lander":
    game_id = "lander"
    game_name = "Lander"
else:
    game_id = "elite"
    game_name = "BBC Micro Elite"

# Regexes
omit_from_compare = "ELITE_A|NES|C64|APPLE"

re_name = re.compile(r'^' + re_comment_delimiter + r'(       Name): (.+)$')
re_type = re.compile(r'^' + re_comment_delimiter + r'(       Type): (.+)$')
re_category = re.compile(r'^' + re_comment_delimiter + r'(   Category): (.+)$')
re_summary = re.compile(r'^' + re_comment_delimiter + r'(    Summary): (.+)$')
re_summary2 = re.compile(r'^' + re_comment_delimiter + r'             ([^ ].+)$')
re_address = re.compile(r'^' + re_comment_delimiter + r'(    Address): (.+)$')
re_deep_dive_in_header = re.compile(r'^' + re_comment_delimiter + r'(  Deep dive): (.+)$')
re_deep_dive_in_header2 = re_summary2
re_deep_dive = re.compile(r'^' + re_comment_delimiter + r' Deep dive: (.+)$')
re_deep_dive_summary = re.compile(r'^' + re_comment_delimiter + r' Summary: (.+)$')
re_deep_dive_summary2 = re.compile(r'^' + re_comment_delimiter + r' (\w.*)$')
re_deep_dive_references = re.compile(r'^' + re_comment_delimiter + r' References: (.+)$')
re_entry_points = re.compile(r'^' + re_comment_delimiter + r' Other entry points:(.*)$')
re_argument_entry1 = re.compile(r"^" + re_comment_delimiter + r"   ([A-Za-z0-9%_\(\)\+\-',]+( [A-Za-z0-9%_\(\)\+\-',\.]+)*)( +)\b(.+)$")
re_argument_entry2 = re.compile(r'^' + re_comment_delimiter + r'                       (.+)$')
re_arguments = re.compile(r'^' + re_comment_delimiter + r' Arguments:(.*)$')
re_returns = re.compile(r'^' + re_comment_delimiter + r' Returns:(.*)$')
re_comment = re.compile(r'^' + re_comment_delimiter + r' \*{78}$')
re_comment2 = re.compile(r'^' + re_comment_delimiter + r' \-{78}$')
re_header = re.compile(r'^' + re_comment_delimiter + r' \-{1, 70}$')
re_url = re.compile(r'(https?://\S+)')
re_unused = re.compile(r'appears? to be unused')

re_if_to_remove = re.compile(r'^IF _MATCH_ORIGINAL_BINARIES')
re_else_to_remove = re.compile(r'^ELSE')
re_endif_to_remove = re.compile(r'^ENDIF')
re_for_loop = re.compile(r'^ *FOR ([^,]+), ([^,]+), ([^,]+)(, [^,]+)?$')

re_empty_line = re.compile(r'^\s*$')
re_empty_comment = re.compile(r'^\s*' + re_comment_delimiter + r'\s*$')
re_empty_line_in_header = re.compile(r'^' + re_comment_delimiter + r'\s*$')
re_line_with_comment = re.compile(r'^([^' + re_comment_delimiter + r']*)( *)' + re_comment_delimiter + r'(.*)$')
re_header_comment = re.compile(r'^' + re_comment_delimiter + r' *(.*?)$')

re_configuration_variable = re.compile(r'^( *)([A-Za-z_][A-Za-z0-9_]*%?)(  *)= ([^' + re_comment_delimiter + r']+?)( *)(' + re_comment_delimiter + r'.*)?$')
re_instruction_line = re.compile(r'^ [A-Z0-9]+')
re_label = re.compile(r'^\s*(\.\^?)(\S+)')
re_label_no_comment = re.compile(r'^\s*(\.\^?)(\S+)$')

re_list_item = re.compile(r'^(\s+)\* (.+)$')
re_numb_item = re.compile(r'^(\s+)\d+\. (.+)$')

re_deep_dive_indented = re.compile(r'^   *[^ \*]')
re_deep_dive_not_indented = re.compile(r'^[^ ]')
re_deep_dive_header = re.compile(r'^\-\-\-')
re_deep_dive_link = re.compile(r'deep dives? on')

# Regexes for comparison tool
re_include_directive = re.compile(r'^ *INCLUDE "(.+)"$')
re_version_if = re.compile(r'(IF|OR) _(CASSETTE_VERSION|ELECTRON_VERSION|6502SP_VERSION|DISC_VERSION|DISC_FLIGHT|DISC_DOCKED|MASTER_VERSION)')
re_version_endif = re.compile(r'^ENDIF.*$')
re_version_if_elite_a = re.compile(r'IF (NOT\()?_(' + omit_from_compare + r')_\w+( OR _(' + omit_from_compare + r')_\w+)*\)?')
re_compare_group = re.compile(r'^Group ([A-Z]): (.*)$')
re_compare_group_link = re.compile(r'^See group ([A-Z])')

# Category summaries for navigation
category_summary = {}
if args.platform == "aviator":
    category_summary["3D geometry"] = "Rotation matrices, coordinate transformations, object calculations and more"
    category_summary["Dashboard"] = "Dials, indicators, radars and flight controls"
    category_summary["Drawing lines"] = "The core line-drawing routines"
    category_summary["Flight model"] = "The aerodynamics behind the Spitfire's realistic movement through the air"
    category_summary["Graphics"] = "General graphics routines for drawing the canopy, clearing the screen and so on"
    category_summary["Keyboard"] = "Processing key presses and joysticks"
    category_summary["Main loop"] = "The core game loop that runs Aviator"
    category_summary["Maths"] = "Addition, subtraction, multiplication, division"
    category_summary["Scoring"] = "Awarding points for flying under the bridge, buzzing the town and killing aliens"
    category_summary["Setup"] = "Moving code around and setting up the game"
    category_summary["Sound"] = "Gunfire, explosions, engine sounds and more"
    category_summary["The Theme"] = "Alien tactics, feeding stages, bullets and guns"
    category_summary["Utility routines"] = "Copying routines, delay routines, random number generators"
    category_summary["Visibility"] = "Processing the on-screen visibility of 3D objects"
    category_summary["Workspaces"] = "Collections of important variables into blocks"
elif args.platform == "revs":
    category_summary["3D objects"] = "Building 3D objects such as cars, signs and corner markers"
    category_summary["Car geometry"] = "Placing and moving cars on the track, and applying tactics to the other drivers"
    category_summary["Dashboard"] = "Wing mirrors, rev counters, tyre treads and starting lights"
    category_summary["Drawing objects"] = "Drawing 3D objects using scaffolded definitions and multiple 2D objects"
    category_summary["Drawing pixels"] = "Tables and routines to support drawing pixels directly onto the screen"
    category_summary["Drawing the track"] = "The complex maths behind drawing the track and its coloured verges"
    category_summary["Drivers"] = "The championship table, awarding race points, lap timers and driver speeds"
    category_summary["Driving model"] = "The sophisticated physics engine behing the first real racing simulation"
    category_summary["Extra tracks"] = "Data and routines from the extra track files in Revs 4 Tracks and Revs+"
    category_summary["Keyboard"] = "Control keys, joysticks, menu choices and fetching various types of input"
    category_summary["Main loop"] = "The main game loop and the main driving loop that together run Revs"
    category_summary["Maths (Arithmetic)"] = "Signs, scaling, multiplication, division"
    category_summary["Maths (Geometry)"] = "Vectors, coordinates matrices"
    category_summary["Screen buffer"] = "The convoluted block-based screen buffer that powers the game's graphics"
    category_summary["Screen mode"] = "The interrupt handler and configuration behind the custom Revs screen mode"
    category_summary["Setup"] = "Loading the game, running the checksums, unpacking the code and starting it up"
    category_summary["Sound"] = "Car collisions, two-tone engines and the sweet sound of squealing tyres"
    category_summary["Tactics"] = "AI tactics for computer-controlled drivers and computer assisted steering (CAS)"
    category_summary["Text"] = "How Revs packs all the game text into a small memory footprint"
    category_summary["Track data"] = "Details of the different racing tracks that Revs supports"
    category_summary["Track geometry"] = "The complex world of track sections, segments, verges and markers"
    category_summary["Workspaces"] = "Collections of important variables into blocks"
elif args.platform == "lander":
    category_summary["3D objects"] = "3D objects such as trees, buildings and ships"
    category_summary["Copy protection"] = "Hiding the Lander code from prying eyes"
    category_summary["Drawing lines"] = "The core horizontal line-drawing routines"
    category_summary["Drawing the screen"] = "Smooth animation using screen switching"
    category_summary["Drawing triangles"] = "The main building block of the 3D world"
    category_summary["Graphics buffers"] = "How Lander draws objects in distance order"
    category_summary["Landscape"] = "The secrets of Lander's undulating landscape"
    category_summary["Particles"] = "Explosions, splashes, sparks and falling rocks"
    category_summary["Player"] = "Moving the player using unique mouse-based controls"
    category_summary["Score bar"] = "Updating the score at the top of screen"
    category_summary["Main loop"] = "The core game loop that runs Lander"
    category_summary["Maths (Arithmetic)"] = "Division, square roots and random numbers"
    category_summary["Maths (Geometry)"] = "Trigonometry, vectors and rotation matrices"
    category_summary["Start and end"] = "Initialising the game and shutting it down"
    category_summary["Workspaces"] = "Collections of important variables into blocks"
else:
    category_summary["Buying ships"] = "Elite-A allows you to fly different ships"
    category_summary["Charts"] = "Long-range and short-range galactic charts"
    category_summary["Copy protection"] = "Hiding the Elite code from prying eyes"
    category_summary["Dashboard"] = "The dials, 3D scanner and compass"
    category_summary["Demo"] = "Star Wars scroll texts and a huge Elite logo"
    if args.platform == "nes":
        category_summary["Drawing circles"] = "Planet ellipses and navigation chart circles"
    else:
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
    category_summary["Market"] = "Market prices, selling, buying and inventory"
    category_summary["Maths (Arithmetic)"] = "Addition, subtraction, multiplication, division"
    category_summary["Maths (Geometry)"] = "Vectors, coordinates, dot products and matrices"
    if args.platform == "nes":
        category_summary["Missions"] = "Hunting ships, evading Thargoids... and Trumbles"
    else:
        category_summary["Missions"] = "Hunting stolen ships and evading Thargoids"
    category_summary["Moving"] = "Moving and rotating ships and planets in space"
    if args.platform == "nes":
        category_summary["Save and load"] = "Commander files, save slots and cheat codes"
    else:
        category_summary["Save and load"] = "Commander files and competition codes"
    category_summary["Ship hangar"] = "The ship hangar that's displayed on docking"
    if args.platform == "nes":
        category_summary["Sound"] = "Sound effects, theme music and The Blue Danube"
    else:
        category_summary["Sound"] = "Explosions, laser fire, hyperspace and more"
    category_summary["Stardust"] = "Stardust generation and movement"
    if args.platform == "nes":
        category_summary["Start and end"] = "The title screens... and the Game Over screen"
    else:
        category_summary["Start and end"] = "The title screen... and the Game Over screen"
    category_summary["Status"] = "Showing the commander's status and rank"
    category_summary["Tactics"] = "AI tactics for enemy ships and missiles"
    if args.platform == "nes":
        category_summary["Text"] = "Recursive text tokens in three languages"
    else:
        category_summary["Text"] = "The game's recursive text tokenisation system"
    category_summary["Tube"] = "Communicating with the Second Processor in Elite"
    category_summary["Universe"] = "Ship spawning, local bubble, system/market data"
    if args.platform == "nes":
        category_summary["Utility routines"] = "NMI, memory, delay and bank-switching routines"
    else:
        category_summary["Utility routines"] = "Memory/screen clearing, delay routines"
    category_summary["Workspaces"] = "Collections of important variables into blocks"
    category_summary["Combat demo"] = "Scroll text and training for first-time players"
    category_summary["Controllers"] = "Routines for scanning both NES controllers"
    category_summary["Drawing sprites"] = "Drawing and hiding sprites"
    category_summary["Sprites"] = "Sprites for Trumbles, laser sights and explosions"
    if args.platform == "nes":
        category_summary["Drawing the screen"] = "Drawing and configuring views and the NMI handler"
    elif args.platform == "electron":
        category_summary["Drawing the screen"] = "The mode 4 screen and configuring screen views"
    else:
        category_summary["Drawing the screen"] = "The split-screen mode and different screen views"
    category_summary["Icon bar"] = "Processing the NES version's unique icon bar"
    category_summary["PPU"] = "Sending data to the Picture Processing Unit (PPU)"

# Tag categories and summaries
tag_categories_with_comments = ["Standard", "Enhanced", "Advanced", "Disc", "Electron", "6502SP", "Master", "Other"]

tag_title = {}
tag_title["Standard"] = "Compare code for features of standard Elite"
tag_title["Enhanced"] = "Compare code for features of enhanced Elite"
tag_title["Advanced"] = "Compare code for features of advanced Elite"
tag_title["Disc"] = "Compare code for features of BBC Micro disc Elite"
tag_title["6502SP"] = "Compare code for features of 6502 Second Processor Elite"
tag_title["Master"] = "Compare code for features of BBC Master Elite"
tag_title["Electron"] = "Compare code for features of Acorn Electron Elite"
tag_title["Other"] = "Compare code in other interesting areas"

tag_summary = {}
tag_summary["Standard"] = "Code variations in the features that are common to all versions (BBC Micro cassette, BBC Micro disc, 6502SP, Master, Electron)"
tag_summary["Enhanced"] = "Code variations in the extra features of the enhanced versions (BBC Micro disc, 6502SP, Master)"
tag_summary["Advanced"] = "Code variations in the extra features of the advanced versions (6502SP, Master)"
tag_summary["Disc"] = "Code variations that are unique to the BBC Micro disc version"
tag_summary["6502SP"] = "Code variations that are unique to the 6502SP version"
tag_summary["Master"] = "Code variations that are unique to the Master version"
tag_summary["Electron"] = "Code variations that are unique to the Electron version"
tag_summary["Other"] = "Other code variations might have an impact, such as bug fixes or faster code"

tag_name = {}
tag_name["Standard"] = "Related to a standard feature"
tag_name["Enhanced"] = "Related to an enhanced feature"
tag_name["Advanced"] = "Related to an advanced feature"
tag_name["Disc"] = "Related to the BBC Micro disc version"
tag_name["6502SP"] = "Related to the 6502SP version"
tag_name["Master"] = "Related to the Master version"
tag_name["Electron"] = "Related to the Electron version"
tag_name["Other"] = "Other (e.g. bug fix, optimisation)"
tag_name["Tube"] = "Related to Elite's use of the Tube"
tag_name["Platform"] = "Specific to an individual platform"
tag_name["Minor"] = "Minor and very low-impact"
tag_name["Comment"] = "A variation in the comments only"
tag_name["Label"] = "A variation in the labels only"
tag_name["Screen"] = "Related to the screen mode"

tag_explanation = {}
tag_explanation["Standard"] = "The following table shows code variations related to the standard features that are found in all the versions of Elite (i.e. the BBC Micro cassette, BBC Micro disc, 6502 Second Processor, BBC Master and Electron versions)."
tag_explanation["Enhanced"] = "The following table shows code variations related to the extra features that are found in the enhanced versions of Elite (i.e. the BBC Micro disc, 6502 Second Processor and BBC Master versions)."
tag_explanation["Advanced"] = "The following table shows code variations related to the extra features that are found in the advanced versions of Elite (i.e. the 6502 Second Processor and BBC Master versions)."
tag_explanation["Disc"] = "The following table shows code variations that are unique to the BBC Micro disc version."
tag_explanation["6502SP"] = "The following table shows code variations that are unique to the 6502 Second Processor version."
tag_explanation["Master"] = "The following table shows code variations that are unique to the BBC Master version."
tag_explanation["Electron"] = "The following table shows code variations that are unique to the Electron version."
tag_explanation["Other"] = "The following table shows code variations such as bug fixes, optimisations, or other notable differences that are not covered by the other curated lists."

# URLS for linking .asm references
elite_source_urls = {
    "elite-source.asm": "/{}all/workspaces.html".format(content_folder),
    "elite-bcfs.asm": "/{}all/bcfs.html".format(content_folder),
    "elite-loader.asm": "/{}all/loader.html".format(content_folder),
    "elite-loader1.asm": "/{}all/loader1.html".format(content_folder),
    "elite-loader2.asm": "/{}all/loader2.html".format(content_folder),
    "elite-loader3.asm": "/{}all/loader3.html".format(content_folder),
    "elite-loader-sideways-ram.asm": "/{}all/loader_sideways_ram.html".format(content_folder),
    "elite-transfer.asm": "/{}all/transfer_program.html".format(content_folder),
    "elite-z.asm": "/{}all/i_o_processor.html".format(content_folder),
    "aviator-source.asm": "/{}all/workspaces.html".format(content_folder),
    "revs-source.asm": "/{}all/workspaces.html".format(content_folder),
    "revs-silverstone.asm": "/{}all/silverstone.html".format(content_folder),
    "revs-brandshatch.asm": "/{}all/brands_hatch.html".format(content_folder),
    "revs-doningtonpark.asm": "/{}all/donington_park.html".format(content_folder),
    "revs-oultonpark.asm": "/{}all/oulton_park.html".format(content_folder),
    "revs-snetterton.asm": "/{}all/snetterton.html".format(content_folder),
    "revs-nurburgring.asm": "/{}all/nurburgring.html".format(content_folder)
}

# Do not link to these variables or try to expand them as configuration variables
no_popups = ['I%',
             'J%',
             'PI',
             'P%',
             'byte_count',
             'pass%'
             ]

no_popups_in_loop = ['B%',
                     'B',
                     'N%',
                     'N'
                     ]

no_popups_in_macro = ['D%',
                      'I%',
                      'PA%',
                      'S%',
                      'ax',
                      'ay',
                      'az',
                      'e',
                      'f',
                      'f1',
                      'f2',
                      'k',
                      'n',
                      's',
                      's_x',
                      's_y',
                      's_z',
                      't',
                      'u',
                      'x',
                      'y',
                      'z',
                      'byte_count',
                      'cycles',
                      'face1',
                      'face2',
                      'face3',
                      'face4',
                      'factor',
                      'mask',
                      'normal_x',
                      'normal_y',
                      'normal_z',
                      'price',
                      'quantity',
                      'units',
                      'vertex1',
                      'vertex2',
                      'visibility'
                      ]

# Important routines
if args.platform == "aviator":
    important_routines = [
        "AlienInAcornsville",
        "ApplyFlightModel (Part 1 of 7)",
        "CheckFlyingSkills (Part 1 of 2)",
        "CheckIfAlienIsHit (Part 1 of 2)",
        "DrawCanopyLine (Part 1 of 4)",
        "Main variable workspace",
        "MainLoop (Part 1 of 15)",
        "MakeSound",
        "Multiply8x8",
        "Multiply16x16",
        "ProcessLanding (Part 1 of 7)",
        "ProcessLine (Part 1 of 7)",
        "ProcessLinesToShow",
        "ProjectPoint (Part 1 of 3)",
        "ResetVariables",
        "SetObjectCoords (Part 1 of 11)",
        "SetRandomNumber",
        "UpdateIndicator (Part 1 of 15)",
        "UpdateAliens (Part 1 of 4)"
    ]
elif args.platform == "revs":
    important_routines = [
        "ApplyDrivingModel",
        "ApplyElevation (Part 1 of 5)",
        "ApplyEngine",
        "AwardRacePoints",
        "BuildPlayerCar",
        "Divide8x8",
        "DrawCarOrSign",
        "DrawCars",
        "DrawCornerMarkers",
        "DrawObject",
        "DrawTrack",
        "DrawTrackBytes (Part 1 of 3)",
        "DrawTrackView (Part 1 of 4)",
        "GetObjectAngles",
        "GetSectionAngles (Part 1 of 3)",
        "GetSegmentAngles (Part 1 of 3)",
        "GetVergeAndMarkers (Part 1 of 4)",
        "Main variable workspace",
        "MainDrivingLoop (Part 1 of 5)",
        "MainLoop (Part 1 of 6)",
        "MakeSound",
        "MoveAndDrawCars",
        "Multiply8x8",
        "PrintToken",
        "ProcessDrivingKeys (Part 1 of 6)",
        "ProcessOvertaking (Part 1 of 3)",
        "RotateCarToCoord",
        "RotateCoordToCar",
        "ScreenHandler",
        "SetCustomScreen",
        "Track section data (Part 1 of 2) (Silverstone)",
        "Track section data (Part 2 of 2) (Silverstone)",
        "UpdateMirrors",
        "xTrackSegmentI (Silverstone)",
        "yTrackSegmentI (Silverstone)",
        "zTrackSegmentI (Silverstone)"
    ]
elif args.platform == "lander":
    important_routines = [
        "CalculateRotationMatrix",
        "DrawGraphicsBuffer",
        "DrawLandscapeAndBuffers (Part 1 of 4)",
        "DrawObject (Part 1 of 5)",
        "DrawObjects (Part 1 of 3)",
        "DrawTriangle (Part 1 of 10)",
        "Entry",
        "GetLandscapeAltitude",
        "GetMouseInPolarCoordinates",
        "GetRandomNumbers",
        "LoseLife",
        "MainLoop",
        "MoveAndDrawPlayer (Part 1 of 5)",
        "PlaceObjectsOnMap"
    ]
else:
    important_routines = [
        "TT22",
        "TT23",
        "DOMOVE",
        "doPROT1",
        "DIALS",
        "COMPAS",
        "DILX",
        "SCAN",
        "BLINE",
        "CIRCLE2",
        "TT128",
        "HFS2",
        "HLOIN",
        "LOIN (Part 1 of 7)",
        "LL145 (Part 1 of 4)",
        "PIXEL",
        "CPIX2",
        "PL9 (Part 1 of 3)",
        "PLL1 (Loader)",
        "PLS22",
        "LL9 (Part 1 of 11)",
        "DOEXP",
        "SUN",
        "EQSHP",
        "PLUT",
        "WARP",
        "TT213",
        "DOKEY",
        "TT102",
        "Loader (Part 5 of 6)",
        "Main game loop (Part 2 of 6)",
        "Main flight loop (Part 1 of 16))",
        "TT167",
        "TT208",
        "TT219",
        "ADD",
        "DVID4",
        "MULTU",
        "TIDY",
        "NORM",
        "MVEIT",
        "MVS4",
        "LOD",
        "SVE",
        "IRQ1",
        "NOISE",
        "STARS",
        "DEATH",
        "TITLE",
        "TT170",
        "STATUS",
        "TACTICS (Part 2 of 7)",
        "HITCH",
        "TT26",
        "BPRNT",
        "TT27",
        "NSWHP",
        "KILLSHP",
        "TT24",
        "TT25",
        "TT54",
        "SFS1",
        "DORND",
        "K%",
        "ZP",
        "NMI",
        "DrawIconBar",
        "DrawSystemImage",
        "DrawCmdrImage",
        "DrawEquipment",
        "SetBank",
        "SendScreenToPPU",
        "ReadControllers",
        "MakeMusic",
        "MakeSound",
        "UnpackToRAM",
        "UnpackToPPU"
    ]

# HTML fragments
html_header1 = '''<?php
include_once("../../templates/template_functions.php");
'''
html_header2 = '''?>
'''
html_footer = '''
\t\t\t</article>

<?php
include_once("../../templates_local/navigation.php");
?>
\t\t</div>
\t</body>
</html>
'''
html_code_header1 = '''<?php
include_once("../../../templates/template_functions.php");
'''
html_code_header2 = '''?>
'''
html_code_footer = '''
\t\t\t</article>

<?php
include_once("../../../templates_local/navigation.php");
?>
\t\t</div>
\t</body>
</html>
'''
html_menu = '\t\t\t\t\t\t\t<li><a id="{}{}{}_{}" href="/{}"><span class="menuTitle">{}</span> <span class="menuSummary">{}</span></a></li>\n'
menu_item_open = '''\t\t\t\t\t<li id="{}{}"><span class="menuTitle">{}</span> <span class="menuSummary menuSummarySubmenu">{}</span>
\t\t\t\t\t\t<ul id="submenu_{}{}">
'''
menu_item_close = '''\t\t\t\t\t\t</ul>
\t\t\t\t\t</li>
'''
html_anchor = '<a id="{0}" name="{0}" class="anchor"></a>'
html_summary_heading = '''<h2 class="articleSubheader">{}<br />{}</h2>
'''
html_summary_item = '''<li><a href="/{}">{}</a> - {}</li>

'''
html_summary_reference_link = '<p><a href="/{}">{}</a></p>'
if args.platform == "lander":
    html_workspace_reference_start = '''{0}                                    \\
{0}                                    \\ <span class="routineLink">[<a class="extraDataLink" href="#">Show more</a>]</span>
<div class="extraData">                                    \\
                                    \\ This variable is used by the following:
                                    \\
'''
    html_workspace_reference_link = '                                    \\   * <a href="/{}">{}</a>\n'
    html_workspace_reference_end = '''                                    \\
                                    \\ This list only includes code that refers
                                    \\ to the variable by name; there may be
                                    \\ other references to this memory location
                                    \\ that don't use this label, and these will
                                    \\ not be mentioned above
</div>'''
else:
    html_workspace_reference_start = '''{0}                        \\
{0}                        \\ <span class="routineLink">[<a class="extraDataLink" href="#">Show more</a>]</span>
<div class="extraData">                        \\
                        \\ This variable is used by the following:
                        \\
'''
    html_workspace_reference_link = '                        \\   * <a href="/{}">{}</a>\n'
    html_workspace_reference_end = '''                        \\
                        \\ This list only includes code that refers to the
                        \\ variable by name; there may be other references to
                        \\ this memory location that don't use this label, and
                        \\ these will not be mentioned above
</div>'''
if not comment_delimiter == '\\':
    html_workspace_reference_start = html_workspace_reference_start.replace('\\', comment_delimiter)
    html_workspace_reference_link = html_workspace_reference_link.replace('\\', comment_delimiter)
    html_workspace_reference_end = html_workspace_reference_end.replace('\\', comment_delimiter)

if args.platform == "aviator" or args.platform == "revs" or args.platform == "lander":
    html_indexes = '''
\t\t\t\t\t<li class="menuItemHeader showForMobile">{2} source code by file</li>
\t\t\t\t\t<li><a id="{3}sources_map_of_the_source_code" href="/{1}articles/map_of_the_source_code.html"><span class="menuTitle">Map of the source code</span> <span class="menuSummary">An overview of how the source code for {2} is structured</span></a></li>
\t\t\t\t\t<li id="{3}all_source"><span class="menuTitle">Annotated source files</span>
\t\t\t\t\t\t<span class="menuSummary menuSummarySubmenu">The fully commented source files</span>
\t\t\t\t\t\t<ul id="submenu_{3}all_source">
'''
elif args.platform == "nes":
    html_indexes = '''
\t\t\t\t\t<li class="menuItemHeader showForMobile">{2} source code by file</li>
\t\t\t\t\t<li><a id="{3}sources_map_of_the_source_code" href="/{1}articles/map_of_the_source_code.html"><span class="menuTitle">Map of the source code</span> <span class="menuSummary">An overview of how the source code for Elite is structured</span></a></li>
\t\t\t\t\t<li id="{3}all_source"><span class="menuTitle">Annotated original source files</span>
\t\t\t\t\t\t<span class="menuSummary menuSummarySubmenu">The source files in their original structure</span>
\t\t\t\t\t\t<ul id="submenu_{3}all_source">
\t\t\t\t\t\t\t<li class="menuItemHeader">Common code</li>
'''
elif args.platform == "c64":
    html_indexes = '''
\t\t\t\t\t<li class="menuItemHeader showForMobile">{2} source code by file</li>
\t\t\t\t\t<li><a id="{3}sources_map_of_the_source_code" href="/{1}articles/map_of_the_source_code.html"><span class="menuTitle">Map of the source code</span> <span class="menuSummary">An overview of how the source code for Elite is structured</span></a></li>
\t\t\t\t\t<li id="{3}all_source"><span class="menuTitle">Annotated original source files</span>
\t\t\t\t\t\t<span class="menuSummary menuSummarySubmenu">The source files in their original structure</span>
\t\t\t\t\t\t<ul id="submenu_{3}all_source">
\t\t\t\t\t\t\t<li class="menuItemHeader">Disk loader</li>
'''
else:
    html_indexes = '''
\t\t\t\t\t<li class="menuItemHeader showForMobile">{2} source code by file</li>
\t\t\t\t\t<li><a id="{3}sources_map_of_the_source_code" href="/{1}articles/map_of_the_source_code.html"><span class="menuTitle">Map of the source code</span> <span class="menuSummary">An overview of how the source code for Elite is structured</span></a></li>
\t\t\t\t\t<li id="{3}all_source"><span class="menuTitle">Annotated original source files</span>
\t\t\t\t\t\t<span class="menuSummary menuSummarySubmenu">The source files in their original structure</span>
\t\t\t\t\t\t<ul id="submenu_{3}all_source">
\t\t\t\t\t\t\t<li class="menuItemHeader">Game loader</li>
'''

if args.platform == "cassette" or args.platform == "electron":
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li><a id="{3}all_source_loader" href="/{1}all/loader.html"><span class="menuTitle">Loader source</span> <span class="menuSummary">The loading screen, copy protection and setup for the main game</span></a></li>
'''

elif args.platform == "disc":
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li><a id="{3}all_source_loader1" href="/{1}all/loader1.html"><span class="menuTitle">Loader 1 source</span> <span class="menuSummary">Initial setup and disc copy protection</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_loader2" href="/{1}all/loader2.html"><span class="menuTitle">Loader 2 source</span> <span class="menuSummary">The mode 7 screen setup for the main game</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_text_tokens" href="/{1}all/text_tokens.html"><span class="menuTitle">Text tokens</span> <span class="menuSummary">Elite's tokenised game text</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_ship_missile" href="/{1}all/ship_missile.html"><span class="menuTitle">Missile ship blueprint</span> <span class="menuSummary">The ship blueprint for the missile</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_loader3" href="/{1}all/loader3.html"><span class="menuTitle">Loader 3 source</span> <span class="menuSummary">The Saturn loading screen and main game loader</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_loader_sideways_ram" href="/{1}all/loader_sideways_ram.html"><span class="menuTitle">Sideways RAM Loader source</span> <span class="menuSummary">The main game loader for the sideways RAM variant</span></a></li>
'''

elif args.platform == "6502sp":
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li><a id="{3}all_source_loader1" href="/{1}all/loader1.html"><span class="menuTitle">Loader 1 source</span> <span class="menuSummary">The Saturn loading screen, copy protection and setup for the main game</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_loader2" href="/{1}all/loader2.html"><span class="menuTitle">Loader 2 source</span> <span class="menuSummary">The rest of the loading screen and main game loader</span></a></li>
'''

elif args.platform == "c64":
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li><a id="{3}all_source_loader1" href="/{1}all/loader1.html"><span class="menuTitle">Disk loader 1 source</span> <span class="menuSummary">BASIC bootstrap for auto-running the disk loader</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_loader2" href="/{1}all/loader2.html"><span class="menuTitle">Disk loader 2 source</span> <span class="menuSummary">Loads the game loader and game binaries</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_loader" href="/{1}all/loader.html"><span class="menuTitle">Game loader source</span> <span class="menuSummary">Loads and decrypts the game data</span></a></li>
'''

elif args.platform == "master" or args.platform == "apple":
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li><a id="{3}all_source_loader" href="/{1}all/loader.html"><span class="menuTitle">Loader source</span> <span class="menuSummary">The loading screen and setup for the main game</span></a></li>
'''

elif args.platform == "nes":
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li><a id="{3}all_source_common" href="/{1}all/common.html"><span class="menuTitle">Common source</span> <span class="menuSummary">Variables and macros that are shared by all banks</span></a></li>
'''

elif args.platform == "elite-a":
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li><a id="{3}all_source_loader" href="/{1}all/loader.html"><span class="menuTitle">Loader source</span> <span class="menuSummary">The loading screen, copy protection and setup for the main game</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_text_tokens" href="/{1}all/text_tokens.html"><span class="menuTitle">Text tokens</span> <span class="menuSummary">Elite's tokenised game text</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_ship_missile" href="/{1}all/ship_missile.html"><span class="menuTitle">Missile ship blueprint</span> <span class="menuSummary">The ship blueprint for the missile</span></a></li>
'''

if args.platform == "cassette" or args.platform == "electron" or args.platform == "6502sp":
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li class="menuItemHeader">Main game</li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_workspaces" href="/{1}all/workspaces.html"><span class="menuTitle">Workspaces and configuration</span> <span class="menuSummary">The main variable workspaces used in Elite</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_text_tokens" href="/{1}all/text_tokens.html"><span class="menuTitle">Text tokens</span> <span class="menuSummary">Elite's tokenised game text</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_a" href="/{1}all/elite_a.html"><span class="menuTitle">Elite A source</span> <span class="menuSummary">Part 1 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_b" href="/{1}all/elite_b.html"><span class="menuTitle">Elite B source</span> <span class="menuSummary">Part 2 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_c" href="/{1}all/elite_c.html"><span class="menuTitle">Elite C source</span> <span class="menuSummary">Part 3 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_d" href="/{1}all/elite_d.html"><span class="menuTitle">Elite D source</span> <span class="menuSummary">Part 4 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_e" href="/{1}all/elite_e.html"><span class="menuTitle">Elite E source</span> <span class="menuSummary">Part 5 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_f" href="/{1}all/elite_f.html"><span class="menuTitle">Elite F source</span> <span class="menuSummary">Part 6 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_g" href="/{1}all/elite_g.html"><span class="menuTitle">Elite G source</span> <span class="menuSummary">Part 7 of the main game code</span></a></li>
'''

elif args.platform == "c64" or args.platform == "apple":
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li class="menuItemHeader">Main game</li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_workspaces" href="/{1}all/workspaces.html"><span class="menuTitle">Workspaces and configuration</span> <span class="menuSummary">The main variable workspaces used in Elite</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_a" href="/{1}all/elite_a.html"><span class="menuTitle">Elite A source</span> <span class="menuSummary">Part 1 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_b" href="/{1}all/elite_b.html"><span class="menuTitle">Elite B source</span> <span class="menuSummary">Part 2 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_c" href="/{1}all/elite_c.html"><span class="menuTitle">Elite C source</span> <span class="menuSummary">Part 3 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_d" href="/{1}all/elite_d.html"><span class="menuTitle">Elite D source</span> <span class="menuSummary">Part 4 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_e" href="/{1}all/elite_e.html"><span class="menuTitle">Elite E source</span> <span class="menuSummary">Part 5 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_f" href="/{1}all/elite_f.html"><span class="menuTitle">Elite F source</span> <span class="menuSummary">Part 6 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_g" href="/{1}all/elite_g.html"><span class="menuTitle">Elite G source</span> <span class="menuSummary">Part 7 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_h" href="/{1}all/elite_h.html"><span class="menuTitle">Elite H source</span> <span class="menuSummary">Part 8 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_i" href="/{1}all/elite_i.html"><span class="menuTitle">Elite I source</span> <span class="menuSummary">Part 9 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_j" href="/{1}all/elite_j.html"><span class="menuTitle">Elite J source</span> <span class="menuSummary">Part 10 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_k" href="/{1}all/elite_k.html"><span class="menuTitle">Elite K source</span> <span class="menuSummary">Part 11 of the main game code</span></a></li>
'''

elif args.platform == "master":
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li class="menuItemHeader">Main game</li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_workspaces" href="/{1}all/workspaces.html"><span class="menuTitle">Workspaces and configuration</span> <span class="menuSummary">The main variable workspaces used in Elite</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_a" href="/{1}all/elite_a.html"><span class="menuTitle">Elite A source</span> <span class="menuSummary">Part 1 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_b" href="/{1}all/elite_b.html"><span class="menuTitle">Elite B source</span> <span class="menuSummary">Part 2 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_c" href="/{1}all/elite_c.html"><span class="menuTitle">Elite C source</span> <span class="menuSummary">Part 3 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_d" href="/{1}all/elite_d.html"><span class="menuTitle">Elite D source</span> <span class="menuSummary">Part 4 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_e" href="/{1}all/elite_e.html"><span class="menuTitle">Elite E source</span> <span class="menuSummary">Part 5 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_f" href="/{1}all/elite_f.html"><span class="menuTitle">Elite F source</span> <span class="menuSummary">Part 6 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_g" href="/{1}all/elite_g.html"><span class="menuTitle">Elite G source</span> <span class="menuSummary">Part 7 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_h" href="/{1}all/elite_h.html"><span class="menuTitle">Elite H source</span> <span class="menuSummary">Part 8 of the main game code</span></a></li>
'''

elif args.platform == "disc" or args.platform == "elite-a":
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li class="menuItemHeader">Main game docked code</li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_workspaces_docked" href="/{1}all/workspaces_docked.html"><span class="menuTitle">Docked workspaces</span> <span class="menuSummary">The main variable workspaces used when docked</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_a_docked" href="/{1}all/elite_a_docked.html"><span class="menuTitle">Elite A docked source</span> <span class="menuSummary">Part 1 of the main docked code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_b_docked" href="/{1}all/elite_b_docked.html"><span class="menuTitle">Elite B docked source</span> <span class="menuSummary">Part 2 of the main docked code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_c_docked" href="/{1}all/elite_c_docked.html"><span class="menuTitle">Elite C docked source</span> <span class="menuSummary">Part 3 of the main docked code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_d_docked" href="/{1}all/elite_d_docked.html"><span class="menuTitle">Elite D docked source</span> <span class="menuSummary">Part 4 of the main docked code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_e_docked" href="/{1}all/elite_e_docked.html"><span class="menuTitle">Elite E docked source</span> <span class="menuSummary">Part 5 of the main docked code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_f_docked" href="/{1}all/elite_f_docked.html"><span class="menuTitle">Elite F docked source</span> <span class="menuSummary">Part 6 of the main docked code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_g_docked" href="/{1}all/elite_g_docked.html"><span class="menuTitle">Elite G docked source</span> <span class="menuSummary">Part 7 of the main docked code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_h_docked" href="/{1}all/elite_h_docked.html"><span class="menuTitle">Elite H docked source</span> <span class="menuSummary">Part 8 of the main docked code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_docked" href="/{1}all/elite_ships_docked.html"><span class="menuTitle">Ship hangar blueprints</span> <span class="menuSummary">Data for ships in the ship hangar</span></a></li>
'''
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li class="menuItemHeader">Main game flight code</li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_workspaces_flight" href="/{1}all/workspaces_flight.html"><span class="menuTitle">Flight workspaces</span> <span class="menuSummary">The main variable workspaces used in flight</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_a_flight" href="/{1}all/elite_a_flight.html"><span class="menuTitle">Elite A flight source</span> <span class="menuSummary">Part 1 of the main flight code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_b_flight" href="/{1}all/elite_b_flight.html"><span class="menuTitle">Elite B flight source</span> <span class="menuSummary">Part 2 of the main flight code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_c_flight" href="/{1}all/elite_c_flight.html"><span class="menuTitle">Elite C flight source</span> <span class="menuSummary">Part 3 of the main flight code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_d_flight" href="/{1}all/elite_d_flight.html"><span class="menuTitle">Elite D flight source</span> <span class="menuSummary">Part 4 of the main flight code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_e_flight" href="/{1}all/elite_e_flight.html"><span class="menuTitle">Elite E flight source</span> <span class="menuSummary">Part 5 of the main flight code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_f_flight" href="/{1}all/elite_f_flight.html"><span class="menuTitle">Elite F flight source</span> <span class="menuSummary">Part 6 of the main flight code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_g_flight" href="/{1}all/elite_g_flight.html"><span class="menuTitle">Elite G flight source</span> <span class="menuSummary">Part 7 of the main flight code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_h_flight" href="/{1}all/elite_h_flight.html"><span class="menuTitle">Elite H flight source</span> <span class="menuSummary">Part 8 of the main flight code</span></a></li>
'''
elif args.platform == "nes":
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li class="menuItemHeader">Main game</li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_header" href="/{1}all/header.html"><span class="menuTitle">iNES header source</span> <span class="menuSummary">Source for the iNES header</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bank_0_1" href="/{1}all/bank_0_1.html"><span class="menuTitle">Bank 0 source (Part 1 of 5)</span> <span class="menuSummary">The contents of ROM bank 0 (first part)</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bank_0_2" href="/{1}all/bank_0_2.html"><span class="menuTitle">Bank 0 source (Part 2 of 5)</span> <span class="menuSummary">The contents of ROM bank 0 (second part)</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bank_0_3" href="/{1}all/bank_0_3.html"><span class="menuTitle">Bank 0 source (Part 3 of 5)</span> <span class="menuSummary">The contents of ROM bank 0 (third part)</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bank_0_4" href="/{1}all/bank_0_4.html"><span class="menuTitle">Bank 0 source (Part 4 of 5)</span> <span class="menuSummary">The contents of ROM bank 0 (fourth part)</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bank_0_5" href="/{1}all/bank_0_5.html"><span class="menuTitle">Bank 0 source (Part 5 of 5)</span> <span class="menuSummary">The contents of ROM bank 0 (fifth part)</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bank_1_1" href="/{1}all/bank_1_1.html"><span class="menuTitle">Bank 1 source (Part 1 of 3)</span> <span class="menuSummary">The contents of ROM bank 1 (first part)</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bank_1_2" href="/{1}all/bank_1_2.html"><span class="menuTitle">Bank 1 source (Part 2 of 3)</span> <span class="menuSummary">The contents of ROM bank 1 (second part)</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bank_1_3" href="/{1}all/bank_1_3.html"><span class="menuTitle">Bank 1 source (Part 3 of 3)</span> <span class="menuSummary">The contents of ROM bank 1 (third part)</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bank_2_1" href="/{1}all/bank_2_1.html"><span class="menuTitle">Bank 2 source (Part 1 of 4)</span> <span class="menuSummary">The contents of ROM bank 2 (first part)</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bank_2_2" href="/{1}all/bank_2_2.html"><span class="menuTitle">Bank 2 source (Part 2 of 4)</span> <span class="menuSummary">The contents of ROM bank 2 (second part)</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bank_2_3" href="/{1}all/bank_2_3.html"><span class="menuTitle">Bank 2 source (Part 3 of 4)</span> <span class="menuSummary">The contents of ROM bank 2 (third part)</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bank_2_4" href="/{1}all/bank_2_4.html"><span class="menuTitle">Bank 2 source (Part 4 of 4)</span> <span class="menuSummary">The contents of ROM bank 2 (fourth part)</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bank_3_1" href="/{1}all/bank_3_1.html"><span class="menuTitle">Bank 3 source (Part 1 of 2)</span> <span class="menuSummary">The contents of ROM bank 3 (first part)</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bank_3_2" href="/{1}all/bank_3_2.html"><span class="menuTitle">Bank 3 source (Part 2 of 2)</span> <span class="menuSummary">The contents of ROM bank 3 (second part)</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bank_4" href="/{1}all/bank_4.html"><span class="menuTitle">Bank 4 source</span> <span class="menuSummary">The contents of ROM bank 4</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bank_5" href="/{1}all/bank_5.html"><span class="menuTitle">Bank 5 source</span> <span class="menuSummary">The contents of ROM bank 5</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bank_6_1" href="/{1}all/bank_6_1.html"><span class="menuTitle">Bank 6 source (Part 1 of 3)</span> <span class="menuSummary">The contents of ROM bank 6 (first part)</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bank_6_2" href="/{1}all/bank_6_2.html"><span class="menuTitle">Bank 6 source (Part 2 of 3)</span> <span class="menuSummary">The contents of ROM bank 6 (second part)</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bank_6_3" href="/{1}all/bank_6_3.html"><span class="menuTitle">Bank 6 source (Part 3 of 3)</span> <span class="menuSummary">The contents of ROM bank 6 (third part)</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bank_7_1" href="/{1}all/bank_7_1.html"><span class="menuTitle">Bank 7 source (Part 1 of 4)</span> <span class="menuSummary">The contents of ROM bank 7 (first part)</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bank_7_2" href="/{1}all/bank_7_2.html"><span class="menuTitle">Bank 7 source (Part 2 of 4)</span> <span class="menuSummary">The contents of ROM bank 7 (second part)</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bank_7_3" href="/{1}all/bank_7_3.html"><span class="menuTitle">Bank 7 source (Part 3 of 4)</span> <span class="menuSummary">The contents of ROM bank 7 (third part)</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bank_7_4" href="/{1}all/bank_7_4.html"><span class="menuTitle">Bank 7 source (Part 4 of 4)</span> <span class="menuSummary">The contents of ROM bank 7 (fourth part)</span></a></li>
'''

if args.platform == "elite-a":
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li class="menuItemHeader">Main game encyclopedia code</li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_workspaces_encyclopedia" href="/{1}all/workspaces_encyclopedia.html"><span class="menuTitle">Encyclopedia workspaces</span> <span class="menuSummary">The main variable workspaces used in encyclopedia</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_a_encyclopedia" href="/{1}all/elite_a_encyclopedia.html"><span class="menuTitle">Elite A encyclopedia source</span> <span class="menuSummary">Part 1 of the main encyclopedia code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_b_encyclopedia" href="/{1}all/elite_b_encyclopedia.html"><span class="menuTitle">Elite B encyclopedia source</span> <span class="menuSummary">Part 2 of the main encyclopedia code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_c_encyclopedia" href="/{1}all/elite_c_encyclopedia.html"><span class="menuTitle">Elite C encyclopedia source</span> <span class="menuSummary">Part 3 of the main encyclopedia code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_d_encyclopedia" href="/{1}all/elite_d_encyclopedia.html"><span class="menuTitle">Elite D encyclopedia source</span> <span class="menuSummary">Part 4 of the main encyclopedia code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_e_encyclopedia" href="/{1}all/elite_e_encyclopedia.html"><span class="menuTitle">Elite E encyclopedia source</span> <span class="menuSummary">Part 5 of the main encyclopedia code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_f_encyclopedia" href="/{1}all/elite_f_encyclopedia.html"><span class="menuTitle">Elite F encyclopedia source</span> <span class="menuSummary">Part 6 of the main encyclopedia code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_g_encyclopedia" href="/{1}all/elite_g_encyclopedia.html"><span class="menuTitle">Elite G encyclopedia source</span> <span class="menuSummary">Part 7 of the main encyclopedia code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_h_encyclopedia" href="/{1}all/elite_h_encyclopedia.html"><span class="menuTitle">Elite H encyclopedia source</span> <span class="menuSummary">Part 8 of the main encyclopedia code</span></a></li>
'''

if args.platform == "disc":
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li class="menuItemHeader">Ship blueprint files</li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_a" href="/{1}all/elite_ships_a.html"><span class="menuTitle">Ship blueprints A source</span> <span class="menuSummary">The D.MOA ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_b" href="/{1}all/elite_ships_b.html"><span class="menuTitle">Ship blueprints B source</span> <span class="menuSummary">The D.MOB ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_c" href="/{1}all/elite_ships_c.html"><span class="menuTitle">Ship blueprints C source</span> <span class="menuSummary">The D.MOC ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_d" href="/{1}all/elite_ships_d.html"><span class="menuTitle">Ship blueprints D source</span> <span class="menuSummary">The D.MOD ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_e" href="/{1}all/elite_ships_e.html"><span class="menuTitle">Ship blueprints E source</span> <span class="menuSummary">The D.MOE ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_f" href="/{1}all/elite_ships_f.html"><span class="menuTitle">Ship blueprints F source</span> <span class="menuSummary">The D.MOF ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_g" href="/{1}all/elite_ships_g.html"><span class="menuTitle">Ship blueprints G source</span> <span class="menuSummary">The D.MOG ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_h" href="/{1}all/elite_ships_h.html"><span class="menuTitle">Ship blueprints H source</span> <span class="menuSummary">The D.MOH ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_i" href="/{1}all/elite_ships_i.html"><span class="menuTitle">Ship blueprints I source</span> <span class="menuSummary">The D.MOI ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_j" href="/{1}all/elite_ships_j.html"><span class="menuTitle">Ship blueprints J source</span> <span class="menuSummary">The D.MOJ ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_k" href="/{1}all/elite_ships_k.html"><span class="menuTitle">Ship blueprints K source</span> <span class="menuSummary">The D.MOK ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_l" href="/{1}all/elite_ships_l.html"><span class="menuTitle">Ship blueprints L source</span> <span class="menuSummary">The D.MOL ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_m" href="/{1}all/elite_ships_m.html"><span class="menuTitle">Ship blueprints M source</span> <span class="menuSummary">The D.MOM ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_n" href="/{1}all/elite_ships_n.html"><span class="menuTitle">Ship blueprints N source</span> <span class="menuSummary">The D.MON ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_o" href="/{1}all/elite_ships_o.html"><span class="menuTitle">Ship blueprints O source</span> <span class="menuSummary">The D.MOO ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_p" href="/{1}all/elite_ships_p.html"><span class="menuTitle">Ship blueprints P source</span> <span class="menuSummary">The D.MOP ship blueprints file</span></a></li>
'''

elif args.platform == "elite-a":
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li class="menuItemHeader">Ship blueprint files</li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_a" href="/{1}all/elite_ships_a.html"><span class="menuTitle">Ship blueprints A source</span> <span class="menuSummary">The S.A ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_b" href="/{1}all/elite_ships_b.html"><span class="menuTitle">Ship blueprints B source</span> <span class="menuSummary">The S.B ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_c" href="/{1}all/elite_ships_c.html"><span class="menuTitle">Ship blueprints C source</span> <span class="menuSummary">The S.C ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_d" href="/{1}all/elite_ships_d.html"><span class="menuTitle">Ship blueprints D source</span> <span class="menuSummary">The S.D ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_e" href="/{1}all/elite_ships_e.html"><span class="menuTitle">Ship blueprints E source</span> <span class="menuSummary">The S.E ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_f" href="/{1}all/elite_ships_f.html"><span class="menuTitle">Ship blueprints F source</span> <span class="menuSummary">The S.F ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_g" href="/{1}all/elite_ships_g.html"><span class="menuTitle">Ship blueprints G source</span> <span class="menuSummary">The S.G ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_h" href="/{1}all/elite_ships_h.html"><span class="menuTitle">Ship blueprints H source</span> <span class="menuSummary">The S.H ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_i" href="/{1}all/elite_ships_i.html"><span class="menuTitle">Ship blueprints I source</span> <span class="menuSummary">The S.I ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_j" href="/{1}all/elite_ships_j.html"><span class="menuTitle">Ship blueprints J source</span> <span class="menuSummary">The S.J ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_k" href="/{1}all/elite_ships_k.html"><span class="menuTitle">Ship blueprints K source</span> <span class="menuSummary">The S.K ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_l" href="/{1}all/elite_ships_l.html"><span class="menuTitle">Ship blueprints L source</span> <span class="menuSummary">The S.L ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_m" href="/{1}all/elite_ships_m.html"><span class="menuTitle">Ship blueprints M source</span> <span class="menuSummary">The S.M ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_n" href="/{1}all/elite_ships_n.html"><span class="menuTitle">Ship blueprints N source</span> <span class="menuSummary">The S.N ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_o" href="/{1}all/elite_ships_o.html"><span class="menuTitle">Ship blueprints O source</span> <span class="menuSummary">The S.O ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_p" href="/{1}all/elite_ships_p.html"><span class="menuTitle">Ship blueprints P source</span> <span class="menuSummary">The S.P ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_q" href="/{1}all/elite_ships_q.html"><span class="menuTitle">Ship blueprints Q source</span> <span class="menuSummary">The S.Q ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_r" href="/{1}all/elite_ships_r.html"><span class="menuTitle">Ship blueprints R source</span> <span class="menuSummary">The S.R ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_s" href="/{1}all/elite_ships_s.html"><span class="menuTitle">Ship blueprints S source</span> <span class="menuSummary">The S.S ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_t" href="/{1}all/elite_ships_t.html"><span class="menuTitle">Ship blueprints T source</span> <span class="menuSummary">The S.T ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_u" href="/{1}all/elite_ships_u.html"><span class="menuTitle">Ship blueprints U source</span> <span class="menuSummary">The S.U ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_v" href="/{1}all/elite_ships_v.html"><span class="menuTitle">Ship blueprints V source</span> <span class="menuSummary">The S.V ship blueprints file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_w" href="/{1}all/elite_ships_w.html"><span class="menuTitle">Ship blueprints W source</span> <span class="menuSummary">The S.W ship blueprints file</span></a></li>
'''

if args.platform == "cassette":
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships" href="/{1}all/elite_ships.html"><span class="menuTitle">Ship blueprints</span> <span class="menuSummary">Data for the 13 different ship designs</span></a></li>
\t\t\t\t\t\t\t<li class="menuItemHeader">Big Code File</li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bcfs" href="/{1}all/bcfs.html"><span class="menuTitle">Big Code File source</span> <span class="menuSummary">Concatenates the individual source code parts into one big game file</span></a></li>
'''

elif args.platform == "electron":
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships" href="/{1}all/elite_ships.html"><span class="menuTitle">Ship blueprints</span> <span class="menuSummary">Data for the 11 different ship designs</span></a></li>
\t\t\t\t\t\t\t<li class="menuItemHeader">Big Code File</li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bcfs" href="/{1}all/bcfs.html"><span class="menuTitle">Big Code File source</span> <span class="menuSummary">Concatenates the individual source code parts into one big game file</span></a></li>
'''

elif args.platform == "6502sp":
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_h" href="/{1}all/elite_h.html"><span class="menuTitle">Elite H source</span> <span class="menuSummary">Part 8 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_i" href="/{1}all/elite_i.html"><span class="menuTitle">Elite I source</span> <span class="menuSummary">Part 9 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_j" href="/{1}all/elite_j.html"><span class="menuTitle">Elite J source</span> <span class="menuSummary">Part 10 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships" href="/{1}all/elite_ships.html"><span class="menuTitle">Ship blueprints</span> <span class="menuSummary">Data for the 33 different ship designs</span></a></li>
'''
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li class="menuItemHeader">I/O processor source</li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_i_o_processor" href="/{1}all/i_o_processor.html"><span class="menuTitle">I/O processor source</span> <span class="menuSummary">The I/O processor source</span></a></li>
'''
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li class="menuItemHeader">Big Code File</li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bcfs" href="/{1}all/bcfs.html"><span class="menuTitle">Big Code File source</span> <span class="menuSummary">Concatenates the individual source code parts into one big game file</span></a></li>
'''

elif args.platform == "c64":
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li class="menuItemHeader">Game data</li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_data" href="/{1}all/elite_data.html"><span class="menuTitle">Game data source</span> <span class="menuSummary">The game data file, which contains the ship blueprints and text tokens</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships" href="/{1}all/elite_ships.html"><span class="menuTitle">Ship blueprints</span> <span class="menuSummary">Data for the 33 different ship designs</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_text_tokens" href="/{1}all/text_tokens.html"><span class="menuTitle">Text tokens</span> <span class="menuSummary">Elite's tokenised game text</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_sprites" href="/{1}all/elite_sprites.html"><span class="menuTitle">Sprites</span> <span class="menuSummary">Sprite definitions for the laser sights, explosions and Trumbles</span></a></li>
'''

elif args.platform == "apple":
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li class="menuItemHeader">Game data</li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_data" href="/{1}all/elite_data.html"><span class="menuTitle">Game data source</span> <span class="menuSummary">The game data file, which contains the ship blueprints and text tokens</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships" href="/{1}all/elite_ships.html"><span class="menuTitle">Ship blueprints</span> <span class="menuSummary">Data for the 33 different ship designs</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_text_tokens" href="/{1}all/text_tokens.html"><span class="menuTitle">Text tokens</span> <span class="menuSummary">Elite's tokenised game text</span></a></li>
'''
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li class="menuItemHeader">Big Code File</li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_bcfs" href="/{1}all/bcfs.html"><span class="menuTitle">Big Code File source</span> <span class="menuSummary">Concatenates the individual source code parts into one big game file</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_transfer" href="/{1}all/transfer_program.html"><span class="menuTitle">Transfer program</span> <span class="menuSummary">Wraps the game binaries for serial transfer or disk loading</span></a></li>
'''

elif args.platform == "master":
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li class="menuItemHeader">Game data</li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_data" href="/{1}all/elite_data.html"><span class="menuTitle">Game data source</span> <span class="menuSummary">The game data file, which contains the dashboard image, ship blueprints and text tokens</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships" href="/{1}all/elite_ships.html"><span class="menuTitle">Ship blueprints</span> <span class="menuSummary">Data for the 33 different ship designs</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_text_tokens" href="/{1}all/text_tokens.html"><span class="menuTitle">Text tokens</span> <span class="menuSummary">Elite's tokenised game text</span></a></li>
'''

elif args.platform == "elite-a":
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li class="menuItemHeader">6502 Second Processor source</li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_i_o_processor" href="/{1}all/i_o_processor.html"><span class="menuTitle">I/O processor source</span> <span class="menuSummary">The I/O processor source</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_workspaces_parasite" href="/{1}all/workspaces_parasite.html"><span class="menuTitle">Parasite workspaces</span> <span class="menuSummary">The main variable workspaces used when parasite</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_a_parasite" href="/{1}all/elite_a_parasite.html"><span class="menuTitle">Elite A parasite source</span> <span class="menuSummary">Part 1 of the main parasite code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_b_parasite" href="/{1}all/elite_b_parasite.html"><span class="menuTitle">Elite B parasite source</span> <span class="menuSummary">Part 2 of the main parasite code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_c_parasite" href="/{1}all/elite_c_parasite.html"><span class="menuTitle">Elite C parasite source</span> <span class="menuSummary">Part 3 of the main parasite code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_d_parasite" href="/{1}all/elite_d_parasite.html"><span class="menuTitle">Elite D parasite source</span> <span class="menuSummary">Part 4 of the main parasite code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_e_parasite" href="/{1}all/elite_e_parasite.html"><span class="menuTitle">Elite E parasite source</span> <span class="menuSummary">Part 5 of the main parasite code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_f_parasite" href="/{1}all/elite_f_parasite.html"><span class="menuTitle">Elite F parasite source</span> <span class="menuSummary">Part 6 of the main parasite code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_g_parasite" href="/{1}all/elite_g_parasite.html"><span class="menuTitle">Elite G parasite source</span> <span class="menuSummary">Part 7 of the main parasite code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_h_parasite" href="/{1}all/elite_h_parasite.html"><span class="menuTitle">Elite H parasite source</span> <span class="menuSummary">Part 8 of the main parasite code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_i_parasite" href="/{1}all/elite_i_parasite.html"><span class="menuTitle">Elite I parasite source</span> <span class="menuSummary">Part 9 of the main parasite code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_j_parasite" href="/{1}all/elite_j_parasite.html"><span class="menuTitle">Elite J parasite source</span> <span class="menuSummary">Part 10 of the main parasite code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_k_parasite" href="/{1}all/elite_k_parasite.html"><span class="menuTitle">Elite K parasite source</span> <span class="menuSummary">Part 11 of the main parasite code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_l_parasite" href="/{1}all/elite_l_parasite.html"><span class="menuTitle">Elite L parasite source</span> <span class="menuSummary">Part 12 of the main parasite code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_m_parasite" href="/{1}all/elite_m_parasite.html"><span class="menuTitle">Elite M parasite source</span> <span class="menuSummary">Part 13 of the main parasite code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_elite_ships_parasite" href="/{1}all/elite_ships_parasite.html"><span class="menuTitle">Ship blueprints parasite source</span> <span class="menuSummary">Data for ships in the parasite</span></a></li>
'''

if args.platform == "aviator":
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li class="menuItemHeader">Aviator source files</li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_workspaces" href="/{1}all/workspaces.html"><span class="menuTitle">Workspaces and configuration</span> <span class="menuSummary">The main variable workspaces used in Aviator</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_aviator_a" href="/{1}all/aviator_a.html"><span class="menuTitle">Aviator A source</span> <span class="menuSummary">Part 1 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_aviator_b" href="/{1}all/aviator_b.html"><span class="menuTitle">Aviator B source</span> <span class="menuSummary">Part 2 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_aviator_c" href="/{1}all/aviator_c.html"><span class="menuTitle">Aviator C source</span> <span class="menuSummary">Part 3 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_aviator_d" href="/{1}all/aviator_d.html"><span class="menuTitle">Aviator D source</span> <span class="menuSummary">Part 4 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_aviator_e" href="/{1}all/aviator_e.html"><span class="menuTitle">Aviator E source</span> <span class="menuSummary">Part 5 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_aviator_f" href="/{1}all/aviator_f.html"><span class="menuTitle">Aviator F source</span> <span class="menuSummary">Part 6 of the main game code</span></a></li>
'''

if args.platform == "revs":
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li class="menuItemHeader">Revs source files</li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_workspaces" href="/{1}all/workspaces.html"><span class="menuTitle">Workspaces and configuration</span> <span class="menuSummary">The main variable workspaces used in Revs</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_revs_a" href="/{1}all/revs_a.html"><span class="menuTitle">Revs A source</span> <span class="menuSummary">Part 1 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_revs_b" href="/{1}all/revs_b.html"><span class="menuTitle">Revs B source</span> <span class="menuSummary">Part 2 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_revs_c" href="/{1}all/revs_c.html"><span class="menuTitle">Revs C source</span> <span class="menuSummary">Part 3 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_revs_d" href="/{1}all/revs_d.html"><span class="menuTitle">Revs D source</span> <span class="menuSummary">Part 4 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_revs_e" href="/{1}all/revs_e.html"><span class="menuTitle">Revs E source</span> <span class="menuSummary">Part 5 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_revs_f" href="/{1}all/revs_f.html"><span class="menuTitle">Revs F source</span> <span class="menuSummary">Part 6 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_revs_g" href="/{1}all/revs_g.html"><span class="menuTitle">Revs G source</span> <span class="menuSummary">Part 7 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_revs_h" href="/{1}all/revs_h.html"><span class="menuTitle">Revs H source</span> <span class="menuSummary">Part 8 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_revs_i" href="/{1}all/revs_i.html"><span class="menuTitle">Revs I source</span> <span class="menuSummary">Part 9 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li class="menuItemHeader">Track data files</li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_revs_silverstone" href="/{1}all/revs_silverstone.html"><span class="menuTitle">Silverstone track data file</span> <span class="menuSummary">Data for the Silverstone track</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_revs_brands_hatch" href="/{1}all/revs_brands_hatch.html"><span class="menuTitle">Brands Hatch track data file</span> <span class="menuSummary">Data for the Brands Hatch track</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_revs_donington_park" href="/{1}all/revs_donington_park.html"><span class="menuTitle">Donington Park track data file</span> <span class="menuSummary">Data for the Donington Park track</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_revs_oulton_park" href="/{1}all/revs_oulton_park.html"><span class="menuTitle">Oulton Park track data file</span> <span class="menuSummary">Data for the Oulton Park track</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_revs_snetterton" href="/{1}all/revs_snetterton.html"><span class="menuTitle">Snetterton track data file</span> <span class="menuSummary">Data for the Snetterton track</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_revs_nurburgring" href="/{1}all/revs_nurburgring.html"><span class="menuTitle">Nürburgring track data file</span> <span class="menuSummary">Data for the Nürburgring track</span></a></li>
'''

if args.platform == "lander":
    html_indexes = html_indexes + '''\t\t\t\t\t\t\t<li class="menuItemHeader">Lander source files</li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_workspaces" href="/{1}all/workspaces.html"><span class="menuTitle">Workspaces and configuration</span> <span class="menuSummary">The main variable workspaces used in Lander</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_lander_a" href="/{1}all/lander_a.html"><span class="menuTitle">Lander A source</span> <span class="menuSummary">Part 1 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_lander_b" href="/{1}all/lander_b.html"><span class="menuTitle">Lander B source</span> <span class="menuSummary">Part 2 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_lander_c" href="/{1}all/lander_c.html"><span class="menuTitle">Lander C source</span> <span class="menuSummary">Part 3 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_lander_d" href="/{1}all/lander_d.html"><span class="menuTitle">Lander D source</span> <span class="menuSummary">Part 4 of the main game code</span></a></li>
\t\t\t\t\t\t\t<li><a id="{3}all_source_runimage" href="/{1}all/runimage.html"><span class="menuTitle">!RunImage source</span> <span class="menuSummary">The !RunImage source for RISC OS</span></a></li>
'''

html_indexes = html_indexes + '''\t\t\t\t\t\t</ul>
\t\t\t\t\t</li>
\t\t\t\t\t<li class="menuItemHeader showForMobile">{2} source code by category</li>
'''

html_compare_indexes = '''\t\t\t\t\t<li class="menuItemHeader">Versions and variants</li>
\t\t\t\t\t<li><a id="compare_sources_versions_of_elite" href="/compare/versions_of_elite.html"><span class="menuTitle">Versions of Elite on the 6502</span> <span class="menuSummary">From the humble BBC Micro cassette to the 6502 Second Processor and beyond</span></a></li>
\t\t\t\t\t<li><a id="compare_sources_feature_comparison" href="/compare/feature_comparison.html"><span class="menuTitle">Feature comparison table</span> <span class="menuSummary">A comprehensive table comparing features of the different versions of Elite on the 6502</span></a></li>
\t\t\t\t\t<li><a id="compare_sources_releases" href="/compare/releases.html"><span class="menuTitle">Different variants of each version</span> <span class="menuSummary">Bug fixes, unofficial versions and extra platforms</span></a></li>
\t\t\t\t\t<li class="menuItemHeader">Explore all the code variations in Acornsoft Elite</li>
\t\t\t\t\t<li><a id="compare_sources_how_to_compare" href="/compare/how_to_compare.html"><span class="menuTitle">How to compare the Acornsoft versions of Elite</span> <span class="menuSummary">A quick guide to using this section to compare the different versions of Acornsoft Elite</span></a></li>
\t\t\t\t\t<li id="compare_shared"><span class="menuTitle">Code comparisons of different versions</span> <span class="menuSummary menuSummarySubmenu">Code-level comparisons of features that occur in multiple versions of Acornsoft Elite</span>
\t\t\t\t\t\t<ul id="submenu_compare_shared">
\t\t\t\t\t\t\t<li class="menuItemHeader">Compare the main versions</li>
'''
html_compare_category_index = '''\t\t\t\t\t\t\t<li><a id="compare_shared_shared_code_{1}" href="/compare/indexes/shared_code_{1}.html"><span class="menuTitle">{0}</span> <span class="menuSummary">{2}</span></a></li>
'''
html_compare_category_index_subheader = '''\t\t\t\t\t\t\t<li class="menuItemHeader">Compare other versions</li>
'''
html_compare_indexes2 = '''\t\t\t\t\t\t\t<li><a id="compare_shared_shared_code_other_variations" href="/compare/indexes/shared_code_other_variations.html"><span class="menuTitle">Minor variations between versions</span> <span class="menuSummary">Smaller differences between the versions that don't have a noticeable effect in-game</span></a></li>
\t\t\t\t\t\t</ul>
\t\t\t\t\t</li>
\t\t\t\t\t<li class="menuItemHeader showForMobile">All code variations by category</li>
'''

html_prev_next = '''
\t\t\t\t<div class="codeBlockWrapper nav">
\t\t\t\t\t<nav class="codeBlock previousNext"><a class="previous" rel="prev" title="Previous routine" href="/{}">{}</a><a class="next" rel="next" title="Next routine" href="/{}">{}</a></nav>
\t\t\t\t</div>
'''
html_prev = '''
\t\t\t\t<div class="codeBlockWrapper nav">
\t\t\t\t\t<nav class="codeBlock previousNext"><a class="previous" rel="prev" title="Previous routine" href="/{}">{}</a></nav>
\t\t\t\t</div>
'''
html_next = '''
\t\t\t\t<div class="codeBlockWrapper nav">
\t\t\t\t\t<nav class="codeBlock previousNext"><a class="next" rel="next" title="Next routine" href="/{}">{}</a></nav>
\t\t\t\t</div>
'''

if args.platform == "cassette":
    html_large_source_code_page_links = '''<p>This page contains a map of all the routines, variables and macros in the original source files for the BBC Micro cassette version of Elite, in the order in which they appear in the original source. The source files are structured like this:</p>
<ul>
<li>The <a href="#header-loader">Loader</a>, which displays the loading screen, implements the copy protection and sets things up for the main game</li>
<li>The main game source, which consists of <a href="#header-workspaces">Workspaces</a>, <a href="#header-text-tokens">Text tokens</a>, <a href="#header-elite-a">Elite A</a>, <a href="#header-elite-b">Elite B</a>, <a href="#header-elite-c">Elite C</a>, <a href="#header-elite-d">Elite D</a>, <a href="#header-elite-e">Elite E</a>, <a href="#header-elite-f">Elite F</a>, <a href="#header-elite-g">Elite G</a> and <a href="#header-ship-blueprints">Ship blueprints</a></li>
<li>The <a href="#header-big-code-file">Big Code File</a>, which concatenates the files produced by the above and adds a bit more copy protection</li>
</ul>

<p>You can click on the links above to jump to the relevant part of the map.</p>

'''
elif args.platform == "electron":
    html_large_source_code_page_links = '''<p>This page contains a map of all the routines, variables and macros in the original source files for the Electron version of Elite, in the order in which they appear in the original source. The source files are structured like this:</p>
<ul>
<li>The <a href="#header-loader">Loader</a>, which displays the loading screen, implements the copy protection and sets things up for the main game</li>
<li>The main game source, which consists of <a href="#header-workspaces">Workspaces</a>, <a href="#header-text-tokens">Text tokens</a>, <a href="#header-elite-a">Elite A</a>, <a href="#header-elite-b">Elite B</a>, <a href="#header-elite-c">Elite C</a>, <a href="#header-elite-d">Elite D</a>, <a href="#header-elite-e">Elite E</a>, <a href="#header-elite-f">Elite F</a>, <a href="#header-elite-g">Elite G</a> and <a href="#header-ship-blueprints">Ship blueprints</a></li>
<li>The Big Code File, which concatenates the files produced by the above (but which doesn't contain any code, so there is no entry below)</li>
</ul>

<p>You can click on the links above to jump to the relevant part of the map.</p>

'''
elif args.platform == "disc":
    html_large_source_code_page_links = '''<p>This page contains a map of all the routines, variables and macros in the BBC Micro disc version of Elite. The source files are structured like this:</p>
<ul>
<li>The three loader sources, <a href="#header-loader-1">Loader 1</a>, <a href="#header-loader-2">Loader 2</a> and <a href="#header-loader-3">Loader 3</a>, which display the loading screen, implement the copy protection and set things up for the main game</li>
<li>The <a href="#header-sideways-ram-loader">sideways RAM loader</a>, which replaces the three original loaders in the sideways RAM variant</li>
<li>The <a href="#header-text-tokens">Text tokens</a> and <a href="#header-missile-ship-blueprint">Missile ship blueprint</a>, which are bundled as part of Loader 3 and get unpacked during the loading process</li>
<li>The main game source for when we are docked, which consists of <a href="#header-workspaces-docked">Workspaces</a>, <a href="#header-elite-a-docked">Elite A</a>, <a href="#header-elite-b-docked">Elite B</a>, <a href="#header-elite-c-docked">Elite C</a>, <a href="#header-elite-d-docked">Elite D</a>, <a href="#header-elite-e-docked">Elite E</a>, <a href="#header-elite-f-docked">Elite F</a>, <a href="#header-elite-g-docked">Elite G</a>, <a href="#header-elite-h-docked">Elite H</a> and <a href="#header-ship-hangar-blueprints">Ship hangar blueprints</a></li>
<li>The main game source for flight, which consists of <a href="#header-workspaces-flight">Workspaces</a>, <a href="#header-elite-a-flight">Elite A</a>, <a href="#header-elite-b-flight">Elite B</a>, <a href="#header-elite-c-flight">Elite C</a>, <a href="#header-elite-d-flight">Elite D</a>, <a href="#header-elite-e-flight">Elite E</a>, <a href="#header-elite-f-flight">Elite F</a>, <a href="#header-elite-g-flight">Elite G</a> and <a href="#header-elite-h-flight">Elite H</a></li>
<li>The 16 ship blueprint files, one of which gets loaded on launching from the station: <a href="#header-ship-blueprints-a">A</a>, <a href="#header-ship-blueprints-b">B</a>, <a href="#header-ship-blueprints-c">C</a>, <a href="#header-ship-blueprints-d">D</a>, <a href="#header-ship-blueprints-e">E</a>, <a href="#header-ship-blueprints-f">F</a>, <a href="#header-ship-blueprints-g">G</a>, <a href="#header-ship-blueprints-h">H</a>, <a href="#header-ship-blueprints-i">I</a>, <a href="#header-ship-blueprints-j">J</a>, <a href="#header-ship-blueprints-k">K</a>, <a href="#header-ship-blueprints-l">L</a>, <a href="#header-ship-blueprints-m">M</a>, <a href="#header-ship-blueprints-n">N</a>, <a href="#header-ship-blueprints-o">O</a> and <a href="#header-ship-blueprints-p">P</a>.</li>
</ul>

<p>You can click on the links above to jump to the relevant part of the map.</p>

'''
elif args.platform == "6502sp":
    html_large_source_code_page_links = '''<p>This page contains a map of all the routines, variables and macros in the original source files for the 6502 Second Processor version of Elite, in the order in which they appear in the original source. The source files are structured like this:</p>
<ul>
<li>The two loader sources, <a href="#header-loader-1">Loader 1</a> and <a href="#header-loader-2">Loader 2</a>, which display the loading screen, implement the copy protection and set things up for the main game</li>
<li>The main game source, which consists of <a href="#header-workspaces">Workspaces</a>, <a href="#header-text-tokens">Text tokens</a>, <a href="#header-elite-a">Elite A</a>, <a href="#header-elite-b">Elite B</a>, <a href="#header-elite-c">Elite C</a>, <a href="#header-elite-d">Elite D</a>, <a href="#header-elite-e">Elite E</a>, <a href="#header-elite-f">Elite F</a>, <a href="#header-elite-g">Elite G</a>, <a href="#header-elite-h">Elite H</a>, <a href="#header-elite-i">Elite I</a>, <a href="#header-elite-j">Elite J</a> and <a href="#header-ship-blueprints">Ship blueprints</a></li>
<li>The <a href="#header-i-o-processor">I/O processor</a> source, which runs on the BBC Micro and handles the screen, keyboard etc.</li>
<li>The Big Code File, which concatenates the files produced by the above (but which doesn't contain any code, so there is no entry below)</li>
</ul>

<p>You can click on the links above to jump to the relevant part of the map.</p>

'''
elif args.platform == "c64":
    html_large_source_code_page_links = '''<p>This page contains a map of all the routines, variables and macros in the Commodore 64 version of Elite. The source files are structured like this:</p>
<ul>
<li>The two disk loader sources, <a href="#header-disk-loader-1">Disk Loader 1</a> and <a href="#header-disk-loader-2">Disk Loader 2</a>, which boot the disk and load the game loader and game binaries</li>
<li>The <a href="#header-game-loader">Game Loader</a>, which loads and decrypts the game data</li>
<li>The main game source, which consists of <a href="#header-workspaces">Workspaces</a>, <a href="#header-elite-a">Elite A</a>, <a href="#header-elite-b">Elite B</a>, <a href="#header-elite-c">Elite C</a>, <a href="#header-elite-d">Elite D</a>, <a href="#header-elite-e">Elite E</a>, <a href="#header-elite-f">Elite F</a>, <a href="#header-elite-g">Elite G</a>, <a href="#header-elite-h">Elite H</a>, <a href="#header-elite-i">Elite I</a>, <a href="#header-elite-j">Elite J</a> and <a href="#header-elite-k">Elite K</a></li>
<li>The <a href="#header-game-data">Game data</a> source, which contains game images, ship blueprints and text tokens</li>
<li>The <a href="#header-sprites">Sprites</a> source, which contains sprite definitions for the laser sights, explosions and Trumbles</li>
</ul>

<p>You can click on the links above to jump to the relevant part of the map.</p>

'''
elif args.platform == "apple":
    html_large_source_code_page_links = '''<p>This page contains a map of all the routines, variables and macros in the Apple II version of Elite. The source files are structured like this:</p>
<ul>
<li>The <a href="#header-loader">Loader</a>, which loads the game data, game binaries and loading screen</li>
<li>The main game source, which consists of <a href="#header-workspaces">Workspaces</a>, <a href="#header-elite-a">Elite A</a>, <a href="#header-elite-b">Elite B</a>, <a href="#header-elite-c">Elite C</a>, <a href="#header-elite-d">Elite D</a>, <a href="#header-elite-e">Elite E</a>, <a href="#header-elite-f">Elite F</a>, <a href="#header-elite-g">Elite G</a>, <a href="#header-elite-h">Elite H</a>, <a href="#header-elite-i">Elite I</a>, <a href="#header-elite-j">Elite J</a> and <a href="#header-elite-k">Elite K</a></li>
<li>The <a href="#header-game-data">Game data</a> source, which contains game images, ship blueprints and text tokens</li>
<li>The Big Code File, which concatenates the files produced by the above (but which doesn't contain any code, so there is no entry below)</li>
<li>The <a href="#header-transfer-program">Transfer program</a>, which wraps the game binaries up for serial transfer to an Apple II or loading from disk</li>
</ul>

<p>You can click on the links above to jump to the relevant part of the map.</p>

'''
elif args.platform == "master":
    html_large_source_code_page_links = '''<p>This page contains a map of all the routines, variables and macros in the BBC Master version of Elite. The source files are structured like this:</p>
<ul>
<li>The <a href="#header-loader">Loader</a>, which displays the loading screen, implements the copy protection and sets things up for the main game</li>
<li>The main game source, which consists of <a href="#header-workspaces">Workspaces</a>, <a href="#header-elite-a">Elite A</a>, <a href="#header-elite-b">Elite B</a>, <a href="#header-elite-c">Elite C</a>, <a href="#header-elite-d">Elite D</a>, <a href="#header-elite-e">Elite E</a>, <a href="#header-elite-f">Elite F</a>, <a href="#header-elite-g">Elite G</a> and <a href="#header-elite-h">Elite H</a></li>
<li>The <a href="#header-game-data">Game data</a> source, which contains game images, ship blueprints and text tokens</li>
</ul>

<p>You can click on the links above to jump to the relevant part of the map.</p>

'''
elif args.platform == "elite-a":
    html_large_source_code_page_links = '''<p>This page contains a map of all the routines, variables and macros in Elite-A, Angus Duggan's modified version of BBC Micro disc Elite. The source files are structured like this:</p>
<ul>
<li>The <a href="#header-loader">Loader</a>, which displays the loading screen, checks for Tube and BBC Master hardware, and sets things up for the main game.</li>
<li>The <a href="#header-text-tokens">Text tokens</a> and <a href="#header-missile-ship-blueprint">Missile ship blueprint</a>, which are bundled as part of the loader and get unpacked during the loading process.</li>
<li>The main game source for when we are docked, which consists of <a href="#header-workspaces-docked">Workspaces</a>, <a href="#header-elite-a-docked">Elite A</a>, <a href="#header-elite-b-docked">Elite B</a>, <a href="#header-elite-c-docked">Elite C</a>, <a href="#header-elite-d-docked">Elite D</a>, <a href="#header-elite-e-docked">Elite E</a>, <a href="#header-elite-f-docked">Elite F</a>, <a href="#header-elite-g-docked">Elite G</a>, <a href="#header-elite-h-docked">Elite H</a> and <a href="#header-ship-hangar-blueprints">Ship hangar blueprints</a>.</li>
<li>The main game source for flight, which consists of <a href="#header-workspaces-flight">Workspaces</a>, <a href="#header-elite-a-flight">Elite A</a>, <a href="#header-elite-b-flight">Elite B</a>, <a href="#header-elite-c-flight">Elite C</a>, <a href="#header-elite-d-flight">Elite D</a>, <a href="#header-elite-e-flight">Elite E</a>, <a href="#header-elite-f-flight">Elite F</a>, <a href="#header-elite-g-flight">Elite G</a> and <a href="#header-elite-h-flight">Elite H</a>.</li>
<li>The main game source for the encyclopedia, which consists of <a href="#header-workspaces-encyclopedia">Workspaces</a>, <a href="#header-elite-a-encyclopedia">Elite A</a>, <a href="#header-elite-b-encyclopedia">Elite B</a>, <a href="#header-elite-c-encyclopedia">Elite C</a>, <a href="#header-elite-d-encyclopedia">Elite D</a>, <a href="#header-elite-e-encyclopedia">Elite E</a>, <a href="#header-elite-f-encyclopedia">Elite F</a>, <a href="#header-elite-g-encyclopedia">Elite G</a> and <a href="#header-elite-h-encyclopedia">Elite H</a>.</li>
<li>The 23 ship blueprint files, one of which gets loaded on launching from the station: <a href="#header-ship-blueprints-a">A</a>, <a href="#header-ship-blueprints-b">B</a>, <a href="#header-ship-blueprints-c">C</a>, <a href="#header-ship-blueprints-d">D</a>, <a href="#header-ship-blueprints-e">E</a>, <a href="#header-ship-blueprints-f">F</a>, <a href="#header-ship-blueprints-g">G</a>, <a href="#header-ship-blueprints-h">H</a>, <a href="#header-ship-blueprints-i">I</a>, <a href="#header-ship-blueprints-j">J</a>, <a href="#header-ship-blueprints-k">K</a>, <a href="#header-ship-blueprints-l">L</a>, <a href="#header-ship-blueprints-m">M</a>, <a href="#header-ship-blueprints-n">N</a>, <a href="#header-ship-blueprints-o">O</a>, <a href="#header-ship-blueprints-p">P</a>, <a href="#header-ship-blueprints-q">Q</a>, <a href="#header-ship-blueprints-r">R</a>, <a href="#header-ship-blueprints-s">S</a>, <a href="#header-ship-blueprints-t">T</a>, <a href="#header-ship-blueprints-u">U</a>, <a href="#header-ship-blueprints-v">V</a> and <a href="#header-ship-blueprints-w">W</a>.</li>
<li>The 6502 Second Processor version of the game, which consists of the <a href="#header-i-o-processor">I/O processor</a> source, which runs on the BBC Micro, and the parasite source, which runs on the 6502 Second Processor and consists of <a href="#header-workspaces-parasite">Workspaces</a>, <a href="#header-elite-a-parasite">Elite A</a>, <a href="#header-elite-b-parasite">Elite B</a>, <a href="#header-elite-c-parasite">Elite C</a>, <a href="#header-elite-d-parasite">Elite D</a>, <a href="#header-elite-e-parasite">Elite E</a>, <a href="#header-elite-f-parasite">Elite F</a>, <a href="#header-elite-g-parasite">Elite G</a>, <a href="#header-elite-h-parasite">Elite H</a>, <a href="#header-elite-i-parasite">Elite I</a>, <a href="#header-elite-j-parasite">Elite J</a>, <a href="#header-elite-k-parasite">Elite K</a>, <a href="#header-elite-l-parasite">Elite L</a>, <a href="#header-elite-m-parasite">Elite M</a> and <a href="#header-ship-blueprints-parasite">Ship blueprints</a>.</li>
</ul>

<p>You can click on the links above to jump to the relevant part of the map.</p>

'''
elif args.platform == "nes":
    html_large_source_code_page_links = '''<p>This page contains a map of all the routines, variables and macros in the NES version of Elite. To make them easier to browse on the web, ROM banks with large source code files have been split into smaller parts, though each bank still produces exactly 16K when assembled. The source files are structured like this:</p>
<ul>
<li>The <a href="#header-common">common game code</a>, which contains variable and macro definitions used throughout the code.</li>
<li>The <a href="#header-ines-header">iNES header</a>, which tells emulators how to configure the ROM cartridge for emulation.</li>
<li>Bank 7 (part <a href="#header-bank-7-part-1-of-4">1</a>, <a href="#header-bank-7-part-2-of-4">2</a>, <a href="#header-bank-7-part-3-of-4">3</a>, <a href="#header-bank-7-part-4-of-4">4</a>), which is the only ROM bank that remains in memory at all times, swapping banks 0 to 6 in and out of memory as required.</li>
<li>The seven ROM banks that contain most of the game code, and which are swapped in and out of memory by bank 7: bank 0 (part <a href="#header-bank-0-part-1-of-5">1</a>, <a href="#header-bank-0-part-2-of-5">2</a>, <a href="#header-bank-0-part-3-of-5">3</a>, <a href="#header-bank-0-part-4-of-5">4</a>, <a href="#header-bank-0-part-5-of-5">5</a>), bank 1 (part <a href="#header-bank-1-part-1-of-3">1</a>, <a href="#header-bank-1-part-2-of-3">2</a>, <a href="#header-bank-1-part-3-of-3">3</a>), bank 2 (part <a href="#header-bank-2-part-1-of-4">1</a>, <a href="#header-bank-2-part-2-of-4">2</a>, <a href="#header-bank-2-part-3-of-4">3</a>, <a href="#header-bank-2-part-4-of-4">4</a>), bank 3 (part <a href="#header-bank-3-part-1-of-2">1</a>, <a href="#header-bank-3-part-2-of-2">2</a>), <a href="#header-bank-4">bank 4</a>, <a href="#header-bank-5">bank 5</a> and bank 6 (part <a href="#header-bank-6-part-1-of-3">1</a>, <a href="#header-bank-6-part-2-of-3">2</a>, <a href="#header-bank-6-part-3-of-3">3</a>).</li>
</ul>

<p>You can click on the links above to jump to the relevant part of the map.</p>

'''
elif args.platform == "aviator":
    html_large_source_code_page_links = '''<p>This page contains a map of all the routines and variables in the original version of Aviator, in the order in which they appear in the original source. The source files are structured like this:</p>
<ul>
<li>The main game source, which consists of <a href="#header-workspaces">Workspaces</a>, <a href="#header-aviator-a">Aviator A</a>, <a href="#header-aviator-b">Aviator B</a>, <a href="#header-aviator-c">Aviator C</a>, <a href="#header-aviator-d">Aviator D</a>, <a href="#header-aviator-e">Aviator E</a> and <a href="#header-aviator-f">Aviator F</a></li>
</ul>

<p>You can click on the links above to jump to the relevant part of the map.</p>

'''
elif args.platform == "revs":
    html_large_source_code_page_links = '''<p>This page contains a map of all the routines and variables in the original version of Revs, in the order in which they appear in the original source. The source files are structured like this:</p>
<ul>
<li>The main game source, which consists of <a href="#header-workspaces">Workspaces</a>, <a href="#header-revs-a">Revs A</a>, <a href="#header-revs-b">Revs B</a>, <a href="#header-revs-c">Revs C</a>, <a href="#header-revs-d">Revs D</a>, <a href="#header-revs-e">Revs E</a>, <a href="#header-revs-f">Revs F</a>, <a href="#header-revs-g">Revs G</a>, <a href="#header-revs-h">Revs H</a> and <a href="#header-revs-i">Revs I</a></li>
<li>The track data files for <a href="#header-silverstone-track-data-file">Silverstone</a>, <a href="#header-brands-hatch-track-data-file">Brands Hatch</a>,  <a href="#header-donington-park-track-data-file">Donington Park</a>, <a href="#header-oulton-park-track-data-file">Oulton Park</a>, <a href="#header-snetterton-track-data-file">Snetterton</a> and the <a href="#header-nurburgring-track-data-file">Nürburgring</a></li>
</ul>

<p>You can click on the links above to jump to the relevant part of the map.</p>

'''
elif args.platform == "lander":
    html_large_source_code_page_links = '''<p>This page contains a map of all the routines and variables in the original version of Lander, in the order in which they appear in the original source. The source files are structured like this:</p>
<ul>
<li>The main game source, which consists of <a href="#header-lander-a">Lander A</a>, <a href="#header-lander-b">Lander B</a>, <a href="#header-lander-c">Lander C</a> and <a href="#header-lander-d">Lander D</a></li>
<li>The <a href="#header-runimage">!RunImage source</a> for the RISC OS version</li>
</ul>

<p>You can click on the links above to jump to the relevant part of the map.</p>

'''

if args.platform == "aviator" or args.platform == "lander":
    html_source_code_stats_intro = '''<p>Here's a statistical breakdown of the source code for {}. Click on the table headers to sort by that statistic. For more information, see the notes after the table.</p>
'''
    html_source_code_stats_footer = '''<p>Some notes on the above:</p>
<ul>
<li>The instruction count does not include EQUB, EQUW, EQUD, EQUS or SKIP operatives; these are counted as data.</li>
<li>Each part of a multi-part subroutine counts as an individual subroutine.</li>
<li>The statistics are produced by a relatively simple static analysis of the source code. They are not 100% accurate, though they are pretty close.</li>
</ul>
'''
elif args.platform == "revs":
    html_source_code_stats_intro = '''<p>Here's a statistical breakdown of the source code for {}. Click on the table headers to sort by that statistic. For more information, see the notes after the table.</p>
'''
    html_source_code_stats_footer = '''<p>Some notes on the above:</p>
<ul>
<li>The instruction count does not include EQUB, EQUW, EQUD, EQUS or SKIP operatives; these are counted as data.</li>
<li>Each part of a multi-part subroutine counts as an individual subroutine.</li>
<li>The statistics are produced by a relatively simple static analysis of the source code. They are not 100% accurate, though they are pretty close.</li>
<li>The totals cover all code in the main game, including all of the track data files.</li>
</ul>
'''
elif args.platform == "c64" or args.platform == "apple" or args.platform == "nes":
    html_source_code_stats_intro = '''<p>Here's a statistical breakdown of the source code for {}. Click on the table headers to sort by that statistic. For more information, see the notes after the table.</p>
'''
    html_source_code_stats_footer = '''<p>Some notes on the above:</p>
<ul>
<li>The instruction count does not include EQUB, EQUW, EQUD, EQUS or SKIP operatives; these are counted as data even when they are buried in code (so EQUB $2C "BIT skip" instructions are counted as data, for example).</li>
<li>INCBIN files are not included in the counts, so the data count doesn't include bytes from binary source files.</li>
<li>Each part of a multi-part subroutine counts as an individual subroutine.</li>
<li>The statistics are produced by a relatively simple static analysis of the source code. They are not 100% accurate, though they are pretty close.</li>
<li>The totals cover all code in the project, including loaders and ship data files.</li>
</ul>
'''
else:
    html_source_code_stats_intro = '''<p>Here's a statistical breakdown of the source code for {}. Click on the table headers to sort by that statistic. For more information, see the notes after the table.</p>
'''
    html_source_code_stats_footer = '''<p>Some notes on the above:</p>
<ul>
<li>The instruction count does not include EQUB, EQUW, EQUD, EQUS or SKIP operatives; these are counted as data even when they are buried in code (so EQUB &amp;2C "BIT skip" instructions are counted as data, for example).</li>
<li>INCBIN files are not included in the counts, so the data count doesn't include bytes from binary source files.</li>
<li>Each part of a multi-part subroutine counts as an individual subroutine.</li>
<li>The statistics are produced by a relatively simple static analysis of the source code. They are not 100% accurate, though they are pretty close.</li>
<li>The totals cover all code in the project, including loaders, docked and flight code, Tube code and ship data files.</li>
</ul>
'''

html_source_code_stats_sorter = '''<script>
const getCellValue = (tr, idx) => tr.children[idx].children[0].innerText || tr.children[idx].children[0].textContent;

const comparer = (idx, asc) => (a, b) => ((v1, v2) =>
    v1 !== '' && v2 !== '' && !isNaN(v1) && !isNaN(v2) ? v2 - v1 : v1.toString().localeCompare(v2)
    )(getCellValue(asc ? a : b, idx), getCellValue(asc ? b : a, idx));

document.querySelectorAll('tbody th').forEach(th => th.addEventListener('click', (() => {
    const table = th.closest('table tbody');
    const footer = table.querySelectorAll('.footer');
    footerClone = footer[0].cloneNode(true);
    footer[0].remove();
    Array.from(table.querySelectorAll('tr:nth-child(n+2)'))
        .sort(comparer(Array.from(th.parentNode.children).indexOf(th), this.asc = !this.asc))
        .forEach(tr => table.appendChild(tr)
    );
    table.append(footerClone);
})));
</script>
'''
html_az_index_start = '<ul class="indexLinks small">\n'
html_az_index_link = '\t<li><a href="#{}">{}</a></li>\n'
html_az_index_end = '</ul>\n'
html_az_links = '''\t\t\t\t\t\t<ul class="indexLinks">
\t\t\t\t\t\t\t<li><a href="#a">A</a></li>
\t\t\t\t\t\t\t<li><a href="#b">B</a></li>
\t\t\t\t\t\t\t<li><a href="#c">C</a></li>
\t\t\t\t\t\t\t<li><a href="#d">D</a></li>
\t\t\t\t\t\t\t<li><a href="#e">E</a></li>
\t\t\t\t\t\t\t<li><a href="#f">F</a></li>
\t\t\t\t\t\t\t<li><a href="#g">G</a></li>
\t\t\t\t\t\t\t<li><a href="#h">H</a></li>
\t\t\t\t\t\t\t<li><a href="#i">I</a></li>
\t\t\t\t\t\t\t<li><a href="#j">J</a></li>
\t\t\t\t\t\t\t<li><a href="#k">K</a></li>
\t\t\t\t\t\t\t<li><a href="#l">L</a></li>
\t\t\t\t\t\t\t<li><a href="#m">M</a></li>
\t\t\t\t\t\t\t<li><a href="#n">N</a></li>
\t\t\t\t\t\t\t<li><a href="#o">O</a></li>
\t\t\t\t\t\t\t<li><a href="#p">P</a></li>
\t\t\t\t\t\t\t<li><a href="#q">Q</a></li>
\t\t\t\t\t\t\t<li><a href="#r">R</a></li>
\t\t\t\t\t\t\t<li><a href="#s">S</a></li>
\t\t\t\t\t\t\t<li><a href="#t">T</a></li>
\t\t\t\t\t\t\t<li><a href="#u">U</a></li>
\t\t\t\t\t\t\t<li><a href="#v">V</a></li>
\t\t\t\t\t\t\t<li><a href="#w">W</a></li>
\t\t\t\t\t\t\t<li><a href="#x">X</a></li>
\t\t\t\t\t\t\t<li><a href="#y">Y</a></li>
\t\t\t\t\t\t\t<li><a href="#z">Z</a></li>
\t\t\t\t\t\t</ul>
'''
html_source_code_cross_references_intro = '''\t\t\t\t\t\t<p>Here's a list of every label and variable in the source code for {}, with details of where each of them is used.</p>
''' + html_az_links

if args.platform == "aviator":
    html_az_index_intro = '''<p>This index contains every subroutine, entry point, variable and workspace that appears in the source code for {}, sorted alphabetically.</p>
''' + html_az_links
elif args.platform == "lander":
    html_az_index_intro = '''<p>This index contains every subroutine, entry point and variable that appears in the source code for {}, sorted alphabetically.</p>
''' + html_az_links
else:
    html_az_index_intro = '''<p>This index contains every subroutine, entry point, variable, workspace and macro that appears in the source code for {}, sorted alphabetically.</p>
''' + html_az_links

html_subroutine_index_intro = '''<p>This index contains every subroutine and entry point that appears in the source code for {}, grouped by category. An entry points is a label within a subroutine that is called from outside the subroutine, which typically implements a subset or variation of the functionality of the parent subroutine.</p>
'''
html_variable_index_intro = '''<p>This index contains every variable that appears in the source code for {}, grouped by category. A variable is defined as a labelled memory location that is used for storing data, and this list includes both variables that are defined in workspaces, and variables that are declared within the body of the source code.</p>
'''
html_workspace_index_intro = '''<p>This index contains every workspace that appears in the source code for {}, grouped by category. A workspace is defined as a collection of variables, defined in a block.</p>
'''
html_macro_index_intro = '''<p>This index contains every macro that appears in the source code for {}, grouped by category.</p>
'''
html_deep_dive_index_intro = '''<p>This index contains every deep dive article on this site, grouped by category. If you want to learn how Elite works under the hood, then this is the section for you.</p>
'''
html_compare_intro = '''<div class="codeBlockWrapper"><div class="codeBlock article">
\t<p>This code appears in the following version{} (click to see it in the source code):</p>
\t<ul class="tightList">
\t\t<li>{}</li>
\t</ul>
\t<p>Code variations between these versions are shown below.</p>
</div></div>
'''
html_compare_intro_tap_instructions = '''<p>Tap on a block to expand it, and tap it again to revert.</p>
'''
html_multi_varies_intro = '''<div class="codeBlockWrapper"><div class="codeBlock article">
\t<p>The following subroutines, variables and workspaces appear in more than one version of Elite, and their code differs between those versions. Click on a name in the table below to see the code differences, or click on a version name to see the relevant code as it appears in that version. "Cassette" refers to the BBC Micro cassette version, while "Docked" and "Flight" refer to the BBC Micro disc version.</p>
\t<p>Note that if you click into a workspace, it will show the differences in the contents of that workspace (i.e. in the variables it contains), but for clarity it won't show any differences within those variable definitions. For this, you need to click on the variable name itself to view differences in its code.</p>
\t<table class="spacedTableBorder codeSummary middle">
\t\t<tr class="codeSummaryHeader"><th class="codeSummaryLabel">Name</th><th class="center" colspan="6">Versions that contain this routine</th></tr>
'''
html_multi_same_intro = '''<div class="codeBlockWrapper"><div class="codeBlock article">
\t<p>The following subroutines, variables, workspaces and macros appear in multiple versions of Elite, and the code is the same in all those versions. Click on the version name to see the relevant code as it appears in that version. "Cassette" refers to the BBC Micro cassette version, while "Docked" and "Flight" refer to the BBC Micro disc version.</p>
\t<table class="spacedTableBorder codeSummary middle">
\t\t<tr class="codeSummaryHeader"><th class="codeSummaryLabel">Name</th><th class="center" colspan="6">Versions that contain this routine</th></tr>
'''
html_mono_intro = '''<div class="codeBlockWrapper"><div class="codeBlock article">
\t<p>The following subroutines, variables, workspaces and macros appear in just one version of Elite. Click on the version name to see the relevant code as it appears in that version. "Cassette" refers to the BBC Micro cassette version, while "Docked" and "Flight" refer to the BBC Micro disc version.</p>
\t<table class="spacedTableBorder codeSummary middle">
\t\t<tr class="codeSummaryHeader"><th class="codeSummaryLabel">Name</th><th class="center" colspan="6">Versions that contain this routine</th></tr>
'''
html_shared_category_intro = '''<div class="codeBlockWrapper"><div class="codeBlock article">
\t<p>{}</p>
\t<p>Click on a name to see all the code differences for that part of the codebase, or click on an individual variation to focus on that particular feature.</p>
\t<table class="spacedTableBorder codeSummary"><tbody>
\t\t<tr class="codeSummaryHeader"><th class="codeSummaryLabel">Name</th><th>Comments</th>'''
html_shared_other_variations_intro = '''<div class="codeBlockWrapper"><div class="codeBlock article">
\t<p>The following table shows minor code variations that are not covered by the curated lists. The categories are described in the page on <a href="/compare/how_to_compare.html">how to compare versions</a>.</p>
\t<p>Click on a name to see all the code differences for that part of the codebase.</p>
\t<table class="spacedTableBorder codeSummary middle"><tbody>
\t\t<tr class="codeSummaryHeader"><th class="codeSummaryLabel">Name</th>'''

if args.platform == "cassette":
    next_prev_all = {
        "map_of_the_source_code": {
            "prev": {"filename": content_folder + "releases.html", "name": "Different variants of the BBC Micro cassette version"},
            "next": {"filename": content_folder + "all/loader.html", "name": "Loader source"}
        },
        "loader": {
            "prev": {"filename": content_folder + "articles/map_of_the_source_code.html", "name": "Map of the source code"},
            "next": {"filename": content_folder + "all/workspaces.html", "name": "Workspaces and configuration"}
        },
        "workspaces": {
            "prev": {"filename": content_folder + "all/loader.html", "name": "Loader source"},
            "next": {"filename": content_folder + "all/text_tokens.html", "name": "Text tokens"}
        },
        "text_tokens": {
            "prev": {"filename": content_folder + "all/workspaces.html", "name": "Workspaces and configuration"},
            "next": {"filename": content_folder + "all/elite_a.html", "name": "Elite A source"}
        },
        "elite_a": {
            "prev": {"filename": content_folder + "all/text_tokens.html", "name": "Text tokens"},
            "next": {"filename": content_folder + "all/elite_b.html", "name": "Elite B source"}
        },
        "elite_b": {
            "prev": {"filename": content_folder + "all/elite_a.html", "name": "Elite A source"},
            "next": {"filename": content_folder + "all/elite_c.html", "name": "Elite C source"}
        },
        "elite_c": {
            "prev": {"filename": content_folder + "all/elite_b.html", "name": "Elite B source"},
            "next": {"filename": content_folder + "all/elite_d.html", "name": "Elite D source"}
        },
        "elite_d": {
            "prev": {"filename": content_folder + "all/elite_c.html", "name": "Elite C source"},
            "next": {"filename": content_folder + "all/elite_e.html", "name": "Elite E source"}
        },
        "elite_e": {
            "prev": {"filename": content_folder + "all/elite_d.html", "name": "Elite D source"},
            "next": {"filename": content_folder + "all/elite_f.html", "name": "Elite F source"}
        },
        "elite_f": {
            "prev": {"filename": content_folder + "all/elite_e.html", "name": "Elite E source"},
            "next": {"filename": content_folder + "all/elite_g.html", "name": "Elite G source"}
        },
        "elite_g": {
            "prev": {"filename": content_folder + "all/elite_f.html", "name": "Elite F source"},
            "next": {"filename": content_folder + "all/elite_ships.html", "name": "Ship blueprints"}
        },
        "elite_ships": {
            "prev": {"filename": content_folder + "all/elite_g.html", "name": "Elite G source"},
            "next": {"filename": content_folder + "all/bcfs.html", "name": "Big Code File source"}
        },
        "bcfs": {
            "prev": {"filename": content_folder + "all/elite_ships.html", "name": "Ship blueprints"},
            "next": None
        }
    }
elif args.platform == "electron":
    next_prev_all = {
        "map_of_the_source_code": {
            "prev": {"filename": content_folder + "releases.html", "name": "Different variants of the Acorn Electron version"},
            "next": {"filename": content_folder + "all/loader.html", "name": "Loader source"}
        },
        "loader": {
            "prev": {"filename": content_folder + "articles/map_of_the_source_code.html", "name": "Map of the source code"},
            "next": {"filename": content_folder + "all/workspaces.html", "name": "Workspaces and configuration"}
        },
        "workspaces": {
            "prev": {"filename": content_folder + "all/loader.html", "name": "Loader source"},
            "next": {"filename": content_folder + "all/text_tokens.html", "name": "Text tokens"}
        },
        "text_tokens": {
            "prev": {"filename": content_folder + "all/workspaces.html", "name": "Workspaces and configuration"},
            "next": {"filename": content_folder + "all/elite_a.html", "name": "Elite A source"}
        },
        "elite_a": {
            "prev": {"filename": content_folder + "all/text_tokens.html", "name": "Text tokens"},
            "next": {"filename": content_folder + "all/elite_b.html", "name": "Elite B source"}
        },
        "elite_b": {
            "prev": {"filename": content_folder + "all/elite_a.html", "name": "Elite A source"},
            "next": {"filename": content_folder + "all/elite_c.html", "name": "Elite C source"}
        },
        "elite_c": {
            "prev": {"filename": content_folder + "all/elite_b.html", "name": "Elite B source"},
            "next": {"filename": content_folder + "all/elite_d.html", "name": "Elite D source"}
        },
        "elite_d": {
            "prev": {"filename": content_folder + "all/elite_c.html", "name": "Elite C source"},
            "next": {"filename": content_folder + "all/elite_e.html", "name": "Elite E source"}
        },
        "elite_e": {
            "prev": {"filename": content_folder + "all/elite_d.html", "name": "Elite D source"},
            "next": {"filename": content_folder + "all/elite_f.html", "name": "Elite F source"}
        },
        "elite_f": {
            "prev": {"filename": content_folder + "all/elite_e.html", "name": "Elite E source"},
            "next": {"filename": content_folder + "all/elite_g.html", "name": "Elite G source"}
        },
        "elite_g": {
            "prev": {"filename": content_folder + "all/elite_f.html", "name": "Elite F source"},
            "next": {"filename": content_folder + "all/elite_ships.html", "name": "Ship blueprints"}
        },
        "elite_ships": {
            "prev": {"filename": content_folder + "all/elite_g.html", "name": "Elite G source"},
            "next": {"filename": content_folder + "all/bcfs.html", "name": "Big Code File source"}
        },
        "bcfs": {
            "prev": {"filename": content_folder + "all/elite_ships.html", "name": "Ship blueprints"},
            "next": None
        }
    }
elif args.platform == "disc":
    next_prev_all = {
        "map_of_the_source_code": {
            "prev": {"filename": content_folder + "releases.html", "name": "Different variants of the BBC Micro disc version"},
            "next": {"filename": content_folder + "all/loader1.html", "name": "Loader 1 source"}
        },
        "loader1": {
            "prev": {"filename": content_folder + "articles/map_of_the_source_code.html", "name": "Map of the source code"},
            "next": {"filename": content_folder + "all/loader2.html", "name": "Loader 2 source"}
        },
        "loader2": {
            "prev": {"filename": content_folder + "all/loader1.html", "name": "Loader 1 source"},
            "next": {"filename": content_folder + "all/text_tokens.html", "name": "Text tokens"}
        },
        "text_tokens": {
            "prev": {"filename": content_folder + "all/loader2.html", "name": "Loader 2 source"},
            "next": {"filename": content_folder + "all/ship_missile.html", "name": "Missile ship blueprint"}
        },
        "ship_missile": {
            "prev": {"filename": content_folder + "all/text_tokens.html", "name": "Text tokens"},
            "next": {"filename": content_folder + "all/loader3.html", "name": "Loader 3 source"}
        },
        "loader3": {
            "prev": {"filename": content_folder + "all/ship_missile.html", "name": "Missile ship blueprint"},
            "next": {"filename": content_folder + "all/loader_sideways_ram.html", "name": "Sideways RAM Loader source"}
        },
        "loader_sideways_ram": {
            "prev": {"filename": content_folder + "all/loader3.html", "name": "Loader 3 source"},
            "next": {"filename": content_folder + "all/workspaces_docked.html", "name": "Docked workspaces"}
        },
        "workspaces_docked": {
            "prev": {"filename": content_folder + "all/loader_sideways_ram.html", "name": "Sideways RAM Loader source"},
            "next": {"filename": content_folder + "all/elite_a_docked.html", "name": "Elite A docked source"},
        },
        "elite_a_docked": {
            "prev": {"filename": content_folder + "all/workspaces_docked.html", "name": "Docked workspaces"},
            "next": {"filename": content_folder + "all/elite_b_docked.html", "name": "Elite B docked source"}
        },
        "elite_b_docked": {
            "prev": {"filename": content_folder + "all/elite_a_docked.html", "name": "Elite A docked source"},
            "next": {"filename": content_folder + "all/elite_c_docked.html", "name": "Elite C docked source"}
        },
        "elite_c_docked": {
            "prev": {"filename": content_folder + "all/elite_b_docked.html", "name": "Elite B docked source"},
            "next": {"filename": content_folder + "all/elite_d_docked.html", "name": "Elite D docked source"}
        },
        "elite_d_docked": {
            "prev": {"filename": content_folder + "all/elite_c_docked.html", "name": "Elite C docked source"},
            "next": {"filename": content_folder + "all/elite_e_docked.html", "name": "Elite E docked source"}
        },
        "elite_e_docked": {
            "prev": {"filename": content_folder + "all/elite_d_docked.html", "name": "Elite D docked source"},
            "next": {"filename": content_folder + "all/elite_f_docked.html", "name": "Elite F docked source"}
        },
        "elite_f_docked": {
            "prev": {"filename": content_folder + "all/elite_e_docked.html", "name": "Elite E docked source"},
            "next": {"filename": content_folder + "all/elite_g_docked.html", "name": "Elite G docked source"}
        },
        "elite_g_docked": {
            "prev": {"filename": content_folder + "all/elite_f_docked.html", "name": "Elite F docked source"},
            "next": {"filename": content_folder + "all/elite_h_docked.html", "name": "Elite H docked source"}
        },
        "elite_h_docked": {
            "prev": {"filename": content_folder + "all/elite_g_docked.html", "name": "Elite G docked source"},
            "next": {"filename": content_folder + "all/elite_ships_docked.html", "name": "Ship hangar blueprints"}
        },
        "elite_ships_docked": {
            "prev": {"filename": content_folder + "all/elite_h_docked.html", "name": "Elite H docked source"},
            "next": {"filename": content_folder + "all/workspaces_flight.html", "name": "Flight workspaces"}
        },
        "workspaces_flight": {
            "prev": {"filename": content_folder + "all/elite_ships_docked.html", "name": "Ship hangar blueprints"},
            "next": {"filename": content_folder + "all/elite_a_flight.html", "name": "Elite A flight source"},
        },
        "elite_a_flight": {
            "prev": {"filename": content_folder + "all/workspaces_flight.html", "name": "Flight workspaces"},
            "next": {"filename": content_folder + "all/elite_b_flight.html", "name": "Elite B flight source"}
        },
        "elite_b_flight": {
            "prev": {"filename": content_folder + "all/elite_a_flight.html", "name": "Elite A flight source"},
            "next": {"filename": content_folder + "all/elite_c_flight.html", "name": "Elite C flight source"}
        },
        "elite_c_flight": {
            "prev": {"filename": content_folder + "all/elite_b_flight.html", "name": "Elite B flight source"},
            "next": {"filename": content_folder + "all/elite_d_flight.html", "name": "Elite D flight source"}
        },
        "elite_d_flight": {
            "prev": {"filename": content_folder + "all/elite_c_flight.html", "name": "Elite C flight source"},
            "next": {"filename": content_folder + "all/elite_e_flight.html", "name": "Elite E flight source"}
        },
        "elite_e_flight": {
            "prev": {"filename": content_folder + "all/elite_d_flight.html", "name": "Elite D flight source"},
            "next": {"filename": content_folder + "all/elite_f_flight.html", "name": "Elite F flight source"}
        },
        "elite_f_flight": {
            "prev": {"filename": content_folder + "all/elite_e_flight.html", "name": "Elite E flight source"},
            "next": {"filename": content_folder + "all/elite_g_flight.html", "name": "Elite G flight source"}
        },
        "elite_g_flight": {
            "prev": {"filename": content_folder + "all/elite_f_flight.html", "name": "Elite F flight source"},
            "next": {"filename": content_folder + "all/elite_h_flight.html", "name": "Elite H flight source"}
        },
        "elite_h_flight": {
            "prev": {"filename": content_folder + "all/elite_g_flight.html", "name": "Elite G flight source"},
            "next": {"filename": content_folder + "all/elite_ships_a.html", "name": "Ship blueprints A"}
        },
        "elite_ships_a": {
            "prev": {"filename": content_folder + "all/elite_h_flight.html", "name": "Elite H flight source"},
            "next": {"filename": content_folder + "all/elite_ships_b.html", "name": "Ship blueprints B"}
        },
        "elite_ships_b": {
            "prev": {"filename": content_folder + "all/elite_ships_a.html", "name": "Ship blueprints A"},
            "next": {"filename": content_folder + "all/elite_ships_c.html", "name": "Ship blueprints C"}
        },
        "elite_ships_c": {
            "prev": {"filename": content_folder + "all/elite_ships_b.html", "name": "Ship blueprints B"},
            "next": {"filename": content_folder + "all/elite_ships_d.html", "name": "Ship blueprints D"}
        },
        "elite_ships_d": {
            "prev": {"filename": content_folder + "all/elite_ships_c.html", "name": "Ship blueprints C"},
            "next": {"filename": content_folder + "all/elite_ships_e.html", "name": "Ship blueprints E"}
        },
        "elite_ships_e": {
            "prev": {"filename": content_folder + "all/elite_ships_d.html", "name": "Ship blueprints D"},
            "next": {"filename": content_folder + "all/elite_ships_f.html", "name": "Ship blueprints F"}
        },
        "elite_ships_f": {
            "prev": {"filename": content_folder + "all/elite_ships_e.html", "name": "Ship blueprints E"},
            "next": {"filename": content_folder + "all/elite_ships_g.html", "name": "Ship blueprints G"}
        },
        "elite_ships_g": {
            "prev": {"filename": content_folder + "all/elite_ships_f.html", "name": "Ship blueprints F"},
            "next": {"filename": content_folder + "all/elite_ships_h.html", "name": "Ship blueprints H"}
        },
        "elite_ships_h": {
            "prev": {"filename": content_folder + "all/elite_ships_g.html", "name": "Ship blueprints G"},
            "next": {"filename": content_folder + "all/elite_ships_i.html", "name": "Ship blueprints I"}
        },
        "elite_ships_i": {
            "prev": {"filename": content_folder + "all/elite_ships_h.html", "name": "Ship blueprints H"},
            "next": {"filename": content_folder + "all/elite_ships_j.html", "name": "Ship blueprints J"}
        },
        "elite_ships_j": {
            "prev": {"filename": content_folder + "all/elite_ships_i.html", "name": "Ship blueprints I"},
            "next": {"filename": content_folder + "all/elite_ships_k.html", "name": "Ship blueprints K"}
        },
        "elite_ships_k": {
            "prev": {"filename": content_folder + "all/elite_ships_j.html", "name": "Ship blueprints J"},
            "next": {"filename": content_folder + "all/elite_ships_l.html", "name": "Ship blueprints L"}
        },
        "elite_ships_l": {
            "prev": {"filename": content_folder + "all/elite_ships_k.html", "name": "Ship blueprints K"},
            "next": {"filename": content_folder + "all/elite_ships_m.html", "name": "Ship blueprints M"}
        },
        "elite_ships_m": {
            "prev": {"filename": content_folder + "all/elite_ships_l.html", "name": "Ship blueprints L"},
            "next": {"filename": content_folder + "all/elite_ships_n.html", "name": "Ship blueprints N"}
        },
        "elite_ships_n": {
            "prev": {"filename": content_folder + "all/elite_ships_m.html", "name": "Ship blueprints M"},
            "next": {"filename": content_folder + "all/elite_ships_o.html", "name": "Ship blueprints O"}
        },
        "elite_ships_o": {
            "prev": {"filename": content_folder + "all/elite_ships_n.html", "name": "Ship blueprints N"},
            "next": {"filename": content_folder + "all/elite_ships_p.html", "name": "Ship blueprints P"}
        },
        "elite_ships_p": {
            "prev": {"filename": content_folder + "all/elite_ships_o.html", "name": "Ship blueprints O"},
            "next": None
        }
    }
elif args.platform == "6502sp":
    next_prev_all = {
        "map_of_the_source_code": {
            "prev": {"filename": content_folder + "releases.html", "name": "Different variants of the 6502 Second Processor version"},
            "next": {"filename": content_folder + "all/loader1.html", "name": "Loader 1 source"}
        },
        "loader1": {
            "prev": {"filename": content_folder + "articles/map_of_the_source_code.html", "name": "Map of the source code"},
            "next": {"filename": content_folder + "all/loader2.html", "name": "Loader 2 source"}
        },
        "loader2": {
            "prev": {"filename": content_folder + "all/loader1.html", "name": "Loader 1 source"},
            "next": {"filename": content_folder + "all/workspaces.html", "name": "Workspaces and configuration"}
        },
        "workspaces": {
            "prev": {"filename": content_folder + "all/loader2.html", "name": "Loader 2 source"},
            "next": {"filename": content_folder + "all/text_tokens.html", "name": "Text tokens"}
        },
        "text_tokens": {
            "prev": {"filename": content_folder + "all/workspaces.html", "name": "Workspaces and configuration"},
            "next": {"filename": content_folder + "all/elite_a.html", "name": "Elite A source"}
        },
        "elite_a": {
            "prev": {"filename": content_folder + "all/text_tokens.html", "name": "Text tokens"},
            "next": {"filename": content_folder + "all/elite_b.html", "name": "Elite B source"}
        },
        "elite_b": {
            "prev": {"filename": content_folder + "all/elite_a.html", "name": "Elite A source"},
            "next": {"filename": content_folder + "all/elite_c.html", "name": "Elite C source"}
        },
        "elite_c": {
            "prev": {"filename": content_folder + "all/elite_b.html", "name": "Elite B source"},
            "next": {"filename": content_folder + "all/elite_d.html", "name": "Elite D source"}
        },
        "elite_d": {
            "prev": {"filename": content_folder + "all/elite_c.html", "name": "Elite C source"},
            "next": {"filename": content_folder + "all/elite_e.html", "name": "Elite E source"}
        },
        "elite_e": {
            "prev": {"filename": content_folder + "all/elite_d.html", "name": "Elite D source"},
            "next": {"filename": content_folder + "all/elite_f.html", "name": "Elite F source"}
        },
        "elite_f": {
            "prev": {"filename": content_folder + "all/elite_e.html", "name": "Elite E source"},
            "next": {"filename": content_folder + "all/elite_g.html", "name": "Elite G source"}
        },
        "elite_g": {
            "prev": {"filename": content_folder + "all/elite_f.html", "name": "Elite F source"},
            "next": {"filename": content_folder + "all/elite_h.html", "name": "Elite H source"}
        },
        "elite_h": {
            "prev": {"filename": content_folder + "all/elite_g.html", "name": "Elite G source"},
            "next": {"filename": content_folder + "all/elite_i.html", "name": "Elite I source"}
        },
        "elite_i": {
            "prev": {"filename": content_folder + "all/elite_h.html", "name": "Elite H source"},
            "next": {"filename": content_folder + "all/elite_j.html", "name": "Elite J source"}
        },
        "elite_j": {
            "prev": {"filename": content_folder + "all/elite_i.html", "name": "Elite I source"},
            "next": {"filename": content_folder + "all/elite_ships.html", "name": "Ship blueprints"}
        },
        "elite_ships": {
            "prev": {"filename": content_folder + "all/elite_g.html", "name": "Elite G source"},
            "next": {"filename": content_folder + "all/i_o_processor.html", "name": "I/O processor source"}
        },
        "i_o_processor": {
            "prev": {"filename": content_folder + "all/elite_ships.html", "name": "Ship blueprints"},
            "next": {"filename": content_folder + "all/bcfs.html", "name": "Big Code File source"}
        },
        "bcfs": {
            "prev": {"filename": content_folder + "all/i_o_processor.html", "name": "I/O processor source"},
            "next": None
        }
    }
elif args.platform == "c64":
    next_prev_all = {
        "map_of_the_source_code": {
            "prev": {"filename": content_folder + "releases.html", "name": "Different variants of the Commodore 64 version"},
            "next": {"filename": content_folder + "all/loader1.html", "name": "Disk Loader 1 source"}
        },
        "loader1": {
            "prev": {"filename": content_folder + "articles/map_of_the_source_code.html", "name": "Map of the source code"},
            "next": {"filename": content_folder + "all/loader2.html", "name": "Disk Loader 2 source"}
        },
        "loader2": {
            "prev": {"filename": content_folder + "all/loader1.html", "name": "Disk Loader 1 source"},
            "next": {"filename": content_folder + "all/loader.html", "name": "Game Loader source"}
        },
        "loader": {
            "prev": {"filename": content_folder + "all/loader2.html", "name": "Disk Loader 2 source"},
            "next": {"filename": content_folder + "all/workspaces.html", "name": "Workspaces and configuration"}
        },
        "workspaces": {
            "prev": {"filename": content_folder + "all/loader.html", "name": "Game Loader source"},
            "next": {"filename": content_folder + "all/elite_a.html", "name": "Elite A source"}
        },
        "elite_a": {
            "prev": {"filename": content_folder + "all/workspaces.html", "name": "Workspaces and configuration"},
            "next": {"filename": content_folder + "all/elite_b.html", "name": "Elite B source"}
        },
        "elite_b": {
            "prev": {"filename": content_folder + "all/elite_a.html", "name": "Elite A source"},
            "next": {"filename": content_folder + "all/elite_c.html", "name": "Elite C source"}
        },
        "elite_c": {
            "prev": {"filename": content_folder + "all/elite_b.html", "name": "Elite B source"},
            "next": {"filename": content_folder + "all/elite_d.html", "name": "Elite D source"}
        },
        "elite_d": {
            "prev": {"filename": content_folder + "all/elite_c.html", "name": "Elite C source"},
            "next": {"filename": content_folder + "all/elite_e.html", "name": "Elite E source"}
        },
        "elite_e": {
            "prev": {"filename": content_folder + "all/elite_d.html", "name": "Elite D source"},
            "next": {"filename": content_folder + "all/elite_f.html", "name": "Elite F source"}
        },
        "elite_f": {
            "prev": {"filename": content_folder + "all/elite_e.html", "name": "Elite E source"},
            "next": {"filename": content_folder + "all/elite_g.html", "name": "Elite G source"}
        },
        "elite_g": {
            "prev": {"filename": content_folder + "all/elite_f.html", "name": "Elite F source"},
            "next": {"filename": content_folder + "all/elite_h.html", "name": "Elite H source"}
        },
        "elite_h": {
            "prev": {"filename": content_folder + "all/elite_g.html", "name": "Elite G source"},
            "next": {"filename": content_folder + "all/elite_i.html", "name": "Elite I source"}
        },
        "elite_i": {
            "prev": {"filename": content_folder + "all/elite_h.html", "name": "Elite H source"},
            "next": {"filename": content_folder + "all/elite_j.html", "name": "Elite J source"}
        },
        "elite_j": {
            "prev": {"filename": content_folder + "all/elite_i.html", "name": "Elite I source"},
            "next": {"filename": content_folder + "all/elite_k.html", "name": "Elite K source"}
        },
        "elite_k": {
            "prev": {"filename": content_folder + "all/elite_j.html", "name": "Elite J source"},
            "next": {"filename": content_folder + "all/elite_data.html", "name": "Game data"}
        },
        "elite_data": {
            "prev": {"filename": content_folder + "all/elite_k.html", "name": "Elite K source"},
            "next": {"filename": content_folder + "all/elite_ships.html", "name": "Ship blueprints"}
        },
        "elite_ships": {
            "prev": {"filename": content_folder + "all/elite_data.html", "name": "Game data"},
            "next": {"filename": content_folder + "all/text_tokens.html", "name": "Text tokens"}
        },
        "text_tokens": {
            "prev": {"filename": content_folder + "all/elite_ships.html", "name": "Ship blueprints"},
            "next": {"filename": content_folder + "all/elite_sprites.html", "name": "Sprites"}
        },
        "elite_sprites": {
            "prev": {"filename": content_folder + "all/text_tokens.html", "name": "Text tokens"},
            "next": None
        }
    }
elif args.platform == "apple":
    next_prev_all = {
        "map_of_the_source_code": {
            "prev": {"filename": content_folder + "releases.html", "name": "Different variants of the Apple II version"},
            "next": {"filename": content_folder + "all/loader.html", "name": "Game Loader source"}
        },
        "loader": {
            "prev": {"filename": content_folder + "articles/map_of_the_source_code.html", "name": "Map of the source code"},
            "next": {"filename": content_folder + "all/workspaces.html", "name": "Workspaces and configuration"}
        },
        "workspaces": {
            "prev": {"filename": content_folder + "all/loader.html", "name": "Game Loader source"},
            "next": {"filename": content_folder + "all/elite_a.html", "name": "Elite A source"}
        },
        "elite_a": {
            "prev": {"filename": content_folder + "all/workspaces.html", "name": "Workspaces and configuration"},
            "next": {"filename": content_folder + "all/elite_b.html", "name": "Elite B source"}
        },
        "elite_b": {
            "prev": {"filename": content_folder + "all/elite_a.html", "name": "Elite A source"},
            "next": {"filename": content_folder + "all/elite_c.html", "name": "Elite C source"}
        },
        "elite_c": {
            "prev": {"filename": content_folder + "all/elite_b.html", "name": "Elite B source"},
            "next": {"filename": content_folder + "all/elite_d.html", "name": "Elite D source"}
        },
        "elite_d": {
            "prev": {"filename": content_folder + "all/elite_c.html", "name": "Elite C source"},
            "next": {"filename": content_folder + "all/elite_e.html", "name": "Elite E source"}
        },
        "elite_e": {
            "prev": {"filename": content_folder + "all/elite_d.html", "name": "Elite D source"},
            "next": {"filename": content_folder + "all/elite_f.html", "name": "Elite F source"}
        },
        "elite_f": {
            "prev": {"filename": content_folder + "all/elite_e.html", "name": "Elite E source"},
            "next": {"filename": content_folder + "all/elite_g.html", "name": "Elite G source"}
        },
        "elite_g": {
            "prev": {"filename": content_folder + "all/elite_f.html", "name": "Elite F source"},
            "next": {"filename": content_folder + "all/elite_h.html", "name": "Elite H source"}
        },
        "elite_h": {
            "prev": {"filename": content_folder + "all/elite_g.html", "name": "Elite G source"},
            "next": {"filename": content_folder + "all/elite_i.html", "name": "Elite I source"}
        },
        "elite_i": {
            "prev": {"filename": content_folder + "all/elite_h.html", "name": "Elite H source"},
            "next": {"filename": content_folder + "all/elite_j.html", "name": "Elite J source"}
        },
        "elite_j": {
            "prev": {"filename": content_folder + "all/elite_i.html", "name": "Elite I source"},
            "next": {"filename": content_folder + "all/elite_k.html", "name": "Elite K source"}
        },
        "elite_k": {
            "prev": {"filename": content_folder + "all/elite_j.html", "name": "Elite J source"},
            "next": {"filename": content_folder + "all/elite_data.html", "name": "Game data"}
        },
        "elite_data": {
            "prev": {"filename": content_folder + "all/elite_k.html", "name": "Elite K source"},
            "next": {"filename": content_folder + "all/elite_ships.html", "name": "Ship blueprints"}
        },
        "elite_ships": {
            "prev": {"filename": content_folder + "all/elite_data.html", "name": "Game data"},
            "next": {"filename": content_folder + "all/text_tokens.html", "name": "Text tokens"}
        },
        "text_tokens": {
            "prev": {"filename": content_folder + "all/elite_ships.html", "name": "Ship blueprints"},
            "next": {"filename": content_folder + "all/bcfs.html", "name": "Big Code File source"}
        },
        "bcfs": {
            "prev": {"filename": content_folder + "all/text_tokens.html", "name": "Text tokens"},
            "next": {"filename": content_folder + "all/transfer_program.html", "name": "Transfer program source"}
        },
        "transfer_program": {
            "prev": {"filename": content_folder + "all/bcfs.html", "name": "Big Code File source"},
            "next": None
        }
    }
elif args.platform == "master":
    next_prev_all = {
        "map_of_the_source_code": {
            "prev": {"filename": content_folder + "releases.html", "name": "Different variants of the BBC Master version"},
            "next": {"filename": content_folder + "all/loader.html", "name": "Loader source"}
        },
        "loader": {
            "prev": {"filename": content_folder + "articles/map_of_the_source_code.html", "name": "Map of the source code"},
            "next": {"filename": content_folder + "all/workspaces.html", "name": "Workspaces and configuration"}
        },
        "workspaces": {
            "prev": {"filename": content_folder + "all/loader.html", "name": "Loader source"},
            "next": {"filename": content_folder + "all/elite_a.html", "name": "Elite A source"}
        },
        "elite_a": {
            "prev": {"filename": content_folder + "all/workspaces.html", "name": "Workspaces and configuration"},
            "next": {"filename": content_folder + "all/elite_b.html", "name": "Elite B source"}
        },
        "elite_b": {
            "prev": {"filename": content_folder + "all/elite_a.html", "name": "Elite A source"},
            "next": {"filename": content_folder + "all/elite_c.html", "name": "Elite C source"}
        },
        "elite_c": {
            "prev": {"filename": content_folder + "all/elite_b.html", "name": "Elite B source"},
            "next": {"filename": content_folder + "all/elite_d.html", "name": "Elite D source"}
        },
        "elite_d": {
            "prev": {"filename": content_folder + "all/elite_c.html", "name": "Elite C source"},
            "next": {"filename": content_folder + "all/elite_e.html", "name": "Elite E source"}
        },
        "elite_e": {
            "prev": {"filename": content_folder + "all/elite_d.html", "name": "Elite D source"},
            "next": {"filename": content_folder + "all/elite_f.html", "name": "Elite F source"}
        },
        "elite_f": {
            "prev": {"filename": content_folder + "all/elite_e.html", "name": "Elite E source"},
            "next": {"filename": content_folder + "all/elite_g.html", "name": "Elite G source"}
        },
        "elite_g": {
            "prev": {"filename": content_folder + "all/elite_f.html", "name": "Elite F source"},
            "next": {"filename": content_folder + "all/elite_h.html", "name": "Elite H source"}
        },
        "elite_h": {
            "prev": {"filename": content_folder + "all/elite_g.html", "name": "Elite G source"},
            "next": {"filename": content_folder + "all/elite_data.html", "name": "Game data"}
        },
        "elite_data": {
            "prev": {"filename": content_folder + "all/elite_h.html", "name": "Elite H source"},
            "next": {"filename": content_folder + "all/elite_ships.html", "name": "Ship blueprints"}
        },
        "elite_ships": {
            "prev": {"filename": content_folder + "all/elite_data.html", "name": "Game data"},
            "next": {"filename": content_folder + "all/text_tokens.html", "name": "Text tokens"}
        },
        "text_tokens": {
            "prev": {"filename": content_folder + "all/elite_ships.html", "name": "Ship blueprints"},
            "next": None
        }
    }
elif args.platform == "elite-a":
    next_prev_all = {
        "map_of_the_source_code": {
            "prev": {"filename": content_folder + "releases.html", "name": "Different variants of Elite-A"},
            "next": {"filename": content_folder + "all/loader.html", "name": "Loader source"}
        },
        "loader": {
            "prev": {"filename": content_folder + "articles/map_of_the_source_code.html", "name": "Map of the source code"},
            "next": {"filename": content_folder + "all/text_tokens.html", "name": "Text tokens"}
        },
        "text_tokens": {
            "prev": {"filename": content_folder + "all/loader.html", "name": "Loader source"},
            "next": {"filename": content_folder + "all/ship_missile.html", "name": "Missile ship blueprint"}
        },
        "ship_missile": {
            "prev": {"filename": content_folder + "all/text_tokens.html", "name": "Text tokens"},
            "next": {"filename": content_folder + "all/workspaces_docked.html", "name": "Docked workspaces"}
        },
        "workspaces_docked": {
            "prev": {"filename": content_folder + "all/loader.html", "name": "Loader source"},
            "next": {"filename": content_folder + "all/elite_a_docked.html", "name": "Elite A docked source"},
        },
        "elite_a_docked": {
            "prev": {"filename": content_folder + "all/workspaces_docked.html", "name": "Docked workspaces"},
            "next": {"filename": content_folder + "all/elite_b_docked.html", "name": "Elite B docked source"}
        },
        "elite_b_docked": {
            "prev": {"filename": content_folder + "all/elite_a_docked.html", "name": "Elite A docked source"},
            "next": {"filename": content_folder + "all/elite_c_docked.html", "name": "Elite C docked source"}
        },
        "elite_c_docked": {
            "prev": {"filename": content_folder + "all/elite_b_docked.html", "name": "Elite B docked source"},
            "next": {"filename": content_folder + "all/elite_d_docked.html", "name": "Elite D docked source"}
        },
        "elite_d_docked": {
            "prev": {"filename": content_folder + "all/elite_c_docked.html", "name": "Elite C docked source"},
            "next": {"filename": content_folder + "all/elite_e_docked.html", "name": "Elite E docked source"}
        },
        "elite_e_docked": {
            "prev": {"filename": content_folder + "all/elite_d_docked.html", "name": "Elite D docked source"},
            "next": {"filename": content_folder + "all/elite_f_docked.html", "name": "Elite F docked source"}
        },
        "elite_f_docked": {
            "prev": {"filename": content_folder + "all/elite_e_docked.html", "name": "Elite E docked source"},
            "next": {"filename": content_folder + "all/elite_g_docked.html", "name": "Elite G docked source"}
        },
        "elite_g_docked": {
            "prev": {"filename": content_folder + "all/elite_f_docked.html", "name": "Elite F docked source"},
            "next": {"filename": content_folder + "all/elite_h_docked.html", "name": "Elite H docked source"}
        },
        "elite_h_docked": {
            "prev": {"filename": content_folder + "all/elite_g_docked.html", "name": "Elite G docked source"},
            "next": {"filename": content_folder + "all/elite_ships_docked.html", "name": "Ship hangar blueprints"}
        },
        "elite_ships_docked": {
            "prev": {"filename": content_folder + "all/elite_h_docked.html", "name": "Elite H docked source"},
            "next": {"filename": content_folder + "all/workspaces_flight.html", "name": "Flight workspaces"}
        },
        "workspaces_flight": {
            "prev": {"filename": content_folder + "all/elite_ships_docked.html", "name": "Ship hangar blueprints"},
            "next": {"filename": content_folder + "all/elite_a_flight.html", "name": "Elite A flight source"},
        },
        "elite_a_flight": {
            "prev": {"filename": content_folder + "all/workspaces_flight.html", "name": "Flight workspaces"},
            "next": {"filename": content_folder + "all/elite_b_flight.html", "name": "Elite B flight source"}
        },
        "elite_b_flight": {
            "prev": {"filename": content_folder + "all/elite_a_flight.html", "name": "Elite A flight source"},
            "next": {"filename": content_folder + "all/elite_c_flight.html", "name": "Elite C flight source"}
        },
        "elite_c_flight": {
            "prev": {"filename": content_folder + "all/elite_b_flight.html", "name": "Elite B flight source"},
            "next": {"filename": content_folder + "all/elite_d_flight.html", "name": "Elite D flight source"}
        },
        "elite_d_flight": {
            "prev": {"filename": content_folder + "all/elite_c_flight.html", "name": "Elite C flight source"},
            "next": {"filename": content_folder + "all/elite_e_flight.html", "name": "Elite E flight source"}
        },
        "elite_e_flight": {
            "prev": {"filename": content_folder + "all/elite_d_flight.html", "name": "Elite D flight source"},
            "next": {"filename": content_folder + "all/elite_f_flight.html", "name": "Elite F flight source"}
        },
        "elite_f_flight": {
            "prev": {"filename": content_folder + "all/elite_e_flight.html", "name": "Elite E flight source"},
            "next": {"filename": content_folder + "all/elite_g_flight.html", "name": "Elite G flight source"}
        },
        "elite_g_flight": {
            "prev": {"filename": content_folder + "all/elite_f_flight.html", "name": "Elite F flight source"},
            "next": {"filename": content_folder + "all/elite_h_flight.html", "name": "Elite H flight source"}
        },
        "elite_h_flight": {
            "prev": {"filename": content_folder + "all/elite_g_flight.html", "name": "Elite G flight source"},
            "next": {"filename": content_folder + "all/workspaces_encyclopedia.html", "name": "Encyclopedia workspaces"}
        },
        "workspaces_encyclopedia": {
            "prev": {"filename": content_folder + "all/elite_h_flight.html", "name": "Elite H flight source"},
            "next": {"filename": content_folder + "all/elite_a_encyclopedia.html", "name": "Elite A encyclopedia source"},
        },
        "elite_a_encyclopedia": {
            "prev": {"filename": content_folder + "all/workspaces_encyclopedia.html", "name": "Encyclopedia workspaces"},
            "next": {"filename": content_folder + "all/elite_b_encyclopedia.html", "name": "Elite B encyclopedia source"}
        },
        "elite_b_encyclopedia": {
            "prev": {"filename": content_folder + "all/elite_a_encyclopedia.html", "name": "Elite A encyclopedia source"},
            "next": {"filename": content_folder + "all/elite_c_encyclopedia.html", "name": "Elite C encyclopedia source"}
        },
        "elite_c_encyclopedia": {
            "prev": {"filename": content_folder + "all/elite_b_encyclopedia.html", "name": "Elite B encyclopedia source"},
            "next": {"filename": content_folder + "all/elite_d_encyclopedia.html", "name": "Elite D encyclopedia source"}
        },
        "elite_d_encyclopedia": {
            "prev": {"filename": content_folder + "all/elite_c_encyclopedia.html", "name": "Elite C encyclopedia source"},
            "next": {"filename": content_folder + "all/elite_e_encyclopedia.html", "name": "Elite E encyclopedia source"}
        },
        "elite_e_encyclopedia": {
            "prev": {"filename": content_folder + "all/elite_d_encyclopedia.html", "name": "Elite D encyclopedia source"},
            "next": {"filename": content_folder + "all/elite_f_encyclopedia.html", "name": "Elite F encyclopedia source"}
        },
        "elite_f_encyclopedia": {
            "prev": {"filename": content_folder + "all/elite_e_encyclopedia.html", "name": "Elite E encyclopedia source"},
            "next": {"filename": content_folder + "all/elite_g_encyclopedia.html", "name": "Elite G encyclopedia source"}
        },
        "elite_g_encyclopedia": {
            "prev": {"filename": content_folder + "all/elite_f_encyclopedia.html", "name": "Elite F encyclopedia source"},
            "next": {"filename": content_folder + "all/elite_h_encyclopedia.html", "name": "Elite H encyclopedia source"}
        },
        "elite_h_encyclopedia": {
            "prev": {"filename": content_folder + "all/elite_g_encyclopedia.html", "name": "Elite G encyclopedia source"},
            "next": {"filename": content_folder + "all/elite_ships_a.html", "name": "Ship blueprints A"}
        },
        "elite_ships_a": {
            "prev": {"filename": content_folder + "all/elite_h_encyclopedia.html", "name": "Elite H encyclopedia source"},
            "next": {"filename": content_folder + "all/elite_ships_b.html", "name": "Ship blueprints B"}
        },
        "elite_ships_b": {
            "prev": {"filename": content_folder + "all/elite_ships_a.html", "name": "Ship blueprints A"},
            "next": {"filename": content_folder + "all/elite_ships_c.html", "name": "Ship blueprints C"}
        },
        "elite_ships_c": {
            "prev": {"filename": content_folder + "all/elite_ships_b.html", "name": "Ship blueprints B"},
            "next": {"filename": content_folder + "all/elite_ships_d.html", "name": "Ship blueprints D"}
        },
        "elite_ships_d": {
            "prev": {"filename": content_folder + "all/elite_ships_c.html", "name": "Ship blueprints C"},
            "next": {"filename": content_folder + "all/elite_ships_e.html", "name": "Ship blueprints E"}
        },
        "elite_ships_e": {
            "prev": {"filename": content_folder + "all/elite_ships_d.html", "name": "Ship blueprints D"},
            "next": {"filename": content_folder + "all/elite_ships_f.html", "name": "Ship blueprints F"}
        },
        "elite_ships_f": {
            "prev": {"filename": content_folder + "all/elite_ships_e.html", "name": "Ship blueprints E"},
            "next": {"filename": content_folder + "all/elite_ships_g.html", "name": "Ship blueprints G"}
        },
        "elite_ships_g": {
            "prev": {"filename": content_folder + "all/elite_ships_f.html", "name": "Ship blueprints F"},
            "next": {"filename": content_folder + "all/elite_ships_h.html", "name": "Ship blueprints H"}
        },
        "elite_ships_h": {
            "prev": {"filename": content_folder + "all/elite_ships_g.html", "name": "Ship blueprints G"},
            "next": {"filename": content_folder + "all/elite_ships_i.html", "name": "Ship blueprints I"}
        },
        "elite_ships_i": {
            "prev": {"filename": content_folder + "all/elite_ships_h.html", "name": "Ship blueprints H"},
            "next": {"filename": content_folder + "all/elite_ships_j.html", "name": "Ship blueprints J"}
        },
        "elite_ships_j": {
            "prev": {"filename": content_folder + "all/elite_ships_i.html", "name": "Ship blueprints I"},
            "next": {"filename": content_folder + "all/elite_ships_k.html", "name": "Ship blueprints K"}
        },
        "elite_ships_k": {
            "prev": {"filename": content_folder + "all/elite_ships_j.html", "name": "Ship blueprints J"},
            "next": {"filename": content_folder + "all/elite_ships_l.html", "name": "Ship blueprints L"}
        },
        "elite_ships_l": {
            "prev": {"filename": content_folder + "all/elite_ships_k.html", "name": "Ship blueprints K"},
            "next": {"filename": content_folder + "all/elite_ships_m.html", "name": "Ship blueprints M"}
        },
        "elite_ships_m": {
            "prev": {"filename": content_folder + "all/elite_ships_l.html", "name": "Ship blueprints L"},
            "next": {"filename": content_folder + "all/elite_ships_n.html", "name": "Ship blueprints N"}
        },
        "elite_ships_n": {
            "prev": {"filename": content_folder + "all/elite_ships_m.html", "name": "Ship blueprints M"},
            "next": {"filename": content_folder + "all/elite_ships_o.html", "name": "Ship blueprints O"}
        },
        "elite_ships_o": {
            "prev": {"filename": content_folder + "all/elite_ships_n.html", "name": "Ship blueprints N"},
            "next": {"filename": content_folder + "all/elite_ships_p.html", "name": "Ship blueprints P"}
        },
        "elite_ships_p": {
            "prev": {"filename": content_folder + "all/elite_ships_o.html", "name": "Ship blueprints O"},
            "next": {"filename": content_folder + "all/elite_ships_q.html", "name": "Ship blueprints Q"}
        },
        "elite_ships_q": {
            "prev": {"filename": content_folder + "all/elite_ships_p.html", "name": "Ship blueprints P"},
            "next": {"filename": content_folder + "all/elite_ships_r.html", "name": "Ship blueprints R"}
        },
        "elite_ships_r": {
            "prev": {"filename": content_folder + "all/elite_ships_q.html", "name": "Ship blueprints Q"},
            "next": {"filename": content_folder + "all/elite_ships_s.html", "name": "Ship blueprints S"}
        },
        "elite_ships_s": {
            "prev": {"filename": content_folder + "all/elite_ships_r.html", "name": "Ship blueprints R"},
            "next": {"filename": content_folder + "all/elite_ships_t.html", "name": "Ship blueprints T"}
        },
        "elite_ships_t": {
            "prev": {"filename": content_folder + "all/elite_ships_s.html", "name": "Ship blueprints S"},
            "next": {"filename": content_folder + "all/elite_ships_u.html", "name": "Ship blueprints U"}
        },
        "elite_ships_u": {
            "prev": {"filename": content_folder + "all/elite_ships_t.html", "name": "Ship blueprints T"},
            "next": {"filename": content_folder + "all/elite_ships_v.html", "name": "Ship blueprints V"}
        },
        "elite_ships_v": {
            "prev": {"filename": content_folder + "all/elite_ships_u.html", "name": "Ship blueprints U"},
            "next": {"filename": content_folder + "all/elite_ships_w.html", "name": "Ship blueprints W"}
        },
        "elite_ships_w": {
            "prev": {"filename": content_folder + "all/elite_ships_v.html", "name": "Ship blueprints V"},
            "next": {"filename": content_folder + "all/i_o_processor.html", "name": "I/O processor source"}
        },
        "i_o_processor": {
            "prev": {"filename": content_folder + "all/elite_ships_w.html", "name": "Ship blueprints W"},
            "next": {"filename": content_folder + "all/workspaces_parasite.html", "name": "Parasite workspaces"}
        },
        "workspaces_parasite": {
            "prev": {"filename": content_folder + "all/i_o_processor.html", "name": "I/O processor source"},
            "next": {"filename": content_folder + "all/elite_a_parasite.html", "name": "Elite A parasite source"},
        },
        "elite_a_parasite": {
            "prev": {"filename": content_folder + "all/workspaces_parasite.html", "name": "Parasite workspaces"},
            "next": {"filename": content_folder + "all/elite_b_parasite.html", "name": "Elite B parasite source"}
        },
        "elite_b_parasite": {
            "prev": {"filename": content_folder + "all/elite_a_parasite.html", "name": "Elite A parasite source"},
            "next": {"filename": content_folder + "all/elite_c_parasite.html", "name": "Elite C parasite source"}
        },
        "elite_c_parasite": {
            "prev": {"filename": content_folder + "all/elite_b_parasite.html", "name": "Elite B parasite source"},
            "next": {"filename": content_folder + "all/elite_d_parasite.html", "name": "Elite D parasite source"}
        },
        "elite_d_parasite": {
            "prev": {"filename": content_folder + "all/elite_c_parasite.html", "name": "Elite C parasite source"},
            "next": {"filename": content_folder + "all/elite_e_parasite.html", "name": "Elite E parasite source"}
        },
        "elite_e_parasite": {
            "prev": {"filename": content_folder + "all/elite_d_parasite.html", "name": "Elite D parasite source"},
            "next": {"filename": content_folder + "all/elite_f_parasite.html", "name": "Elite F parasite source"}
        },
        "elite_f_parasite": {
            "prev": {"filename": content_folder + "all/elite_e_parasite.html", "name": "Elite E parasite source"},
            "next": {"filename": content_folder + "all/elite_g_parasite.html", "name": "Elite G parasite source"}
        },
        "elite_g_parasite": {
            "prev": {"filename": content_folder + "all/elite_f_parasite.html", "name": "Elite F parasite source"},
            "next": {"filename": content_folder + "all/elite_h_parasite.html", "name": "Elite H parasite source"}
        },
        "elite_h_parasite": {
            "prev": {"filename": content_folder + "all/elite_g_parasite.html", "name": "Elite G parasite source"},
            "next": {"filename": content_folder + "all/elite_i_parasite.html", "name": "Elite I parasite source"}
        },
        "elite_i_parasite": {
            "prev": {"filename": content_folder + "all/elite_h_parasite.html", "name": "Elite H parasite source"},
            "next": {"filename": content_folder + "all/elite_j_parasite.html", "name": "Elite J parasite source"}
        },
        "elite_j_parasite": {
            "prev": {"filename": content_folder + "all/elite_i_parasite.html", "name": "Elite I parasite source"},
            "next": {"filename": content_folder + "all/elite_k_parasite.html", "name": "Elite K parasite source"}
        },
        "elite_k_parasite": {
            "prev": {"filename": content_folder + "all/elite_j_parasite.html", "name": "Elite J parasite source"},
            "next": {"filename": content_folder + "all/elite_l_parasite.html", "name": "Elite L parasite source"}
        },
        "elite_l_parasite": {
            "prev": {"filename": content_folder + "all/elite_k_parasite.html", "name": "Elite K parasite source"},
            "next": {"filename": content_folder + "all/elite_m_parasite.html", "name": "Elite M parasite source"}
        },
        "elite_m_parasite": {
            "prev": {"filename": content_folder + "all/elite_l_parasite.html", "name": "Elite L parasite source"},
            "next": {"filename": content_folder + "all/elite_ships_parasite.html", "name": "Ship blueprints parasite source"}
        },
        "elite_ships_parasite": {
            "prev": {"filename": content_folder + "all/elite_m_parasite.html", "name": "Elite M parasite source"},
            "next": None
        }
    }
elif args.platform == "nes":
    next_prev_all = {
        "map_of_the_source_code": {
            "prev": {"filename": content_folder + "releases.html", "name": "Different variants of the NES version"},
            "next": {"filename": content_folder + "all/common.html", "name": "Common source"}
        },
        "common": {
            "prev": {"filename": content_folder + "articles/map_of_the_source_code.html", "name": "Map of the source code"},
            "next": {"filename": content_folder + "all/header.html", "name": "iNES header source"}
        },
        "header": {
            "prev": {"filename": content_folder + "all/common.html", "name": "Common source"},
            "next": {"filename": content_folder + "all/bank_0_1.html", "name": "Bank 0 source (Part 1 of 5)"}
        },
        "bank_0_1": {
            "prev": {"filename": content_folder + "all/header.html", "name": "iNES header source"},
            "next": {"filename": content_folder + "all/bank_0_2.html", "name": "Bank 0 source (Part 2 of 5)"}
        },
        "bank_0_2": {
            "prev": {"filename": content_folder + "all/bank_0_1.html", "name": "Bank 0 source (Part 1 of 5)"},
            "next": {"filename": content_folder + "all/bank_0_3.html", "name": "Bank 0 source (Part 3 of 5)"}
        },
        "bank_0_3": {
            "prev": {"filename": content_folder + "all/bank_0_2.html", "name": "Bank 0 source (Part 2 of 5)"},
            "next": {"filename": content_folder + "all/bank_0_4.html", "name": "Bank 0 source (Part 4 of 5)"}
        },
        "bank_0_4": {
            "prev": {"filename": content_folder + "all/bank_0_3.html", "name": "Bank 0 source (Part 3 of 5)"},
            "next": {"filename": content_folder + "all/bank_0_5.html", "name": "Bank 0 source (Part 5 of 5)"}
        },
        "bank_0_5": {
            "prev": {"filename": content_folder + "all/bank_0_4.html", "name": "Bank 0 source (Part 4 of 5)"},
            "next": {"filename": content_folder + "all/bank_1_1.html", "name": "Bank 1 source (Part 1 of 3)"}
        },
        "bank_1_1": {
            "prev": {"filename": content_folder + "all/bank_0_5.html", "name": "Bank 0 source (Part 5 of 5)"},
            "next": {"filename": content_folder + "all/bank_1_2.html", "name": "Bank 1 source (Part 2 of 3)"}
        },
        "bank_1_2": {
            "prev": {"filename": content_folder + "all/bank_1_1.html", "name": "Bank 1 source (Part 1 of 3)"},
            "next": {"filename": content_folder + "all/bank_1_3.html", "name": "Bank 1 source (Part 3 of 3)"}
        },
        "bank_1_3": {
            "prev": {"filename": content_folder + "all/bank_1_2.html", "name": "Bank 1 source (Part 2 of 3)"},
            "next": {"filename": content_folder + "all/bank_2_1.html", "name": "Bank 2 source (Part 1 of 4)"}
        },
        "bank_2_1": {
            "prev": {"filename": content_folder + "all/bank_1_3.html", "name": "Bank 1 source (Part 3 of 3)"},
            "next": {"filename": content_folder + "all/bank_2_2.html", "name": "Bank 2 source (Part 2 of 4)"}
        },
        "bank_2_2": {
            "prev": {"filename": content_folder + "all/bank_2_1.html", "name": "Bank 2 source (Part 1 of 4)"},
            "next": {"filename": content_folder + "all/bank_2_3.html", "name": "Bank 2 source (Part 3 of 4)"}
        },
        "bank_2_3": {
            "prev": {"filename": content_folder + "all/bank_2_2.html", "name": "Bank 2 source (Part 2 of 4)"},
            "next": {"filename": content_folder + "all/bank_2_4.html", "name": "Bank 2 source (Part 4 of 4)"}
        },
        "bank_2_4": {
            "prev": {"filename": content_folder + "all/bank_2_3.html", "name": "Bank 2 source (Part 3 of 4)"},
            "next": {"filename": content_folder + "all/bank_3_1.html", "name": "Bank 3 source (Part 1 of 2)"}
        },
        "bank_3_1": {
            "prev": {"filename": content_folder + "all/bank_2_4.html", "name": "Bank 2 source (Part 4 of 4)"},
            "next": {"filename": content_folder + "all/bank_3_2.html", "name": "Bank 3 source (Part 2 of 2)"}
        },
        "bank_3_2": {
            "prev": {"filename": content_folder + "all/bank_3_1.html", "name": "Bank 3 source (Part 1 of 2)"},
            "next": {"filename": content_folder + "all/bank_4.html", "name": "Bank 4 source"}
        },
        "bank_4": {
            "prev": {"filename": content_folder + "all/bank_3_2.html", "name": "Bank 3 source (Part 2 of 2)"},
            "next": {"filename": content_folder + "all/bank_5.html", "name": "Bank 5 source"}
        },
        "bank_5": {
            "prev": {"filename": content_folder + "all/bank_4.html", "name": "Bank 4 source"},
            "next": {"filename": content_folder + "all/bank_6_1.html", "name": "Bank 6 source (Part 1 of 3)"}
        },
        "bank_6_1": {
            "prev": {"filename": content_folder + "all/bank_5.html", "name": "Bank 5 source"},
            "next": {"filename": content_folder + "all/bank_6_2.html", "name": "Bank 6 source (Part 2 of 3)"}
        },
        "bank_6_2": {
            "prev": {"filename": content_folder + "all/bank_6_1.html", "name": "Bank 6 source (Part 1 of 3)"},
            "next": {"filename": content_folder + "all/bank_6_3.html", "name": "Bank 6 source (Part 3 of 3)"}
        },
        "bank_6_3": {
            "prev": {"filename": content_folder + "all/bank_6_2.html", "name": "Bank 6 source (Part 2 of 3)"},
            "next": {"filename": content_folder + "all/bank_7_1.html", "name": "Bank 7 source (Part 1 of 4)"}
        },
        "bank_7_1": {
            "prev": {"filename": content_folder + "all/bank_6_3.html", "name": "Bank 6 source (Part 3 of 3)"},
            "next": {"filename": content_folder + "all/bank_7_2.html", "name": "Bank 7 source (Part 2 of 4)"}
        },
        "bank_7_2": {
            "prev": {"filename": content_folder + "all/bank_7_1.html", "name": "Bank 7 source (Part 1 of 4)"},
            "next": {"filename": content_folder + "all/bank_7_3.html", "name": "Bank 7 source (Part 3 of 4)"}
        },
        "bank_7_3": {
            "prev": {"filename": content_folder + "all/bank_7_2.html", "name": "Bank 7 source (Part 2 of 4)"},
            "next": {"filename": content_folder + "all/bank_7_4.html", "name": "Bank 7 source (Part 4 of 4)"}
        },
        "bank_7_4": {
            "prev": {"filename": content_folder + "all/bank_7_3.html", "name": "Bank 7 source (Part 3 of 4)"},
            "next": None
        }
    }
elif args.platform == "aviator":
    next_prev_all = {
        "map_of_the_source_code": {
            "prev": {"filename": content_folder + "index.html", "name": "About the version of Aviator on this site"},
            "next": {"filename": content_folder + "all/workspaces.html", "name": "Workspaces and configuration"}
        },
        "workspaces": {
            "prev": {"filename": content_folder + "articles/map_of_the_source_code.html", "name": "Map of the source code"},
            "next": {"filename": content_folder + "all/aviator_a.html", "name": "Aviator A source"}
        },
        "aviator_a": {
            "prev": {"filename": content_folder + "all/workspaces.html", "name": "Workspaces and configuration"},
            "next": {"filename": content_folder + "all/aviator_b.html", "name": "Aviator B source"}
        },
        "aviator_b": {
            "prev": {"filename": content_folder + "all/aviator_a.html", "name": "Aviator A source"},
            "next": {"filename": content_folder + "all/aviator_c.html", "name": "Aviator C source"}
        },
        "aviator_c": {
            "prev": {"filename": content_folder + "all/aviator_b.html", "name": "Aviator B source"},
            "next": {"filename": content_folder + "all/aviator_d.html", "name": "Aviator D source"}
        },
        "aviator_d": {
            "prev": {"filename": content_folder + "all/aviator_c.html", "name": "Aviator C source"},
            "next": {"filename": content_folder + "all/aviator_e.html", "name": "Aviator E source"}
        },
        "aviator_e": {
            "prev": {"filename": content_folder + "all/aviator_d.html", "name": "Aviator D source"},
            "next": {"filename": content_folder + "all/aviator_f.html", "name": "Aviator F source"}
        },
        "aviator_f": {
            "prev": {"filename": content_folder + "all/aviator_e.html", "name": "Aviator E source"},
            "next": None
        }
    }
elif args.platform == "revs":
    next_prev_all = {
        "map_of_the_source_code": {
            "prev": {"filename": content_folder + "releases.html", "name": "Different variants of BBC Micro Revs"},
            "next": {"filename": content_folder + "all/workspaces.html", "name": "Workspaces and configuration"}
        },
        "workspaces": {
            "prev": {"filename": content_folder + "articles/map_of_the_source_code.html", "name": "Map of the source code"},
            "next": {"filename": content_folder + "all/revs_a.html", "name": "Revs A source"}
        },
        "revs_a": {
            "prev": {"filename": content_folder + "all/workspaces.html", "name": "Workspaces and configuration"},
            "next": {"filename": content_folder + "all/revs_b.html", "name": "Revs B source"}
        },
        "revs_b": {
            "prev": {"filename": content_folder + "all/revs_a.html", "name": "Revs A source"},
            "next": {"filename": content_folder + "all/revs_c.html", "name": "Revs C source"}
        },
        "revs_c": {
            "prev": {"filename": content_folder + "all/revs_b.html", "name": "Revs B source"},
            "next": {"filename": content_folder + "all/revs_d.html", "name": "Revs D source"}
        },
        "revs_d": {
            "prev": {"filename": content_folder + "all/revs_c.html", "name": "Revs C source"},
            "next": {"filename": content_folder + "all/revs_e.html", "name": "Revs E source"}
        },
        "revs_e": {
            "prev": {"filename": content_folder + "all/revs_d.html", "name": "Revs D source"},
            "next": {"filename": content_folder + "all/revs_f.html", "name": "Revs F source"}
        },
        "revs_f": {
            "prev": {"filename": content_folder + "all/revs_e.html", "name": "Revs E source"},
            "next": {"filename": content_folder + "all/revs_g.html", "name": "Revs G source"}
        },
        "revs_g": {
            "prev": {"filename": content_folder + "all/revs_f.html", "name": "Revs F source"},
            "next": {"filename": content_folder + "all/revs_h.html", "name": "Revs H source"}
        },
        "revs_h": {
            "prev": {"filename": content_folder + "all/revs_g.html", "name": "Revs G source"},
            "next": {"filename": content_folder + "all/revs_i.html", "name": "Revs I source"}
        },
        "revs_i": {
            "prev": {"filename": content_folder + "all/revs_h.html", "name": "Revs H source"},
            "next": {"filename": content_folder + "all/revs_silverstone.html", "name": "Silverstone track data file"}
        },
        "revs_silverstone": {
            "prev": {"filename": content_folder + "all/revs_i.html", "name": "Revs I source"},
            "next": {"filename": content_folder + "all/revs_brands_hatch.html", "name": "Brands Hatch track data file"}
        },
        "revs_brands_hatch": {
            "prev": {"filename": content_folder + "all/revs_silverstone.html", "name": "Silverstone track data file"},
            "next": {"filename": content_folder + "all/revs_donington_park.html", "name": "Donington Park track data file"}
        },
        "revs_donington_park": {
            "prev": {"filename": content_folder + "all/revs_brands_hatch.html", "name": "Brands Hatch track data file"},
            "next": {"filename": content_folder + "all/revs_oulton_park.html", "name": "Oulton Park track data file"}
        },
        "revs_oulton_park": {
            "prev": {"filename": content_folder + "all/revs_donington_park.html", "name": "Donington Park track data file"},
            "next": {"filename": content_folder + "all/revs_snetterton.html", "name": "Snetterton track data file"}
        },
        "revs_snetterton": {
            "prev": {"filename": content_folder + "all/revs_oulton_park.html", "name": "Oulton Park track data file"},
            "next": {"filename": content_folder + "all/revs_nurburgring.html", "name": "Nürburgring track data file"}
        },
        "revs_nurburgring": {
            "prev": {"filename": content_folder + "all/revs_snetterton.html", "name": "Snetterton track data file"},
            "next": None
        }
    }
elif args.platform == "lander":
    next_prev_all = {
        "map_of_the_source_code": {
            "prev": {"filename": content_folder + "index.html", "name": "About the version of Lander on this site"},
            "next": {"filename": content_folder + "all/workspaces.html", "name": "Workspaces and configuration"}
        },
        "workspaces": {
            "prev": {"filename": content_folder + "articles/map_of_the_source_code.html", "name": "Map of the source code"},
            "next": {"filename": content_folder + "all/lander_a.html", "name": "Lander A source"}
        },
        "lander_a": {
            "prev": {"filename": content_folder + "all/workspaces.html", "name": "Workspaces and configuration"},
            "next": {"filename": content_folder + "all/lander_b.html", "name": "Lander B source"}
        },
        "lander_b": {
            "prev": {"filename": content_folder + "all/lander_a.html", "name": "Lander A source"},
            "next": {"filename": content_folder + "all/lander_c.html", "name": "Lander C source"}
        },
        "lander_c": {
            "prev": {"filename": content_folder + "all/lander_b.html", "name": "Lander B source"},
            "next": {"filename": content_folder + "all/lander_d.html", "name": "Lander D source"}
        },
        "lander_d": {
            "prev": {"filename": content_folder + "all/lander_c.html", "name": "Lander C source"},
            "next": {"filename": content_folder + "all/runimage.html", "name": "!RunImage source"}
        },
        "lander_runimage": {
            "prev": {"filename": content_folder + "all/lander_d.html", "name": "Lander D source"},
            "next": None
        }
    }

next_prev_compare_categories = {
    "standard": {
        "prev": {"filename": content_folder + "how_to_compare.html", "name": "How to compare different versions"},
        "next": {"filename": content_folder + "indexes/shared_code_enhanced.html", "name": "Variations in enhanced Elite"}
    },
    "enhanced": {
        "prev": {"filename": content_folder + "indexes/shared_code_standard.html", "name": "Variations in standard Elite"},
        "next": {"filename": content_folder + "indexes/shared_code_advanced.html", "name": "Variations in advanced Elite"}
    },
    "advanced": {
        "prev": {"filename": content_folder + "indexes/shared_code_enhanced.html", "name": "Variations in enhanced Elite"},
        "next": {"filename": content_folder + "indexes/shared_code_disc.html", "name": "Variations in disc Elite"}
    },
    "disc": {
        "prev": {"filename": content_folder + "indexes/shared_code_advanced.html", "name": "Variations in advanced Elite"},
        "next": {"filename": content_folder + "indexes/shared_code_electron.html", "name": "Variations in the Electron version"}
    },
    "electron": {
        "prev": {"filename": content_folder + "indexes/shared_code_disc.html", "name": "Variations in disc Elite"},
        "next": {"filename": content_folder + "indexes/shared_code_6502sp.html", "name": "Variations in 6502SP Elite"}
    },
    "6502sp": {
        "prev": {"filename": content_folder + "indexes/shared_code_electron.html", "name": "Variations in the Electron version"},
        "next": {"filename": content_folder + "indexes/shared_code_master.html", "name": "Variations in the Master version"}
    },
    "master": {
        "prev": {"filename": content_folder + "indexes/shared_code_6502sp.html", "name": "Variations in 6502SP Elite"},
        "next": {"filename": content_folder + "indexes/shared_code_other.html", "name": "Other interesting variations"}
    },
    "other": {
        "prev": {"filename": content_folder + "indexes/shared_code_master.html", "name": "Variations in the Master version"},
        "next": {"filename": content_folder + "indexes/shared_code_other_variations.html", "name": "Minor variations"}
    },
    "other_categories": {
        "prev": {"filename": content_folder + "indexes/shared_code_other.html", "name": "Other interesting variations"},
        "next": None
    }
}

next_prev_compare_indexes = {
    "shared_code_with_variations": {
        "prev": None,
        "next": {"filename": content_folder + "indexes/shared_code_no_variations.html", "name": "Shared code, no variations"}
    },
    "shared_code_no_variations": {
        "prev": {"filename": content_folder + "indexes/shared_code_with_variations.html", "name": "Shared code with variations"},
        "next": {"filename": content_folder + "indexes/version_specific_code.html", "name": "Version-specific code"}
    },
    "version_specific_code": {
        "prev": {"filename": content_folder + "indexes/shared_code_no_variations.html", "name": "Shared code, no variations"},
        "next": None
    }
}
if args.platform == "aviator":
    next_prev_indexes = {
        "a-z": {
            "prev": None,
            "next": {"filename": content_folder + "articles/source_code_cross-references.html", "name": "Source code cross-references"}
        },
        "cross-references": {
            "prev": {"filename": content_folder + "indexes/a-z.html", "name": "A-Z index of the source code"},
            "next": {"filename": content_folder + "indexes/subroutines.html", "name": "List of all subroutines"}
        },
        "subroutines": {
            "prev": {"filename": content_folder + "articles/source_code_cross-references.html", "name": "Source code cross-references"},
            "next": {"filename": content_folder + "indexes/variables.html", "name": "List of all variables"}
        },
        "variables": {
            "prev": {"filename": content_folder + "indexes/subroutines.html", "name": "List of all subroutines"},
            "next": {"filename": content_folder + "indexes/workspaces.html", "name": "List of all workspaces"}
        },
        "workspaces": {
            "prev": {"filename": content_folder + "indexes/variables.html", "name": "List of all variables"},
            "next": None
        }
    }
elif args.platform == "lander":
    next_prev_indexes = {
        "a-z": {
            "prev": None,
            "next": {"filename": content_folder + "articles/source_code_cross-references.html", "name": "Source code cross-references"}
        },
        "cross-references": {
            "prev": {"filename": content_folder + "indexes/a-z.html", "name": "A-Z index of the source code"},
            "next": {"filename": content_folder + "indexes/subroutines.html", "name": "List of all subroutines"}
        },
        "subroutines": {
            "prev": {"filename": content_folder + "articles/source_code_cross-references.html", "name": "Source code cross-references"},
            "next": {"filename": content_folder + "indexes/variables.html", "name": "List of all variables"}
        },
        "variables": {
            "prev": {"filename": content_folder + "indexes/subroutines.html", "name": "List of all subroutines"},
            "next": None
        }
    }
elif args.platform == "revs":
    next_prev_indexes = {
        "a-z": {
            "prev": None,
            "next": {"filename": content_folder + "articles/source_code_cross-references.html", "name": "Source code cross-references"}
        },
        "cross-references": {
            "prev": {"filename": content_folder + "indexes/a-z.html", "name": "A-Z index of the source code"},
            "next": {"filename": content_folder + "indexes/subroutines.html", "name": "List of all subroutines"}
        },
        "subroutines": {
            "prev": {"filename": content_folder + "articles/source_code_cross-references.html", "name": "Source code cross-references"},
            "next": {"filename": content_folder + "indexes/variables.html", "name": "List of all variables"}
        },
        "variables": {
            "prev": {"filename": content_folder + "indexes/subroutines.html", "name": "List of all subroutines"},
            "next": {"filename": content_folder + "indexes/workspaces.html", "name": "List of all workspaces"}
        },
        "workspaces": {
            "prev": {"filename": content_folder + "indexes/variables.html", "name": "List of all variables"},
            "next": {"filename": content_folder + "indexes/macros.html", "name": "List of all macros"}
        },
        "macros": {
            "prev": {"filename": content_folder + "indexes/workspaces.html", "name": "List of all workspaces"},
            "next": None
        }
    }
else:
    next_prev_indexes = {
        "a-z": {
            "prev": None,
            "next": {"filename": content_folder + "articles/source_code_cross-references.html", "name": "Source code cross-references"}
        },
        "cross-references": {
            "prev": {"filename": content_folder + "indexes/a-z.html", "name": "A-Z index of the source code"},
            "next": {"filename": content_folder + "indexes/subroutines.html", "name": "List of all subroutines"}
        },
        "subroutines": {
            "prev": {"filename": content_folder + "articles/source_code_cross-references.html", "name": "Source code cross-references"},
            "next": {"filename": content_folder + "indexes/variables.html", "name": "List of all variables"}
        },
        "variables": {
            "prev": {"filename": content_folder + "indexes/subroutines.html", "name": "List of all subroutines"},
            "next": {"filename": content_folder + "indexes/workspaces.html", "name": "List of all workspaces"}
        },
        "workspaces": {
            "prev": {"filename": content_folder + "indexes/variables.html", "name": "List of all variables"},
            "next": {"filename": content_folder + "indexes/macros.html", "name": "List of all macros"}
        },
        "macros": {
            "prev": {"filename": content_folder + "indexes/workspaces.html", "name": "List of all workspaces"},
            "next": None
        }
    }

next_prev_statistics = {
    "cassette": {
        "prev": None,
        "next": {"filename": "disc/articles/source_code_statistics.html", "name": "Statistics for the BBC Micro disc version"}
    },
    "disc": {
        "prev": {"filename": "cassette/articles/source_code_statistics.html", "name": "Statistics for the cassette version"},
        "next": {"filename": "electron/articles/source_code_statistics.html", "name": "Statistics for the Electron version"}
    },
    "electron": {
        "prev": {"filename": "disc/articles/source_code_statistics.html", "name": "Statistics for the disc version"},
        "next": {"filename": "6502sp/articles/source_code_statistics.html", "name": "Statistics for the 6502SP version"}
    },
    "6502sp": {
        "prev": {"filename": "electron/articles/source_code_statistics.html", "name": "Statistics for the Electron version"},
        "next": {"filename": "c64/articles/source_code_statistics.html", "name": "Statistics for the C64 version"}
    },
    "c64": {
        "prev": {"filename": "6502sp/articles/source_code_statistics.html", "name": "Statistics for the 6502SP version"},
        "next": {"filename": "apple/articles/source_code_statistics.html", "name": "Statistics for the Apple II version"}
    },
    "apple": {
        "prev": {"filename": "c64/articles/source_code_statistics.html", "name": "Statistics for the Commodore 64 version"},
        "next": {"filename": "master/articles/source_code_statistics.html", "name": "Statistics for the Master version"}
    },
    "master": {
        "prev": {"filename": "apple/articles/source_code_statistics.html", "name": "Statistics for the Apple II version"},
        "next": {"filename": "nes/articles/source_code_statistics.html", "name": "Statistics for the NES version"}
    },
    "nes": {
        "prev": {"filename": "master/articles/source_code_statistics.html", "name": "Statistics for the Master version"},
        "next": {"filename": "elite-a/articles/source_code_statistics.html", "name": "Statistics for Elite-A"}
    },
    "elite-a": {
        "prev": {"filename": "nes/articles/source_code_statistics.html", "name": "Statistics for the NES version"},
        "next": None
    },
    "aviator": {
        "prev": None,
        "next": None
    },
    "revs": {
        "prev": None,
        "next": None
    },
    "lander": {
        "prev": None,
        "next": None
    }
}

# Deep dives
if args.platform == "aviator":
    deep_dive_headers = [
        {
            "filename": "deep_dives/3d_objects.html",
            "name": "3D objects"
        },
        {
            "filename": "deep_dives/adding_bullets_to_the_world.html",
            "name": "Adding bullets to the world"
        },
        {
            "filename": "deep_dives/alien_feeding_and_growth_patterns.html",
            "name": "Alien feeding and growth patterns"
        },
        {
            "filename": "deep_dives/aliens_attack_acornsville.html",
            "name": "Aliens attack Acornsville!"
        },
        {
            "filename": "deep_dives/clock_hands_and_dial_indicators.html",
            "name": "Clock hands and dial indicators"
        },
        {
            "filename": "deep_dives/converting_pixel_coordinates_to_screen_addresses.html",
            "name": "Converting pixel coordinates to screen addresses"
        },
        {
            "filename": "deep_dives/detecting_alien_hits.html",
            "name": "Detecting alien hits"
        },
        {
            "filename": "deep_dives/explosions_and_turbulence.html",
            "name": "Explosions and turbulence"
        },
        {
            "filename": "deep_dives/flicker-free_animation_through_colour_cycling.html",
            "name": "Flicker-free animation through colour cycling"
        },
        {
            "filename": "deep_dives/flying_skills.html",
            "name": "Flying skills"
        },
        {
            "filename": "deep_dives/the_flight_model.html",
            "name": "The flight model"
        },
        {
            "filename": "deep_dives/hard-coded_division_in_the_dashboard_routines.html",
            "name": "Hard-coded division in the dashboard routines"
        },
        {
            "filename": "deep_dives/the_key_logger.html",
            "name": "The key logger"
        },
        {
            "filename": "deep_dives/line_buffers.html",
            "name": "Line buffers"
        },
        {
            "filename": "deep_dives/lines_and_points.html",
            "name": "Lines and points"
        },
        {
            "filename": "deep_dives/matching_the_code_to_the_flight_model.html",
            "name": "Matching the code to the flight model"
        },
        {
            "filename": "deep_dives/multi-byte_variables.html",
            "name": "Multi-byte variables"
        },
        {
            "filename": "deep_dives/on-ground_calculations.html",
            "name": "On-ground calculations"
        },
        {
            "filename": "deep_dives/placing_objects_on_the_map.html",
            "name": "Placing objects on the map"
        },
        {
            "filename": "deep_dives/program_flow_of_the_main_game_loop.html",
            "name": "Program flow of the main game loop"
        },
        {
            "filename": "deep_dives/random_numbers.html",
            "name": "Random numbers"
        },
        {
            "filename": "deep_dives/ripping_the_wings_off.html",
            "name": "Ripping the wings off"
        },
        {
            "filename": "deep_dives/rotation_matrices.html",
            "name": "Rotation matrices"
        },
        {
            "filename": "deep_dives/rotating_and_translating_points_in_3d_space.html",
            "name": "Rotating and translating points in 3D space"
        },
        {
            "filename": "deep_dives/scheduling_tasks_in_the_main_loop.html",
            "name": "Scheduling tasks in the main loop"
        },
        {
            "filename": "deep_dives/source_code_clues_hidden_in_the_game_binary.html",
            "name": "Source code clues hidden in the game binary"
        },
        {
            "filename": "deep_dives/stalling_and_recovery.html",
            "name": "Stalling and recovery"
        },
        {
            "filename": "deep_dives/take-offs_and_landings.html",
            "name": "Take-offs and landings"
        },
        {
            "filename": "deep_dives/times_tables_and_nibble_arithmetic.html",
            "name": "Times tables and nibble arithmetic"
        },
        {
            "filename": "deep_dives/trigonometry.html",
            "name": "Trigonometry"
        },
        {
            "filename": "deep_dives/visibility_checks.html",
            "name": "Visibility checks"
        }
    ]
elif args.platform == "revs":
    deep_dive_headers = [
        {
            "filename": "deep_dives/backporting_the_nurburgring_track.html",
            "name": "Backporting the Nürburgring track"
        },
        {
            "filename": "deep_dives/the_brands_hatch_track.html",
            "name": "The Brands Hatch track"
        },
        {
            "filename": "deep_dives/building_a_3d_track_from_sections_and_segments.html",
            "name": "Building a 3D track from sections and segments"
        },
        {
            "filename": "deep_dives/computer_assisted_steering.html",
            "name": "Computer assisted steering (CAS)"
        },
        {
            "filename": "deep_dives/the_core_driving_model.html",
            "name": "The core driving model"
        },
        {
            "filename": "deep_dives/code_hooks_in_the_extra_tracks.html",
            "name": "Code hooks in the extra tracks"
        },
        {
            "filename": "deep_dives/comparing_the_tracks.html",
            "name": "Comparing the tracks"
        },
        {
            "filename": "deep_dives/corner_markers.html",
            "name": "Corner markers"
        },
        {
            "filename": "deep_dives/creating_objects_from_edges.html",
            "name": "Creating objects from edges"
        },
        {
            "filename": "deep_dives/data_structures_for_the_track_calculations.html",
            "name": "Data structures for the track calculations"
        },
        {
            "filename": "deep_dives/the_donington_park_track.html",
            "name": "The Donington Park track"
        },
        {
            "filename": "deep_dives/drawing_a_3d_car_from_2d_parts.html",
            "name": "Drawing a 3D car from 2D parts"
        },
        {
            "filename": "deep_dives/drawing_around_the_dashboard.html",
            "name": "Drawing around the dashboard"
        },
        {
            "filename": "deep_dives/drawing_the_track_verges.html",
            "name": "Drawing the track verges"
        },
        {
            "filename": "deep_dives/drawing_the_track_view.html",
            "name": "Drawing the track view"
        },
        {
            "filename": "deep_dives/driving_on_grass.html",
            "name": "Driving on grass"
        },
        {
            "filename": "deep_dives/dynamic_track_generation_in_the_extra_tracks.html",
            "name": "Dynamic track generation in the extra tracks"
        },
        {
            "filename": "deep_dives/the_engine_sounds.html",
            "name": "The engine sounds"
        },
        {
            "filename": "deep_dives/the_extra_tracks_data_file_format.html",
            "name": "The extra tracks data file format"
        },
        {
            "filename": "deep_dives/hidden_secrets_of_the_custom_screen_mode.html",
            "name": "Hidden secrets of the custom screen mode"
        },
        {
            "filename": "deep_dives/jumps_and_drops.html",
            "name": "Jumps and drops"
        },
        {
            "filename": "deep_dives/major_variable_blocks.html",
            "name": "Major variable blocks"
        },
        {
            "filename": "deep_dives/matching_the_code_to_the_driving_model.html",
            "name": "Matching the code to the driving model"
        },
        {
            "filename": "deep_dives/modelling_the_engine.html",
            "name": "Modelling the engine"
        },
        {
            "filename": "deep_dives/the_nurburgring_track.html",
            "name": "The Nürburgring track"
        },
        {
            "filename": "deep_dives/object_definitions.html",
            "name": "Object definitions"
        },
        {
            "filename": "deep_dives/the_oulton_park_track.html",
            "name": "The Oulton Park track"
        },
        {
            "filename": "deep_dives/summary_of_the_driving_model.html",
            "name": "An overview of the driving model"
        },
        {
            "filename": "deep_dives/pitch_and_yaw_angles.html",
            "name": "Pitch and yaw angles"
        },
        {
            "filename": "deep_dives/placing_cars_on_the_track.html",
            "name": "Placing cars on the track"
        },
        {
            "filename": "deep_dives/program_flow_of_the_main_game_loop.html",
            "name": "Program flow of the main game loop"
        },
        {
            "filename": "deep_dives/random_numbers.html",
            "name": "Random numbers"
        },
        {
            "filename": "deep_dives/road_signs.html",
            "name": "Road signs"
        },
        {
            "filename": "deep_dives/scaling_objects_with_scaffolds.html",
            "name": "Scaling objects with scaffolds"
        },
        {
            "filename": "deep_dives/scheduling_tasks_in_the_main_loop.html",
            "name": "Scheduling tasks in the main loop"
        },
        {
            "filename": "deep_dives/secrets_of_the_extra_tracks.html",
            "name": "Secrets of the extra tracks"
        },
        {
            "filename": "deep_dives/the_silverstone_track.html",
            "name": "The Silverstone track"
        },
        {
            "filename": "deep_dives/skidding.html",
            "name": "Skidding"
        },
        {
            "filename": "deep_dives/the_snetterton_track.html",
            "name": "The Snetterton track"
        },
        {
            "filename": "deep_dives/starting_lights.html",
            "name": "Starting lights"
        },
        {
            "filename": "deep_dives/tactics_of_the_non-player_drivers.html",
            "name": "Tactics of the non-player drivers"
        },
        {
            "filename": "deep_dives/text_tokens.html",
            "name": "Text tokens"
        },
        {
            "filename": "deep_dives/the_revs_memory_map.html",
            "name": "The Revs memory map"
        },
        {
            "filename": "deep_dives/the_jigsaw_puzzle_binary.html",
            "name": "The jigsaw puzzle binary"
        },
        {
            "filename": "deep_dives/the_track_data_file_format.html",
            "name": "The track data file format"
        },
        {
            "filename": "deep_dives/the_track_verges.html",
            "name": "The track verges"
        },
        {
            "filename": "deep_dives/trigonometry.html",
            "name": "Trigonometry"
        },
        {
            "filename": "deep_dives/wing_mirrors.html",
            "name": "Wing mirrors"
        }
    ]
elif args.platform == "lander":
    deep_dive_headers = [
        {
            "filename": "deep_dives/camera_and_landscape_offset.html",
            "name": "The camera and the landscape offset"
        },
        {
            "filename": "deep_dives/comparing_lander_to_zarch.html",
            "name": "Comparing Lander to Zarch"
        },
        {
            "filename": "deep_dives/collisions_and_bullets.html",
            "name": "Collisions and bullets"
        },
        {
            "filename": "deep_dives/depth-sorting_with_the_graphics_buffers.html",
            "name": "Depth-sorting with the graphics buffers"
        },
        {
            "filename": "deep_dives/drawing_3d_objects.html",
            "name": "Drawing 3D objects"
        },
        {
            "filename": "deep_dives/drawing_the_landscape.html",
            "name": "Drawing the landscape"
        },
        {
            "filename": "deep_dives/drawing_triangles.html",
            "name": "Drawing triangles"
        },
        {
            "filename": "deep_dives/flying_by_mouse.html",
            "name": "Flying by mouse"
        },
        {
            "filename": "deep_dives/generating_the_landscape.html",
            "name": "Generating the landscape"
        },
        {
            "filename": "deep_dives/hacking_the_landscape.html",
            "name": "Hacking the landscape"
        },
        {
            "filename": "deep_dives/in_david_brabens_own_words.html",
            "name": "In David Braben's own words..."
        },
        {
            "filename": "deep_dives/landers_origins_on_the_arm1.html",
            "name": "Lander's origins on the ARM1"
        },
        {
            "filename": "deep_dives/main_game_loop.html",
            "name": "The main game loop"
        },
        {
            "filename": "deep_dives/object_blueprints.html",
            "name": "Object blueprints"
        },
        {
            "filename": "deep_dives/particles_and_particle_clouds.html",
            "name": "Particles and particle clouds"
        },
        {
            "filename": "deep_dives/placing_objects_on_the_map.html",
            "name": "Placing objects on the map"
        },
        {
            "filename": "deep_dives/projecting_onto_the_screen.html",
            "name": "Projecting onto the screen"
        },
        {
            "filename": "deep_dives/random_numbers.html",
            "name": "Random numbers"
        },
        {
            "filename": "deep_dives/screen_memory_in_the_archimedes.html",
            "name": "Screen memory in the Archimedes"
        },
        {
            "filename": "deep_dives/the_lander_memory_map.html",
            "name": "The Lander memory map"
        },
        {
            "filename": "deep_dives/unused_code_in_lander.html",
            "name": "Unused code in Lander"
        }
    ]
else:
    deep_dive_headers = [
        {
            "filename": "deep_dives/6502sp_demo_mode.html",
            "name": "The 6502 Second Processor demo mode"
        },
        {
            "filename": "deep_dives/6502sp_tube_communication.html",
            "name": "6502 Second Processor Tube communication"
        },
        {
            "filename": "deep_dives/the_3d_scanner.html",
            "name": "The 3D scanner"
        },
        {
            "filename": "deep_dives/adding_sign-magnitude_numbers.html",
            "name": "Adding sign-magnitude numbers"
        },
        {
            "filename": "deep_dives/advanced_tactics_with_the_newb_flags.html",
            "name": "Advanced tactics with the NEWB flags"
        },
        {
            "filename": "deep_dives/auto-playing_the_combat_demo.html",
            "name": "Auto-playing the combat demo"
        },
        {
            "filename": "deep_dives/back-face_culling.html",
            "name": "Back-face culling"
        },
        {
            "filename": "deep_dives/the_ball_line_heap.html",
            "name": "The ball line heap"
        },
        {
            "filename": "deep_dives/bitplanes_in_nes_elite.html",
            "name": "Bitplanes in NES Elite"
        },
        {
            "filename": "deep_dives/bolting_nes_controllers_onto_the_key_logger.html",
            "name": "Bolting NES controllers onto the key logger"
        },
        {
            "filename": "deep_dives/bresenhams_line_algorithm.html",
            "name": "Bresenham's line algorithm"
        },
        {
            "filename": "deep_dives/building_commodore_64_elite_from_the_source_disk.html",
            "name": "Building Commodore 64 Elite from the source disk"
        },
        {
            "filename": "deep_dives/elite-a_buying_and_flying_ships.html",
            "name": "Buying and flying ships in Elite-A"
        },
        {
            "filename": "deep_dives/calculating_square_roots.html",
            "name": "Calculating square roots"
        },
        {
            "filename": "deep_dives/calculating_vertex_coordinates.html",
            "name": "Calculating vertex coordinates"
        },
        {
            "filename": "deep_dives/colouring_the_commodore_64_bitmap_screen.html",
            "name": "Colouring the Commodore 64 bitmap screen"
        },
        {
            "filename": "deep_dives/combat_rank.html",
            "name": "Combat rank"
        },
        {
            "filename": "deep_dives/commander_save_files.html",
            "name": "Commander save files"
        },
        {
            "filename": "deep_dives/the_elite_memory_map_commodore_64.html",
            "name": "Commodore 64 Elite memory map"
        },
        {
            "filename": "deep_dives/comparing_nes_elite_with_the_other_versions.html",
            "name": "Comparing NES Elite with the other versions"
        },
        {
            "filename": "deep_dives/comparing_ship_specifications.html",
            "name": "Comparing ship specifications"
        },
        {
            "filename": "deep_dives/the_competition_code.html",
            "name": "The competition code"
        },
        {
            "filename": "deep_dives/the_constrictor_mission.html",
            "name": "The Constrictor mission"
        },
        {
            "filename": "deep_dives/the_dashboard_indicators.html",
            "name": "The dashboard indicators"
        },
        {
            "filename": "deep_dives/elite-a_delta_14b_joystick_support.html",
            "name": "Delta 14B joystick support"
        },
        {
            "filename": "deep_dives/developing_commodore_64_elite_on_a_bbc_micro.html",
            "name": "Developing Commodore 64 Elite on a BBC Micro"
        },
        {
            "filename": "deep_dives/displaying_two-layer_images.html",
            "name": "Displaying two-layer images"
        },
        {
            "filename": "deep_dives/docking_checks.html",
            "name": "Docking checks"
        },
        {
            "filename": "deep_dives/the_docking_computer.html",
            "name": "The docking computer"
        },
        {
            "filename": "deep_dives/drawing_circles.html",
            "name": "Drawing circles"
        },
        {
            "filename": "deep_dives/drawing_colour_pixels_in_mode_5.html",
            "name": "Drawing colour pixels on the BBC Micro"
        },
        {
            "filename": "deep_dives/drawing_craters.html",
            "name": "Drawing craters"
        },
        {
            "filename": "deep_dives/drawing_ellipses.html",
            "name": "Drawing ellipses"
        },
        {
            "filename": "deep_dives/drawing_explosion_clouds.html",
            "name": "Drawing explosion clouds"
        },
        {
            "filename": "deep_dives/drawing_lines_in_the_nes_version.html",
            "name": "Drawing lines in the NES version"
        },
        {
            "filename": "deep_dives/drawing_meridians_and_equators.html",
            "name": "Drawing meridians and equators"
        },
        {
            "filename": "deep_dives/drawing_monochrome_pixels_in_mode_4.html",
            "name": "Drawing monochrome pixels on the BBC Micro"
        },
        {
            "filename": "deep_dives/drawing_pixels_in_the_commodore_64_version.html",
            "name": "Drawing pixels in the Commodore 64 version"
        },
        {
            "filename": "deep_dives/drawing_pixels_in_the_electron_version.html",
            "name": "Drawing pixels in the Electron version"
        },
        {
            "filename": "deep_dives/drawing_pixels_in_the_nes_version.html",
            "name": "Drawing pixels in the NES version"
        },
        {
            "filename": "deep_dives/drawing_saturn_on_the_loading_screen.html",
            "name": "Drawing Saturn on the loading screen"
        },
        {
            "filename": "deep_dives/drawing_ships.html",
            "name": "Drawing ships"
        },
        {
            "filename": "deep_dives/drawing_text.html",
            "name": "Drawing text"
        },
        {
            "filename": "deep_dives/drawing_the_sun.html",
            "name": "Drawing the sun"
        },
        {
            "filename": "deep_dives/drawing_vector_graphics_using_nes_tiles.html",
            "name": "Drawing vector graphics using NES tiles"
        },
        {
            "filename": "deep_dives/the_elusive_cougar.html",
            "name": "The elusive Cougar"
        },
        {
            "filename": "deep_dives/elite-a_the_encyclopedia_galactica.html",
            "name": "The Encyclopedia Galactica"
        },
        {
            "filename": "deep_dives/extended_screen_coordinates.html",
            "name": "Extended screen coordinates"
        },
        {
            "filename": "deep_dives/extended_system_descriptions.html",
            "name": "Extended system descriptions"
        },
        {
            "filename": "deep_dives/extended_text_tokens.html",
            "name": "Extended text tokens"
        },
        {
            "filename": "deep_dives/elite-a_fixing_ship_positions.html",
            "name": "Fixing ship positions"
        },
        {
            "filename": "deep_dives/flicker-free_ship_drawing.html",
            "name": "Flicker-free ship drawing"
        },
        {
            "filename": "deep_dives/flipping_axes_between_space_views.html",
            "name": "Flipping axes between space views"
        },
        {
            "filename": "deep_dives/fonts_in_nes_elite.html",
            "name": "Fonts in NES Elite"
        },
        {
            "filename": "deep_dives/galaxy_and_system_seeds.html",
            "name": "Galaxy and system seeds"
        },
        {
            "filename": "deep_dives/generating_random_numbers.html",
            "name": "Generating random numbers"
        },
        {
            "filename": "deep_dives/generating_system_data.html",
            "name": "Generating system data"
        },
        {
            "filename": "deep_dives/generating_system_names.html",
            "name": "Generating system names"
        },
        {
            "filename": "deep_dives/elite-a_the_iff_system.html",
            "name": "The I.F.F. system"
        },
        {
            "filename": "deep_dives/image_and_data_compression.html",
            "name": "Image and data compression"
        },
        {
            "filename": "deep_dives/in_the_crosshairs.html",
            "name": "In the crosshairs"
        },
        {
            "filename": "deep_dives/the_key_logger.html",
            "name": "The key logger"
        },
        {
            "filename": "deep_dives/line-clipping.html",
            "name": "Line-clipping"
        },
        {
            "filename": "deep_dives/the_local_bubble_of_universe.html",
            "name": "The local bubble of universe"
        },
        {
            "filename": "deep_dives/elite-a_making_room_for_the_modifications.html",
            "name": "Making room for the modifications in Elite-A"
        },
        {
            "filename": "deep_dives/market_item_prices_and_availability.html",
            "name": "Market item prices and availability"
        },
        {
            "filename": "deep_dives/the_elite_memory_map.html",
            "name": "BBC Micro cassette Elite memory map"
        },
        {
            "filename": "deep_dives/the_elite_memory_map_disc.html",
            "name": "BBC Micro disc Elite memory map"
        },
        {
            "filename": "deep_dives/the_elite_memory_map_6502sp.html",
            "name": "6502 Second Processor Elite memory map"
        },
        {
            "filename": "deep_dives/the_elite_memory_map_master.html",
            "name": "BBC Master Elite memory map"
        },
        {
            "filename": "deep_dives/the_elite_memory_map_electron.html",
            "name": "Acorn Electron Elite memory map"
        },
        {
            "filename": "deep_dives/the_nes_combat_demo.html",
            "name": "The NES combat demo"
        },
        {
            "filename": "deep_dives/the_elite_memory_map_nes.html",
            "name": "NES Elite memory map"
        },
        {
            "filename": "deep_dives/multi-language_support_in_nes_elite.html",
            "name": "Multi-language support in NES Elite"
        },
        {
            "filename": "deep_dives/multiplication_and_division_using_logarithms.html",
            "name": "Multiplication and division using logarithms"
        },
        {
            "filename": "deep_dives/music_in_commodore_64_elite.html",
            "name": "Music in Commodore 64 Elite"
        },
        {
            "filename": "deep_dives/music_in_nes_elite.html",
            "name": "Music in NES Elite"
        },
        {
            "filename": "deep_dives/orientation_vectors.html",
            "name": "Orientation vectors"
        },
        {
            "filename": "deep_dives/elite-a_the_original_source_files.html",
            "name": "The original Elite-A source files"
        },
        {
            "filename": "deep_dives/pattern_and_nametable_buffers.html",
            "name": "The pattern and nametable buffers"
        },
        {
            "filename": "deep_dives/pitching_and_rolling_by_a_fixed_angle.html",
            "name": "Pitching and rolling by a fixed angle"
        },
        {
            "filename": "deep_dives/pitching_and_rolling.html",
            "name": "Pitching and rolling"
        },
        {
            "filename": "deep_dives/printing_decimal_numbers.html",
            "name": "Printing decimal numbers"
        },
        {
            "filename": "deep_dives/printing_text_tokens.html",
            "name": "Printing text tokens"
        },
        {
            "filename": "deep_dives/program_flow_of_the_main_game_loop.html",
            "name": "Program flow of the main game loop"
        },
        {
            "filename": "deep_dives/program_flow_of_the_ship-moving_routine.html",
            "name": "Program flow of the ship-moving routine"
        },
        {
            "filename": "deep_dives/program_flow_of_the_tactics_routine.html",
            "name": "Program flow of the tactics routine"
        },
        {
            "filename": "deep_dives/scheduling_tasks_with_the_main_loop_counter.html",
            "name": "Scheduling tasks with the main loop counter"
        },
        {
            "filename": "deep_dives/secrets_of_the_executive_version.html",
            "name": "Secrets of the Executive version"
        },
        {
            "filename": "deep_dives/a_sense_of_scale.html",
            "name": "A sense of scale"
        },
        {
            "filename": "deep_dives/shift-and-add_multiplication.html",
            "name": "Shift-and-add multiplication"
        },
        {
            "filename": "deep_dives/shift-and-subtract_division.html",
            "name": "Shift-and-subtract division"
        },
        {
            "filename": "deep_dives/ship_blueprints_in_the_disc_version.html",
            "name": "Ship blueprints in the BBC Micro disc version"
        },
        {
            "filename": "deep_dives/elite-a_ship_blueprints.html",
            "name": "Ship blueprints in Elite-A"
        },
        {
            "filename": "deep_dives/ship_blueprints.html",
            "name": "Ship blueprints"
        },
        {
            "filename": "deep_dives/ship_data_blocks.html",
            "name": "Ship data blocks"
        },
        {
            "filename": "deep_dives/the_sine_cosine_and_arctan_tables.html",
            "name": "The sine, cosine and arctan tables"
        },
        {
            "filename": "deep_dives/sound_effects_in_commodore_64_elite.html",
            "name": "Sound effects in Commodore 64 Elite"
        },
        {
            "filename": "deep_dives/sound_effects_in_nes_elite.html",
            "name": "Sound effects in NES Elite"
        },
        {
            "filename": "deep_dives/the_space_station_safe_zone.html",
            "name": "The space station safe zone"
        },
        {
            "filename": "deep_dives/elite-a_special_cargo_missions.html",
            "name": "Special cargo missions"
        },
        {
            "filename": "deep_dives/the_split-screen_mode.html",
            "name": "The split-screen mode in BBC Micro Elite"
        },
        {
            "filename": "deep_dives/the_split-screen_mode_commodore_64.html",
            "name": "The split-screen mode in Commodore 64 Elite"
        },
        {
            "filename": "deep_dives/the_split-screen_mode_nes.html",
            "name": "The split-screen mode in NES Elite"
        },
        {
            "filename": "deep_dives/splitting_nes_elite_across_multiple_rom_banks.html",
            "name": "Splitting NES Elite across multiple ROM banks"
        },
        {
            "filename": "deep_dives/splitting_the_main_loop_in_the_nes_version.html",
            "name": "Splitting the main loop in the NES version"
        },
        {
            "filename": "deep_dives/sprite_usage_in_commodore_64_elite.html",
            "name": "Sprite usage in Commodore 64 Elite"
        },
        {
            "filename": "deep_dives/sprite_usage_in_nes_elite.html",
            "name": "Sprite usage in NES Elite"
        },
        {
            "filename": "deep_dives/stardust_in_the_front_view.html",
            "name": "Stardust in the front view"
        },
        {
            "filename": "deep_dives/stardust_in_the_side_views.html",
            "name": "Stardust in the side views"
        },
        {
            "filename": "deep_dives/docked_and_flight_code.html",
            "name": "Swapping between the docked and flight code"
        },
        {
            "filename": "deep_dives/reading_the_commodore_64_keyboard_matrix.html",
            "name": "Reading the Commodore 64 keyboard matrix"
        },
        {
            "filename": "deep_dives/rotating_the_universe.html",
            "name": "Rotating the universe"
        },
        {
            "filename": "deep_dives/the_thargoid_plans_mission.html",
            "name": "The Thargoid Plans mission"
        },
        {
            "filename": "deep_dives/tidying_orthonormal_vectors.html",
            "name": "Tidying orthonormal vectors"
        },
        {
            "filename": "deep_dives/the_tina_hook.html",
            "name": "The TINA hook"
        },
        {
            "filename": "deep_dives/the_trumbles_mission.html",
            "name": "The Trumbles mission"
        },
        {
            "filename": "deep_dives/elite-a_tube_communication.html",
            "name": "Tube communication in Elite-A"
        },
        {
            "filename": "deep_dives/twisting_the_system_seeds.html",
            "name": "Twisting the system seeds"
        },
        {
            "filename": "deep_dives/understanding_the_nes_for_elite.html",
            "name": "Understanding the NES for Elite"
        },
        {
            "filename": "deep_dives/views_and_view_types_in_nes_elite.html",
            "name": "Views and view types in NES Elite"
        }
    ]

# Config for statistics
macro_instruction_count = {
    "FNE": 4,
    "DRAW_BYTE": 7,
    "MVE": 10,
    "DKS4": 10
}
macro_data_count = {
    "CHAR": 1,
    "CONT": 1,
    "RTOK": 1,
    "ECHR": 1,
    "EJMP": 1,
    "ETOK": 1,
    "TWOK": 2,
    "ETWO": 2,
    "ITEM": 4,
    "EDGE": 4,
    "VERTEX": 6,
    "FACE": 6
}

# Config for comparison tool
sites_to_compare = [
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/cassette/1-source-files/main-sources/",
        "source_files": ["elite-loader.asm", "elite-source.asm", "elite-bcfs.asm"],
        "do_not_expand_all_includes": ["elite-header.h.asm"],
        "dest_folder": content_folder + "cassette/",
        "this_version": [
            "CASSETTE"
        ],
        "version_key": "CASSETTE"
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/disc/1-source-files/main-sources/",
        "source_files": ["elite-text-tokens.asm", "elite-missile.asm", "elite-loader1.asm", "elite-loader2.asm", "elite-loader3.asm", "elite-source-flight.asm", "elite-ships-a.asm", "elite-ships-b.asm", "elite-ships-c.asm", "elite-ships-d.asm", "elite-ships-e.asm", "elite-ships-f.asm", "elite-ships-g.asm", "elite-ships-h.asm", "elite-ships-i.asm", "elite-ships-j.asm", "elite-ships-k.asm", "elite-ships-l.asm", "elite-ships-m.asm", "elite-ships-n.asm", "elite-ships-o.asm", "elite-ships-p.asm"],
        "do_not_expand_all_includes": ["elite-header.h.asm"],
        "dest_folder": content_folder + "disc/",
        "this_version": [
            "DISC_VERSION",
            "DISC_FLIGHT"
        ],
        "version_key": "DISC_FLIGHT"
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/disc/1-source-files/main-sources/",
        "source_files": ["elite-source-docked.asm"],
        "do_not_expand_all_includes": ["elite-header.h.asm"],
        "dest_folder": content_folder + "disc/",
        "this_version": [
            "DISC_VERSION",
            "DISC_DOCKED"
        ],
        "version_key": "DISC_DOCKED"
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/6502sp/1-source-files/main-sources/",
        "source_files": ["elite-loader1.asm", "elite-loader2.asm", "elite-source.asm", "elite-bcfs.asm", "elite-z.asm", "elite-checksum.asm"],
        "do_not_expand_all_includes": ["elite-header.h.asm"],
        "dest_folder": content_folder + "6502sp/",
        "this_version": [
            "6502SP"
        ],
        "version_key": "6502SP"
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/master/1-source-files/main-sources/",
        "source_files": ["elite-loader.asm", "elite-source.asm", "elite-data.asm"],
        "do_not_expand_all_includes": ["elite-header.h.asm"],
        "dest_folder": content_folder + "master/",
        "this_version": [
            "MASTER"
        ],
        "version_key": "MASTER"
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/electron/1-source-files/main-sources/",
        "source_files": ["elite-loader.asm", "elite-source.asm", "elite-bcfs.asm"],
        "do_not_expand_all_includes": ["elite-header.h.asm"],
        "dest_folder": content_folder + "electron/",
        "this_version": [
            "ELECTRON"
        ],
        "version_key": "ELECTRON"
    }
]

# Exclude catlod.asm as it is purely commented-out code
omit_includes_from_compare = [
    "6502sp/main/subroutine/catlod.asm",
    "elite-build-options.asm"
]

# Routines from other sources
exported_routines = {
    "nes": {
        "UpdateView": "Bank 0",
        "DrawScreenInNMI": "Bank 0",
        "MVS5": "Bank 0",
        "PlayDemo": "Bank 0",
        "SetupAfterLoad": "Bank 0",
        "PrintCtrlCode": "Bank 0",
        "ZINF": "Bank 0",
        "MAS4": "Bank 0",
        "CheckForPause": "Bank 0",
        "ShowStartScreen": "Bank 0",
        "DEATH2": "Bank 0",
        "StartGame": "Bank 0",
        "ChangeToView": "Bank 0",
        "TITLE": "Bank 0",
        "PAS1": "Bank 0",
        "TT66": "Bank 0",
        "E%": "Bank 1",
        "KWL%": "Bank 1",
        "KWH%": "Bank 1",
        "SHIP_MISSILE": "Bank 1",
        "SHIP_CORIOLIS": "Bank 1",
        "SHIP_ESCAPE_POD": "Bank 1",
        "SHIP_PLATE": "Bank 1",
        "SHIP_CANISTER": "Bank 1",
        "SHIP_BOULDER": "Bank 1",
        "SHIP_ASTEROID": "Bank 1",
        "SHIP_SPLINTER": "Bank 1",
        "SHIP_SHUTTLE": "Bank 1",
        "SHIP_TRANSPORTER": "Bank 1",
        "SHIP_COBRA_MK_3": "Bank 1",
        "SHIP_PYTHON": "Bank 1",
        "SHIP_BOA": "Bank 1",
        "SHIP_ANACONDA": "Bank 1",
        "SHIP_ROCK_HERMIT": "Bank 1",
        "SHIP_VIPER": "Bank 1",
        "SHIP_SIDEWINDER": "Bank 1",
        "SHIP_MAMBA": "Bank 1",
        "SHIP_KRAIT": "Bank 1",
        "SHIP_ADDER": "Bank 1",
        "SHIP_GECKO": "Bank 1",
        "SHIP_COBRA_MK_1": "Bank 1",
        "SHIP_WORM": "Bank 1",
        "SHIP_COBRA_MK_3_P": "Bank 1",
        "SHIP_ASP_MK_2": "Bank 1",
        "SHIP_PYTHON_P": "Bank 1",
        "SHIP_FER_DE_LANCE": "Bank 1",
        "SHIP_MORAY": "Bank 1",
        "SHIP_THARGOID": "Bank 1",
        "SHIP_THARGON": "Bank 1",
        "SHIP_CONSTRICTOR": "Bank 1",
        "SHIP_COUGAR": "Bank 1",
        "SHIP_DODO": "Bank 1",
        "LL9": "Bank 1",
        "CLIP": "Bank 1",
        "CIRCLE2": "Bank 1",
        "SUN": "Bank 1",
        "STARS": "Bank 1",
        "HALL": "Bank 1",
        "TIDY": "Bank 1",
        "SCAN": "Bank 1",
        "HideFromScanner": "Bank 1",
        "TKN1": "Bank 2",
        "TKN1_DE": "Bank 2",
        "TKN1_FR": "Bank 2",
        "QQ18": "Bank 2",
        "QQ18_DE": "Bank 2",
        "QQ18_FR": "Bank 2",
        "DETOK": "Bank 2",
        "DTS": "Bank 2",
        "PDESC": "Bank 2",
        "TT27": "Bank 2",
        "ex": "Bank 2",
        "DASC": "Bank 2",
        "CHPR": "Bank 2",
        "iconBarImage0": "Bank 3",
        "iconBarImage1": "Bank 3",
        "iconBarImage2": "Bank 3",
        "iconBarImage3": "Bank 3",
        "iconBarImage4": "Bank 3",
        "DrawDashNames": "Bank 3",
        "ResetScanner": "Bank 3",
        "SendViewToPPU": "Bank 3",
        "SendBitplaneToPPU": "Bank 3",
        "SetupViewInNMI": "Bank 3",
        "ResetScreen": "Bank 3",
        "ShowIconBar": "Bank 3",
        "UpdateIconBar": "Bank 3",
        "SetupIconBar": "Bank 3",
        "SetLinePatterns": "Bank 3",
        "LoadNormalFont": "Bank 3",
        "LoadHighFont": "Bank 3",
        "DrawSystemImage": "Bank 3",
        "DrawImageFrame": "Bank 3",
        "DrawSmallBox": "Bank 3",
        "DrawBackground": "Bank 3",
        "ClearScreen": "Bank 3",
        "FadeToBlack": "Bank 3",
        "FadeToColour": "Bank 3",
        "SetViewAttrs": "Bank 3",
        "SIGHT": "Bank 3",
        "cobraNames": "Bank 4",
        "GetHeadshotType": "Bank 4",
        "GetHeadshot": "Bank 4",
        "GetCmdrImage": "Bank 4",
        "DrawBigLogo": "Bank 4",
        "DrawImageNames": "Bank 4",
        "DrawSmallLogo": "Bank 4",
        "GetSystemImage": "Bank 5",
        "GetSystemBack": "Bank 5",
        "SetDemoAutoPlay": "Bank 5",
        "StopSoundsS": "Bank 6",
        "ChooseMusic": "Bank 6",
        "MakeSounds": "Bank 6",
        "StartEffect": "Bank 6",
        "DrawCmdrImage": "Bank 6",
        "DrawSpriteImage": "Bank 6",
        "PauseGame": "Bank 6",
        "DIALS": "Bank 6",
        "DrawEquipment": "Bank 6",
        "ShowScrollText": "Bank 6",
        "SVE": "Bank 6",
        "CheckSaveSlots": "Bank 6",
        "ResetCommander": "Bank 6",
        "JAMESON": "Bank 6",
        "DrawLightning": "Bank 6",
        "LL164": "Bank 6",
        "DrawLaunchBox": "Bank 6",
        "InputName": "Bank 6",
        "ChangeCmdrName": "Bank 6",
        "SetKeyLogger": "Bank 6",
        "ChooseLanguage": "Bank 6",
        "TT24": "Bank 6",
        "ClearDashEdge": "Bank 6",
        "ChangeCmdrName_b6": "Bank 7"
    }
}

# Global variables
i = 0
in_macro = False
in_loop = False
loop_count_stack = [1]
in_list = False
in_pre = False
in_workspace = False
in_if_to_remove = False
in_else_to_remove = False
current_list_indent = 0
last_tag = ""
variables = {}
subroutines = {}
entry_points = {}
workspaces = {}
macros = {}
categories = {}
workspace_variables = []
configuration_variables = {}
all_headers = []
macro_names = []
references = set()
instruction_count = 0
data_byte_count = 0
source_code_stats = {"all": {}, "categories": {}}
references_library = {}
mentions = {}
analysing_arguments = False
analysing_summary = False
analysing_deep_dive_header = False
add_popup_links_to_code = True
compare_buffer = ""
most_recent_compare_line = ""
multi_versions_buffer_is_header = False
close_deep_dive_link = ""
includes_in_versions = {}
all_includes = {}
compare_source_folder = ""
compare_do_not_expand_all_includes = []
compare_this_version = ""
compare_version_key = ""
tag_categories = set()
current_if_block_anchor = 0
workspace_variable_extra_data_html = ""


def create_folder(name):
    if not os.path.isdir(dest_folder + name):
        os.mkdir(dest_folder + name.replace("ü", "u"))


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def make_url_name(name):
    return "{}".format(
        name.replace("/", "_")
            .replace(" ", "_")
            .replace("(", "")
            .replace(")", "")
            .replace('"', "")
            .replace("'", "")
            .replace(",", "")
            .replace("%", "_per_cent")
            .replace("ü", "u")
            .replace("!", "")
            .lower()
    )


def make_id(name):
    return "{}".format(
        name.replace("/", "-")
            .replace(" ", "-")
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


def make_id_for_entry_point(name):
    return make_id(re.sub(r"[+-]\d+$", "", name))


def add_full_stop(line):
    if line[-1] in "?.!":
        full_stop = ""
    else:
        full_stop = "."
    return line + full_stop


def add_deep_dive_link_with_quotes(line):
    for deep_dive in deep_dive_headers:
        if '"' + deep_dive["name"] + '"' in line:
            line = line.replace('"' + deep_dive["name"] + '"', '<a href="/{}">{}</a>'.format(deep_dive["filename"], deep_dive["name"]))
            break
    return line


def add_deep_dive_link(line):
    found = False
    for deep_dive in deep_dive_headers:
        if deep_dive["name"] in line:
            line = line.replace(deep_dive["name"], '<a href="/{}">{}</a>'.format(deep_dive["filename"], deep_dive["name"]))
            found = True
            break
    if not found:
        print("\nERROR! Deep dive name not found in header: " + line)
    return line


def routine_extra_data(name, type, mentions, compare_url, context_text, context_url):
    full_name = name
    name = re.sub(r" \(Part \d+ of \d+\)", "", name)

    if type == "Variable" or type == "Workspace" or type == "Macro":
        verb = "used"
    else:
        verb = "called"

    mention_list = ""
    fetch_references = False

    # This is not a (Part n of m) routine, so include references if there are any
    if name == full_name and name in mentions:
        fetch_references = True

    # This is a (Part n of m) routine, so only include entry points that appear within this part
    if name != full_name and name in references_library and "parent_name" in references_library[name] and references_library[name]["parent_name"] == full_name:
        fetch_references = True

    if fetch_references and name in mentions:
        name_no_stage = remove_stage(name)
        if type == "Subroutine":
            suffix = ' calls '
        else:
            suffix = ' uses '
        suffix += '<a href="#{}">{}</a></span>\n'.format(make_id(name_no_stage), name_no_stage)
        mention_list += fetch_cross_references(name, '             <span class="headerEntry">* <a href="/{}">{}</a>' + suffix, include_stage=False)[0]

    # Entry points
    for key in references_library:
        if "entry_point" in references_library[key] and "parent_name" in references_library[key] and references_library[key]["parent_name"] == full_name:
            name_no_stage = remove_stage(key)
            entry_point_anchor = make_id_for_entry_point(name_no_stage)
            suffix = ' calls via <a href="#{}">{}</a></span></span>\n'.format(entry_point_anchor, name_no_stage)
            entry_refs = fetch_cross_references(key, '             <span class="headerEntry">* <a href="/{}">{}</a>' + suffix, include_stage=False)[0]
            if entry_refs:
                mention_list += entry_refs

    routine_extra_data_html = '<span class="headerLabel">    Context:</span> <span class="headerEntry">See this {} <a href="/{}">{}</a></span>\n'.format(type.lower(), context_url, context_text)

    if compare_url:
        routine_extra_data_html += '<span class="headerLabel"> Variations:</span> <span class="headerEntry">See <a href="/{}">code variations</a> for this {} in the different versions</span>\n'.format(compare_url, type.lower())

    if mention_list:
        routine_extra_data_html += '<span class="headerLabel"> References:</span> <span class="headerEntry">This {} is {} as follows:</span>\n'.format(type.lower(), verb) + mention_list
    else:
        routine_extra_data_html += '<span class="headerLabel"> References:</span> <span class="headerEntry">No direct references to this {} in this source file</span>\n'.format(type.lower())

    routine_extra_data_html = '<div class="extraData">' + routine_extra_data_html + '</div>'

    return routine_extra_data_html


def tidy_source_header_line(line, context_link, context_link_length):
    global analysing_arguments, analysing_summary, analysing_deep_dive_header
    line = line.replace("<", "&lt;")
    line = line.replace(">", "&gt;")
    cr = ""
    if "\n" in line:
        cr = "\n"
        line = line.rstrip()
    if analysing_summary and re_summary2.match(line):
        m = re_summary2.match(line)
        if analysing_arguments:
            line = '             <span class="argumentEntry">' + m.group(1) + '</span>' + cr
        else:
            line = '             <span class="headerEntry">' + m.group(1) + '</span>' + cr
        return line
    elif analysing_deep_dive_header and re_deep_dive_in_header2.match(line):
        m = re_deep_dive_in_header2.match(line)
        line = '             <span class="headerEntry">' + m.group(1) + '</span>' + cr
        return add_deep_dive_link(line)
    else:
        analysing_summary = False
        analysing_deep_dive_header = False
    if re_entry_points.match(line) or re_arguments.match(line) or re_returns.match(line):
        analysing_arguments = True
        line = re.sub(r"^" + re_comment_delimiter, "", line)
        line = '<span class="subheader">' + line + '</span>' + cr
    elif re_name.match(line):
        m = re_name.match(line)
        if context_link:
            padding_size = 80 - 13 - len(m.group(2)) - context_link_length
            context_link_padding = " " * padding_size
        else:
            context_link_padding = ""
        line = '<span class="headerLabel">' + m.group(1) + ':</span> <span class="headerEntry">' + m.group(2) + '</span>' + context_link_padding + context_link + cr
    elif re_type.match(line):
        m = re_type.match(line)
        line = '<span class="headerLabel">' + m.group(1) + ':</span> <span class="headerEntry">' + m.group(2) + '</span>' + cr
    elif re_category.match(line):
        m = re_category.match(line)
        line = '<span class="headerLabel">' + m.group(1) + ':</span> <span class="headerEntry">' + m.group(2) + '</span>' + cr
    elif re_summary.match(line):
        analysing_summary = True
        m = re_summary.match(line)
        line = '<span class="headerLabel">' + m.group(1) + ':</span> <span class="headerEntry">' + m.group(2) + '</span>' + cr
    elif re_address.match(line):
        m = re_address.match(line)
        line = '<span class="headerLabel">' + m.group(1) + ':</span> <span class="headerEntry">' + m.group(2) + '</span>' + cr
    elif re_deep_dive_in_header.match(line):
        analysing_deep_dive_header = True
        m = re_deep_dive_in_header.match(line)
        line = '<span class="headerLabel">' + m.group(1) + ':</span> <span class="headerEntry">' + m.group(2) + '</span>' + cr
        line = add_deep_dive_link(line)
    elif analysing_arguments and re_argument_entry1.match(line):
        m = re_argument_entry1.match(line)
        line = '   <span class="argumentLabel">' + m.group(1) + '</span> ' + m.group(3) + '<span class="argumentEntry">' + m.group(4) + '</span>' + cr
    elif analysing_arguments and re_argument_entry2.match(line):
        m = re_argument_entry2.match(line)
        if analysing_arguments:
            line = '                        <span class="argumentEntry">' + m.group(1) + '</span>' + cr
        else:
            line = '                        <span class="headerEntry">' + m.group(1) + '</span>' + cr
    else:
        line = re.sub(r"^" + re_comment_delimiter, "", line) + cr
    if re_url.search(line):
        line = re_url.sub(r'<a href="\1">\1</a>', line)
    if args.platform != "compare":
        for file_url in elite_source_urls:
            if file_url in line:
                line = line.replace(file_url, '<a href="{}">{}</a>'.format(elite_source_urls[file_url], file_url))
    return line


def tidy_code(line, stage, name, refs_only, statistics):
    global references, in_macro, in_loop, loop_count_stack, instruction_count, data_byte_count, add_popup_links_to_code, workspace_variable_extra_data_html

    comment = ""
    indent = ""
    instruction = ""
    operand = ""
    spaces1 = ""
    spaces2 = ""

    # Remove one-space indent from lines in removed IF blocks, moving comment to the right
    # if in_else_to_remove:
    #     line = line[1:].replace(" " + re_comment_delimiter, "  " + re_comment_delimiter)

    # Remove the carriage return from the end of the line
    code = re.sub(r"\n", "", line)

    if re_configuration_variable.match(code):
        # Separate trailing comment
        c = re_configuration_variable.match(code)
        anchor = html_anchor.format(make_id(c.group(2)))
        output = c.group(1) + '<span class="config">' + c.group(2) + '</span>' + anchor + c.group(3) + '<span class="operator">=</span> <span class="configValue">' + c.group(4) + '</span>'
        if c.group(6):
            output += c.group(5) + '<span class="comment">' + escape_comment(c.group(6)) + '</span>'
        return output + '\n'

    # Process commented instruction
    if re.match(r"^" + re_comment_delimiter, code):
        code = re.sub(r"^(" + re_comment_delimiter + r".*)$", r'<span class="comment">\1</span>', code)
        return code + "\n"

    # Separate trailing comment
    m = re.match(r"^([^" + re_comment_delimiter + r"]*)( *)(" + re_comment_delimiter + r".*)$", code)
    if m:
        n = re.match(r'^([^\'"' + re_comment_delimiter + r']+"[^"]*)' + re_comment_delimiter + r'([^"]*".*)$', code)
        if n:
            # Comment delimiter is inside a string
            code = n.group(1) + "!DELIMITER!" + n.group(2)
            m = re.match(r"^([^" + re_comment_delimiter + r"]*)( *)(" + re_comment_delimiter + r".*)$", code)
            if m:
                code = m.group(1).replace("!DELIMITER!", re_comment_delimiter)
        else:
            code = m.group(1)
        if m:
            if "-->" in m.group(3):
                comment = m.group(2) + '<span class="comment diff">' + m.group(3) + '</span>'
            else:
                comment = m.group(2) + '<span class="comment">' + escape_comment(m.group(3)) + '</span>'

    # Process macro definitions
    if in_macro or re.match(r"^ *(MACRO|ENDMACRO)", code):
        if re.match(r"^ *MACRO", code):
            in_macro = True
            code = re.sub(r"^(.*)$", r'<span class="macro">\1</span>', code)
            return code + comment + "\n"
        if re.match(r"^ENDMACRO", code):
            in_macro = False
            code = re.sub(r"^(.*)$", r'<span class="macro">\1</span>', code)
            return code + comment + "\n"

    # Process loops
    if in_loop or (re.match(r"^ *(FOR|NEXT)", code) and not re.search(r"pass%", code)):
        if re.match(r"^ *FOR", code):
            in_loop = True
            f = re_for_loop.match(code)
            if f and f.group(2) not in no_popups and f.group(3) not in no_popups:
                loop_start = eval(f.group(2), {}, configuration_variables)
                loop_end = eval(f.group(3), {}, configuration_variables)
                loop_size = abs(loop_end - loop_start) + 1
                loop_count_stack.append(loop_size)
            else:
                loop_count_stack.append(1)
        if re.match(r"^ *NEXT", code):
            loop_count_stack.pop()
            if len(loop_count_stack) == 1:
                in_loop = False
    #     code = re.sub(r"^(.*)$", r'<span class="loop">\1</span>', code)
    #     return code + comment + "\n"

    # Process commented-out directive
    if re.match(r"^ *" + re_comment_delimiter + r" *(ALIGN|CPU|IF|ELIF|ELSE|ENDIF|PRINT|SAVE|INCLUDE|INCBIN|GUARD|ORG|COPYBLOCK|FOR|NEXT|CLEAR|DIM|OPT|OSCLI)", code):
        code = re.sub(r"^(.*)$", r'<span class="comment">\1</span>', code)
        return code + comment + "\n"

    # Process directive
    if re.match(r"^ *(ALIGN|CPU|IF|ELIF|ELSE|ENDIF|PRINT|SAVE|INCLUDE|INCBIN|GUARD|ORG|COPYBLOCK|FOR|NEXT|CLEAR|DIM|OPT|OSCLI)", code):
        code = re.sub(r"^(.*)$", r'<span class="directive">\1</span>', code)
        return code + comment + "\n"

    # Label
    if re.match(re_label, code):
        m = re.match(re_label, code)
        if m:
            anchor = html_anchor.format(make_id(m.group(2)))
            if in_workspace:
                mention_list = fetch_cross_references(add_stage(m.group(2), stage), html_workspace_reference_link, include_stage=False)[0]
                if mention_list:
                    workspace_variable_extra_data_html = mention_list
            code = re.sub(re_label, r'<span class="label">\1\2</span>' + anchor, code)
        return code + comment + "\n"

    # Delimiter races
    if re.match(r"^({|})", code):
        code = re.sub(r"^({|})", r'<span class="brace">\1</span>', code)
        return code + comment + "\n"

    # No code
    m = re_empty_line.match(code)
    if m:
        return code + comment + "\n"

    # Separate instructions from operands
    m = re.match(r"^( *)([^ ]+)( *)(.*?)( *)$", code)
    if m:
        indent = m.group(1)
        instruction = m.group(2)
        spaces1 = m.group(3)
        operand = m.group(4)
        spaces2 = m.group(5)
    else:
        instruction = code

    if statistics:
        instructions_to_add = 0
        data_bytes_to_add = 0
        if instruction == "SKIP":
            if not re_unused.search(line):
                if operand.isnumeric():
                    data_bytes_to_add = int(operand)
                else:
                    var_value = operand.replace("%", "_per_cent")
                    data_bytes_to_add = eval(var_value, {}, configuration_variables)
        elif instruction == "EQUS":
            data_bytes_to_add = len(operand) - 2
        elif instruction == "EQUB":
            data_bytes_to_add = len(operand.split(","))
        elif instruction == "EQUW":
            data_bytes_to_add = len(operand.split(",")) * 2
        elif instruction == "EQUD":
            data_bytes_to_add = len(operand.split(",")) * 4
        else:
            is_macro = False
            for macro in macro_instruction_count:
                if instruction == macro:
                    instructions_to_add = macro_instruction_count[macro] - 1
                    is_macro = True
                    break
            for macro in macro_data_count:
                if instruction == macro:
                    data_bytes_to_add = macro_data_count[macro]
                    is_macro = True
                    break
            if not is_macro:
                instructions_to_add = 1
        instruction_count += instructions_to_add * loop_count_stack[-1]
        data_byte_count += data_bytes_to_add * loop_count_stack[-1]

    if operand:
        operand = markup_operand(operand, instruction, constant=False, refs_only=refs_only, name=name, indirect=False)

    # Process macro calls
    if instruction in macro_names:
        references.add(instruction)
        if add_popup_links_to_code:
            return indent + '<a class="popup destination">' + instruction + '</a>' + spaces1 + operand + spaces2 + comment + "\n"
        else:
            return indent + '<span class="destination">' + instruction + '</span>' + spaces1 + operand + spaces2 + comment + "\n"

    return indent + '<span class="mne">' + instruction + '</span>' + spaces1 + operand + spaces2 + comment + "\n"


def markup_operand(operand, instruction, constant, refs_only, name, indirect):
    global add_popup_links_to_code, in_macro, in_loop

    # Spaces at start
    if operand.startswith(" "):
        return ' ' + markup_operand(operand[1:], instruction, constant, refs_only, name, indirect)

    # Spaces at end
    if operand.endswith(" "):
        return markup_operand(operand[:-1], instruction, constant, refs_only, name, indirect) + ' '

    # Constant
    if operand.startswith("#"):
        return '<span class="hash">#</span>' + markup_operand(operand[1:], instruction, True, refs_only, name, indirect)

    # LO(...)
    if operand.startswith("LO("):
        m = re.match(r"^LO\((.+)\)(.*)$", operand)
        if m:
            return '<span class="operator">LO</span><span class="bracket">(</span>' + markup_operand(m.group(1), instruction, constant, refs_only, name, indirect) + '<span class="bracket">)</span>' + markup_operand(m.group(2), instruction, constant, refs_only, name, indirect)

    # HI(...)
    if operand.startswith("HI("):
        m = re.match(r"^HI\((.+)\)(.*)$", operand)
        if m:
            return '<span class="operator">HI</span><span class="bracket">(</span>' + markup_operand(m.group(1), instruction, constant, refs_only, name, indirect) + '<span class="bracket">)</span>' + markup_operand(m.group(2), instruction, constant, refs_only, name, indirect)

    # ...,X or ...,Y
    m = re.match(r"^(.+),([X|Y])$", operand)
    if m:
        return markup_operand(m.group(1), instruction, constant, refs_only, name, indirect) + "," + markup_operand(m.group(2), instruction, constant, refs_only, name, indirect)

    # (...),X or (...),Y
    m = re.match(r"^\((.+)\),([X|Y])$", operand)
    if m:
        return '<span class="bracket">(</span>' + markup_operand(m.group(1), instruction, constant, refs_only, name, indirect=True) + '<span class="bracket">)</span><span class="comma">,</span>' + markup_operand(m.group(2), instruction, constant, refs_only, name, indirect=True)

    # (...,X) or (...,Y)
    m = re.match(r"^\((.+),([X|Y])\)$", operand)
    if m:
        return '<span class="bracket">(</span>' + markup_operand(m.group(1), instruction, constant, refs_only, name, indirect=True) + '<span class="comma">,</span>' + markup_operand(m.group(2), instruction, constant, refs_only, name, indirect=True) + '<span class="bracket">)</span>'

    # (...)
    m = re.match(r"^\((.+)\)$", operand)
    if m:
        if re.match(r"(BC.|BEQ|BMI|BNE|BPL|BV.|JMP|JSR|B(EQ|NE|VS|VC|MI|PL|AL|NV|LO|CC|LS|HI|HS|CS|GE|LT|GT|LE)|BL(EQ|NE|VS|VC|MI|PL|AL|NV|LO|CC|LS|HI|HS|CS|GE|LT|GT|LE))", instruction):
            indirect = True
        return '<span class="bracket">(</span>' + markup_operand(m.group(1), instruction, constant, refs_only, name, indirect) + '<span class="bracket">)</span>'

    # [...]
    m = re.match(r"^\[(.+)\]$", operand)
    if m:
        if re.match(r"(LDR|STR)", instruction):
            indirect = True
        return '<span class="bracket">[</span>' + markup_operand(m.group(1), instruction, constant, refs_only, name, indirect) + '<span class="bracket">]</span>'

    # {...}
    m = re.match(r"^\{(.+)\}$", operand)
    if m:
        if re.match(r"(LDR|STR)", instruction):
            indirect = True
        return '<span class="bracket">{</span>' + markup_operand(m.group(1), instruction, constant, refs_only, name, indirect) + '<span class="bracket">}</span>'

    # (...
    m = re.match(r"^\((.+)$", operand)
    if m:
        return '<span class="bracket">(</span>' + markup_operand(m.group(1), instruction, constant, refs_only, name, indirect)

    # [...
    m = re.match(r"^\[(.+)$", operand)
    if m:
        return '<span class="bracket">[</span>' + markup_operand(m.group(1), instruction, constant, refs_only, name, indirect)

    # {...
    m = re.match(r"^\{(.+)$", operand)
    if m:
        return '<span class="bracket">{</span>' + markup_operand(m.group(1), instruction, constant, refs_only, name, indirect)

    # ...)
    m = re.match(r"^(.+)\)$", operand)
    if m:
        return markup_operand(m.group(1), instruction, constant, refs_only, name, indirect) + '<span class="bracket">)</span>'

    # ...]
    m = re.match(r"^(.+)\]$", operand)
    if m:
        return markup_operand(m.group(1), instruction, constant, refs_only, name, indirect) + '<span class="bracket">]</span>'

    # ...}
    m = re.match(r"^(.+)\}$", operand)
    if m:
        return markup_operand(m.group(1), instruction, constant, refs_only, name, indirect) + '<span class="bracket">}</span>'

    # '...'
    m = re.match(r"^'(.+)'$", operand)
    if m:
        return '<span class="character">\'' + m.group(1) + '\'</span>'

    # "..."
    m = re.match(r'^"(.+)"$', operand)
    if m:
        return '<span class="string">"' + m.group(1) + '"</span>'

    # A X Y registers
    m = re.match(r'^(A|X|Y)$', operand)
    if m and not constant:
        return '<span class="register">' + m.group(1) + '</span>'

    # Rn registers (ARM only)
    if args.platform == "lander":
        m = re.match(r'^((R\d+!?)|PC)$', operand)
        if m and not constant:
            return '<span class="arm_register">' + m.group(1) + '</span>'

    # Shifts (ARM only)
    if args.platform == "lander":
        m = re.match(r'^(ASL|LSL|LSR|ASR|ROR|RRX)$', operand)
        if m and not constant:
            return '<span class="mne">' + m.group(1) + '</span>'

    # Binary numbers
    m = re.match(r'^(%[0-1]+)$', operand)
    if m:
        return '<span class="binary">' + m.group(1) + '</span>'

    # Hexadecimal numbers
    m = re.match(r'^(' + re_hex_prefix + r'[0-9A-F]+)$', operand)
    if m:
        return '<span class="hex">' + m.group(1) + '</span>'

    # Decimal numbers
    m = re.match(r'^(\-?[0-9]+)$', operand)
    if m:
        return '<span class="decimal">' + m.group(1) + '</span>'

    # Comma-separated values
    m = re.match(r'^(.+),( ?)(.+)$', operand)
    if m:
        return markup_operand(m.group(1), instruction, constant, refs_only, name, indirect) + '<span class="comma">,</span>' + m.group(2) + markup_operand(m.group(3), instruction, constant, refs_only, name, indirect)

    # Labels containing + or -
    m = re.match(r'^([A-Za-z]+[A-Za-z0-9]*)([\+\-])([0-9]+)$', operand)
    if m:
        if re.match(r"(BC.|BEQ|BMI|BNE|BPL|BV.|JMP|JSR|B(EQ|NE|VS|VC|MI|PL|AL|NV|LO|CC|LS|HI|HS|CS|GE|LT|GT|LE)|BL(EQ|NE|VS|VC|MI|PL|AL|NV|LO|CC|LS|HI|HS|CS|GE|LT|GT|LE))", instruction):
            destination_name = m.group(1) + m.group(2) + m.group(3)
            references.add(destination_name)
            if refs_only or destination_name in references_library or find_reference_with_stage(destination_name):
                if add_popup_links_to_code:
                    if indirect:
                        return '<a class="popup variable">' + destination_name + '</a>'
                    else:
                        return '<a class="popup destination">' + destination_name + '</a>'
                else:
                    if indirect:
                        return '<span class="variable">' + destination_name + '</span>'
                    else:
                        return '<span class="destination">' + destination_name + '</span>'
            else:
                if (not refs_only) and name and (not indirect):
                    matched_entry_point = False
                    for ref in references_library:
                        if "parent_name" in references_library[ref] and references_library[ref]["parent_name"] == name and "name_no_stage" in references_library[ref] and references_library[ref]["name_no_stage"] == m.group(1):
                            matched_entry_point = True
                            break
                    if not matched_entry_point:
                        print("\nERROR! {} used in {} in {} but is not an entry point".format(destination_name, instruction, name))
                return markup_operand(m.group(1), instruction, constant, refs_only, name, indirect) + '<span class="operator">' + m.group(2) + '</span>' + markup_operand(m.group(3), instruction, constant, refs_only, name, indirect)
        else:
            return markup_operand(m.group(1), instruction, constant, refs_only, name, indirect) + '<span class="operator">' + m.group(2) + '</span>' + markup_operand(m.group(3), instruction, constant, refs_only, name, indirect)

    # P%
    m = re.match(r'^P%([\+\-])([0-9]+)$', operand)
    if m:
        if re.match(r"(BC.|BEQ|BMI|BNE|BPL|BV.|JMP|JSR|B(EQ|NE|VS|VC|MI|PL|AL|NV|LO|CC|LS|HI|HS|CS|GE|LT|GT|LE)|BL(EQ|NE|VS|VC|MI|PL|AL|NV|LO|CC|LS|HI|HS|CS|GE|LT|GT|LE))", instruction):
            return '<span class="skip">P%' + m.group(1) + m.group(2) + '</span>'
        else:
            return markup_operand('P%', instruction, constant, refs_only, name, indirect) + m.group(1) + markup_operand(m.group(2), instruction, constant, refs_only, name, indirect)

    # + - * . operators
    m = re.match(r'^(.+)([\+\-\*\/])(.+)$', operand)
    if m:
        return markup_operand(m.group(1), instruction, constant, refs_only, name, indirect) + '<span class="operator">' + m.group(2) + '</span>' + markup_operand(m.group(3), instruction, constant, refs_only, name, indirect)

    # - operator as negation operator
    m = re.match(r'^(\-)(.+)$', operand)
    if m:
        return '<span class="operator">' + m.group(1) + '</span>' + markup_operand(m.group(2), instruction, constant, refs_only, name, indirect)

    # LOGIC and modulus operators
    m = re.match(r'^(.+)\b(AND|EOR|OR|MOD|DIV)\b(.+)$', operand)
    if m:
        return markup_operand(m.group(1), instruction, constant, refs_only, name, indirect) + '<span class="operator">' + m.group(2) + '</span>' + markup_operand(m.group(3), instruction, constant, refs_only, name, indirect)

    # LOGIC constants
    m = re.match(r'^(TRUE|FALSE)$', operand)
    if m:
        return '<span class="logical">' + m.group(1) + '</span>'

    # Integer variables
    m = re.match(r'^([A-Za-z]+[A-Za-z0-9]*%)$', operand)
    if m:
        variable_name = m.group(1)
        if (variable_name in no_popups) or (in_loop and (variable_name in no_popups_in_loop)):
            return '<span class="variableInteger">' + variable_name + '</span>'
        else:
            references.add(variable_name)
            if add_popup_links_to_code:
                return '<a class="popup variableInteger">' + variable_name + '</a>'
        return '<span class="variableInteger">' + variable_name + '</span>'

    # Variables
    m = re.match(r'^([A-Za-z]+[A-Za-z0-9_]*)$', operand)
    if m:
        variable_name = m.group(1)
        if (variable_name in no_popups) or (in_loop and (variable_name in no_popups_in_loop)):
            return '<span class="variable">' + variable_name + '</span>'
        else:
            references.add(variable_name)
            if re.match(r"(BC.|BEQ|BMI|BNE|BPL|BV.|JMP|JSR|B(EQ|NE|VS|VC|MI|PL|AL|NV|LO|CC|LS|HI|HS|CS|GE|LT|GT|LE)|BL(EQ|NE|VS|VC|MI|PL|AL|NV|LO|CC|LS|HI|HS|CS|GE|LT|GT|LE))", instruction):
                if (not refs_only) and name and (not indirect):
                    matched_entry_point = False
                    for ref in references_library:
                        if "type" in references_library[ref] and (references_library[ref]["type"] == "Subroutine" or references_library[ref]["type"] == "Entry point") and "name_no_stage" in references_library[ref] and references_library[ref]["name_no_stage"] == variable_name:
                            matched_entry_point = True
                            break
                        if "type" in references_library[ref] and references_library[ref]["type"] == "Label" and "name_no_stage" in references_library[ref] and references_library[ref]["name_no_stage"] == variable_name and "parent_name" in references_library[ref]:
                            parent_ref = references_library[ref]["parent_name"]
                            if parent_ref in references_library and remove_part_and_stage(references_library[parent_ref]["name_no_stage"]) == remove_part_and_stage(name):
                                matched_entry_point = True
                                break
                        if "parent_name" in references_library[ref] and references_library[ref]["parent_name"] == name and "name_no_stage" in references_library[ref] and references_library[ref]["name_no_stage"] == variable_name:
                            matched_entry_point = True
                            break
                        if "type" in references_library[ref] and references_library[ref]["type"] == "Configuration variable" and references_library[ref]["name_no_stage"] == variable_name:
                            matched_entry_point = True
                            break
                        if remove_stage(name) == "Unused duplicate of MULTU":
                            matched_entry_point = True
                            break
                        if args.platform == "disc" and variable_name == "KYTB":
                            matched_entry_point = True
                            break
                        if args.platform == "6502sp" and variable_name == "KYTB":
                            matched_entry_point = True
                            break
                        if args.platform == "elite-a" and variable_name == "KYTB":
                            matched_entry_point = True
                            break
                        if args.platform == "master" and (variable_name == "KYTB" or variable_name == "DELL1" or variable_name == "EE3"):
                            matched_entry_point = True
                            break
                    if not matched_entry_point:
                        print("\nERROR! {} used in {} in {} but is not an entry point or routine".format(variable_name, instruction, name))
                if add_popup_links_to_code:
                    if indirect:
                        return '<a class="popup variable">' + variable_name + '</a>'
                    else:
                        return '<a class="popup destination">' + variable_name + '</a>'
                else:
                    if indirect:
                        return '<span class="variable">' + variable_name + '</span>'
                    else:
                        return '<span class="destination">' + variable_name + '</span>'
            else:
                if add_popup_links_to_code:
                    if in_macro:
                        if variable_name not in no_popups_in_macro:
                            return '<a class="popup variable">' + variable_name + '</a>'
                    else:
                        return '<a class="popup variable">' + variable_name + '</a>'
        return '<span class="variable">' + variable_name + '</span>'

    # Spaces
    m = re.match(r'^(.+)( )(.+)$', operand)
    if m:
        return markup_operand(m.group(1), instruction, constant, refs_only, name, indirect) + ' ' + markup_operand(m.group(3), instruction, constant, refs_only, name, indirect)

    return operand


def add_stage(string, stage):
    if stage and not string.endswith(" (" + stage + ")"):
        return string + " (" + stage + ")"
    else:
        return string


def remove_stage(string):
    if re.search(r" \(Part \d+ of \d+\)$", string):
        return string
    return re.sub(r" \([^)]+\)$", "", string)


def remove_part_and_stage(string):
    string = re.sub(r" \(Part \d+ of \d+\)", "", string)
    return remove_stage(string)


def escape_comment(string):
    return re.sub(r"<", "&lt;", string)


def add_to_references_library(name, item, stage):
    global references_library

    if name in no_popups:
        return

    name = add_stage(name, stage)
    item["name"] = add_stage(item["name"], stage)

    if name in references_library:
        existing = references_library[name]

        if ("summary" not in existing) or \
           (not existing["summary"] and item["summary"]):
            if "summary" in item:
                existing["summary"] = item["summary"]

        if ("parent_name" not in existing) or \
           (not existing["parent_name"] and item["parent_name"]):
            if "parent_name" in item:
                existing["parent_name"] = item["parent_name"]
    else:
        references_library[name] = item


def extract_entry_point(source, j, line, parent_name, stage, parent_category, parent_url_category, parent_url_name, parent_filename, local_entry_points):
    # Entry point
    m = re_argument_entry1.match(line)
    if m:
        this_item = {}
        name = m.group(1)
        name_with_stage = add_stage(name, stage)
        summary = m.group(4) + fetch_header_comments(source, j)
        this_item["name"] = name_with_stage
        this_item["name_no_stage"] = name
        this_item["parent_name"] = parent_name
        this_item["type"] = "Entry point"
        this_item["summary"] = summary
        this_item["entry_point"] = True
        add_to_references_library(name, this_item, stage)
        add_article(entry_points, "Details of the " + name + " entry point", parent_url_category, parent_url_name, parent_filename, name_with_stage, summary, parent_category, stage)
        local_entry_points.append(name)


def extract_labels(source, j, references_library, parent_name, stage, parent_name_no_stage, local_labels):
    # Remove initial comment (but not from commented instructions)
    code = re.sub(r"^" + re_comment_delimiter + r"\n", "", source[j])
    code = re.sub(r"^" + re_comment_delimiter + r" ", "", code)
    code = re.sub(r"\n", "", code)

    # Include commented-out labels in removed routines in Elite-A only
    elite_a_removed_label = False
    if parent_name_no_stage.endswith(", Removed") and args.platform == "elite-a":
        code = re.sub(r"^" + re_comment_delimiter + r"\.", ".", code)
        elite_a_removed_label = True

    # Label
    m = re.match(re_label, code)
    if m:
        this_item = {}
        name = m.group(2)
        this_item["name"] = name
        this_item["name_no_stage"] = name
        this_item["parent_name"] = parent_name
        summary = fetch_comments(source, j, r"(ALIGN|SKIP|EQU.)(?! &2(C|4))", 2)
        this_item["summary"] = summary
        if name == re.sub(r" \(Part \d+ of \d+\)", "", parent_name_no_stage):
            this_item["type"] = "Subroutine"
        elif summary:
            this_item["type"] = "Variable"
            add_source_code_stats("variable_" + name, "Variable", "Workspaces", 0, 0)
        else:
            this_item["type"] = "Label"
        if not elite_a_removed_label:
            add_to_references_library(name, this_item, stage)
        local_labels.append(name)


def fetch_comments(source, i, regex, skip):
    summary = ""
    i = i + skip
    if i < len(source):
        line = source[i]
        if re.search(regex, line):
            n = re_line_with_comment.match(line)
            while n:
                summary += n.group(3)
                i += 1
                line = source[i]
                if re_empty_comment.match(line) or re_empty_line.match(line) \
                   or re_instruction_line.search(line) or re_configuration_variable.match(line):
                    break
                else:
                    n = re_line_with_comment.match(line)
    return summary


def fetch_header_comments(source, i):
    summary = ""
    i = i + 1
    line = source[i]
    n = re_header_comment.match(line)
    while n:
        summary += " " + n.group(1)
        i += 1
        line = source[i]
        if re_empty_comment.match(line) or re_empty_line.match(line) \
           or re_empty_line_in_header.match(line) or re_comment.match(line) \
           or re_comment2.match(line):
            break
        else:
            n = re_header_comment.match(line)
    return summary


def fetch_header_summary(source, i, regex):
    summary = ""
    i = i + 1
    line = source[i]
    n = regex.match(line)
    while n:
        summary += " " + n.group(1)
        i += 1
        line = source[i]
        if re_empty_comment.match(line) or re_empty_line.match(line) \
           or re_empty_line_in_header.match(line) or re_comment.match(line) \
           or re_comment2.match(line):
            break
        else:
            n = regex.match(line)
    return {"summary": summary, "index": i}


def start_html(handle, section, url_name, seo_title, title, description):
    handle.write(html_header1)
    title = title.replace('"', "'")
    if platform_short_name:
        seo_title = seo_title + " in " + versionise("{}", platform_name)
        subtitle = "[" + version(platform_name) + "]"
    else:
        subtitle = ""
    handle.write('page_header("{}", "{}.html", "{}", "{}", "{}", "{}-index", "{}{}", "{}", "{}");\n'.format(
        section.replace('"', "'"),
        url_name.replace('"', "'"),
        seo_title.replace('"', "'"),
        title,
        description.replace('"', "'"),
        game_id,
        platform_id,
        section.replace('"', "'"),
        url_name.replace('"', "'").replace(".html", ""),
        subtitle
    ))
    handle.write(html_header2)


def start_html_index(handle, section, url_name, seo_title, title, description):
    handle.write(html_header1)
    title = title.replace('"', "'")
    if platform_short_name:
        subtitle = "[" + version(platform_name) + "]"
    else:
        subtitle = ""
    handle.write('page_header("{}", "{}.html", "{}", "{}", "{}", "{}-index", "{}", "{}", "{}");\n'.format(
        section.replace('"', "'"),
        url_name.replace('"', "'"),
        seo_title.replace('"', "'"),
        title,
        description.replace('"', "'"),
        game_id,
        section.replace('"', "'"),
        url_name.replace('"', "'").replace(".html", ""),
        subtitle
    ))
    handle.write(html_header2)


def end_html(handle):
    handle.write(html_footer)


def start_code_html(handle, section, url_name, seo_title, title, description, stage):
    handle.write(html_code_header1)
    title = title.replace('"', "'")
    if platform_short_name:
        if stage:
            subtitle = "[" + version(platform_name) + ", " + stage + "]"
        else:
            subtitle = "[" + version(platform_name) + "]"
    else:
        subtitle = ""
    if stage:
        menu_stage = make_id(stage) + "_"
    else:
        menu_stage = ""
    handle.write('page_header("{}", "{}.html", "{}", "{}", "{}", "{}-code", "{}{}", "{}", "{}");\n'.format(
        section.replace('"', "'"),
        url_name.replace('"', "'"),
        seo_title.replace('"', "'"),
        title,
        description.replace('"', "'"),
        game_id,
        platform_id,
        section.replace('"', "'"),
        menu_stage + url_name.replace('"', "'").replace(".html", ""),
        subtitle
    ))
    handle.write(html_code_header2)


def end_code_html(handle):
    handle.write(html_code_footer)


def add_article(array, description, section, url_name, filename, name, summary, category, stage):
    if section in array:
        array[section].append({"description": description, "url_name": url_name, "filename": filename, "name": name, "summary": summary, "category": category, "stage": stage.lower()})
    else:
        array[section] = [{"description": description, "url_name": url_name, "filename": filename, "name": name, "summary": summary, "category": category, "stage": stage.lower()}]


def output_next_prev(next_prev, page_file):
    if next_prev["prev"] and next_prev["next"]:
        page_file.write(html_prev_next.format(next_prev["prev"]["filename"], next_prev["prev"]["name"], next_prev["next"]["filename"], next_prev["next"]["name"]))
    elif next_prev["prev"]:
        page_file.write(html_prev.format(next_prev["prev"]["filename"], next_prev["prev"]["name"]))
    elif next_prev["next"]:
        page_file.write(html_next.format(next_prev["next"]["filename"], next_prev["next"]["name"]))


def output_map_of_source_code():
    filename = content_folder + "articles/map_of_the_source_code.html"
    with open(dest_folder + filename, "w") as page_file:
        start_html(page_file, "sources", "map_of_the_source_code", "Map of the source code", "Map of the source code", versionise("A fully referenced map of the source code for {}", platform_name))

        next_prev = next_prev_all["map_of_the_source_code"]
        output_next_prev(next_prev, page_file)

        page_file.write('<div class="codeBlockWrapper"><div class="codeBlock article">')
        page_file.write(html_large_source_code_page_links)

        previous_header = all_headers[0]["source_name"]
        underline = "-" * len(previous_header)
        page_file.write(html_anchor.format("header-" + make_id(previous_header)))
        page_file.write(html_summary_heading.format(previous_header, underline))
        page_file.write('<table class="spacedTableBorder codeSummary">')
        page_file.write('<tr class="codeSummaryHeader"><th class="codeSummaryLabel">Category</th><th>Details</th></tr>')

        for header in all_headers:
            if previous_header != header["source_name"]:
                previous_header = header["source_name"]
                underline = "-" * len(previous_header)
                page_file.write("</table>")
                page_file.write(html_anchor.format("header-" + make_id(previous_header)))
                page_file.write(html_summary_heading.format(previous_header, underline))
                page_file.write('<table class="spacedTableBorder codeSummary">')
                page_file.write('<tr class="codeSummaryHeader"><th class="codeSummaryLabel">Category</th><th>Details</th></tr>')

            page_file.write('<tr><td class="codeSummaryCategory"><p>{2}</p></td><td><p><a href="/{4}">{1}: {0}</a></p><p class="codeSummarySummary">{3}</p></td></tr>'.format(
                header["name"],
                header["type"],
                header["category"],
                header["summary"],
                header["filename"]
            ))

        page_file.write("</table>")
        page_file.write('</div></div>')
        next_prev = next_prev_all["map_of_the_source_code"]
        output_next_prev(next_prev, page_file)
        end_html(page_file)


def output_source_code_stats():
    filename = content_folder + "articles/source_code_statistics.html"
    total_instructions = 0
    total_data_bytes = 0
    total_subroutines = 0
    total_variables = 0
    total_workspaces = 0
    total_macros = 0
    max_instructions = 0
    max_data_bytes = 0
    max_subroutines = 0
    max_variables = 0
    max_workspaces = 0
    max_macros = 0

    with open(dest_folder + filename, "w") as page_file:
        if args.platform == "aviator" or args.platform == "revs" or args.platform == "lander":
            index_section = "source_statistics"
            start_html_index(page_file, index_section, "home", "Source code statistics", "Source code statistics", versionise("A statistical breakdown of the source code for {}", platform_name))
        else:
            index_section = "compare_statistics"
            start_html_index(page_file, index_section, platform_id + "statistics", "Source code statistics", "Source code statistics", versionise("A statistical breakdown of the source code for {}", platform_name))

        next_prev = next_prev_statistics[platform_key]
        output_next_prev(next_prev, page_file)

        page_file.write('<div class="codeBlockWrapper"><div class="codeBlock article">')
        page_file.write(versionise(html_source_code_stats_intro, platform_name))
        page_file.write('<table class="spacedTableBorder codeSummary codeStatistics">')
        page_file.write('<tbody><tr class="codeSummaryHeader"><th class="codeSummaryLabel">Category</th><th>Instructions</th><th>Subroutines</th><th>Variables</th><th>Data (bytes)</th><!--<th>Workspaces</th><th>Macros</th>--></tr>')

        for category in sorted(source_code_stats["categories"]):
            instructions = source_code_stats["categories"][category]["instruction_count"]
            total_instructions += instructions
            max_instructions = max(max_instructions, instructions)
            data_bytes = source_code_stats["categories"][category]["data_byte_count"]
            total_data_bytes += data_bytes
            max_data_bytes = max(max_data_bytes, data_bytes)
            subroutines = source_code_stats["categories"][category]["subroutine_count"]
            total_subroutines += subroutines
            max_subroutines = max(max_subroutines, subroutines)
            variables = source_code_stats["categories"][category]["variable_count"]
            total_variables += variables
            max_variables = max(max_variables, variables)
            workspaces = source_code_stats["categories"][category]["workspace_count"]
            total_workspaces += workspaces
            max_workspaces = max(max_workspaces, workspaces)
            macros = source_code_stats["categories"][category]["macro_count"]
            total_macros += macros
            max_macros = max(max_macros, macros)

        for category in sorted(source_code_stats["categories"]):
            instructions = source_code_stats["categories"][category]["instruction_count"]
            data_bytes = source_code_stats["categories"][category]["data_byte_count"]
            subroutines = source_code_stats["categories"][category]["subroutine_count"]
            variables = source_code_stats["categories"][category]["variable_count"]
            workspaces = source_code_stats["categories"][category]["workspace_count"]
            macros = source_code_stats["categories"][category]["macro_count"]
            page_file.write('<tr><td class="codeSummaryCategory"><span>{}</span></td><td><span class="yes">{}</span>{}</td><td><span class="yes">{}</span>{}</td><td><span class="yes">{}</span>{}</td><td><span class="yes">{}</span>{}</td><!--<td><span class="yes">{}</span>{}</td><td><span class="yes">{}</span>{}</td>--></tr>'.format(
                category,
                padding(instructions, max_instructions),
                percentage(instructions, total_instructions),
                padding(subroutines, max_subroutines),
                percentage(subroutines, total_subroutines),
                padding(variables, max_variables),
                percentage(variables, total_variables),
                padding(data_bytes, max_data_bytes),
                percentage(data_bytes, total_data_bytes),
                padding(workspaces, max_workspaces),
                percentage(workspaces, total_workspaces),
                padding(macros, max_macros),
                percentage(macros, total_macros)
            ))

        page_file.write('<tr class="codeSummaryHeader footer"><th>{}</th><th>{}</th><th>{}</th><th>{}</th><th>{}</th><!--<th>{}</th><th>{}</th>--></tr></tbody>'.format(
            "Totals",
            total_instructions,
            total_subroutines,
            total_variables,
            total_data_bytes,
            total_workspaces,
            total_macros
        ))

        page_file.write("</table>")
        page_file.write(html_source_code_stats_sorter)
        page_file.write(html_source_code_stats_footer)
        page_file.write('</div></div>')
        next_prev = next_prev_statistics[platform_key]
        output_next_prev(next_prev, page_file)
        end_html(page_file)


def output_source_code_cross_references():
    filename = content_folder + "articles/source_code_cross-references.html"

    previous_letter = "a"

    with open(dest_folder + filename, "w") as page_file:
        start_html(page_file, "indexes", "source_code_cross-references", "Source code cross-references", "Source code cross-references", versionise("An index of cross-references in the source for {}", platform_name))

        next_prev = next_prev_indexes["cross-references"]
        output_next_prev(next_prev, page_file)

        page_file.write('\t\t\t\t<div class="codeBlockWrapper">\n')
        page_file.write('\t\t\t\t\t<div class="codeBlock article">\n')
        page_file.write(versionise(html_source_code_cross_references_intro, platform_name))
        page_file.write('\t\t\t\t\t\t<table class="spacedTableBorder codeSummary crossReferences">\n')
        page_file.write('\t\t\t\t\t\t\t<tr class="blank"><td colspan="3">{}</td></tr>\n'.format(html_anchor.format(previous_letter)))
        page_file.write('\t\t\t\t\t\t\t<tr class="codeSummaryHeader"><th>Name</th><th>Type</th><th>Referenced by</th></tr>\n')

        for ref in sorted(mentions, key=sort_reference_names):
            (mention_list, mention_link, letter, ref_type) = fetch_cross_references(ref, html_summary_reference_link, include_stage=True)

            if letter:
                if previous_letter != letter:
                    previous_letter = letter
                    page_file.write('\t\t\t\t\t\t\t<tr class="blank"><td colspan="3">{}</td></tr>\n'.format(html_anchor.format(previous_letter)))

                if not mention_list:
                    mention_list = "n/a"

                page_file.write('\t\t\t\t\t\t\t<tr><td>{}</td><td>{}</td><td>{}</td></tr>\n'.format(
                    mention_link,
                    ref_type,
                    mention_list
                ))

        page_file.write("\t\t\t\t\t\t</table>\n")
        page_file.write("\t\t\t\t\t</div>\n")
        page_file.write("\t\t\t\t</div>\n")
        next_prev = next_prev_indexes["cross-references"]
        output_next_prev(next_prev, page_file)
        end_html(page_file)


def fetch_cross_references(ref, list_format, include_stage=True):
    global references_library

    mention_list = None
    mention_link = None
    letter = None
    ref_type = None

    if ref in references_library:

        ref_filename = ""
        ref_type = ""
        ref_no_stage = ref
        parent_filename = ""
        parent_name = ""

        if "filename" in references_library[ref]:
            ref_filename = references_library[ref]["filename"]

        if "type" in references_library[ref]:
            ref_type = references_library[ref]["type"]

        if "parent_name" in references_library[ref] and references_library[ref]["parent_name"] != ref:
            parent_name = references_library[ref]["parent_name"]
            if parent_name in references_library and 'filename' in references_library[parent_name]:
                parent_filename = references_library[parent_name]['filename']

        if "name_no_stage" in references_library[ref]:
            ref_no_stage = references_library[ref]["name_no_stage"]

        if ref_no_stage == "dontdolinefeedontheprinternow":
            ref_no_stage = "dontdolinefeed ontheprinternow"

        if ref_filename:
            mention_link = '<a href="/{}">{}</a>'.format(ref_filename, ref_no_stage)
        elif parent_name:
            parent_filename_with_anchor = parent_filename + "#" + make_id(ref_no_stage)
            mention_link = '<a href="/{}">{}</a>'.format(parent_filename_with_anchor, ref_no_stage)
        elif ref_type == "Configuration variable" and "source_filename" in references_library[ref]:
            parent_filename_with_anchor = references_library[ref]["source_filename"]
            mention_link = '<a href="/{}">{}</a>'.format(parent_filename_with_anchor, ref_no_stage)
        else:
            mention_link = ref_no_stage

        mention_list = ""
        if ref in mentions:
            for label in sorted(mentions[ref], key=sort_reference_names):
                href = references_library[label]["filename"]
                if include_stage:
                    mention_list += list_format.format(href, label)
                else:
                    # If this is a reference within a header block, don't show refs to itself
                    if label != parent_name:
                        mention_list += list_format.format(href, remove_stage(label))

        letter = ref_no_stage[:1].lower()

    return (mention_list, mention_link, letter, ref_type)


def percentage(number, total):
    if number > 0:
        return "({:.1f}%)".format(100 * number / total).rjust(7, "\u00A0")
    return "({:.1f}%)".format(0).rjust(7, "\u00A0")


def padding(number, max):
    width = len(str(max)) + 1
    return "{}".format(number).ljust(width, "\u00A0")


def extract_popup_data(source, stage, source_file, source_name):
    global i, references_library, configuration_variables

    i = 0

    if stage == "Docked" or stage == "Flight" or stage == "Encyclopedia" or stage == "Parasite":
        append_file = "_" + stage.lower()
        append_name = " (" + stage + ")"
        source_file = "workspaces" + append_file
        source_name = "Workspaces" + append_name

    while i < len(source):
        line = source[i]
        name = ""

        if args.platform == "aviator":
            if line.endswith("AVIATOR MAIN GAME CODE\n"):
                source_file = "aviator_a"
                source_name = "Aviator A"
            elif line.endswith("Name: EraseCanopyLines\n"):
                source_file = "aviator_b"
                source_name = "Aviator B"
            elif line.endswith("Name: ArtificialHorizon\n"):
                source_file = "aviator_c"
                source_name = "Aviator C"
            elif line.endswith("Name: AlienInAcornsville\n"):
                source_file = "aviator_d"
                source_name = "Aviator D"
            elif line.endswith("Name: lineBufferR\n"):
                source_file = "aviator_e"
                source_name = "Aviator E"
            elif line.endswith("Name: PrintTooLate\n"):
                source_file = "aviator_f"
                source_name = "Aviator F"

        elif args.platform == "revs":
            if line.endswith("REVS MAIN GAME CODE\n"):
                source_file = "revs_a"
                source_name = "Revs A"
            elif line.endswith("Name: MainDrivingLoop (Part 1 of 5)\n"):
                source_file = "revs_b"
                source_name = "Revs B"
            elif line.endswith("Name: GetColour (Part 1 of 3)\n"):
                source_file = "revs_c"
                source_name = "Revs C"
            elif line.endswith("Name: ProcessOvertaking (Part 1 of 3)\n"):
                source_file = "revs_d"
                source_name = "Revs D"
            elif line.endswith("Name: token26\n"):
                source_file = "revs_e"
                source_name = "Revs E"
            elif line.endswith("Name: GetWingSettings\n"):
                source_file = "revs_f"
                source_name = "Revs F"
            elif line.endswith("Name: MultiplyCoords\n"):
                source_file = "revs_g"
                source_name = "Revs G"
            elif line.endswith("Name: xVergeRightLo\n"):
                source_file = "revs_h"
                source_name = "Revs H"
            elif line.endswith("Name: GetTextInput\n"):
                source_file = "revs_i"
                source_name = "Revs I"
            elif line.endswith("REVS SILVERSTONE TRACK SOURCE\n"):
                source_file = "revs_silverstone"
                source_name = "Silverstone track data file"
            elif line.endswith("REVS BRANDS HATCH TRACK SOURCE\n"):
                source_file = "revs_brands_hatch"
                source_name = "Brands Hatch track data file"
            elif line.endswith("REVS DONINGTON PARK TRACK SOURCE\n"):
                source_file = "revs_donington_park"
                source_name = "Donington Park track data file"
            elif line.endswith("REVS OULTON PARK TRACK SOURCE\n"):
                source_file = "revs_oulton_park"
                source_name = "Oulton Park track data file"
            elif line.endswith("REVS SNETTERTON TRACK SOURCE\n"):
                source_file = "revs_snetterton"
                source_name = "Snetterton track data file"
            elif line.endswith("REVS NÜRBURGRING TRACK SOURCE\n"):
                source_file = "revs_nurburgring"
                source_name = "Nürburgring track data file"

        elif args.platform == "lander":
            if line.endswith("LANDER MAIN GAME CODE\n"):
                source_file = "lander_a"
                source_name = "Lander A"
            elif line.endswith("Name: StoreParticleData\n"):
                source_file = "lander_b"
                source_name = "Lander B"
            elif line.endswith("Name: ProjectParticleOntoScreen\n"):
                source_file = "lander_c"
                source_name = "Lander C"
            elif line.endswith("Name: lineJump\n"):
                source_file = "lander_d"
                source_name = "Lander D"

        elif args.platform == "nes":
            if line.endswith("NES ELITE GAME SOURCE (BANK 0)\n"):
                source_file = "bank_0_1"
                source_name = "Bank 0 (Part 1 of 5)"
            elif line.endswith("Name: TACTICS (Part 1 of 7)\n"):
                source_file = "bank_0_2"
                source_name = "Bank 0 (Part 2 of 5)"
            elif line.endswith("Name: TT14\n"):
                source_file = "bank_0_3"
                source_name = "Bank 0 (Part 3 of 5)"
            elif line.endswith("Name: PrintLaserView\n"):
                source_file = "bank_0_4"
                source_name = "Bank 0 (Part 4 of 5)"
            elif line.endswith("Name: ShowStartScreen\n"):
                source_file = "bank_0_5"
                source_name = "Bank 0 (Part 5 of 5)"

            if line.endswith("NES ELITE GAME SOURCE (BANK 1)\n"):
                source_file = "bank_1_1"
                source_name = "Bank 1 (Part 1 of 3)"
            elif line.endswith("Name: LL61\n"):
                source_file = "bank_1_2"
                source_name = "Bank 1 (Part 2 of 3)"
            elif line.endswith("Name: EDGES\n"):
                source_file = "bank_1_3"
                source_name = "Bank 1 (Part 3 of 3)"

            if line.endswith("NES ELITE GAME SOURCE (BANK 2)\n"):
                source_file = "bank_2_1"
                source_name = "Bank 2 (Part 1 of 4)"
            elif line.endswith("Name: TKN1_DE\n"):
                source_file = "bank_2_2"
                source_name = "Bank 2 (Part 2 of 4)"
            elif line.endswith("Name: TKN1_FR\n"):
                source_file = "bank_2_3"
                source_name = "Bank 2 (Part 3 of 4)"
            elif line.endswith("Name: QQ18_FR\n"):
                source_file = "bank_2_4"
                source_name = "Bank 2 (Part 4 of 4)"

            if line.endswith("NES ELITE GAME SOURCE (BANK 3)\n"):
                source_file = "bank_3_1"
                source_name = "Bank 3 (Part 1 of 2)"
            elif line.endswith("Name: HideIconBar\n"):
                source_file = "bank_3_2"
                source_name = "Bank 3 (Part 2 of 2)"

            if line.endswith("NES ELITE GAME SOURCE (BANK 6)\n"):
                source_file = "bank_6_1"
                source_name = "Bank 6 (Part 1 of 3)"
            elif line.endswith("Name: tuneData\n"):
                source_file = "bank_6_2"
                source_name = "Bank 6 (Part 2 of 3)"
            elif line.endswith("Name: LTDEF\n"):
                source_file = "bank_6_3"
                source_name = "Bank 6 (Part 3 of 3)"

            if line.endswith("NES ELITE GAME SOURCE (BANK 7)\n"):
                source_file = "bank_7_1"
                source_name = "Bank 7 (Part 1 of 4)"
            elif line.endswith("Name: ClearMemory\n"):
                source_file = "bank_7_2"
                source_name = "Bank 7 (Part 2 of 4)"
            elif line.endswith("Name: autoplayKeys1_DE\n"):
                source_file = "bank_7_3"
                source_name = "Bank 7 (Part 3 of 4)"
            elif line.endswith("Name: SetupFullViewInNMI\n"):
                source_file = "bank_7_4"
                source_name = "Bank 7 (Part 4 of 4)"

        elif stage == "":
            if line.endswith("ELITE RECURSIVE TEXT TOKEN FILE\n"):
                source_file = "text_tokens"
                source_name = "Text tokens"
            elif line.endswith("Name: K%\n"):
                source_file = "workspaces"
                source_name = "Workspaces"
            elif line.endswith("ELITE A FILE\n"):
                source_file = "elite_a"
                source_name = "Elite A"
            elif line.endswith("ELITE B FILE\n"):
                source_file = "elite_b"
                source_name = "Elite B"
            elif line.endswith("ELITE C FILE\n"):
                source_file = "elite_c"
                source_name = "Elite C"
            elif line.endswith("ELITE D FILE\n"):
                source_file = "elite_d"
                source_name = "Elite D"
            elif line.endswith("ELITE E FILE\n"):
                source_file = "elite_e"
                source_name = "Elite E"
            elif line.endswith("ELITE F FILE\n"):
                source_file = "elite_f"
                source_name = "Elite F"
            elif line.endswith("ELITE G FILE\n"):
                source_file = "elite_g"
                source_name = "Elite G"
            elif line.endswith("ELITE H FILE\n"):
                source_file = "elite_h"
                source_name = "Elite H"
            elif line.endswith("ELITE I FILE\n"):
                source_file = "elite_i"
                source_name = "Elite I"
            elif line.endswith("ELITE J FILE\n"):
                source_file = "elite_j"
                source_name = "Elite J"
            elif line.endswith("ELITE K FILE\n"):
                source_file = "elite_k"
                source_name = "Elite K"
            elif line.endswith("ELITE SHIP BLUEPRINTS FILE\n"):
                source_file = "elite_ships"
                source_name = "Ship blueprints"
            elif line.endswith("ELITE Z FILE\n"):
                source_file = "i_o_processor"
                source_name = "I/O processor"
            elif line.endswith("ELITE GAME DATA FILE\n"):
                source_file = "elite_data"
                source_name = "Game data"

        elif stage == "Docked" or stage == "Flight" or stage == "Encyclopedia" or stage == "Parasite":
            if line.endswith("ELITE A FILE\n"):
                source_file = "elite_a" + append_file
                source_name = "Elite A" + append_name
            elif line.endswith("ELITE B FILE\n"):
                source_file = "elite_b" + append_file
                source_name = "Elite B" + append_name
            elif line.endswith("ELITE C FILE\n"):
                source_file = "elite_c" + append_file
                source_name = "Elite C" + append_name
            elif line.endswith("ELITE D FILE\n"):
                source_file = "elite_d" + append_file
                source_name = "Elite D" + append_name
            elif line.endswith("ELITE E FILE\n"):
                source_file = "elite_e" + append_file
                source_name = "Elite E" + append_name
            elif line.endswith("ELITE F FILE\n"):
                source_file = "elite_f" + append_file
                source_name = "Elite F" + append_name
            elif line.endswith("ELITE G FILE\n"):
                source_file = "elite_g" + append_file
                source_name = "Elite G" + append_name
            elif line.endswith("ELITE H FILE\n"):
                source_file = "elite_h" + append_file
                source_name = "Elite H" + append_name
            elif line.endswith("ELITE I FILE\n"):
                source_file = "elite_i" + append_file
                source_name = "Elite H" + append_name
            elif line.endswith("ELITE J FILE\n"):
                source_file = "elite_j" + append_file
                source_name = "Elite J" + append_name
            elif line.endswith("ELITE K FILE\n"):
                source_file = "elite_k" + append_file
                source_name = "Elite K" + append_name
            elif line.endswith("ELITE L FILE\n"):
                source_file = "elite_l" + append_file
                source_name = "Elite L" + append_name
            elif line.endswith("ELITE M FILE\n"):
                source_file = "elite_m" + append_file
                source_name = "Elite M" + append_name
            elif line.endswith("ELITE SHIP HANGAR BLUEPRINTS FILE\n"):
                source_file = "elite_ships_docked"
                source_name = "Ship hangar blueprints"
            elif line.endswith("ELITE SHIP BLUEPRINTS FILE\n") and stage == "Parasite":
                source_file = "elite_ships_parasite"
                source_name = "Ship blueprints (Parasite)"
            elif line.endswith("ELITE SHIP BLUEPRINTS FILE\n"):
                source_file = "elite_ships"
                source_name = "Ship blueprints"

        v = re_configuration_variable.match(line)
        if v:
            var_name = v.group(2)
            var_value = v.group(4)
            item = {}
            item["name"] = var_name
            item["name_no_stage"] = var_name
            item["source_file"] = source_file
            item["source_filename"] = content_folder + "all/" + source_file + ".html#" + make_id(var_name)
            item["type"] = "Configuration variable"
            item["value"] = var_value
            item["summary"] = fetch_comments(source, i, r"(=)", 0)
            add_to_references_library(var_name, item, stage)
            if var_value.isnumeric():
                configuration_variables[var_name.replace("%", "_per_cent")] = int(var_value)

        n = re_name.match(line)
        if n:
            name = n.group(2)

            type = ""
            category = ""
            summary = ""

            j = i + 1
            while j < len(source):
                info_line = source[j]

                t = re_type.match(info_line)
                if t:
                    type = t.group(2)

                c = re_category.match(info_line)
                if c:
                    category = c.group(2)

                s = re_summary.match(info_line)
                if s:
                    summary = s.group(2) + fetch_header_summary(source, j, re_summary2)["summary"]

                e = re_empty_line.match(info_line)
                if e:
                    break

                j += 1

            if not (type and category and summary):
                print("\nERROR! Missing a header entry in routine {} ({})\n".format(name, source_file))

            parse_header(source, name, type, category, summary, stage, source_file, source_name)

        i += 1


def move_data_to_end(block_name):
    global all_headers
    bank_7_data = []
    other_data = []
    for header in all_headers:
        if header["source_file"] == block_name:
            bank_7_data.append(header)
        else:
            other_data.append(header)
    all_headers = other_data + bank_7_data


def output_individual_code_pages(source, stage):
    global i

    i = 0

    while i < len(source):
        line = source[i]
        name = ""

        n = re_name.match(line)
        if n:
            name = n.group(2)

            type = ""
            category = ""
            summary = ""

            j = i + 1
            while j < len(source):
                info_line = source[j]

                t = re_type.match(info_line)
                if t:
                    type = t.group(2)

                c = re_category.match(info_line)
                if c:
                    category = c.group(2)

                s = re_summary.match(info_line)
                if s:
                    summary = s.group(2) + fetch_header_summary(source, j, re_summary2)["summary"]

                e = re_empty_line.match(info_line)
                if e:
                    break

                j += 1

            build_individual_code_page(source, name, type, category, summary, stage)

        i += 1


def output_large_source_code_page(source, stage, name, source_file_name, start_line, end_line):
    global i, references

    start_html(all_file, "all_source", source_file_name, name, name, "The " + name + " file in " + versionise("{}", platform_name))

    next_prev = next_prev_all[source_file_name]
    output_next_prev(next_prev, all_file)

    all_file.write('\n\t\t\t\t<div class="codeBlockWrapper"><pre class="codeBlock sourceCode initial">')

    if (args.platform == "aviator" or args.platform == "revs" or args.platform == "lander" or args.platform == "nes") and start_line.startswith("Name:"):
        # There are no A/B/C headers in Aviator, Revs, Lander or NES Elite, so we don't need to open a header block
        all_file.write('<div><div>')
    else:
        all_file.write('<div class="headerBlockWrapper"><div class="headerBlock">')

    references = set()

    if type(start_line) is list:
        for line_number in range(len(start_line)):
            large_source_code_page_contents(source, stage, name, source_file_name, start_line[line_number], end_line[line_number])
    else:
        large_source_code_page_contents(source, stage, name, source_file_name, start_line, end_line)

    all_file.write('</pre></div>')

    output_next_prev(next_prev, all_file)

    add_reference_popups(references, stage, all_file, name, True)
    end_html(all_file)


def large_source_code_page_contents(source, stage, name, source_file_name, start_line, end_line):
    global i, references, in_macro

    i = 0
    in_other_header = not start_line.startswith("Name:")
    in_if_to_remove = False
    in_else_to_remove = False
    configuration_variable_extra_data_html = ""

    if start_line:
        while i < len(source):
            line = source[i]
            if line.endswith(start_line + "\n"):
                break
            i += 1
    else:
        i += 2

    while i < len(source):
        line = source[i]
        name = ""

        if end_line and line.endswith(end_line + "\n"):
            break

        if in_macro or re.match(r"^(MACRO|ENDMACRO)", line):
            if re.match(r"^MACRO", line):
                in_macro = True
                all_file.write(re.sub(r"^(.*)$", r'<span class="macro">\1</span>', line))
            if re.match(r"^ENDMACRO", line):
                in_macro = False
                all_file.write(re.sub(r"^(.*)$", r'<span class="macro">\1</span>', line))

        n = re_name.match(line)

        if re_if_to_remove.search(line):
            # Remove IF _MATCH_ORIGINAL_BINARIES
            in_if_to_remove = True
            in_else_to_remove = False

        elif in_if_to_remove:
            # Remove contents of IF _MATCH_ORIGINAL_BINARIES
            if re_else_to_remove.search(line):
                # Until we reach the ELSE
                in_if_to_remove = False
                in_else_to_remove = True
                i += 1

        elif in_else_to_remove and re_endif_to_remove.search(line):
            # Remove ENDIF from IF _MATCH_ORIGINAL_BINARIES
            in_else_to_remove = False

        elif re_if_to_remove.search(line):
            in_if_to_remove = True

        elif n:
            name = n.group(2)
            type = ""
            category = ""
            summary = ""

            j = i + 1
            while j < len(source):
                info_line = source[j]

                t = re_type.match(info_line)
                if t:
                    type = t.group(2)

                c = re_category.match(info_line)
                if c:
                    category = c.group(2)

                s = re_summary.match(info_line)
                if s:
                    summary = s.group(2) + fetch_header_summary(source, j, re_summary2)["summary"]

                e = re_empty_line.match(info_line)
                if e:
                    break

                j += 1

            build_large_source_code_page(source, name, type, category, summary, stage)

        elif re_comment.match(line):
            if in_other_header and i < len(source) - 1 and re_empty_line.match(source[i + 1]):
                all_file.write('</div></div>')
                in_other_header = False
            elif not in_other_header and i < len(source) - 2 and re_empty_line_in_header.match(source[i + 1]) and not re_name.match(source[i + 2]):
                if end_line and source[i + 2].endswith(end_line + "\n"):
                    # Don't show empty box at end of page
                    in_other_header = False
                else:
                    all_file.write('<div class="headerBlockWrapper"><div class="headerBlock">')
                    in_other_header = True
                    i += 1

        elif re_comment2.match(line):
            all_file.write('<hr class="light" />')

        elif re.match(re_label, line):
            m = re.match(re_label, line)
            anchor = html_anchor.format(make_id(m.group(2)))
            all_file.write(re.sub(re_label, r'<span class="label">\1\2</span>' + anchor, line))

        elif re.match(r"^ *" + re_comment_delimiter + r" *(ALIGN|CPU|IF|ELIF|ELSE|ENDIF|PRINT|SAVE|INCLUDE|INCBIN|GUARD|ORG|COPYBLOCK|FOR|NEXT|CLEAR|DIM|OPT|OSCLI)", line):
            all_file.write(re.sub(r"^(.*)$", r'<span class="comment">\1</span>', line))

        # Process configuration variable
        elif re_configuration_variable.match(line):
            # Separate trailing comment
            c = re_configuration_variable.match(line)
            anchor = html_anchor.format(make_id(c.group(2)))
            output = c.group(1) + '<span class="config">' + c.group(2) + '</span>' + anchor + c.group(3) + '<span class="operator">=</span> <span class="configValue">' + c.group(4) + '</span>'
            if c.group(6):
                output += c.group(5) + '<span class="comment">' + escape_comment(c.group(6)) + '</span>'
            all_file.write(output + '\n')
            mention_list = fetch_cross_references(add_stage(c.group(2), stage), html_workspace_reference_link, include_stage=False)[0]
            if mention_list:
                configuration_variable_extra_data_html = mention_list

        elif re.match(r"^ *(ALIGN|CPU|IF|ELIF|ELSE|ENDIF|PRINT|SAVE|INCLUDE|INCBIN|GUARD|ORG|COPYBLOCK|FOR|NEXT|CLEAR|DIM|OPT|OSCLI)", line):
            # Separate trailing comment
            m = re.match(r"^([^" + re_comment_delimiter + r"]*)( *)(" + re_comment_delimiter + r".*)$", line)
            if m:
                if "-->" in m.group(3):
                    all_file.write('<span class="directive">' + m.group(1) + '</span>' + m.group(2) + '<span class="comment diff">' + m.group(3) + '</span>\n')
                else:
                    all_file.write('<span class="directive">' + m.group(1) + '</span>' + m.group(2) + '<span class="comment">' + escape_comment(m.group(3)) + '</span>\n')
            else:
                all_file.write(re.sub(r"^(.*)$", r'<span class="directive">\1</span>', line))

        elif "SKIP" in line or "ALIGN" in line or "EQU" in line:
            # Catch code that is outside a routine
            all_file.write(tidy_code(line, stage, name, refs_only=False, statistics=True))

        elif "   " + comment_delimiter in line:
            # Catch indented comments in files like BCFS
            all_file.write(tidy_code(line, stage, name, refs_only=False, statistics=True))

        else:
            # Catches lines outside of routines - i.e. ELITE A header, etc.
            if line.startswith(comment_delimiter + " "):
                line = tidy_source_header_line(line, "", 0)
            elif line == comment_delimiter + "\n":
                line = "\n"
            else:
                line = tidy_code(line, stage, name, refs_only=False, statistics=True)

            if not re_empty_line.match(line) and not re_empty_comment.match(line) and not re_empty_line_in_header.match(line):
                debug_file.write(line)

            all_file.write(line)

        if configuration_variable_extra_data_html and re_line_with_comment.search(line) and (i == len(source) - 1 or (i < len(source) - 1 and re_empty_line.match(source[i + 1]))):
            extra_indent = ' ' * (line.find(comment_delimiter) - html_workspace_reference_link.find(comment_delimiter))
            all_file.write(html_workspace_reference_start.format(extra_indent) + configuration_variable_extra_data_html + html_workspace_reference_end)
            configuration_variable_extra_data_html = ""

        i += 1


def parse_header(source, name, type, category, summary, stage, source_file, source_name):
    global i, references, references_library, all_headers

    this_item = {}
    references = set()

    # print("{}: {} ({})".format(type, name, category))
    print(".", end="", flush=True)

    name_no_stage = name
    name = add_stage(name, stage)

    url_category = add_category(category)
    url_name = make_url_name(type) + "_" + make_url_name(name_no_stage)
    stage_name = add_stage_folder(stage, type)
    filename = content_folder + stage_name + "/" + make_url_name(type) + "/" + make_url_name(name_no_stage) + ".html"

    this_item["name"] = name
    this_item["name_no_stage"] = name_no_stage
    this_item["type"] = type
    this_item["category"] = category
    this_item["summary"] = summary
    this_item["filename"] = filename
    this_item["source_file"] = source_file
    this_item["source_name"] = source_name
    this_item["source_filename"] = content_folder + "all/" + source_file + ".html#header-" + make_id(name_no_stage)
    this_item["url_category"] = url_category
    this_item["url_name"] = url_name

    add_to_references_library(name, this_item, stage)

    all_headers.append(this_item)

    if this_item["type"] == "Macro":
        macro_names.append(this_item["name_no_stage"])

    analysing = True
    analysing_body = False
    analysing_header = True
    analysing_entry_points = False

    local_labels = []
    local_entry_points = []

    while i < len(source) and analysing:
        line = source[i]

        v = re_configuration_variable.match(line)
        if v:
            item = {}
            item["name"] = v.group(2)
            item["name_no_stage"] = v.group(2)
            item["parent_name"] = name
            item["type"] = "Configuration variable"
            item["value"] = v.group(4)
            item["summary"] = fetch_comments(source, i, r"(=)", 0)
            add_to_references_library(v.group(2), item, stage)

        elif re_empty_line.match(line):
            if i < len(source) - 1 and not re_comment.match(source[i + 1]) and not re_comment2.match(source[i + 1]):
                pass

        elif re_comment.match(line):
            analysing_header = False
            analysing_entry_points = False

            if analysing_body:
                analysing = False
            elif i < len(source) - 1 and re_empty_line.match(source[i + 1]):
                analysing_body = True

        elif analysing_entry_points and re_argument_entry1.match(line):
            extract_entry_point(source, i, line, name, stage, category, url_category, url_name, filename, local_entry_points)

        elif re_entry_points.match(line):
            analysing_entry_points = True

        elif re_arguments.match(line):
            analysing_entry_points = False

        elif re_returns.match(line):
            analysing_entry_points = False

        elif re_comment2.match(line):
            pass

        elif analysing and analysing_header:
            pass

        elif analysing and analysing_body:
            extract_labels(source, i, references_library, name, stage, name_no_stage, local_labels)
            tidy_code(line, stage, name, refs_only=True, statistics=True)

        i += 1

    i -= 1

    add_mentions(references, stage, name)

    for local_entry_point in local_entry_points:
        local_entry_point_label = re.sub(r"[-+]\d+$", "", local_entry_point)
        if local_entry_point_label not in local_labels:
            print("\nERROR! Entry point header entry {} has no matching local label in {}".format(local_entry_point, source_file))


def build_individual_code_page(source, name, type, category, summary, stage):
    global i, references, references_library, analysing_arguments, instruction_count, data_byte_count, in_if_to_remove, in_else_to_remove, in_workspace, workspace_variable_extra_data_html

    references = set()
    instruction_count = 0
    data_byte_count = 0
    in_workspace = (type == "Workspace")

    # print("{}: {} ({})".format(type, name, category))
    print(".", end="", flush=True)

    name_no_stage = name
    name = add_stage(name, stage)

    url_category = add_category(category)
    url_name = make_url_name(type) + "_" + make_url_name(name_no_stage)
    stage_name = add_stage_folder(stage, type)
    filename = content_folder + stage_name + "/" + make_url_name(type) + "/" + make_url_name(name_no_stage) + ".html"

    if type == "Variable":
        array = variables
    elif type == "Workspace":
        array = workspaces
    elif type == "Macro":
        array = macros
    else:
        array = subroutines

    add_article(array, "Details of the " + name + " " + type, url_category, url_name, filename, name, summary, category, stage)

    if os.path.exists(dest_folder + filename):
        print("\nERROR! File for individual code file already exists: {}\n".format(dest_folder + filename))

    with open(dest_folder + filename, "w") as page_file:

        start_code_html(page_file, url_category, url_name, "The " + name + " " + type.lower(), category + ": " + name_no_stage, "Annotated code for the " + name + " " + type.lower() + " in " + game_name, stage)

        next_prev = fetch_next_prev(name, all_headers, type)
        output_next_prev(next_prev, page_file)

        analysing = True
        analysing_body = False
        analysing_header = True
        analysing_arguments = False
        page_file.write('\n\t\t\t\t<div class="codeBlockWrapper"><pre class="codeBlock sourceCode initial"><div class="headerBlockWrapper"><div class="headerBlock">')

        context_text = "Show more"
        context_link_length = len(context_text) + 3
        context_link = ' <span class="routineLink">[<a class="extraDataLink" href="#">{}</a>]</span>'.format(context_text)

        compare_url = get_compare_url(platform_key, stage_name, name_no_stage)
        context_url = references_library[name]["source_filename"]

        routine_extra_data_html = routine_extra_data(name, type, mentions, compare_url, "in context in the source code", context_url)

        while i < len(source) and analysing:
            line = source[i]

            if re_if_to_remove.search(line):
                # Remove IF _MATCH_ORIGINAL_BINARIES
                in_if_to_remove = True
                in_else_to_remove = False

            elif in_if_to_remove:
                # Remove contents of IF _MATCH_ORIGINAL_BINARIES
                if re_else_to_remove.search(line):
                    # Until we reach the ELSE
                    in_if_to_remove = False
                    in_else_to_remove = True
                    i += 1

            elif in_else_to_remove and re_endif_to_remove.search(line):
                # Remove ENDIF from IF _MATCH_ORIGINAL_BINARIES
                in_else_to_remove = False

            elif re_if_to_remove.search(line):
                in_if_to_remove = True

            elif re_empty_line.match(line):
                if i < len(source) - 1 and not re_comment.match(source[i + 1]) and not re_comment2.match(source[i + 1]):
                    page_file.write("\n")

            elif re_comment.match(line):
                if analysing_header:
                    page_file.write("</div></div>")
                analysing_header = False

                if analysing_body:
                    analysing = False
                elif i < len(source) - 1 and re_empty_line.match(source[i + 1]):
                    analysing_body = True

            elif re_comment2.match(line):
                page_file.write('<hr class="light" />')

            elif analysing and analysing_header:
                if routine_extra_data_html and re_empty_line_in_header.match(line) and i < len(source) - 1 and (re_comment.match(source[i + 1]) or re_comment2.match(source[i + 1])):
                    page_file.write(routine_extra_data_html)
                    routine_extra_data_html = ""
                page_file.write(tidy_source_header_line(line, context_link, context_link_length))

            elif analysing and analysing_body:
                page_file.write(tidy_code(line, stage, name, refs_only=False, statistics=True))
                if workspace_variable_extra_data_html and re_line_with_comment.search(line) and (i == len(source) - 1 or (i < len(source) - 1 and re_empty_line.match(source[i + 1]))):
                    extra_indent = ' ' * (line.find('\\') - html_workspace_reference_link.find('\\'))
                    page_file.write(html_workspace_reference_start.format(extra_indent) + workspace_variable_extra_data_html + html_workspace_reference_end)
                    workspace_variable_extra_data_html = ""

            i += 1

        add_source_code_stats(url_name, type, category, instruction_count, data_byte_count)

        page_file.write('</pre></div>')

        add_reference_popups(references, stage, page_file, name, False)

        output_next_prev(next_prev, page_file)
        end_code_html(page_file)
        i -= 1


def get_compare_url(platform_name, stage_name, routine_name):
    if platform_name == "elite-a" or args.platform == "c64" or args.platform == "apple" or args.platform == "nes" or args.platform == "aviator" or args.platform == "lander" or args.platform == "revs":
        return ""

    if platform_name == "disc":
        if stage_name == "docked" or stage_name == "flight":
            platform_name = stage_name
        elif "ship_blueprints_" in stage_name or stage_name == "text_tokens":
            platform_name = "flight"
        else:
            return ""
    routine_asm = "/" + make_url_name(routine_name) + ".asm"

    include = [i for i in includes_in_versions[platform_name] if routine_asm in i]

    if len(include) > 1:
        if stage_name == "docked" or stage_name == "flight":
            stage = "main"
        else:
            stage = re.sub(r'_\d+', '', stage_name)
        include = [i for i in include if stage in i]
        if len(include) > 1:
            print("\nERROR! Multiple files found for variable: {}".format(routine_asm))

    if len(include) > 0:
        if (stage_name == "docked" or stage_name == "flight" or "ship_blueprints_" in stage_name) and "/e_per_cent.asm" in include[0]:
            return ""
        elif not is_shared_routine(include[0]):
            return ""
        else:
            parts = include[0].split("/")
            return "compare/" + parts[2] + "/" + parts[3] + "/" + parts[4].replace(".asm", "") + ".html"

    re_routine1_asm = re.compile(r"/([^/]+\-" + make_url_name(routine_name) + r")\.asm")
    re_routine2_asm = re.compile(r"/(" + make_url_name(routine_name) + r"\-[^/]+)\.asm")

    for include in includes_in_versions[platform_name]:
        if is_shared_routine(include):
            m = re_routine1_asm.search(include)
            if m:
                parts = include.split("/")
                return "compare/" + parts[2] + "/" + parts[3] + "/" + m.group(1) + ".html"
            m = re_routine2_asm.search(include)
            if m:
                parts = include.split("/")
                return "compare/" + parts[2] + "/" + parts[3] + "/" + m.group(1) + ".html"

    return ""


def is_shared_routine(include):
    return '/advanced/' in include \
        or '/common/' in include \
        or '/enhanced/' in include \
        or '/original/' in include


def add_source_code_stats(url_name, type, category, instruction_count, data_byte_count):
    global source_code_stats
    # print("{} = {}".format(url_name, instruction_count))

    if url_name in source_code_stats["all"]:
        source_code_stats["all"][url_name]["instruction_count"] = instruction_count
        source_code_stats["all"][url_name]["data_byte_count"] = data_byte_count
    else:
        source_code_stats["all"][url_name] = {"instruction_count": instruction_count, "data_byte_count": data_byte_count}

    if category not in source_code_stats["categories"]:
        source_code_stats["categories"][category] = {"instruction_count": 0, "data_byte_count": 0, "subroutine_count": 0, "variable_count": 0, "workspace_count": 0, "macro_count": 0}

    if url_name.startswith("subroutine_"):
        source_code_stats["categories"][category]["instruction_count"] += instruction_count
        source_code_stats["categories"][category]["data_byte_count"] += data_byte_count
        source_code_stats["categories"][category]["subroutine_count"] += 1

    if url_name.startswith("variable_"):
        source_code_stats["categories"][category]["variable_count"] += 1
        source_code_stats["categories"][category]["data_byte_count"] += data_byte_count

    if url_name.startswith("workspace_"):
        source_code_stats["categories"][category]["workspace_count"] += 1
        source_code_stats["categories"][category]["data_byte_count"] += data_byte_count

    if url_name.startswith("macro_"):
        source_code_stats["categories"][category]["macro_count"] += 1


def add_mentions(references, stage, name):
    for ref in sorted(references):
        if args.platform in exported_routines and ref in exported_routines[args.platform]:
            ref = add_stage(ref, exported_routines[args.platform][ref])
        else:
            if args.platform == "nes":
                check_common = add_stage(ref, "Common")
                if check_common in references_library:
                    ref = check_common
                else:
                    check_bank_7 = add_stage(ref, "Bank 7")
                    if check_bank_7 in references_library:
                        ref = check_bank_7
                    else:
                        ref = add_stage(ref, stage)
            else:
                ref = add_stage(ref, stage)
        if ref != name:
            if ref not in mentions:
                mentions[ref] = []
            mentions[ref].append(name)
    if name not in mentions:
        mentions[name] = []


def add_reference_popups(references, stage, page_file, name, is_all_file):
    for ref in sorted(references):
        page_file.write('\n\t\t\t\t<div class="codeBlockWrapper popupWrapper" id="popup-{}"><div class="codeBlock"><div class="close">[X]</div><div class="content">'.format(make_id(ref)))

        ref_no_stage = ref
        ref = add_stage(ref, stage)

        if ("(Bank " in ref or "(Common)" in ref) and ref not in references_library:
            for i in range(0, 8):
                try_this_bank = ref_no_stage + " (Bank " + str(i) + ")"
                if try_this_bank in references_library:
                    ref = try_this_bank
                    break
            if ref_no_stage + " (Common)" in references_library:
                ref = ref_no_stage + " (Common)"

        if ref in references_library:
            ref_filename = ""
            ref_type = ""
            ref_category = ""
            ref_summary = ""
            ref_entry_point = ""
            parent_name = ""
            parent_name_no_stage = ""
            parent_type = "section"
            parent_filename = ""
            name_label = "Name"

            if (references_library[ref]["type"] == "Label" or references_library[ref]["type"] == "Subroutine") and "parent_name" in references_library[ref] and references_library[ref]["parent_name"].startswith(ref_no_stage + " (Part "):
                ref = references_library[ref]["parent_name"]

            # Fetch popup data
            if "filename" in references_library[ref]:
                ref_filename = references_library[ref]["filename"]

            if "name_no_stage" in references_library[ref]:
                ref_name_no_stage = references_library[ref]["name_no_stage"]
            else:
                ref_name_no_stage = ref

            if "type" in references_library[ref]:
                ref_type = references_library[ref]["type"]

            if "value" in references_library[ref]:
                ref_value = references_library[ref]["value"]

            if "category" in references_library[ref]:
                ref_category = references_library[ref]["category"]

            if "parent_name" in references_library[ref] and references_library[ref]["parent_name"] != ref:
                parent_name = references_library[ref]["parent_name"]
                if parent_name in references_library and 'type' in references_library[parent_name]:
                    parent_type = references_library[parent_name]['type'].lower()
                if parent_name in references_library and 'filename' in references_library[parent_name]:
                    parent_filename = references_library[parent_name]['filename']
                if "name_no_stage" in references_library[parent_name]:
                    parent_name_no_stage = references_library[parent_name]["name_no_stage"]
                else:
                    parent_name_no_stage = parent_name

            if "summary" in references_library[ref] and references_library[ref]["summary"]:
                ref_summary = references_library[ref]["summary"].lstrip().rstrip(":")
                ref_summary = add_deep_dive_link_with_quotes(ref_summary)

            if parent_name and "entry_point" in references_library[ref] and references_library[ref]["entry_point"]:
                ref_entry_point = references_library[parent_name]["summary"]
                ref_category = references_library[parent_name]["category"]

            # Fix links for large source code pages
            if is_all_file:
                if "source_filename" in references_library[ref]:
                    ref_filename = references_library[ref]["source_filename"]
                if parent_name in references_library and 'source_filename' in references_library[parent_name]:
                    parent_filename = references_library[parent_name]['source_filename']
                parent_filename_with_anchor = parent_filename.split('#')[0] + "#" + make_id_for_entry_point(ref_no_stage)
            else:
                parent_filename_with_anchor = parent_filename + "#" + make_id_for_entry_point(ref_no_stage)

            # Compose popup
            if ref_type:
                name_label = ref_type

            if ref_entry_point:
                page_file.write('<div class="name">{} <a href="/{}">{}</a> in {} <a href="/{}">{}</a>'.format(name_label,
                                parent_filename_with_anchor,
                                ref_name_no_stage,
                                parent_type,
                                parent_filename,
                                parent_name_no_stage)
                                )
            else:
                if ref_filename:
                    page_file.write('<div class="link">{} <a href="/{}">{}</a>'.format(name_label, ref_filename, ref_name_no_stage))
                    if parent_name:
                        if parent_filename:
                            page_file.write(' in {} <a href="/{}">{}</a>'.format(parent_type, parent_filename_with_anchor, parent_name_no_stage))
                        else:
                            page_file.write(' in {} {}'.format(parent_type, parent_name_no_stage))
                elif name_label == "Configuration variable":
                    if parent_name == name:
                        page_file.write('<div class="name">{} <a href="/{}">{}</a>'.format(name_label, parent_filename_with_anchor, ref_name_no_stage))
                        page_file.write(' is local to this routine')
                    elif parent_filename:
                        page_file.write('<div class="name">{} <a href="/{}">{}</a>'.format(name_label, parent_filename_with_anchor, ref_name_no_stage))
                        page_file.write(' in {} <a href="/{}">{}</a>'.format(parent_type, parent_filename, parent_name_no_stage))
                    else:
                        parent_filename_with_anchor = references_library[ref]["source_filename"]
                        page_file.write('<div class="name">{} <a href="/{}">{}</a>'.format(name_label, parent_filename_with_anchor, ref_name_no_stage))
                        page_file.write(' = {}'.format(ref_value))
                elif parent_name:
                    if parent_name == name:
                        page_file.write('<div class="name">{} <a href="/{}">{}</a>'.format(name_label, parent_filename_with_anchor, ref_name_no_stage))
                        page_file.write(' is local to this routine')
                    elif parent_filename:
                        page_file.write('<div class="name">{} <a href="/{}">{}</a>'.format(name_label, parent_filename_with_anchor, ref_name_no_stage))
                        page_file.write(' in {} <a href="/{}">{}</a>'.format(parent_type, parent_filename, parent_name_no_stage))
                    else:
                        page_file.write('<div class="name">{} {}'.format(name_label, ref_name_no_stage))
                        page_file.write(' in {} {}'.format(parent_type, parent_name_no_stage))
                else:
                    if ref_value:
                        page_file.write('<div class="name">{}: {} = {}'.format(name_label, ref_name_no_stage, ref_value))
                    else:
                        page_file.write('<div class="name">{}: {}'.format(name_label, ref_name_no_stage))

            if ref_category:
                page_file.write(' (category: {})'.format(ref_category))
            page_file.write('</div>')

            if ref_entry_point:
                # page_file.write('<div class="summary">{}: {}</div>'.format(parent_name, ref_entry_point))
                page_file.write('<div class="summary">{}</div>'.format(ref_summary))
            elif ref_summary:
                page_file.write('<div class="summary">{}</div>'.format(ref_summary))

        # else:
        #    page_file.write('<div class="name">Name {}</div>'.format(ref))

        page_file.write('</div></div></div>\n')


def build_large_source_code_page(source, name, type, category, summary, stage):
    global i, references, references_library, analysing_arguments, in_if_to_remove, in_else_to_remove, in_workspace, workspace_variable_extra_data_html

    print(".", end="", flush=True)

    in_workspace = (type == "Workspace")

    name_no_stage = name
    name = add_stage(name, stage)

    analysing = True
    analysing_body = False
    analysing_header = True
    analysing_arguments = False
    all_file.write('<div class="headerBlockWrapper"><div class="headerBlock">')
    all_file.write(html_anchor.format("header-" + make_id(name_no_stage)))

    context_text = "Show more"
    context_link_length = len(context_text) + 3
    context_link = ' <span class="routineLink">[<a class="extraDataLink" href="#">{}</a>]</span>'.format(context_text)

    stage_name = "main" if stage == "" else make_url_name(stage)
    compare_url = get_compare_url(platform_key, stage_name, name_no_stage)
    context_url = references_library[name]["filename"]

    routine_extra_data_html = routine_extra_data(name, type, mentions, compare_url, "on its own page", context_url)

    while i < len(source) and analysing:
        line = source[i]

        if re_if_to_remove.search(line):
            # Remove IF _MATCH_ORIGINAL_BINARIES
            in_if_to_remove = True
            in_else_to_remove = False

        elif in_if_to_remove:
            # Remove contents of IF _MATCH_ORIGINAL_BINARIES
            if re_else_to_remove.search(line):
                # Until we reach the ELSE
                in_if_to_remove = False
                in_else_to_remove = True
                i += 1

        elif in_else_to_remove and re_endif_to_remove.search(line):
            # Remove ENDIF from IF _MATCH_ORIGINAL_BINARIES
            in_else_to_remove = False

        elif re_if_to_remove.search(line):
            in_if_to_remove = True

        elif re_empty_line.match(line):
            if i < len(source) - 1 and not re_comment2.match(source[i + 1]):
                all_file.write("\n")

        elif re_comment.match(line):
            if analysing_header:
                all_file.write("</div></div>")
            analysing_header = False

            if analysing_body:
                analysing = False
                i -= 1
            elif i < len(source) - 1 and re_empty_line.match(source[i + 1]):
                analysing_body = True

        elif re_comment2.match(line):
            all_file.write('<hr class="light"/>')

        elif analysing and analysing_header:
            if routine_extra_data_html and re_empty_line_in_header.match(line) and i < len(source) - 1 and (re_comment.match(source[i + 1]) or re_comment2.match(source[i + 1])):
                all_file.write(routine_extra_data_html)
                routine_extra_data_html = ""
            all_file.write(tidy_source_header_line(line, context_link, context_link_length))

        elif analysing and analysing_body:
            all_file.write(tidy_code(line, stage, name, refs_only=False, statistics=True))
            if workspace_variable_extra_data_html and re_line_with_comment.search(line) and (i == len(source) - 1 or (i < len(source) - 1 and re_empty_line.match(source[i + 1]))):
                extra_indent = ' ' * (line.find('\\') - html_workspace_reference_link.find('\\'))
                all_file.write(html_workspace_reference_start.format(extra_indent) + workspace_variable_extra_data_html + html_workspace_reference_end)
                workspace_variable_extra_data_html = ""

        elif analysing_header or analysing_body:
            all_file.write(line)

        i += 1

    i -= 1


def fetch_next_prev(name, array, type):
    prev = None
    next = None
    for i in range(len(array)):
        if array[i]["name"] == name and array[i]["type"] == type:
            if i > 0:
                prev = array[i - 1]
            if i < len(array) - 1:
                next = array[i + 1]
            break
    return {"next": next, "prev": prev}


def add_category(category):
    section = make_url_name(category)
    if section not in categories:
        categories[section] = category
    return section


def add_stage_folder(stage, type):
    if stage == "":
        stage = "main"
    section = make_url_name(stage)
    subsection = make_url_name(type)
    create_folder(content_folder + section)
    create_folder(content_folder + section + "/" + subsection)
    return section


def sort_reference_names(k):
    key_fixed = k.lower()
    key_fixed = re.sub(r"part (.)a of", r"part 0\1_ of", key_fixed)
    key_fixed = re.sub(r"part (.) of", r"part 0\1 of", key_fixed)
    key_fixed = re.sub(r"dashdata(\d)$", r"dashdata0\1", key_fixed)
    key_fixed = re.sub(r"token(\d)$", r"token0\1", key_fixed)
    return key_fixed


def sort_nav_items(k):
    key_fixed = k["name"].lower()
    key_fixed = re.sub(r"part (.)a of", r"part 0\1_ of", key_fixed)
    key_fixed = re.sub(r"part (.) of", r"part 0\1 of", key_fixed)
    key_fixed = re.sub(r"dashdata(\d)$", r"dashdata0\1", key_fixed)
    key_fixed = re.sub(r"token(\d)$", r"token0\1", key_fixed)
    return key_fixed


def output_menus(file):
    firstPass = True

    file.write(html_indexes.format(explore_folder, content_folder, platform_name_capitalised, platform_id))

    for category in sorted(categories.keys()):
        print(".", end="", flush=True)
        if not firstPass:
            file.write(menu_item_close)
        firstPass = False
        category_name = categories[category]
        file.write(menu_item_open.format(platform_id, category, category_name, category_summary[category_name], platform_id, category, "Index for " + category_name, platform_id, category, category, category_name))

        if category in subroutines:
            file.write('\t\t\t\t\t\t\t<li class="menuItemHeader">Subroutines</li>\n')
            articles = sorted(subroutines[category], key=sort_nav_items)
            for article in articles:
                important = " *" if remove_stage(article["name"]) in important_routines else ""
                if article["stage"]:
                    stage_id = "_" + make_id(article["stage"])
                else:
                    stage_id = ""
                file.write(html_menu.format(platform_id, category, stage_id, article["url_name"], article["filename"], article["name"] + important, article["summary"]))

        if category in workspaces:
            file.write('\t\t\t\t\t\t\t<li class="menuItemHeader">Workspaces</li>\n')
            articles = sorted(workspaces[category], key=sort_nav_items)
            for article in articles:
                important = " *" if remove_stage(article["name"]) in important_routines else ""
                if article["stage"]:
                    stage_id = "_" + make_id(article["stage"])
                else:
                    stage_id = ""
                file.write(html_menu.format(platform_id, category, stage_id, article["url_name"], article["filename"], article["name"] + important, article["summary"]))

        if category in variables:
            file.write('\t\t\t\t\t\t\t<li class="menuItemHeader">Variables</li>\n')
            articles = sorted(variables[category], key=sort_nav_items)
            for article in articles:
                important = " *" if remove_stage(article["name"]) in important_routines else ""
                if article["stage"]:
                    stage_id = "_" + make_id(article["stage"])
                else:
                    stage_id = ""
                file.write(html_menu.format(platform_id, category, stage_id, article["url_name"], article["filename"], article["name"] + important, article["summary"]))

        if category in macros:
            file.write('\t\t\t\t\t\t\t<li class="menuItemHeader">Macros</li>\n')
            articles = sorted(macros[category], key=sort_nav_items)
            for article in articles:
                important = " *" if remove_stage(article["name"]) in important_routines else ""
                if article["stage"]:
                    stage_id = "_" + make_id(article["stage"])
                else:
                    stage_id = ""
                file.write(html_menu.format(platform_id, category, stage_id, article["url_name"], article["filename"], article["name"] + important, article["summary"]))

    file.write(menu_item_close)


def output_indexes(file, array, intro, section, url_name, seo_title, title, description, add_index):
    start_html(file, section, url_name, seo_title, title, description)

    next_prev = next_prev_indexes[url_name]
    output_next_prev(next_prev, file)

    file.write('<div class="codeBlockWrapper"><div class="codeBlock article">')
    file.write(intro)

    if add_index:
        previous_category = ""
        file.write(html_az_index_start)
        for category in sorted(array):
            if previous_category != categories[category]:
                previous_category = categories[category]
                file.write(html_az_index_link.format(make_id(previous_category), previous_category))
        file.write(html_az_index_end)

    file.write('<table class="spacedTableBorder codeSummary crossReferences">')
    file.write('<tbody>')

    previous_category = ""
    for category in sorted(array):
        if previous_category != categories[category]:
            previous_category = categories[category]
            underline = "-" * len(previous_category)
            file.write('<tr class="blank"><td colspan="2">{}{}</td></tr>'.format(
                html_anchor.format(make_id(previous_category)),
                html_summary_heading.format(previous_category, underline)
            ))

        articles = sorted(array[category], key=sort_nav_items)

        for article in articles:
            file.write('<tr><td><a href="/{}">{}</a></td><td>{}</td></tr>'.format(
                article["filename"],
                article["name"],
                article["summary"]
            ))

    file.write("</table>")
    file.write('</div></div>')
    next_prev = next_prev_indexes[url_name]
    output_next_prev(next_prev, file)
    end_html(file)


def output_a_z_index(file, subroutines, variables, macros, workspaces, intro, section, url_name, seo_title, title, description):
    start_html(file, section, url_name, seo_title, title, description)
    all_items = []
    previous_letter = "a"

    next_prev = next_prev_indexes["a-z"]
    output_next_prev(next_prev, file)

    file.write('<div class="codeBlockWrapper"><div class="codeBlock article">')
    file.write(intro)
    file.write('<table class="spacedTableBorder codeSummary crossReferences">')
    file.write('<tr class="blank"><td colspan="3">{}</td></tr>'.format(html_anchor.format(previous_letter)))
    file.write('<tbody><tr class="codeSummaryHeader"><th>Name</th><th>Category</th><th>Description</th></tr>')

    for category in subroutines:
        articles = subroutines[category]
        for article in articles:
            all_items.append(article)

    for category in variables:
        articles = variables[category]
        for article in articles:
            all_items.append(article)

    for category in macros:
        articles = macros[category]
        for article in articles:
            all_items.append(article)

    for category in workspaces:
        articles = workspaces[category]
        for article in articles:
            all_items.append(article)

    all_items_sorted = sorted(all_items, key=sort_nav_items)

    for article in all_items_sorted:
        letter = article["name"][:1].lower()
        if previous_letter != letter:
            previous_letter = letter
            file.write('<tr class="blank"><td colspan="3">{}</td></tr>'.format(html_anchor.format(previous_letter)))

        if "category" in article:
            category = article["category"]
        else:
            category = "Workspace variable"

        file.write('<tr><td><a href="/{}">{}</a></td><td class="codeSummaryCategory">{}</td><td>{}</td></tr>'.format(
            article["filename"],
            article["name"],
            category,
            article["summary"]
        ))
    file.write("</table>")
    file.write('</div></div>')
    next_prev = next_prev_indexes["a-z"]
    output_next_prev(next_prev, file)
    end_html(file)


def find_reference_with_stage(name):
    for key in references_library.keys():
        if remove_stage(key) == name:
            return references_library[key]
    return None


def add_workspace_variables_to_indexes():
    for ref, value in references_library.items():
        if "type" in value and value["type"] == "Variable" and "parent_name" in value and value["parent_name"] != ref:
            parent_name = value["parent_name"]
            if parent_name in references_library:
                parent = references_library[parent_name]
                if "type" in parent and parent["type"] == "Workspace":
                    ref_no_stage = ref
                    if "name_no_stage" in references_library[ref]:
                        ref_no_stage = references_library[ref]["name_no_stage"]
                    workspace_variables.append({"filename": parent["filename"] + "#" + make_id(ref_no_stage), "name": ref, "summary": value["summary"]})

    categories["workspace_variables"] = "Workspace variables"
    variables["workspace_variables"] = workspace_variables


def add_entry_points_to_indexes():
    global subroutines, entry_points
    for category in entry_points:
        for entry_point in entry_points[category]:
            if category in subroutines:
                subroutines[category].append(entry_point)
            else:
                subroutines[category] = [entry_point]


def analyse_files_for_compare():
    global compare_source_folder, compare_do_not_expand_all_includes, compare_this_version, compare_version_key, tag_categories

    for site in sites_to_compare:
        compare_source_folder = site["source_folder"]
        compare_do_not_expand_all_includes = site["do_not_expand_all_includes"]
        compare_this_version = site["this_version"]
        compare_version_key = site["version_key"]
        # print("Processing version: {}".format(compare_this_version))

        for source_file in site["source_files"]:
            input = compare_source_folder + site["section_folder"] + source_file
            # print("Reading file: {}".format(input))

            with open(input, "r") as input_file:
                print(".", end="", flush=True)
                # print("Reading file: {}".format(site["dest_folder"] + source_file))
                process_compare_file(input_file.readlines(), site["section_folder"] + source_file, "", "")

    for include in all_includes:
        if all_includes[include]["multi_version"]:
            for tag_count in all_includes[include]["tag_count"]:
                tag_categories.add(tag_count)


def add_compare_include(include, version, source_file, include_file, workspace):
    global includes_in_versions, all_includes
    multi_version = file_contains_version_ifs(include_file)

    if multi_version:
        version_key = version.lower().replace("disc_", "")
        if version_key in includes_in_versions:
            if include not in includes_in_versions[version_key]:
                includes_in_versions[version_key].append(include)
        else:
            includes_in_versions[version_key] = [include]

    if include in all_includes:
        if version not in all_includes[include]["versions"]:
            all_includes[include]["versions"].append(version)
            if workspace:
                all_includes[include]["workspace"][version] = extract_workspace(workspace)
        if version not in all_includes[include]["stage_by_version"]:
            all_includes[include]["stage_by_version"][version] = extract_stage(source_file)
        if source_file not in all_includes[include]["included_in"]:
            all_includes[include]["included_in"].append(source_file)
    else:
        names = include.split("/")
        filename = names[4].replace(".asm", "")
        all_includes[include] = {
            "versions": [version],
            "included_in": [source_file],
            "multi_version": multi_version,
            "name": fetch_proper_name(include_file, filename),
            "category": fetch_category(include_file),
            "summary": fetch_summary(include_file),
            "filename": filename,
            "family": names[1],
            "stage": names[2],
            "stage_by_version": {},
            "type": names[3] if names[3] != 'copyblock' else 'subroutine',
            "workspace": {},
            "tag_count": {},
            "tag_comments": {},
            "tags_counted": False
        }
        if workspace:
            all_includes[include]["workspace"][version] = extract_workspace(workspace)
        all_includes[include]["stage_by_version"][version] = extract_stage(source_file)


def count_tag(include, tag, comment):
    if tag in all_includes[include]["tag_count"]:
        all_includes[include]["tag_count"][tag] += 1
    else:
        all_includes[include]["tag_count"][tag] = 1
    if comment and not re_compare_group_link.match(comment):
        m = re_compare_group.match(comment)
        if m:
            comment = m.group(2)
        if tag in all_includes[include]["tag_comments"]:
            all_includes[include]["tag_comments"][tag].append(comment)
        else:
            all_includes[include]["tag_comments"][tag] = [comment]


def extract_workspace(filename):
    if "io_variables.asm" in filename:
        return "i_o_variables"
    return filename.split("/")[-1].replace(".asm", "")


def extract_stage(filename):
    if "elite-source-docked.asm" in filename:
        return "docked"
    elif "elite-source-flight.asm" in filename:
        return "flight"
    elif "elite-z.asm" in filename:
        return "i_o_processor"
    elif "elite-loader.asm" in filename:
        return "loader"
    elif "elite-loader1.asm" in filename:
        return "loader_1"
    elif "elite-loader2.asm" in filename:
        return "loader_2"
    elif "elite-loader3.asm" in filename:
        return "loader_3"
    elif "elite-loader-sideways-ram.asm" in filename:
        return "loader_sideways_ram"
    elif "elite-text-tokens.asm" in filename:
        return "text_tokens"
    elif "elite-bcfs.asm" in filename:
        return "big_code_file"
    elif "elite-data.asm" in filename:
        return "game_data"
    elif "elite-missile.asm" in filename:
        return "missile_ship_blueprint"
    m = re.search(r"elite-ships-([a-z])\.asm", filename)
    if m:
        return "ship_blueprints_" + m.group(1)
    return "main"


def process_compare_file(input_file, source_file, include, workspace):
    input_file = strip_elite_a(input_file)
    if_stack = []
    include_this = True
    for line in input_file:
        m = re_version_if.search(line)
        if m:
            # Version IF or ELIF statement
            include_this = False
            for version in compare_this_version:
                if version in line:
                    include_this = True
            # Version IF statement, type 0 on stack
            if line.startswith("IF "):
                if_stack.append(0)
            if include != "" and not all_includes[include]["tags_counted"]:
                m = re_line_with_comment.search(line)
                if m and m.group(3) != "":
                    if ": " in m.group(3):
                        split_tag = m.group(3).split(": ", 1)
                        tag = split_tag[0].strip()
                        comment = split_tag[1].strip()
                        count_tag(include, tag, comment)
                    else:
                        count_tag(include, m.group(3).strip(), "")
        elif line.startswith("IF "):
            # Other IF statement, type 1 on stack
            if_stack.append(1)
            if include_this:
                process_compare_line(input_file, line, source_file, workspace)
        elif re_version_endif.match(line):
            # ENDIF statement
            if_type = if_stack.pop()
            if include_this and if_type == 1:
                process_compare_line(input_file, line, source_file, workspace)
            if if_type == 0:
                include_this = True
        elif include_this:
            process_compare_line(input_file, line, source_file, workspace)
    if include != "":
        all_includes[include]["tags_counted"] = True


def file_contains_version_ifs(input_file):
    input_lines = input_file.readlines()
    input_lines = strip_elite_a(input_lines)
    contains_ifs = 0
    for line in input_lines:
        m = re_version_if.match(line)
        if m:
            # Version IF or ELIF statement
            contains_ifs += 1
    input_file.seek(0)
    return contains_ifs


def fetch_proper_name(input_file, filename):
    if "-" in filename:
        all_names = ""
        for name in filename.split("-"):
            if all_names != "":
                all_names = all_names + " / "
            all_names = all_names + fetch_proper_name(input_file, name)
        return all_names
    else:
        for line in input_file:
            m = re_name.search(line)
            if m and make_url_name(m.group(2)) == filename:
                input_file.seek(0)
                return m.group(2)

        input_file.seek(0)
        for line in input_file:
            m = re.search(r"^\s*\.([^ \n]+)", line)
            if m and make_url_name(m.group(1)) == filename:
                input_file.seek(0)
                return m.group(1)

    input_file.seek(0)
    return filename


def fetch_category(input_file):
    for line in input_file:
        m = re_category.search(line)
        if m:
            input_file.seek(0)
            add_category(m.group(2))
            return m.group(2)

    input_file.seek(0)
    return ""


def fetch_summary(input_file):
    summary = ""
    in_summary = False
    for line in input_file:
        if in_summary:
            m = re_summary2.search(line)
            if m:
                summary += " " + m.group(1)
            else:
                in_summary = False
                break
        else:
            m = re_summary.search(line)
            if m:
                in_summary = True
                summary += m.group(2)

    input_file.seek(0)
    return summary


def process_compare_line(input_file, line, source_file, workspace):
    m = re_include_directive.match(line)
    if m and include_is_allowed_in_compare(line):
        include = m.group(1)
        if path_leaf(include) not in compare_do_not_expand_all_includes:
            # print("Including file: {}".format(include))
            with open(compare_source_folder + include, "r") as include_file:
                add_compare_include(include, compare_version_key, source_file, include_file, workspace)
                if "/workspace/" in include:
                    process_compare_file(include_file.readlines(), source_file, include, include)
                else:
                    process_compare_file(include_file.readlines(), source_file, include, "")


def include_is_allowed_in_compare(line):
    for i in omit_includes_from_compare:
        if i in line:
            return False
    return True


def output_compare_version_page(source, page_file, include, filename, name, category):
    global analysing_arguments, in_if_to_remove, in_else_to_remove, add_popup_links_to_code, compare_buffer, most_recent_compare_line, multi_versions_buffer_is_header, current_if_block_anchor

    source = strip_elite_a(source)

    start_code_html(page_file, make_url_name(category), filename, "Version analysis of " + name, "Version analysis of " + name, "Version analysis of " + name, "")

    versions_to_show = all_includes[include]["versions"]

    if len(versions_to_show) > 1:
        plural = "s"
    else:
        plural = ""
    version_routine_links = get_links_for_compared_versions(include, versions_to_show, name)
    page_file.write(html_compare_intro.format(plural, convert_versions_to_link_list(version_routine_links)))

    if_stack = []
    inside_version_if = False
    compare_buffer = ""
    most_recent_compare_line = ""
    multi_versions_buffer = {}
    multi_versions_buffer_is_header = False
    compare_groups = {}
    current_if_block = ""
    current_if_comment = ""
    current_if_block_anchor = {}
    current_if_block_number = 0
    total_if_block_count = all_includes[include]["multi_version"]

    analysing = True
    analysing_body = True
    analysing_arguments = False
    add_popup_links_to_code = False

    if re_comment.match(source[0]):
        analysing_header = True
        analysing_body = False
        i = 2
        page_file.write('<div class="codeBlockWrapper compare"><pre class="codeBlock sourceCode initial">')
        page_file.write('<div class="headerBlockWrapper"><div class="headerBlock">')
    else:
        analysing_header = False
        i = 0
        page_file.write('<div class="codeBlockWrapper compare"><pre class="codeBlock sourceCode">')

    while i < len(source) and analysing:
        line = source[i]

        m = re_version_if.search(line)

        if re_if_to_remove.search(line):
            # Remove IF _MATCH_ORIGINAL_BINARIES
            in_if_to_remove = True
            in_else_to_remove = False

        elif in_if_to_remove:
            # Remove contents of IF _MATCH_ORIGINAL_BINARIES
            if re_else_to_remove.search(line):
                # Until we reach the ELSE
                in_if_to_remove = False
                in_else_to_remove = True
                i += 1

        elif in_else_to_remove and re_endif_to_remove.search(line):
            # Remove ENDIF from IF _MATCH_ORIGINAL_BINARIES
            in_else_to_remove = False

        elif re_if_to_remove.search(line):
            in_if_to_remove = True

        elif m:
            # Version IF or ELIF statement
            inside_version_if = True
            current_if_block = ""
            line_no_comment = line.split(comment_delimiter, 1)[0]
            for version_to_show in versions_to_show:
                if version_to_show in line_no_comment or ((version_to_show == "DISC_FLIGHT" or version_to_show == "DISC_DOCKED") and "DISC_VERSION" in line_no_comment):
                    current_if_block = current_if_block + " " + version_to_show
            # Version IF statement, type 0 on stack
            if line.startswith("IF "):
                if_stack.append(0)
                current_if_tags = ""
                current_if_comment = ""
                current_if_block_number += 1
            m = re_line_with_comment.search(line)
            if m and m.group(3) != "":
                if current_if_tags != "":
                    current_if_tags += ", "
                if ": " in m.group(3):
                    split_tag = m.group(3).split(": ", 1)
                    current_if_tags += split_tag[0].strip()
                    if line.startswith("IF "):
                        current_if_comment = split_tag[1].strip()
                else:
                    current_if_tags += m.group(3).strip()

        elif line.startswith("IF "):
            # Other IF statement, type 1 on stack
            if_stack.append(1)
            output_compare_line(inside_version_if, input_file, page_file, line, multi_versions_buffer, current_if_block, analysing, analysing_header, analysing_body, all_includes[include]["type"])

        elif re_version_endif.match(line):
            # ENDIF statement
            if_type = if_stack.pop()
            if if_type == 1:
                output_compare_line(inside_version_if, input_file, page_file, line, multi_versions_buffer, current_if_block, analysing, analysing_header, analysing_body, all_includes[include]["type"])
            if if_type == 0:
                inside_version_if = False
                output_multi_version_section(multi_versions_buffer, page_file, analysing_header, current_if_tags, current_if_comment, versions_to_show, current_if_block_number, total_if_block_count, compare_groups, filename, version_routine_links)
                multi_versions_buffer = {}
                multi_versions_buffer_is_header = False

        elif re_comment.match(line):
            if analysing_header:
                output_buffered_compare_line(page_file)
                page_file.write("</div></div>")
                analysing_header = False
            elif i < len(source) - 1 and re_header_comment.match(source[i + 1]):
                analysing_header = True
                output_buffered_compare_line(page_file)
                page_file.write('<div class="headerBlockWrapper"><div class="headerBlock">')

            if analysing_body:
                pass
            elif i < len(source) - 1 and re_empty_line.match(source[i + 1]):
                analysing_body = True

        elif re_comment2.match(line):
            output_buffered_compare_line(page_file)
            page_file.write('<hr class="light" />')

        else:
            output_compare_line(inside_version_if, input_file, page_file, line, multi_versions_buffer, current_if_block, analysing, analysing_header, analysing_body, all_includes[include]["type"])

        i += 1

    page_file.write('</div></div>')
    end_code_html(page_file)


def output_buffered_compare_line(page_file):
    global compare_buffer
    page_file.write(compare_buffer)
    compare_buffer = ""


def output_compare_line(inside_version_if, input_file, page_file, line, multi_versions_buffer, current_if_block, analysing, analysing_header, analysing_body, source_file_type):
    global compare_buffer, most_recent_compare_line

    if analysing and analysing_header:
        line = tidy_source_header_line(line, "", 0)
    elif analysing and analysing_body:
        if source_file_type == "workspace":
            line = replace_workspace_include_with_variable(line)
        line = tidy_code(line, "", "", refs_only=False, statistics=False)

    if inside_version_if:
        append_multi_version_compare_line(multi_versions_buffer, current_if_block, line, analysing_header)
    else:
        if compare_buffer != "":
            if line.strip() == "":
                compare_buffer += line
                most_recent_compare_line = ""
            else:
                output_buffered_compare_line(page_file)
                page_file.write(line)
                most_recent_compare_line = line.strip()
        else:
            page_file.write(line)
            most_recent_compare_line = line.strip()


def replace_workspace_include_with_variable(line):
    m = re_include_directive.match(line)
    if m:
        include = m.group(1)
        line = " ." + all_includes[include]["name"]
    return line


def append_multi_version_compare_line(multi_versions_buffer, version, line, analysing_header):
    global multi_versions_buffer_is_header
    if len(multi_versions_buffer) == 0:
        multi_versions_buffer_is_header = analysing_header
    if version in multi_versions_buffer:
        multi_versions_buffer[version].append(line)
    elif version:
        multi_versions_buffer[version] = [line]


def output_multi_version_section(multi_versions_buffer, page_file, analysing_header, tags, tag_comment, versions_to_show, block_number, total_number, compare_groups, filename, version_routine_links):
    global compare_buffer, multi_versions_buffer_is_header, current_if_block_anchor, most_recent_compare_line

    if not tags:
        print("\nERROR! Missing tag comment: {}".format(filename))

    if compare_buffer == "":
        if most_recent_compare_line != "":
            page_file.write('\n')
        if analysing_header:
            page_file.write('</div></div>')
        page_file.write('</pre>')

    most_recent_compare_line = ""

    versions_covered = []
    for v1 in multi_versions_buffer:
        for v2 in v1.split(" "):
            if v2:
                versions_covered.append(v2)

    versions_not_covered = []
    for version in versions_to_show:
        if version not in versions_covered:
            versions_not_covered.append(version)

    tag_anchor_index = make_id(tags)
    tag_anchor = ""
    tag_anchor_id = ""
    n = re_compare_group_link.match(tag_comment)
    if not n:
        if tag_anchor_index in current_if_block_anchor:
            current_if_block_anchor[tag_anchor_index] += 1
        else:
            current_if_block_anchor[tag_anchor_index] = 1
        tag_anchor_id = "compare-" + tag_anchor_index + "-" + str(current_if_block_anchor[tag_anchor_index])
        tag_anchor = html_anchor.format(tag_anchor_id)

    page_file.write('<div class="codeCompareBlock">')

    page_file.write('<div class="codeBlock sourceCode compareIntro">')
    page_file.write('<p class="key">')
    if tag_anchor:
        page_file.write(tag_anchor)
    if tags:
        tag_list = tag_name[tags]
    else:
        tag_list = ""
    page_file.write('Code variation {} of {}'.format(block_number, total_number) + '<span class="tags">' + tag_list + '</span></p>')

    m = re_compare_group.match(tag_comment)
    n = re_compare_group_link.match(tag_comment)
    if m:
        letter = m.group(1)
        comment = m.group(2)
        page_file.write('<p>' + add_full_stop(comment) + '</p>')
        page_file.write('<p>See below for more variations related to this code.</p>')
        if tag_anchor_id:
            compare_groups[letter] = '<p>See <a href="#{}">variation {}</a> above for details.</p>'.format(tag_anchor_id, block_number)
        else:
            compare_groups[letter] = '<p>See variation {} above for details.</p>'.format(block_number)
    elif n:
        letter = n.group(1)
        if letter in compare_groups:
            page_file.write('<p>' + compare_groups[letter] + '</p>')
        else:
            print("\nERROR! Missing group entry for letter '{}' in {}\n".format(letter, filename))
    elif tag_comment:
        page_file.write('<p>' + add_full_stop(tag_comment) + '</p>')

    if versions_not_covered:
        if len(versions_not_covered) > 1:
            plural = "s"
        else:
            plural = ""
        page_file.write('<p>This variation is blank in the {} version{}.</p>'.format(convert_versions_to_list(versions_not_covered), plural))
    if len(multi_versions_buffer) > 1:
        page_file.write(html_compare_intro_tap_instructions)
    page_file.write('</div>')

    if analysing_header or multi_versions_buffer_is_header:
        page_file.write('<pre class="codeBlock sourceCode initial compare compareHeader">')
    else:
        page_file.write('<pre class="codeBlock sourceCode initial compare">')

    if len(multi_versions_buffer) > 1:
        expandClass = ' expand'
    else:
        expandClass = ''

    tagList = ''
    # if tags:
    #     tagList = '<span class="tags">[' + tags + ']</span>'

    page_file.write('<div class="row headerRow' + expandClass + '">')

    # Order as follows: Cassette, Disc, Docked, Flight, Master, 6502SP, Electron
    for version in sorted(multi_versions_buffer, key=lambda k: " ".join(sorted(k.lower().replace("6502sp", "sp").replace("electron", "xelectron").split()))):
        page_file.write('<div class="cell headerCell">')
        page_file.write('<p class="key"><span class="legend">' + add_links_to_compared_routines(version, version_routine_links) + '</span>' + tagList + '</p>')
        page_file.write('</div>')
    page_file.write('</div>')

    page_file.write('<div class="row contentRow' + expandClass + '">')

    # Order as follows: Cassette, Disc, Docked, Flight, Master, 6502SP, Electron
    for version in sorted(multi_versions_buffer, key=lambda k: " ".join(sorted(k.lower().replace("6502sp", "sp").replace("electron", "xelectron").split()))):
        page_file.write('<div class="cell contentCell">')
        page_file.write('<div class="cellContents">')
        for line in strip_blank_lines(multi_versions_buffer[version]):
            page_file.write(line)
        page_file.write('</div></div>')
    page_file.write('</div></pre>')

    page_file.write('</div>')

    if analysing_header:
        compare_buffer = ('<pre class="codeBlock sourceCode initial"><div class="headerBlockWrapper"><div class="headerBlock">')
    else:
        compare_buffer = ('<pre class="codeBlock sourceCode">')


def strip_blank_lines(lines):
    return rstrip_blank_lines(lstrip_blank_lines(lines))


def lstrip_blank_lines(lines):
    if lines and re_empty_line.match(lines[0]):
        lines = lstrip_blank_lines(lines[1:])
    return lines


def rstrip_blank_lines(lines):
    if lines and re_empty_line.match(lines[-1]):
        lines = rstrip_blank_lines(lines[:-1])
    return lines


def add_links_to_compared_routines(version, version_routine_links):
    versions = version.split(" ")
    result = ""
    for version in versions:
        urls = [v["url"] for v in version_routine_links if v["version"] == version]
        if result != "":
            result += ", "
        if len(urls) > 0:
            url = urls[0]
            result += '<a href="{}">{}</a>'.format(url, convert_version_to_short_name(version))
        else:
            result += convert_version_to_short_name(version)
    return result


def convert_version_to_short_name(version):
    return version.strip()\
                  .replace("CASSETTE", "Cassette")\
                  .replace("DISC_FLIGHT", "Flight")\
                  .replace("DISC_DOCKED", "Docked")\
                  .replace("DISC_VERSION", "Disc")\
                  .replace("6502SP", "6502SP")\
                  .replace("MASTER", "Master")\
                  .replace("ELECTRON", "Electron")


def convert_version_to_full_name_comma_list(version):
    return version.strip()\
                  .replace(" ", ", ")\
                  .replace("CASSETTE", "Cassette")\
                  .replace("DISC_FLIGHT", "Disc (flight)")\
                  .replace("DISC_DOCKED", "Disc (docked)")\
                  .replace("DISC_VERSION", "Disc")\
                  .replace("6502SP", "6502 Second Processor")\
                  .replace("MASTER", "Master")\
                  .replace("ELECTRON", "Electron")


def get_links_for_compared_versions(include, versions, name):
    all_versions = []
    urls = get_url_for_code_page(include)
    for version in versions:
        if version in urls:
            link_details = {}
            link_details["version"] = version
            link_details["version_name"] = convert_version_to_full_name_comma_list(version)
            link_details["url"] = urls[version]
            all_versions.append(link_details)
    return all_versions


def convert_versions_to_link_list(all_versions):
    result = ""
    for version in all_versions:
        if result != "":
            if version == all_versions[-1]:
                result += " and "
            else:
                result += ", "
        result += '<a href="{}">{}</a>'.format(version["url"], version["version_name"])
    return result


def convert_versions_to_list(versions):
    result = ""
    for version in versions:
        version_name = convert_version_to_full_name_comma_list(version)
        if result != "":
            if version == versions[-1]:
                result += " and "
            else:
                result += ", "
        result += version_name
    return result


def output_compare_menu(file):
    firstPass = True

    routines = {}
    subroutines = set()
    variables = set()
    workspaces = set()
    for include in all_includes:
        if len(all_includes[include]["versions"]) > 1 and all_includes[include]["multi_version"]:
            url = content_folder + all_includes[include]["stage"] + "/" + all_includes[include]["type"] + "/" + all_includes[include]["filename"] + ".html"
            add_compare_article(routines, all_includes[include]["category"], url, all_includes[include]["filename"], all_includes[include]["name"], all_includes[include]["summary"], all_includes[include]["type"])
            if all_includes[include]["type"] == "subroutine":
                subroutines.add(all_includes[include]["category"])
            if all_includes[include]["type"] == "variable":
                variables.add(all_includes[include]["category"])
            if all_includes[include]["type"] == "workspace":
                workspaces.add(all_includes[include]["category"])

    file.write(html_compare_indexes)

    for category in tag_categories_with_comments:
        if category == tag_categories_with_comments[-1]:
            file.write(html_compare_category_index_subheader)
        file.write(html_compare_category_index.format(tag_title[category], category.lower(), tag_summary[category]))

    file.write(html_compare_indexes2)

    for category in sorted(categories.keys()):
        print(".", end="", flush=True)
        category_name = categories[category]
        if category_name in routines:
            if not firstPass:
                file.write(menu_item_close)
            firstPass = False
            file.write(menu_item_open.format(platform_id, category, category_name, category_summary[category_name], platform_id, category, "Index for " + category_name, platform_id, category, category, category_name))

            if category_name in subroutines:
                file.write('\t\t\t\t\t\t\t<li class="menuItemHeader">Subroutines</li>\n')
                articles = sorted(routines[category_name], key=lambda k: re.sub("part (.) of", "part 0$1 of", k["name"].lower()))
                for article in articles:
                    if article["type"] == "subroutine":
                        file.write(html_menu.format(platform_id, category, "", article["filename"], article["url"], article["name"], article["summary"]))

            if category_name in variables:
                file.write('\t\t\t\t\t\t\t<li class="menuItemHeader">Variables</li>\n')
                articles = sorted(routines[category_name], key=lambda k: re.sub("part (.) of", "part 0$1 of", k["name"].lower()))
                for article in articles:
                    if article["type"] == "variable":
                        file.write(html_menu.format(platform_id, category, "", article["filename"], article["url"], article["name"], article["summary"]))

            if category_name in workspaces:
                file.write('\t\t\t\t\t\t\t<li class="menuItemHeader">Workspaces</li>\n')
                articles = sorted(routines[category_name], key=lambda k: re.sub("part (.) of", "part 0$1 of", k["name"].lower()))
                for article in articles:
                    if article["type"] == "workspace":
                        file.write(html_menu.format(platform_id, category, "", article["filename"], article["url"], article["name"], article["summary"]))

    file.write(menu_item_close)


def add_compare_article(array, category, url, filename, name, summary, type):
    if category in array:
        array[category].append({"url": url, "filename": filename, "name": name, "summary": summary, "type": type})
    else:
        array[category] = [{"url": url, "filename": filename, "name": name, "summary": summary, "type": type}]


def output_compares_indexes(multi_varies_page_file, multi_same_page_file, mono_page_file):
    start_html(multi_varies_page_file, "indexes", "shared_code_with_variations", "All shared code that contains variations", "All shared code that contains variations", "All shared code in BBC Micro Elite that contains variations between different versions")
    output_next_prev(next_prev_compare_indexes["shared_code_with_variations"], multi_varies_page_file)
    multi_varies_page_file.write(html_multi_varies_intro)

    start_html(multi_same_page_file, "indexes", "shared_code_no_variations", "All shared code that contains no variations", "All shared code that contains no variations", "All shared code in BBC Micro Elite that contains no variations between different versions")
    output_next_prev(next_prev_compare_indexes["shared_code_no_variations"], multi_same_page_file)
    multi_same_page_file.write(html_multi_same_intro)

    start_html(mono_page_file, "indexes", "version_specific_code", "Version-specific code", "Version-specific code", "Code that only appears in one version")
    output_next_prev(next_prev_compare_indexes["version_specific_code"], mono_page_file)
    mono_page_file.write(html_mono_intro)

    for include in sorted(all_includes, key=lambda k: re.sub("part (.) of", "part 0$1 of", all_includes[k]["name"].lower())):
        urls = get_url_for_code_page(include)

        version_links = '<td class="center">{}</td><td class="center">{}</td><td class="center">{}</td><td class="center">{}</td><td class="center">{}</td><td class="center">{}</td></tr>\n'.format(
            add_code_link(urls, "CASSETTE", "Cassette") if "CASSETTE" in all_includes[include]["versions"] else "-",
            add_code_link(urls, "DISC_DOCKED", "Docked") if "DISC_DOCKED" in all_includes[include]["versions"] else "-",
            add_code_link(urls, "DISC_FLIGHT", "Flight") if "DISC_FLIGHT" in all_includes[include]["versions"] else "-",
            add_code_link(urls, "6502SP", "6502SP") if "6502SP" in all_includes[include]["versions"] else "-",
            add_code_link(urls, "MASTER", "Master") if "MASTER" in all_includes[include]["versions"] else "-",
            add_code_link(urls, "ELECTRON", "Electron") if "ELECTRON" in all_includes[include]["versions"] else "-"
        )
        if all_includes[include]["multi_version"]:
            difference_count = str(all_includes[include]["multi_version"]) + " variation"
            if all_includes[include]["multi_version"] > 1:
                difference_count += "s"
        else:
            difference_count = ""
        row = '<tr><td><a href="{}">{}</a><br /><span class="codeSummaryCategory">{}<br />{}</span><br />{}</td>'.format(
            "/" + content_folder + all_includes[include]["stage"] + "/" + all_includes[include]["type"] + "/" + all_includes[include]["filename"] + ".html",
            all_includes[include]["name"],
            all_includes[include]["type"].capitalize(),
            all_includes[include]["category"],
            difference_count
        )
        row_no_link = '<tr><td>{}<br /><span class="codeSummaryCategory">{}<br />{}</span></td>'.format(
            all_includes[include]["name"],
            all_includes[include]["type"].capitalize(),
            all_includes[include]["category"]
        )
        if len(all_includes[include]["versions"]) == 1:
            mono_page_file.write(row_no_link + version_links)
        elif all_includes[include]["multi_version"]:
            multi_varies_page_file.write(row + version_links)
        else:
            multi_same_page_file.write(row_no_link + version_links)

    multi_varies_page_file.write("</table></div></div>")
    output_next_prev(next_prev_compare_indexes["shared_code_with_variations"], multi_varies_page_file)
    end_html(multi_varies_page_file)
    multi_same_page_file.write("</table></div></div>")
    output_next_prev(next_prev_compare_indexes["shared_code_no_variations"], multi_same_page_file)
    end_html(multi_same_page_file)
    mono_page_file.write("</table></div></div>")
    output_next_prev(next_prev_compare_indexes["version_specific_code"], mono_page_file)
    end_html(mono_page_file)


def output_compare_other_categories_index(page_file):
    tag_categories_to_show = set()
    for category in tag_categories:
        if category not in tag_categories_with_comments:
            tag_categories_to_show.add(category)

    start_html(page_file, "shared", "shared_code_other_variations", "Minor variations between versions", "Minor variations between versions", "A table showing minor variations between versions of Elite")

    next_prev = next_prev_compare_categories["other_categories"]
    output_next_prev(next_prev, page_file)

    page_file.write(html_shared_other_variations_intro)

    for category in sorted(tag_categories_to_show):
        page_file.write('<th class="center">{}</th>'.format(category))
    page_file.write("</tr>")

    for include in sorted(all_includes, key=lambda k: re.sub("part (.) of", "part 0$1 of", all_includes[k]["name"].lower())):
        count_tags = 0
        for category in tag_categories_to_show:
            if category in all_includes[include]["tag_count"]:
                count_tags += all_includes[include]["tag_count"][category]

        if count_tags:
            row = '<tr><td><a href="{}">{}</a><br /><span class="codeSummaryCategory">{}</span></td>'.format(
                "/" + content_folder + all_includes[include]["stage"] + "/" + all_includes[include]["type"] + "/" + all_includes[include]["filename"] + ".html",
                all_includes[include]["name"],
                all_includes[include]["category"]
            )
            page_file.write(row)
            for category in sorted(tag_categories_to_show):
                if category in all_includes[include]["tag_count"]:
                    page_file.write('<td class="center"><span>{}</span</td>'.format(all_includes[include]["tag_count"][category]))
                else:
                    page_file.write('<td class="center"><span></span</td>')

    page_file.write("<tbody></table>")
    page_file.write('</div></div>')

    output_next_prev(next_prev, page_file)
    end_html(page_file)


def output_compare_category_index(page_file, category):
    start_html(page_file, "shared", "shared_code_" + category.lower(), tag_title[category], tag_title[category], tag_summary[category])

    next_prev = next_prev_compare_categories[category.lower()]
    output_next_prev(next_prev, page_file)

    page_file.write(html_shared_category_intro.format(tag_explanation[category]))

    includes_with_category = []

    for include in all_includes:
        if all_includes[include]["multi_version"]:
            if category in all_includes[include]["tag_count"]:
                this_include = all_includes[include]
                this_include["include_name"] = include
                includes_with_category.append(this_include)

    for include in sorted(includes_with_category, key=lambda k: re.sub("part (.) of", "part 0$1 of", k["name"].lower())):
        if len(include["versions"]) > 1:
            url = "/" + content_folder + include["stage"] + "/" + include["type"] + "/" + include["filename"] + ".html"
            row = '<tr><td><a href="{}">{}</a><br /><span class="codeSummaryCategory">{}</span></td><td>{}</td>'.format(
                url,
                include["name"],
                include["category"],
                tag_comments_as_ul(include["tag_comments"], category, url)
            )
        elif len(include["versions"]) == 1:
            # url = "/" + include["family"] + "/" + include["stage"] + "/" + include["type"] + "/" + include["filename"] + ".html"
            version = include["versions"][0]
            urls = get_url_for_code_page(include["include_name"])
            url = urls[version]
            row = '<tr><td><a href="{}">{}</a><br /><span class="codeSummaryCategory">{}</span></td><td>{}</td>'.format(
                url,
                include["name"],
                include["category"],
                tag_comments_for_single_platform_variation(include["tag_comments"], category, url)
            )
        page_file.write(row)

    page_file.write("<tbody></table>")
    page_file.write('</div></div>')

    output_next_prev(next_prev, page_file)
    end_html(page_file)


def tag_comments_as_ul(comments, category, url):
    html = ''
    if category in comments:
        html += '<ul>\n'
        anchor = 1
        for comment in comments[category]:
            link_to_compare = '<div class="moreLink"><a href="{}">See the code variation for this feature</a></div>'.format(url + "#compare-" + make_id(category) + "-" + str(anchor))
            html += '<li>' + add_full_stop(comment) + link_to_compare + '</li>\n'
            anchor += 1
        html += '</ul>\n'
    return html


def tag_comments_for_single_platform_variation(comments, category, url):
    html = ''
    if category in comments:
        html += '<ul>\n'
        for comment in comments[category]:
            link_to_compare = '<div class="moreLink"><a href="{}">See the code containing this feature</a></div>'.format(url)
            html += '<li>' + add_full_stop(comment) + link_to_compare + '</li>\n'
        html += '</ul>\n'
    return html


def get_url_for_code_page(include):
    urls = {}
    if "-" in all_includes[include]["filename"]:
        url_cassette_stage = get_stage("CASSETTE", include) + "/" + all_includes[include]["type"] + "/"
        url_6502sp_stage = get_stage("6502SP", include) + "/" + all_includes[include]["type"] + "/"
        url_docked_stage = get_stage("DISC_DOCKED", include) + "/" + all_includes[include]["type"] + "/"
        url_flight_stage = get_stage("DISC_FLIGHT", include) + "/" + all_includes[include]["type"] + "/"
        url_master_stage = get_stage("MASTER", include) + "/" + all_includes[include]["type"] + "/"
        url_electron_stage = get_stage("ELECTRON", include) + "/" + all_includes[include]["type"] + "/"
        urls["CASSETTE"] = fix_code_link(url_cassette_stage, all_includes[include]["filename"], "cassette")
        urls["6502SP"] = fix_code_link(url_6502sp_stage, all_includes[include]["filename"], "6502sp")
        urls["DISC_DOCKED"] = fix_code_link(url_docked_stage, all_includes[include]["filename"], "disc")
        urls["DISC_FLIGHT"] = fix_code_link(url_flight_stage, all_includes[include]["filename"], "disc")
        urls["MASTER"] = fix_code_link(url_master_stage, all_includes[include]["filename"], "master")
        urls["ELECTRON"] = fix_code_link(url_electron_stage, all_includes[include]["filename"], "electron")
    else:
        if all_includes[include]["type"] == "variable" and len(all_includes[include]["workspace"]):
            if "CASSETTE" in all_includes[include]["workspace"]:
                workspace_name = all_includes[include]["workspace"]["CASSETTE"]
                urls["CASSETTE"] = get_stage("CASSETTE", include) + "/workspace/" + workspace_name + ".html#" + all_includes[include]["filename"]
            else:
                urls["CASSETTE"] = ""

            if "DISC_FLIGHT" in all_includes[include]["workspace"]:
                workspace_name = all_includes[include]["workspace"]["DISC_FLIGHT"]
                urls["DISC_FLIGHT"] = get_stage("DISC_FLIGHT", include) + "/workspace/" + workspace_name + ".html#" + all_includes[include]["filename"]
            else:
                urls["DISC_FLIGHT"] = ""

            if "DISC_DOCKED" in all_includes[include]["workspace"]:
                workspace_name = all_includes[include]["workspace"]["DISC_DOCKED"]
                urls["DISC_DOCKED"] = get_stage("DISC_DOCKED", include) + "/workspace/" + workspace_name + ".html#" + all_includes[include]["filename"]
            else:
                urls["DISC_DOCKED"] = ""

            if "6502SP" in all_includes[include]["workspace"]:
                workspace_name = all_includes[include]["workspace"]["6502SP"]
                urls["6502SP"] = get_stage("6502SP", include) + "/workspace/" + workspace_name + ".html#" + all_includes[include]["filename"]
            else:
                urls["6502SP"] = ""

            if "MASTER" in all_includes[include]["workspace"]:
                workspace_name = all_includes[include]["workspace"]["MASTER"]
                urls["MASTER"] = get_stage("MASTER", include) + "/workspace/" + workspace_name + ".html#" + all_includes[include]["filename"]
            else:
                urls["MASTER"] = ""

            if "ELECTRON" in all_includes[include]["workspace"]:
                workspace_name = all_includes[include]["workspace"]["ELECTRON"]
                urls["ELECTRON"] = get_stage("ELECTRON", include) + "/workspace/" + workspace_name + ".html#" + all_includes[include]["filename"]
            else:
                urls["ELECTRON"] = ""

        else:
            urls["CASSETTE"] = get_stage("CASSETTE", include) + "/" + all_includes[include]["type"] + "/" + all_includes[include]["filename"] + ".html"
            if all_includes[include]["family"] == "common" and all_includes[include]["type"] == "subroutine" and all_includes[include]["filename"] == "dks4":
                urls["6502SP"] = get_stage("6502SP", include) + "/macro/" + all_includes[include]["filename"] + ".html"
            else:
                urls["6502SP"] = get_stage("6502SP", include) + "/" + all_includes[include]["type"] + "/" + all_includes[include]["filename"] + ".html"
            urls["DISC_DOCKED"] = get_stage("DISC_DOCKED", include) + "/" + all_includes[include]["type"] + "/" + all_includes[include]["filename"] + ".html"
            urls["DISC_FLIGHT"] = get_stage("DISC_FLIGHT", include) + "/" + all_includes[include]["type"] + "/" + all_includes[include]["filename"] + ".html"
            urls["MASTER"] = get_stage("MASTER", include) + "/" + all_includes[include]["type"] + "/" + all_includes[include]["filename"] + ".html"
            urls["ELECTRON"] = get_stage("ELECTRON", include) + "/" + all_includes[include]["type"] + "/" + all_includes[include]["filename"] + ".html"
    if urls["CASSETTE"]:
        urls["CASSETTE"] = "/cassette/" + urls["CASSETTE"]
    if urls["DISC_DOCKED"]:
        urls["DISC_DOCKED"] = "/disc/" + urls["DISC_DOCKED"]
    if urls["DISC_FLIGHT"]:
        urls["DISC_FLIGHT"] = "/disc/" + urls["DISC_FLIGHT"]
    if urls["6502SP"]:
        urls["6502SP"] = "/6502sp/" + urls["6502SP"]
    if urls["MASTER"]:
        urls["MASTER"] = "/master/" + urls["MASTER"]
    if urls["ELECTRON"]:
        urls["ELECTRON"] = "/electron/" + urls["ELECTRON"]
    return urls


def get_stage(platform_key, include):
    if platform_key in all_includes[include]["stage_by_version"]:
        stage = all_includes[include]["stage_by_version"][platform_key]
    else:
        stage = all_includes[include]["stage"]
    return stage


def fix_code_link(url_stage, name, platform):
    options = name.split("-")
    if os.path.isfile(dest_folder + platform + "/" + url_stage + options[0] + ".html"):
        return url_stage + options[0] + ".html"
    if os.path.isfile(dest_folder + platform + "/" + url_stage + options[1] + ".html"):
        return url_stage + options[1] + ".html"
    return ""


def char_range(c1, c2):
    for c in range(ord(c1), ord(c2) + 1):
        yield chr(c)


def add_code_link(urls, platform, text):
    if urls[platform]:
        return '<a href="' + urls[platform] + '">' + text + '</a>'
    else:
        return ""


def strip_elite_a(input_file):
    result = []
    if_stack = []
    include_this = True
    processing_elite_a_if = False
    if_block_contains_contents_to_show = False
    skip_blank_lines = False
    for line in input_file:
        if skip_blank_lines and line.strip() == "":
            continue
        skip_blank_lines = False
        clean_line = re.sub(r'_(' + omit_from_compare + r')_\w+ OR ', "", line)
        clean_line = re.sub(r' OR _(' + omit_from_compare + r')_\w+', "", clean_line)
        m = re_version_if_elite_a.search(line)
        n = re_version_if.search(line)
        if n or if_block_contains_contents_to_show:
            if_block_contains_contents_to_show = True
        if m:
            # IF or ELIF statement for site in omit_from_compare, include IF NOT(_xxx_*), exclude IF _xxx_*
            processing_elite_a_if = True
            if line.startswith("IF "):
                if_block_contains_contents_to_show = False
            include_this = False
            if m.group(1):
                include_this = True
            # Version IF statement, type 0 on stack
            if_stack.append(0)
            skip_blank_lines = True
        elif line.startswith("IF "):
            # Other IF statement, type 1 on stack
            if_stack.append(1)
            if include_this:
                result.append(clean_line)
        elif re_version_endif.match(line):
            # ENDIF statement
            if_type = if_stack.pop()
            if include_this and if_type == 1:
                result.append(clean_line)
            if if_type == 0:
                if processing_elite_a_if and if_block_contains_contents_to_show:
                    result.append(clean_line)
                    skip_blank_lines = False
                else:
                    skip_blank_lines = True
                include_this = True
                processing_elite_a_if = False
                if_block_contains_contents_to_show = False
        elif include_this:
            result.append(clean_line)
    return result


def versionise(content, platform_name):
    if args.platform == "elite-a" or args.platform == "aviator" or args.platform == "revs" or args.platform == "lander":
        return content.format(platform_name)
    else:
        return content.format("the " + platform_name + " version of Elite")


def version(platform_name):
    if args.platform == "elite-a" or args.platform == "aviator" or args.platform == "revs" or args.platform == "lander":
        return platform_name
    else:
        return platform_name + " version"


# ################################# Main loop #################################

# Create folders
if not os.path.isdir("websites"):
    os.mkdir("websites")

if not os.path.isdir("debug"):
    os.mkdir("debug")

create_folder("")
create_folder(content_folder)
create_folder("templates_local")

if args.platform != "compare":

    # Create folders
    create_folder(content_folder + "all")
    create_folder(content_folder + "articles")
    create_folder(content_folder + "indexes")

    if args.platform != "aviator" and args.platform != "revs" and args.platform != "lander":
        print("\nAnalysing files for comparison: ", end="", flush=True)
        analyse_files_for_compare()

    categories = {}

    # Read source files
    if args.platform == "cassette" or args.platform == "electron":
        with open(elite_loader, "r") as file:
            source1 = file.readlines()
        with open(elite_source, "r") as file:
            source2 = file.readlines()
        with open(elite_bcfs, "r") as file:
            source3 = file.readlines()
        source = source1 + source2 + source3

    elif args.platform == "disc":
        with open(elite_loader1, "r") as file:
            source1a = file.readlines()
        with open(elite_loader2, "r") as file:
            source1b = file.readlines()
        with open(elite_text_tokens, "r") as file:
            source1c_text_tokens = file.readlines()
        with open(elite_ship_missile, "r") as file:
            source1c_ship_missile = file.readlines()
        with open(elite_loader3, "r") as file:
            source1c = file.readlines()
        with open(elite_loader_sideways_ram, "r") as file:
            source1c_sideways_ram = file.readlines()
        with open(elite_source_docked, "r") as file:
            source_docked = file.readlines()
        with open(elite_source_flight, "r") as file:
            source_flight = file.readlines()
        with open(elite_source_ships_a, "r") as file:
            source_ships_a = file.readlines()
        with open(elite_source_ships_b, "r") as file:
            source_ships_b = file.readlines()
        with open(elite_source_ships_c, "r") as file:
            source_ships_c = file.readlines()
        with open(elite_source_ships_d, "r") as file:
            source_ships_d = file.readlines()
        with open(elite_source_ships_e, "r") as file:
            source_ships_e = file.readlines()
        with open(elite_source_ships_f, "r") as file:
            source_ships_f = file.readlines()
        with open(elite_source_ships_g, "r") as file:
            source_ships_g = file.readlines()
        with open(elite_source_ships_h, "r") as file:
            source_ships_h = file.readlines()
        with open(elite_source_ships_i, "r") as file:
            source_ships_i = file.readlines()
        with open(elite_source_ships_j, "r") as file:
            source_ships_j = file.readlines()
        with open(elite_source_ships_k, "r") as file:
            source_ships_k = file.readlines()
        with open(elite_source_ships_l, "r") as file:
            source_ships_l = file.readlines()
        with open(elite_source_ships_m, "r") as file:
            source_ships_m = file.readlines()
        with open(elite_source_ships_n, "r") as file:
            source_ships_n = file.readlines()
        with open(elite_source_ships_o, "r") as file:
            source_ships_o = file.readlines()
        with open(elite_source_ships_p, "r") as file:
            source_ships_p = file.readlines()
        source = source1a + source1b + source1c_text_tokens + source1c_ship_missile + source1c + source1c_sideways_ram + source_docked + source_flight + source_ships_a + source_ships_b + source_ships_c + source_ships_d + source_ships_e + source_ships_f + source_ships_g + source_ships_h + source_ships_i + source_ships_j + source_ships_k + source_ships_l + source_ships_m + source_ships_n + source_ships_o + source_ships_p

    elif args.platform == "6502sp":
        with open(elite_loader, "r") as file:
            source1a = file.readlines()
        with open(elite_loader2, "r") as file:
            source1b = file.readlines()
        with open(elite_source, "r") as file:
            source2 = file.readlines()
        with open(elite_bcfs, "r") as file:
            source3 = file.readlines()
        with open(elite_io, "r") as file:
            source4 = file.readlines()
        source = source1a + source1b + source2 + source3 + source4

    elif args.platform == "c64":
        with open(elite_loader1, "r") as file:
            source1a = file.readlines()
        with open(elite_loader2, "r") as file:
            source1b = file.readlines()
        with open(elite_loader, "r") as file:
            source2 = file.readlines()
        with open(elite_source, "r") as file:
            source3 = file.readlines()
        with open(elite_data, "r") as file:
            source4 = file.readlines()
        with open(elite_sprites, "r") as file:
            source5 = file.readlines()
        source = source1a + source1b + source2 + source3 + source4 + source5

    elif args.platform == "apple":
        with open(elite_loader, "r") as file:
            source1 = file.readlines()
        with open(elite_source, "r") as file:
            source2 = file.readlines()
        with open(elite_data, "r") as file:
            source3 = file.readlines()
        with open(elite_bcfs, "r") as file:
            source4 = file.readlines()
        with open(elite_transfer, "r") as file:
            source5 = file.readlines()
        source = source1 + source2 + source3 + source4 + source5

    elif args.platform == "master":
        with open(elite_loader, "r") as file:
            source1 = file.readlines()
        with open(elite_source, "r") as file:
            source2 = file.readlines()
        with open(elite_data, "r") as file:
            source3 = file.readlines()
        source = source1 + source2 + source3

    elif args.platform == "elite-a":
        with open(elite_loader, "r") as file:
            source1 = file.readlines()
        with open(elite_text_tokens, "r") as file:
            source_text_tokens = file.readlines()
        with open(elite_ship_missile, "r") as file:
            source_ship_missile = file.readlines()
        with open(elite_source_docked, "r") as file:
            source_docked = file.readlines()
        with open(elite_source_flight, "r") as file:
            source_flight = file.readlines()
        with open(elite_source_encyclopedia, "r") as file:
            source_encyclopedia = file.readlines()
        with open(elite_source_ships_a, "r") as file:
            source_ships_a = file.readlines()
        with open(elite_source_ships_b, "r") as file:
            source_ships_b = file.readlines()
        with open(elite_source_ships_c, "r") as file:
            source_ships_c = file.readlines()
        with open(elite_source_ships_d, "r") as file:
            source_ships_d = file.readlines()
        with open(elite_source_ships_e, "r") as file:
            source_ships_e = file.readlines()
        with open(elite_source_ships_f, "r") as file:
            source_ships_f = file.readlines()
        with open(elite_source_ships_g, "r") as file:
            source_ships_g = file.readlines()
        with open(elite_source_ships_h, "r") as file:
            source_ships_h = file.readlines()
        with open(elite_source_ships_i, "r") as file:
            source_ships_i = file.readlines()
        with open(elite_source_ships_j, "r") as file:
            source_ships_j = file.readlines()
        with open(elite_source_ships_k, "r") as file:
            source_ships_k = file.readlines()
        with open(elite_source_ships_l, "r") as file:
            source_ships_l = file.readlines()
        with open(elite_source_ships_m, "r") as file:
            source_ships_m = file.readlines()
        with open(elite_source_ships_n, "r") as file:
            source_ships_n = file.readlines()
        with open(elite_source_ships_o, "r") as file:
            source_ships_o = file.readlines()
        with open(elite_source_ships_p, "r") as file:
            source_ships_p = file.readlines()
        with open(elite_source_ships_q, "r") as file:
            source_ships_q = file.readlines()
        with open(elite_source_ships_r, "r") as file:
            source_ships_r = file.readlines()
        with open(elite_source_ships_s, "r") as file:
            source_ships_s = file.readlines()
        with open(elite_source_ships_t, "r") as file:
            source_ships_t = file.readlines()
        with open(elite_source_ships_u, "r") as file:
            source_ships_u = file.readlines()
        with open(elite_source_ships_v, "r") as file:
            source_ships_v = file.readlines()
        with open(elite_source_ships_w, "r") as file:
            source_ships_w = file.readlines()
        with open(elite_io, "r") as file:
            source_io = file.readlines()
        with open(elite_parasite, "r") as file:
            source_parasite = file.readlines()
        source = source1 + source_text_tokens + source_ship_missile + source_docked + source_flight + source_encyclopedia + source_ships_a + source_ships_b + source_ships_c + source_ships_d + source_ships_e + source_ships_f + source_ships_g + source_ships_h + source_ships_i + source_ships_j + source_ships_k + source_ships_l + source_ships_m + source_ships_n + source_ships_o + source_ships_p + source_ships_q + source_ships_r + source_ships_s + source_ships_t + source_ships_u + source_ships_v + source_ships_w + source_io + source_parasite

    elif args.platform == "nes":
        with open(elite_source_common, "r") as file:
            source_common = file.readlines()
        with open(elite_source_header, "r") as file:
            source_header = file.readlines()
        with open(elite_source_bank_0, "r") as file:
            source_bank_0 = file.readlines()
        with open(elite_source_bank_1, "r") as file:
            source_bank_1 = file.readlines()
        with open(elite_source_bank_2, "r") as file:
            source_bank_2 = file.readlines()
        with open(elite_source_bank_3, "r") as file:
            source_bank_3 = file.readlines()
        with open(elite_source_bank_4, "r") as file:
            source_bank_4 = file.readlines()
        with open(elite_source_bank_5, "r") as file:
            source_bank_5 = file.readlines()
        with open(elite_source_bank_6, "r") as file:
            source_bank_6 = file.readlines()
        with open(elite_source_bank_7, "r") as file:
            source_bank_7 = file.readlines()
        source = source_common + source_header + source_bank_0 + source_bank_1 + source_bank_2 + source_bank_3 + source_bank_4 + source_bank_5 + source_bank_6 + source_bank_7

    elif args.platform == "aviator":
        with open(aviator_source, "r") as file:
            source1 = file.readlines()
        source = source1

    elif args.platform == "revs":
        with open(revs_source, "r") as file:
            source1 = file.readlines()
        with open(revs_silverstone, "r") as file:
            source_silverstone = file.readlines()
        with open(revs_brands_hatch, "r") as file:
            source_brands_hatch = file.readlines()
        with open(revs_donington_park, "r") as file:
            source_donington_park = file.readlines()
        with open(revs_oulton_park, "r") as file:
            source_oulton_park = file.readlines()
        with open(revs_snetterton, "r") as file:
            source_snetterton = file.readlines()
        with open(revs_nurburgring, "r") as file:
            source_nurburgring = file.readlines()
        source = source1

    elif args.platform == "lander":
        with open(lander_source, "r") as file:
            source1 = file.readlines()
        with open(lander_runimage, "r") as file:
            source_runimage = file.readlines()
        source = source1

    # Extract popup data into:
    #   references_library: one entry per label (routine, variable, workspace etc.), for popup data
    #   all_headers: one entry per header, for the map of the source code
    print("\nExtracting popup data: ", end="", flush=True)

    if args.platform == "cassette" or args.platform == "electron":
        extract_popup_data(source1, "Loader", "loader", "Loader")
        extract_popup_data(source2, "", "workspaces", "Workspaces")
        extract_popup_data(source3, "Big Code file", "bcfs", "Big Code file")

    elif args.platform == "disc":
        extract_popup_data(source1a, "Loader 1", "loader1", "Loader 1")
        extract_popup_data(source1b, "Loader 2", "loader2", "Loader 2")
        extract_popup_data(source1c_text_tokens, "Text tokens", "text_tokens", "Text tokens")
        extract_popup_data(source1c_ship_missile, "Missile ship blueprint", "ship_missile", "Missile ship blueprint")
        extract_popup_data(source1c, "Loader 3", "loader3", "Loader 3")
        extract_popup_data(source1c_sideways_ram, "Sideways RAM Loader", "loader_sideways_ram", "Sideways RAM Loader")
        extract_popup_data(source_docked, "Docked", "workspaces_docked", "Docked")
        extract_popup_data(source_flight, "Flight", "workspaces_flight", "Flight")
        extract_popup_data(source_ships_a, "Ship blueprints A", "elite_ships_a", "Ship blueprints A")
        extract_popup_data(source_ships_b, "Ship blueprints B", "elite_ships_b", "Ship blueprints B")
        extract_popup_data(source_ships_c, "Ship blueprints C", "elite_ships_c", "Ship blueprints C")
        extract_popup_data(source_ships_d, "Ship blueprints D", "elite_ships_d", "Ship blueprints D")
        extract_popup_data(source_ships_e, "Ship blueprints E", "elite_ships_e", "Ship blueprints E")
        extract_popup_data(source_ships_f, "Ship blueprints F", "elite_ships_f", "Ship blueprints F")
        extract_popup_data(source_ships_g, "Ship blueprints G", "elite_ships_g", "Ship blueprints G")
        extract_popup_data(source_ships_h, "Ship blueprints H", "elite_ships_h", "Ship blueprints H")
        extract_popup_data(source_ships_i, "Ship blueprints I", "elite_ships_i", "Ship blueprints I")
        extract_popup_data(source_ships_j, "Ship blueprints J", "elite_ships_j", "Ship blueprints J")
        extract_popup_data(source_ships_k, "Ship blueprints K", "elite_ships_k", "Ship blueprints K")
        extract_popup_data(source_ships_l, "Ship blueprints L", "elite_ships_l", "Ship blueprints L")
        extract_popup_data(source_ships_m, "Ship blueprints M", "elite_ships_m", "Ship blueprints M")
        extract_popup_data(source_ships_n, "Ship blueprints N", "elite_ships_n", "Ship blueprints N")
        extract_popup_data(source_ships_o, "Ship blueprints O", "elite_ships_o", "Ship blueprints O")
        extract_popup_data(source_ships_p, "Ship blueprints P", "elite_ships_p", "Ship blueprints P")

    elif args.platform == "6502sp":
        extract_popup_data(source1a, "Loader 1", "loader1", "Loader 1")
        extract_popup_data(source1b, "Loader 2", "loader2", "Loader 2")
        extract_popup_data(source2, "", "workspaces", "Workspaces")
        extract_popup_data(source3, "Big Code file", "bcfs", "Big Code file")
        extract_popup_data(source4, "I/O processor", "i_o_processor", "I/O processor")

    elif args.platform == "c64":
        extract_popup_data(source1a, "Disk Loader 1", "loader1", "Disk Loader 1")
        extract_popup_data(source1b, "Disk Loader 2", "loader2", "Disk Loader 2")
        extract_popup_data(source2, "Game Loader", "loader", "Game Loader")
        extract_popup_data(source3, "", "workspaces", "Workspaces")
        extract_popup_data(source4, "Game data", "elite_data", "Game data")
        extract_popup_data(source5, "Sprites", "elite_sprites", "Sprites")

    elif args.platform == "apple":
        extract_popup_data(source1, "Loader", "loader", "Loader")
        extract_popup_data(source2, "", "workspaces", "Workspaces")
        extract_popup_data(source3, "Game data", "elite_data", "Game data")
        extract_popup_data(source4, "Big Code file", "bcfs", "Big Code file")
        extract_popup_data(source5, "Transfer program", "transfer_program", "Transfer program")

    elif args.platform == "master":
        extract_popup_data(source1, "Loader", "loader", "Loader")
        extract_popup_data(source2, "", "workspaces", "Workspaces")
        extract_popup_data(source3, "Game data", "elite_data", "Game data")

    elif args.platform == "elite-a":
        extract_popup_data(source1, "Loader", "loader", "Loader")
        extract_popup_data(source_text_tokens, "Text tokens", "text_tokens", "Text tokens")
        extract_popup_data(source_ship_missile, "Missile ship blueprint", "ship_missile", "Missile ship blueprint")
        extract_popup_data(source_docked, "Docked", "workspaces_docked", "Docked")
        extract_popup_data(source_flight, "Flight", "workspaces_flight", "Flight")
        extract_popup_data(source_encyclopedia, "Encyclopedia", "workspaces_encyclopedia", "Encyclopedia")
        extract_popup_data(source_ships_a, "Ship blueprints A", "elite_ships_a", "Ship blueprints A")
        extract_popup_data(source_ships_b, "Ship blueprints B", "elite_ships_b", "Ship blueprints B")
        extract_popup_data(source_ships_c, "Ship blueprints C", "elite_ships_c", "Ship blueprints C")
        extract_popup_data(source_ships_d, "Ship blueprints D", "elite_ships_d", "Ship blueprints D")
        extract_popup_data(source_ships_e, "Ship blueprints E", "elite_ships_e", "Ship blueprints E")
        extract_popup_data(source_ships_f, "Ship blueprints F", "elite_ships_f", "Ship blueprints F")
        extract_popup_data(source_ships_g, "Ship blueprints G", "elite_ships_g", "Ship blueprints G")
        extract_popup_data(source_ships_h, "Ship blueprints H", "elite_ships_h", "Ship blueprints H")
        extract_popup_data(source_ships_i, "Ship blueprints I", "elite_ships_i", "Ship blueprints I")
        extract_popup_data(source_ships_j, "Ship blueprints J", "elite_ships_j", "Ship blueprints J")
        extract_popup_data(source_ships_k, "Ship blueprints K", "elite_ships_k", "Ship blueprints K")
        extract_popup_data(source_ships_l, "Ship blueprints L", "elite_ships_l", "Ship blueprints L")
        extract_popup_data(source_ships_m, "Ship blueprints M", "elite_ships_m", "Ship blueprints M")
        extract_popup_data(source_ships_n, "Ship blueprints N", "elite_ships_n", "Ship blueprints N")
        extract_popup_data(source_ships_o, "Ship blueprints O", "elite_ships_o", "Ship blueprints O")
        extract_popup_data(source_ships_p, "Ship blueprints P", "elite_ships_p", "Ship blueprints P")
        extract_popup_data(source_ships_q, "Ship blueprints Q", "elite_ships_q", "Ship blueprints Q")
        extract_popup_data(source_ships_r, "Ship blueprints R", "elite_ships_r", "Ship blueprints R")
        extract_popup_data(source_ships_s, "Ship blueprints S", "elite_ships_s", "Ship blueprints S")
        extract_popup_data(source_ships_t, "Ship blueprints T", "elite_ships_t", "Ship blueprints T")
        extract_popup_data(source_ships_u, "Ship blueprints U", "elite_ships_u", "Ship blueprints U")
        extract_popup_data(source_ships_v, "Ship blueprints V", "elite_ships_v", "Ship blueprints V")
        extract_popup_data(source_ships_w, "Ship blueprints W", "elite_ships_w", "Ship blueprints W")
        extract_popup_data(source_io, "I/O processor", "i_o_processor", "I/O processor")
        extract_popup_data(source_parasite, "Parasite", "parasite", "Parasite")

    elif args.platform == "nes":
        extract_popup_data(source_common, "Common", "common", "Common")
        extract_popup_data(source_header, "iNES header", "header", "iNES header")
        extract_popup_data(source_bank_7, "Bank 7", "bank_7", "Bank 7")
        extract_popup_data(source_bank_0, "Bank 0", "bank_0", "Bank 0")
        extract_popup_data(source_bank_1, "Bank 1", "bank_1", "Bank 1")
        extract_popup_data(source_bank_2, "Bank 2", "bank_2", "Bank 2")
        extract_popup_data(source_bank_3, "Bank 3", "bank_3", "Bank 3")
        extract_popup_data(source_bank_4, "Bank 4", "bank_4", "Bank 4")
        extract_popup_data(source_bank_5, "Bank 5", "bank_5", "Bank 5")
        extract_popup_data(source_bank_6, "Bank 6", "bank_6", "Bank 6")
        move_data_to_end("bank_7")

    elif args.platform == "aviator":
        extract_popup_data(source1, "", "workspaces", "Workspaces")

    elif args.platform == "revs":
        extract_popup_data(source1, "", "workspaces", "Workspaces")
        extract_popup_data(source_silverstone, "Silverstone", "revs_silverstone", "Silverstone")
        extract_popup_data(source_brands_hatch, "Brands Hatch", "revs_brands_hatch", "Brands Hatch")
        extract_popup_data(source_donington_park, "Donington Park", "revs_donington_park", "Donington Park")
        extract_popup_data(source_oulton_park, "Oulton Park", "revs_oulton_park", "Oulton Park")
        extract_popup_data(source_snetterton, "Snetterton", "revs_snetterton", "Snetterton")
        extract_popup_data(source_nurburgring, "Nürburgring", "revs_nurburgring", "Nürburgring")

    elif args.platform == "lander":
        extract_popup_data(source1, "", "workspaces", "Workspaces")
        extract_popup_data(source_runimage, "!RunImage", "runimage", "!RunImage")

    with open("debug/references_library.txt", "w") as file:
        file.write(json.dumps(references_library, indent=2, sort_keys=True))
    with open("debug/all_headers.txt", "w") as file:
        file.write(json.dumps(all_headers, indent=2, sort_keys=True))
    with open("debug/entry_points.txt", "w") as file:
        file.write(json.dumps(entry_points, indent=2, sort_keys=True))
    with open("debug/mentions.txt", "w") as file:
        file.write(json.dumps(mentions, indent=2, sort_keys=True))

    # Output individual code pages by category and extract mentions
    print("\nWriting articles: ", end="", flush=True)

    if args.platform == "cassette" or args.platform == "electron":
        output_individual_code_pages(source1, "Loader")
        output_individual_code_pages(source2, "")
        output_individual_code_pages(source3, "Big Code file")

    elif args.platform == "disc":
        output_individual_code_pages(source1a, "Loader 1")
        output_individual_code_pages(source1b, "Loader 2")
        output_individual_code_pages(source1c_text_tokens, "Text tokens")
        output_individual_code_pages(source1c_ship_missile, "Missile ship blueprint")
        output_individual_code_pages(source1c, "Loader 3")
        output_individual_code_pages(source1c_sideways_ram, "Sideways RAM Loader")
        output_individual_code_pages(source_docked, "Docked")
        output_individual_code_pages(source_flight, "Flight")
        output_individual_code_pages(source_ships_a, "Ship blueprints A")
        output_individual_code_pages(source_ships_b, "Ship blueprints B")
        output_individual_code_pages(source_ships_c, "Ship blueprints C")
        output_individual_code_pages(source_ships_d, "Ship blueprints D")
        output_individual_code_pages(source_ships_e, "Ship blueprints E")
        output_individual_code_pages(source_ships_f, "Ship blueprints F")
        output_individual_code_pages(source_ships_g, "Ship blueprints G")
        output_individual_code_pages(source_ships_h, "Ship blueprints H")
        output_individual_code_pages(source_ships_i, "Ship blueprints I")
        output_individual_code_pages(source_ships_j, "Ship blueprints J")
        output_individual_code_pages(source_ships_k, "Ship blueprints K")
        output_individual_code_pages(source_ships_l, "Ship blueprints L")
        output_individual_code_pages(source_ships_m, "Ship blueprints M")
        output_individual_code_pages(source_ships_n, "Ship blueprints N")
        output_individual_code_pages(source_ships_o, "Ship blueprints O")
        output_individual_code_pages(source_ships_p, "Ship blueprints P")

    elif args.platform == "6502sp":
        output_individual_code_pages(source1a, "Loader 1")
        output_individual_code_pages(source1b, "Loader 2")
        output_individual_code_pages(source2, "")
        output_individual_code_pages(source3, "Big Code file")
        output_individual_code_pages(source4, "I/O processor")

    elif args.platform == "c64":
        output_individual_code_pages(source1a, "Disk Loader 1")
        output_individual_code_pages(source1b, "Disk Loader 2")
        output_individual_code_pages(source2, "Game Loader")
        output_individual_code_pages(source3, "")
        output_individual_code_pages(source4, "Game data")
        output_individual_code_pages(source5, "Sprites")

    elif args.platform == "apple":
        output_individual_code_pages(source1, "Loader")
        output_individual_code_pages(source2, "")
        output_individual_code_pages(source3, "Game data")
        output_individual_code_pages(source4, "Big Code file")
        output_individual_code_pages(source5, "Transfer program")

    elif args.platform == "master":
        output_individual_code_pages(source1, "Loader")
        output_individual_code_pages(source2, "")
        output_individual_code_pages(source3, "Game data")

    elif args.platform == "elite-a":
        output_individual_code_pages(source1, "Loader")
        output_individual_code_pages(source_text_tokens, "Text tokens")
        output_individual_code_pages(source_ship_missile, "Missile ship blueprint")
        output_individual_code_pages(source_docked, "Docked")
        output_individual_code_pages(source_flight, "Flight")
        output_individual_code_pages(source_encyclopedia, "Encyclopedia")
        output_individual_code_pages(source_ships_a, "Ship blueprints A")
        output_individual_code_pages(source_ships_b, "Ship blueprints B")
        output_individual_code_pages(source_ships_c, "Ship blueprints C")
        output_individual_code_pages(source_ships_d, "Ship blueprints D")
        output_individual_code_pages(source_ships_e, "Ship blueprints E")
        output_individual_code_pages(source_ships_f, "Ship blueprints F")
        output_individual_code_pages(source_ships_g, "Ship blueprints G")
        output_individual_code_pages(source_ships_h, "Ship blueprints H")
        output_individual_code_pages(source_ships_i, "Ship blueprints I")
        output_individual_code_pages(source_ships_j, "Ship blueprints J")
        output_individual_code_pages(source_ships_k, "Ship blueprints K")
        output_individual_code_pages(source_ships_l, "Ship blueprints L")
        output_individual_code_pages(source_ships_m, "Ship blueprints M")
        output_individual_code_pages(source_ships_n, "Ship blueprints N")
        output_individual_code_pages(source_ships_o, "Ship blueprints O")
        output_individual_code_pages(source_ships_p, "Ship blueprints P")
        output_individual_code_pages(source_ships_q, "Ship blueprints Q")
        output_individual_code_pages(source_ships_r, "Ship blueprints R")
        output_individual_code_pages(source_ships_s, "Ship blueprints S")
        output_individual_code_pages(source_ships_t, "Ship blueprints T")
        output_individual_code_pages(source_ships_u, "Ship blueprints U")
        output_individual_code_pages(source_ships_v, "Ship blueprints V")
        output_individual_code_pages(source_ships_w, "Ship blueprints W")
        output_individual_code_pages(source_io, "I/O processor")
        output_individual_code_pages(source_parasite, "Parasite")

    elif args.platform == "nes":
        output_individual_code_pages(source_common, "Common")
        output_individual_code_pages(source_bank_0, "Bank 0")
        output_individual_code_pages(source_bank_1, "Bank 1")
        output_individual_code_pages(source_bank_2, "Bank 2")
        output_individual_code_pages(source_bank_3, "Bank 3")
        output_individual_code_pages(source_bank_4, "Bank 4")
        output_individual_code_pages(source_bank_5, "Bank 5")
        output_individual_code_pages(source_bank_6, "Bank 6")
        output_individual_code_pages(source_bank_7, "Bank 7")
        output_individual_code_pages(source_header, "iNES header")

    elif args.platform == "aviator":
        output_individual_code_pages(source1, "")

    elif args.platform == "revs":
        output_individual_code_pages(source1, "")
        output_individual_code_pages(source_silverstone, "Silverstone")
        output_individual_code_pages(source_brands_hatch, "Brands Hatch")
        output_individual_code_pages(source_donington_park, "Donington Park")
        output_individual_code_pages(source_oulton_park, "Oulton Park")
        output_individual_code_pages(source_snetterton, "Snetterton")
        output_individual_code_pages(source_nurburgring, "Nürburgring")

    elif args.platform == "lander":
        output_individual_code_pages(source1, "")
        output_individual_code_pages(source_runimage, "!RunImage")

    # Output map of source code and extract source code statistics
    output_map_of_source_code()

    with open("debug/source_code_stats.txt", "w") as file:
        file.write(json.dumps(source_code_stats, indent=2, sort_keys=True))

    # Output source code statistics
    output_source_code_stats()

    # Output source code cross-references page
    output_source_code_cross_references()

    # Output large source code pages
    print("\nWriting large source code pages: ", end="", flush=True)

    with open("debug/output_all.txt", "w") as debug_file:

        if args.platform == "cassette" or args.platform == "electron" or args.platform == "apple" or args.platform == "master":
            with open(dest_folder + content_folder + "all/loader.html", "w") as all_file:
                output_large_source_code_page(source1, "Loader", "Loader source", "loader", "", "")
        elif args.platform == "disc":
            with open(dest_folder + content_folder + "all/loader1.html", "w") as all_file:
                output_large_source_code_page(source1a, "Loader 1", "Loader 1 source", "loader1", "", "")
            with open(dest_folder + content_folder + "all/loader2.html", "w") as all_file:
                output_large_source_code_page(source1b, "Loader 2", "Loader 2 source", "loader2", "", "")
            with open(dest_folder + content_folder + "all/text_tokens.html", "w") as all_file:
                output_large_source_code_page(source1c_text_tokens, "Text tokens", "Text tokens source", "text_tokens", "", "")
            with open(dest_folder + content_folder + "all/ship_missile.html", "w") as all_file:
                output_large_source_code_page(source1c_ship_missile, "Missile ship blueprint", "Missile ship blueprint", "ship_missile", "", "")
            with open(dest_folder + content_folder + "all/loader3.html", "w") as all_file:
                output_large_source_code_page(source1c, "Loader 3", "Loader 3 source", "loader3", "", "")
            with open(dest_folder + content_folder + "all/loader_sideways_ram.html", "w") as all_file:
                output_large_source_code_page(source1c_sideways_ram, "Sideways RAM Loader", "Sideways RAM Loader source", "loader_sideways_ram", "", "")
        elif args.platform == "6502sp":
            with open(dest_folder + content_folder + "all/loader1.html", "w") as all_file:
                output_large_source_code_page(source1a, "Loader 1", "Loader 1 source", "loader1", "", "")
            with open(dest_folder + content_folder + "all/loader2.html", "w") as all_file:
                output_large_source_code_page(source1b, "Loader 2", "Loader 2 source", "loader2", "", "")
        elif args.platform == "c64":
            with open(dest_folder + content_folder + "all/loader1.html", "w") as all_file:
                output_large_source_code_page(source1a, "Disk Loader 1", "Disk Loader 1 source", "loader1", "", "")
            with open(dest_folder + content_folder + "all/loader2.html", "w") as all_file:
                output_large_source_code_page(source1b, "Disk Loader 2", "Disk Loader 2 source", "loader2", "", "")
            with open(dest_folder + content_folder + "all/loader.html", "w") as all_file:
                output_large_source_code_page(source2, "Game Loader", "Game Loader source", "loader", "", "")
        elif args.platform == "elite-a":
            with open(dest_folder + content_folder + "all/loader.html", "w") as all_file:
                output_large_source_code_page(source1, "Loader", "Loader source", "loader", "", "")
            with open(dest_folder + content_folder + "all/text_tokens.html", "w") as all_file:
                output_large_source_code_page(source_text_tokens, "Text tokens", "Text tokens source", "text_tokens", "", "")
            with open(dest_folder + content_folder + "all/ship_missile.html", "w") as all_file:
                output_large_source_code_page(source_ship_missile, "Missile ship blueprint", "Missile ship blueprint", "ship_missile", "", "")

        if args.platform == "cassette" or args.platform == "electron" or args.platform == "6502sp":
            with open(dest_folder + content_folder + "all/workspaces.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Workspaces and configuration", "workspaces", ["", "Name: K%"], ["ELITE RECURSIVE TEXT TOKEN FILE", "ELITE A FILE"])
            with open(dest_folder + content_folder + "all/text_tokens.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Text tokens", "text_tokens", "ELITE RECURSIVE TEXT TOKEN FILE", "Name: K%")
            with open(dest_folder + content_folder + "all/elite_a.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite A source", "elite_a", "ELITE A FILE", "ELITE B FILE")
            with open(dest_folder + content_folder + "all/elite_b.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite B source", "elite_b", "ELITE B FILE", "ELITE C FILE")
            with open(dest_folder + content_folder + "all/elite_c.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite C source", "elite_c", "ELITE C FILE", "ELITE D FILE")
            with open(dest_folder + content_folder + "all/elite_d.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite D source", "elite_d", "ELITE D FILE", "ELITE E FILE")
            with open(dest_folder + content_folder + "all/elite_e.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite E source", "elite_e", "ELITE E FILE", "ELITE F FILE")
            with open(dest_folder + content_folder + "all/elite_f.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite F source", "elite_f", "ELITE F FILE", "ELITE G FILE")
        elif args.platform == "disc" or args.platform == "elite-a":
            with open(dest_folder + content_folder + "all/workspaces_docked.html", "w") as all_file:
                output_large_source_code_page(source_docked, "Docked", "Docked workspaces", "workspaces_docked", [""], ["ELITE A FILE"])
            with open(dest_folder + content_folder + "all/elite_a_docked.html", "w") as all_file:
                output_large_source_code_page(source_docked, "Docked", "Elite A docked source", "elite_a_docked", "ELITE A FILE", "ELITE B FILE")
            with open(dest_folder + content_folder + "all/elite_b_docked.html", "w") as all_file:
                output_large_source_code_page(source_docked, "Docked", "Elite B docked source", "elite_b_docked", "ELITE B FILE", "ELITE C FILE")
            with open(dest_folder + content_folder + "all/elite_c_docked.html", "w") as all_file:
                output_large_source_code_page(source_docked, "Docked", "Elite C docked source", "elite_c_docked", "ELITE C FILE", "ELITE D FILE")
            with open(dest_folder + content_folder + "all/elite_d_docked.html", "w") as all_file:
                output_large_source_code_page(source_docked, "Docked", "Elite D docked source", "elite_d_docked", "ELITE D FILE", "ELITE E FILE")
            with open(dest_folder + content_folder + "all/elite_e_docked.html", "w") as all_file:
                output_large_source_code_page(source_docked, "Docked", "Elite E docked source", "elite_e_docked", "ELITE E FILE", "ELITE F FILE")
            with open(dest_folder + content_folder + "all/elite_f_docked.html", "w") as all_file:
                output_large_source_code_page(source_docked, "Docked", "Elite F docked source", "elite_f_docked", "ELITE F FILE", "ELITE G FILE")
            with open(dest_folder + content_folder + "all/elite_g_docked.html", "w") as all_file:
                output_large_source_code_page(source_docked, "Docked", "Elite G docked source", "elite_g_docked", "ELITE G FILE", "ELITE H FILE")
            with open(dest_folder + content_folder + "all/elite_h_docked.html", "w") as all_file:
                output_large_source_code_page(source_docked, "Docked", "Elite H docked source", "elite_h_docked", "ELITE H FILE", "ELITE SHIP BLUEPRINTS FILE")
            with open(dest_folder + content_folder + "all/elite_ships_docked.html", "w") as all_file:
                output_large_source_code_page(source_docked, "Docked", "Ship blueprints", "elite_ships_docked", "ELITE SHIP HANGAR BLUEPRINTS FILE", "")

            with open(dest_folder + content_folder + "all/workspaces_flight.html", "w") as all_file:
                output_large_source_code_page(source_flight, "Flight", "Flight workspaces", "workspaces_flight", [""], ["ELITE A FILE"])
            with open(dest_folder + content_folder + "all/elite_a_flight.html", "w") as all_file:
                output_large_source_code_page(source_flight, "Flight", "Elite A flight source", "elite_a_flight", "ELITE A FILE", "ELITE B FILE")
            with open(dest_folder + content_folder + "all/elite_b_flight.html", "w") as all_file:
                output_large_source_code_page(source_flight, "Flight", "Elite B flight source", "elite_b_flight", "ELITE B FILE", "ELITE C FILE")
            with open(dest_folder + content_folder + "all/elite_c_flight.html", "w") as all_file:
                output_large_source_code_page(source_flight, "Flight", "Elite C flight source", "elite_c_flight", "ELITE C FILE", "ELITE D FILE")
            with open(dest_folder + content_folder + "all/elite_d_flight.html", "w") as all_file:
                output_large_source_code_page(source_flight, "Flight", "Elite D flight source", "elite_d_flight", "ELITE D FILE", "ELITE E FILE")
            with open(dest_folder + content_folder + "all/elite_e_flight.html", "w") as all_file:
                output_large_source_code_page(source_flight, "Flight", "Elite E flight source", "elite_e_flight", "ELITE E FILE", "ELITE F FILE")
            with open(dest_folder + content_folder + "all/elite_f_flight.html", "w") as all_file:
                output_large_source_code_page(source_flight, "Flight", "Elite F flight source", "elite_f_flight", "ELITE F FILE", "ELITE G FILE")
            with open(dest_folder + content_folder + "all/elite_g_flight.html", "w") as all_file:
                output_large_source_code_page(source_flight, "Flight", "Elite G flight source", "elite_g_flight", "ELITE G FILE", "ELITE H FILE")
            with open(dest_folder + content_folder + "all/elite_h_flight.html", "w") as all_file:
                output_large_source_code_page(source_flight, "Flight", "Elite H flight source", "elite_h_flight", "ELITE H FILE", "")

            with open(dest_folder + content_folder + "all/elite_ships_a.html", "w") as all_file:
                output_large_source_code_page(source_ships_a, "Ship blueprints A", "Ship blueprints A", "elite_ships_a", "", "")
            with open(dest_folder + content_folder + "all/elite_ships_b.html", "w") as all_file:
                output_large_source_code_page(source_ships_b, "Ship blueprints B", "Ship blueprints B", "elite_ships_b", "", "")
            with open(dest_folder + content_folder + "all/elite_ships_c.html", "w") as all_file:
                output_large_source_code_page(source_ships_c, "Ship blueprints C", "Ship blueprints C", "elite_ships_c", "", "")
            with open(dest_folder + content_folder + "all/elite_ships_d.html", "w") as all_file:
                output_large_source_code_page(source_ships_d, "Ship blueprints D", "Ship blueprints D", "elite_ships_d", "", "")
            with open(dest_folder + content_folder + "all/elite_ships_e.html", "w") as all_file:
                output_large_source_code_page(source_ships_e, "Ship blueprints E", "Ship blueprints E", "elite_ships_e", "", "")
            with open(dest_folder + content_folder + "all/elite_ships_f.html", "w") as all_file:
                output_large_source_code_page(source_ships_f, "Ship blueprints F", "Ship blueprints F", "elite_ships_f", "", "")
            with open(dest_folder + content_folder + "all/elite_ships_g.html", "w") as all_file:
                output_large_source_code_page(source_ships_g, "Ship blueprints G", "Ship blueprints G", "elite_ships_g", "", "")
            with open(dest_folder + content_folder + "all/elite_ships_h.html", "w") as all_file:
                output_large_source_code_page(source_ships_h, "Ship blueprints H", "Ship blueprints H", "elite_ships_h", "", "")
            with open(dest_folder + content_folder + "all/elite_ships_i.html", "w") as all_file:
                output_large_source_code_page(source_ships_i, "Ship blueprints I", "Ship blueprints I", "elite_ships_i", "", "")
            with open(dest_folder + content_folder + "all/elite_ships_j.html", "w") as all_file:
                output_large_source_code_page(source_ships_j, "Ship blueprints J", "Ship blueprints J", "elite_ships_j", "", "")
            with open(dest_folder + content_folder + "all/elite_ships_k.html", "w") as all_file:
                output_large_source_code_page(source_ships_k, "Ship blueprints K", "Ship blueprints K", "elite_ships_k", "", "")
            with open(dest_folder + content_folder + "all/elite_ships_l.html", "w") as all_file:
                output_large_source_code_page(source_ships_l, "Ship blueprints L", "Ship blueprints L", "elite_ships_l", "", "")
            with open(dest_folder + content_folder + "all/elite_ships_m.html", "w") as all_file:
                output_large_source_code_page(source_ships_m, "Ship blueprints M", "Ship blueprints M", "elite_ships_m", "", "")
            with open(dest_folder + content_folder + "all/elite_ships_n.html", "w") as all_file:
                output_large_source_code_page(source_ships_n, "Ship blueprints N", "Ship blueprints N", "elite_ships_n", "", "")
            with open(dest_folder + content_folder + "all/elite_ships_o.html", "w") as all_file:
                output_large_source_code_page(source_ships_o, "Ship blueprints O", "Ship blueprints O", "elite_ships_o", "", "")
            with open(dest_folder + content_folder + "all/elite_ships_p.html", "w") as all_file:
                output_large_source_code_page(source_ships_p, "Ship blueprints P", "Ship blueprints P", "elite_ships_p", "", "")

        if args.platform == "elite-a":
            with open(dest_folder + content_folder + "all/workspaces_encyclopedia.html", "w") as all_file:
                output_large_source_code_page(source_encyclopedia, "Encyclopedia", "Encyclopedia workspaces", "workspaces_encyclopedia", [""], ["ELITE A FILE"])
            with open(dest_folder + content_folder + "all/elite_a_encyclopedia.html", "w") as all_file:
                output_large_source_code_page(source_encyclopedia, "Encyclopedia", "Elite A encyclopedia source", "elite_a_encyclopedia", "ELITE A FILE", "ELITE B FILE")
            with open(dest_folder + content_folder + "all/elite_b_encyclopedia.html", "w") as all_file:
                output_large_source_code_page(source_encyclopedia, "Encyclopedia", "Elite B encyclopedia source", "elite_b_encyclopedia", "ELITE B FILE", "ELITE C FILE")
            with open(dest_folder + content_folder + "all/elite_c_encyclopedia.html", "w") as all_file:
                output_large_source_code_page(source_encyclopedia, "Encyclopedia", "Elite C encyclopedia source", "elite_c_encyclopedia", "ELITE C FILE", "ELITE D FILE")
            with open(dest_folder + content_folder + "all/elite_d_encyclopedia.html", "w") as all_file:
                output_large_source_code_page(source_encyclopedia, "Encyclopedia", "Elite D encyclopedia source", "elite_d_encyclopedia", "ELITE D FILE", "ELITE E FILE")
            with open(dest_folder + content_folder + "all/elite_e_encyclopedia.html", "w") as all_file:
                output_large_source_code_page(source_encyclopedia, "Encyclopedia", "Elite E encyclopedia source", "elite_e_encyclopedia", "ELITE E FILE", "ELITE F FILE")
            with open(dest_folder + content_folder + "all/elite_f_encyclopedia.html", "w") as all_file:
                output_large_source_code_page(source_encyclopedia, "Encyclopedia", "Elite F encyclopedia source", "elite_f_encyclopedia", "ELITE F FILE", "ELITE G FILE")
            with open(dest_folder + content_folder + "all/elite_g_encyclopedia.html", "w") as all_file:
                output_large_source_code_page(source_encyclopedia, "Encyclopedia", "Elite G encyclopedia source", "elite_g_encyclopedia", "ELITE G FILE", "ELITE H FILE")
            with open(dest_folder + content_folder + "all/elite_h_encyclopedia.html", "w") as all_file:
                output_large_source_code_page(source_encyclopedia, "Encyclopedia", "Elite H encyclopedia source", "elite_h_encyclopedia", "ELITE H FILE", "")

            with open(dest_folder + content_folder + "all/elite_ships_q.html", "w") as all_file:
                output_large_source_code_page(source_ships_q, "Ship blueprints Q", "Ship blueprints Q", "elite_ships_q", "", "")
            with open(dest_folder + content_folder + "all/elite_ships_r.html", "w") as all_file:
                output_large_source_code_page(source_ships_r, "Ship blueprints R", "Ship blueprints R", "elite_ships_r", "", "")
            with open(dest_folder + content_folder + "all/elite_ships_s.html", "w") as all_file:
                output_large_source_code_page(source_ships_s, "Ship blueprints S", "Ship blueprints S", "elite_ships_s", "", "")
            with open(dest_folder + content_folder + "all/elite_ships_t.html", "w") as all_file:
                output_large_source_code_page(source_ships_t, "Ship blueprints T", "Ship blueprints T", "elite_ships_t", "", "")
            with open(dest_folder + content_folder + "all/elite_ships_u.html", "w") as all_file:
                output_large_source_code_page(source_ships_u, "Ship blueprints U", "Ship blueprints U", "elite_ships_u", "", "")
            with open(dest_folder + content_folder + "all/elite_ships_v.html", "w") as all_file:
                output_large_source_code_page(source_ships_v, "Ship blueprints V", "Ship blueprints V", "elite_ships_v", "", "")
            with open(dest_folder + content_folder + "all/elite_ships_w.html", "w") as all_file:
                output_large_source_code_page(source_ships_w, "Ship blueprints W", "Ship blueprints W", "elite_ships_w", "", "")

        if args.platform == "cassette" or args.platform == "electron":
            with open(dest_folder + content_folder + "all/elite_g.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite G source", "elite_g", "ELITE G FILE", "ELITE SHIP BLUEPRINTS FILE")
        elif args.platform == "6502sp":
            with open(dest_folder + content_folder + "all/elite_g.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite G source", "elite_g", "ELITE G FILE", "ELITE H FILE")
            with open(dest_folder + content_folder + "all/elite_h.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite H source", "elite_h", "ELITE H FILE", "ELITE I FILE")
            with open(dest_folder + content_folder + "all/elite_i.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite I source", "elite_i", "ELITE I FILE", "ELITE J FILE")
            with open(dest_folder + content_folder + "all/elite_j.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite J source", "elite_j", "ELITE J FILE", "ELITE SHIP BLUEPRINTS FILE")

        if args.platform == "cassette" or args.platform == "electron" or args.platform == "6502sp":
            with open(dest_folder + content_folder + "all/elite_ships.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Ship blueprints", "elite_ships", "ELITE SHIP BLUEPRINTS FILE", "")
            with open(dest_folder + content_folder + "all/bcfs.html", "w") as all_file:
                output_large_source_code_page(source3, "Big Code file", "Big Code File source", "bcfs", "", "")

        if args.platform == "6502sp":
            with open(dest_folder + content_folder + "all/i_o_processor.html", "w") as all_file:
                output_large_source_code_page(source4, "I/O processor", "I/O processor source", "i_o_processor", "", "")

        if args.platform == "c64":
            with open(dest_folder + content_folder + "all/workspaces.html", "w") as all_file:
                output_large_source_code_page(source3, "", "Workspaces and configuration", "workspaces", "", "ELITE A FILE")
            with open(dest_folder + content_folder + "all/elite_a.html", "w") as all_file:
                output_large_source_code_page(source3, "", "Elite A source", "elite_a", "ELITE A FILE", "ELITE B FILE")
            with open(dest_folder + content_folder + "all/elite_b.html", "w") as all_file:
                output_large_source_code_page(source3, "", "Elite B source", "elite_b", "ELITE B FILE", "ELITE C FILE")
            with open(dest_folder + content_folder + "all/elite_c.html", "w") as all_file:
                output_large_source_code_page(source3, "", "Elite C source", "elite_c", "ELITE C FILE", "ELITE D FILE")
            with open(dest_folder + content_folder + "all/elite_d.html", "w") as all_file:
                output_large_source_code_page(source3, "", "Elite D source", "elite_d", "ELITE D FILE", "ELITE E FILE")
            with open(dest_folder + content_folder + "all/elite_e.html", "w") as all_file:
                output_large_source_code_page(source3, "", "Elite E source", "elite_e", "ELITE E FILE", "ELITE F FILE")
            with open(dest_folder + content_folder + "all/elite_f.html", "w") as all_file:
                output_large_source_code_page(source3, "", "Elite F source", "elite_f", "ELITE F FILE", "ELITE G FILE")
            with open(dest_folder + content_folder + "all/elite_g.html", "w") as all_file:
                output_large_source_code_page(source3, "", "Elite G source", "elite_g", "ELITE G FILE", "ELITE H FILE")
            with open(dest_folder + content_folder + "all/elite_h.html", "w") as all_file:
                output_large_source_code_page(source3, "", "Elite H source", "elite_h", "ELITE H FILE", "ELITE I FILE")
            with open(dest_folder + content_folder + "all/elite_i.html", "w") as all_file:
                output_large_source_code_page(source3, "", "Elite I source", "elite_i", "ELITE I FILE", "ELITE J FILE")
            with open(dest_folder + content_folder + "all/elite_j.html", "w") as all_file:
                output_large_source_code_page(source3, "", "Elite J source", "elite_j", "ELITE J FILE", "ELITE K FILE")
            with open(dest_folder + content_folder + "all/elite_k.html", "w") as all_file:
                output_large_source_code_page(source3, "", "Elite K source", "elite_k", "ELITE K FILE", "")
            with open(dest_folder + content_folder + "all/elite_data.html", "w") as all_file:
                output_large_source_code_page(source4, "Game data", "Game data", "elite_data", "", "ELITE SHIP BLUEPRINTS FILE")
            with open(dest_folder + content_folder + "all/elite_ships.html", "w") as all_file:
                output_large_source_code_page(source4, "Game data", "Ship blueprints", "elite_ships", "ELITE SHIP BLUEPRINTS FILE", "ELITE RECURSIVE TEXT TOKEN FILE")
            with open(dest_folder + content_folder + "all/text_tokens.html", "w") as all_file:
                output_large_source_code_page(source4, "Game data", "Text tokens", "text_tokens", "ELITE RECURSIVE TEXT TOKEN FILE", "")
            with open(dest_folder + content_folder + "all/elite_sprites.html", "w") as all_file:
                output_large_source_code_page(source5, "Sprites", "Sprites", "elite_sprites", "ELITE SPRITES", "")

        if args.platform == "apple":
            with open(dest_folder + content_folder + "all/workspaces.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Workspaces and configuration", "workspaces", "", "ELITE A FILE")
            with open(dest_folder + content_folder + "all/elite_a.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite A source", "elite_a", "ELITE A FILE", "ELITE B FILE")
            with open(dest_folder + content_folder + "all/elite_b.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite B source", "elite_b", "ELITE B FILE", "ELITE C FILE")
            with open(dest_folder + content_folder + "all/elite_c.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite C source", "elite_c", "ELITE C FILE", "ELITE D FILE")
            with open(dest_folder + content_folder + "all/elite_d.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite D source", "elite_d", "ELITE D FILE", "ELITE E FILE")
            with open(dest_folder + content_folder + "all/elite_e.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite E source", "elite_e", "ELITE E FILE", "ELITE F FILE")
            with open(dest_folder + content_folder + "all/elite_f.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite F source", "elite_f", "ELITE F FILE", "ELITE G FILE")
            with open(dest_folder + content_folder + "all/elite_g.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite G source", "elite_g", "ELITE G FILE", "ELITE H FILE")
            with open(dest_folder + content_folder + "all/elite_h.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite H source", "elite_h", "ELITE H FILE", "ELITE I FILE")
            with open(dest_folder + content_folder + "all/elite_i.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite I source", "elite_i", "ELITE I FILE", "ELITE J FILE")
            with open(dest_folder + content_folder + "all/elite_j.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite J source", "elite_j", "ELITE J FILE", "ELITE K FILE")
            with open(dest_folder + content_folder + "all/elite_k.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite K source", "elite_k", "ELITE K FILE", "")
            with open(dest_folder + content_folder + "all/elite_data.html", "w") as all_file:
                output_large_source_code_page(source3, "Game data", "Game data", "elite_data", "", "ELITE SHIP BLUEPRINTS FILE")
            with open(dest_folder + content_folder + "all/elite_ships.html", "w") as all_file:
                output_large_source_code_page(source3, "Game data", "Ship blueprints", "elite_ships", "ELITE SHIP BLUEPRINTS FILE", "ELITE RECURSIVE TEXT TOKEN FILE")
            with open(dest_folder + content_folder + "all/text_tokens.html", "w") as all_file:
                output_large_source_code_page(source3, "Game data", "Text tokens", "text_tokens", "ELITE RECURSIVE TEXT TOKEN FILE", "")
            with open(dest_folder + content_folder + "all/bcfs.html", "w") as all_file:
                output_large_source_code_page(source4, "Big Code file", "Big Code File source", "bcfs", "", "")
            with open(dest_folder + content_folder + "all/transfer_program.html", "w") as all_file:
                output_large_source_code_page(source5, "Transfer program", "Transfer program source", "transfer_program", "", "")

        if args.platform == "master":
            with open(dest_folder + content_folder + "all/workspaces.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Workspaces and configuration", "workspaces", "", "ELITE A FILE")
            with open(dest_folder + content_folder + "all/elite_a.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite A source", "elite_a", "ELITE A FILE", "ELITE B FILE")
            with open(dest_folder + content_folder + "all/elite_b.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite B source", "elite_b", "ELITE B FILE", "ELITE C FILE")
            with open(dest_folder + content_folder + "all/elite_c.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite C source", "elite_c", "ELITE C FILE", "ELITE D FILE")
            with open(dest_folder + content_folder + "all/elite_d.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite D source", "elite_d", "ELITE D FILE", "ELITE E FILE")
            with open(dest_folder + content_folder + "all/elite_e.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite E source", "elite_e", "ELITE E FILE", "ELITE F FILE")
            with open(dest_folder + content_folder + "all/elite_f.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite F source", "elite_f", "ELITE F FILE", "ELITE G FILE")
            with open(dest_folder + content_folder + "all/elite_g.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite G source", "elite_g", "ELITE G FILE", "ELITE H FILE")
            with open(dest_folder + content_folder + "all/elite_h.html", "w") as all_file:
                output_large_source_code_page(source2, "", "Elite H source", "elite_h", "ELITE H FILE", "")
            with open(dest_folder + content_folder + "all/elite_data.html", "w") as all_file:
                output_large_source_code_page(source3, "Game data", "Game data", "elite_data", "", "ELITE SHIP BLUEPRINTS FILE")
            with open(dest_folder + content_folder + "all/elite_ships.html", "w") as all_file:
                output_large_source_code_page(source3, "Game data", "Ship blueprints", "elite_ships", "ELITE SHIP BLUEPRINTS FILE", "ELITE RECURSIVE TEXT TOKEN FILE")
            with open(dest_folder + content_folder + "all/text_tokens.html", "w") as all_file:
                output_large_source_code_page(source3, "Game data", "Text tokens", "text_tokens", "ELITE RECURSIVE TEXT TOKEN FILE", "")

        if args.platform == "elite-a":
            with open(dest_folder + content_folder + "all/i_o_processor.html", "w") as all_file:
                output_large_source_code_page(source_io, "I/O processor", "I/O processor source", "i_o_processor", "", "")
            with open(dest_folder + content_folder + "all/workspaces_parasite.html", "w") as all_file:
                output_large_source_code_page(source_parasite, "Parasite", "Parasite workspaces", "workspaces_parasite", [""], ["ELITE A FILE"])
            with open(dest_folder + content_folder + "all/elite_a_parasite.html", "w") as all_file:
                output_large_source_code_page(source_parasite, "Parasite", "Elite A parasite source", "elite_a_parasite", "ELITE A FILE", "ELITE B FILE")
            with open(dest_folder + content_folder + "all/elite_b_parasite.html", "w") as all_file:
                output_large_source_code_page(source_parasite, "Parasite", "Elite B parasite source", "elite_b_parasite", "ELITE B FILE", "ELITE C FILE")
            with open(dest_folder + content_folder + "all/elite_c_parasite.html", "w") as all_file:
                output_large_source_code_page(source_parasite, "Parasite", "Elite C parasite source", "elite_c_parasite", "ELITE C FILE", "ELITE D FILE")
            with open(dest_folder + content_folder + "all/elite_d_parasite.html", "w") as all_file:
                output_large_source_code_page(source_parasite, "Parasite", "Elite D parasite source", "elite_d_parasite", "ELITE D FILE", "ELITE E FILE")
            with open(dest_folder + content_folder + "all/elite_e_parasite.html", "w") as all_file:
                output_large_source_code_page(source_parasite, "Parasite", "Elite E parasite source", "elite_e_parasite", "ELITE E FILE", "ELITE F FILE")
            with open(dest_folder + content_folder + "all/elite_f_parasite.html", "w") as all_file:
                output_large_source_code_page(source_parasite, "Parasite", "Elite F parasite source", "elite_f_parasite", "ELITE F FILE", "ELITE G FILE")
            with open(dest_folder + content_folder + "all/elite_g_parasite.html", "w") as all_file:
                output_large_source_code_page(source_parasite, "Parasite", "Elite G parasite source", "elite_g_parasite", "ELITE G FILE", "ELITE H FILE")
            with open(dest_folder + content_folder + "all/elite_h_parasite.html", "w") as all_file:
                output_large_source_code_page(source_parasite, "Parasite", "Elite H parasite source", "elite_h_parasite", "ELITE H FILE", "ELITE I FILE")
            with open(dest_folder + content_folder + "all/elite_i_parasite.html", "w") as all_file:
                output_large_source_code_page(source_parasite, "Parasite", "Elite I parasite source", "elite_i_parasite", "ELITE I FILE", "ELITE J FILE")
            with open(dest_folder + content_folder + "all/elite_j_parasite.html", "w") as all_file:
                output_large_source_code_page(source_parasite, "Parasite", "Elite J parasite source", "elite_j_parasite", "ELITE J FILE", "ELITE K FILE")
            with open(dest_folder + content_folder + "all/elite_k_parasite.html", "w") as all_file:
                output_large_source_code_page(source_parasite, "Parasite", "Elite K parasite source", "elite_k_parasite", "ELITE K FILE", "ELITE L FILE")
            with open(dest_folder + content_folder + "all/elite_l_parasite.html", "w") as all_file:
                output_large_source_code_page(source_parasite, "Parasite", "Elite L parasite source", "elite_l_parasite", "ELITE L FILE", "ELITE M FILE")
            with open(dest_folder + content_folder + "all/elite_m_parasite.html", "w") as all_file:
                output_large_source_code_page(source_parasite, "Parasite", "Elite M parasite source", "elite_m_parasite", "ELITE M FILE", "ELITE SHIP BLUEPRINTS FILE")
            with open(dest_folder + content_folder + "all/elite_ships_parasite.html", "w") as all_file:
                output_large_source_code_page(source_parasite, "Parasite", "Ship blueprints parasite source", "elite_ships_parasite", "ELITE SHIP BLUEPRINTS FILE", "")

        if args.platform == "nes":
            with open(dest_folder + content_folder + "all/common.html", "w") as all_file:
                output_large_source_code_page(source_common, "Common", "Common code", "common", "", "")
            with open(dest_folder + content_folder + "all/header.html", "w") as all_file:
                output_large_source_code_page(source_header, "iNES header", "iNES header", "header", "", "")
            with open(dest_folder + content_folder + "all/bank_0_1.html", "w") as all_file:
                output_large_source_code_page(source_bank_0, "Bank 0", "Bank 0 (Part 1 of 5)", "bank_0_1", "", "Name: TACTICS (Part 1 of 7)")
            with open(dest_folder + content_folder + "all/bank_0_2.html", "w") as all_file:
                output_large_source_code_page(source_bank_0, "Bank 0", "Bank 0 (Part 2 of 5)", "bank_0_2", "Name: TACTICS (Part 1 of 7)", "Name: TT14")
            with open(dest_folder + content_folder + "all/bank_0_3.html", "w") as all_file:
                output_large_source_code_page(source_bank_0, "Bank 0", "Bank 0 (Part 3 of 5)", "bank_0_3", "Name: TT14", "Name: PrintLaserView")
            with open(dest_folder + content_folder + "all/bank_0_4.html", "w") as all_file:
                output_large_source_code_page(source_bank_0, "Bank 0", "Bank 0 (Part 4 of 5)", "bank_0_4", "Name: PrintLaserView", "Name: ShowStartScreen")
            with open(dest_folder + content_folder + "all/bank_0_5.html", "w") as all_file:
                output_large_source_code_page(source_bank_0, "Bank 0", "Bank 0 (Part 5 of 5)", "bank_0_5", "Name: ShowStartScreen", "")
            with open(dest_folder + content_folder + "all/bank_1_1.html", "w") as all_file:
                output_large_source_code_page(source_bank_1, "Bank 1", "Bank 1 (Part 1 of 3)", "bank_1_1", "", "Name: LL61")
            with open(dest_folder + content_folder + "all/bank_1_2.html", "w") as all_file:
                output_large_source_code_page(source_bank_1, "Bank 1", "Bank 1 (Part 2 of 3)", "bank_1_2", "Name: LL61", "Name: EDGES")
            with open(dest_folder + content_folder + "all/bank_1_3.html", "w") as all_file:
                output_large_source_code_page(source_bank_1, "Bank 1", "Bank 1 (Part 3 of 3)", "bank_1_3", "Name: EDGES", "")
            with open(dest_folder + content_folder + "all/bank_2_1.html", "w") as all_file:
                output_large_source_code_page(source_bank_2, "Bank 2", "Bank 2 (Part 1 of 4)", "bank_2_1", "", "Name: TKN1_DE")
            with open(dest_folder + content_folder + "all/bank_2_2.html", "w") as all_file:
                output_large_source_code_page(source_bank_2, "Bank 2", "Bank 2 (Part 2 of 4)", "bank_2_2", "Name: TKN1_DE", "Name: TKN1_FR")
            with open(dest_folder + content_folder + "all/bank_2_3.html", "w") as all_file:
                output_large_source_code_page(source_bank_2, "Bank 2", "Bank 2 (Part 3 of 4)", "bank_2_3", "Name: TKN1_FR", "Name: QQ18_FR")
            with open(dest_folder + content_folder + "all/bank_2_4.html", "w") as all_file:
                output_large_source_code_page(source_bank_2, "Bank 2", "Bank 2 (Part 4 of 4)", "bank_2_4", "Name: QQ18_FR", "")
            with open(dest_folder + content_folder + "all/bank_3_1.html", "w") as all_file:
                output_large_source_code_page(source_bank_3, "Bank 3", "Bank 3 (Part 1 of 2)", "bank_3_1", "", "Name: HideIconBar")
            with open(dest_folder + content_folder + "all/bank_3_2.html", "w") as all_file:
                output_large_source_code_page(source_bank_3, "Bank 3", "Bank 3 (Part 2 of 2)", "bank_3_2", "Name: HideIconBar", "")
            with open(dest_folder + content_folder + "all/bank_4.html", "w") as all_file:
                output_large_source_code_page(source_bank_4, "Bank 4", "Bank 4", "bank_4", "", "")
            with open(dest_folder + content_folder + "all/bank_5.html", "w") as all_file:
                output_large_source_code_page(source_bank_5, "Bank 5", "Bank 5", "bank_5", "", "")
            with open(dest_folder + content_folder + "all/bank_6_1.html", "w") as all_file:
                output_large_source_code_page(source_bank_6, "Bank 6", "Bank 6 (Part 1 of 3)", "bank_6_1", "", "Name: tuneData")
            with open(dest_folder + content_folder + "all/bank_6_2.html", "w") as all_file:
                output_large_source_code_page(source_bank_6, "Bank 6", "Bank 6 (Part 2 of 3)", "bank_6_2", "Name: tuneData", "Name: LTDEF")
            with open(dest_folder + content_folder + "all/bank_6_3.html", "w") as all_file:
                output_large_source_code_page(source_bank_6, "Bank 6", "Bank 6 (Part 3 of 3)", "bank_6_3", "Name: LTDEF", "")
            with open(dest_folder + content_folder + "all/bank_7_1.html", "w") as all_file:
                output_large_source_code_page(source_bank_7, "Bank 7", "Bank 7 (Part 1 of 4)", "bank_7_1", "", "Name: ClearMemory")
            with open(dest_folder + content_folder + "all/bank_7_2.html", "w") as all_file:
                output_large_source_code_page(source_bank_7, "Bank 7", "Bank 7 (Part 2 of 4)", "bank_7_2", "Name: ClearMemory", "Name: autoplayKeys1_DE")
            with open(dest_folder + content_folder + "all/bank_7_3.html", "w") as all_file:
                output_large_source_code_page(source_bank_7, "Bank 7", "Bank 7 (Part 3 of 4)", "bank_7_3", "Name: autoplayKeys1_DE", "Name: SetupFullViewInNMI")
            with open(dest_folder + content_folder + "all/bank_7_4.html", "w") as all_file:
                output_large_source_code_page(source_bank_7, "Bank 7", "Bank 7 (Part 4 of 4)", "bank_7_4", "Name: SetupFullViewInNMI", "")

        if args.platform == "aviator":
            with open(dest_folder + content_folder + "all/workspaces.html", "w") as all_file:
                output_large_source_code_page(source1, "", "Workspaces and configuration", "workspaces", "", "AVIATOR MAIN GAME CODE")
            with open(dest_folder + content_folder + "all/aviator_a.html", "w") as all_file:
                output_large_source_code_page(source1, "", "Aviator A source", "aviator_a", "AVIATOR MAIN GAME CODE", "Name: EraseCanopyLines")
            with open(dest_folder + content_folder + "all/aviator_b.html", "w") as all_file:
                output_large_source_code_page(source1, "", "Aviator B source", "aviator_b", "Name: EraseCanopyLines", "Name: ArtificialHorizon")
            with open(dest_folder + content_folder + "all/aviator_c.html", "w") as all_file:
                output_large_source_code_page(source1, "", "Aviator C source", "aviator_c", "Name: ArtificialHorizon", "Name: AlienInAcornsville")
            with open(dest_folder + content_folder + "all/aviator_d.html", "w") as all_file:
                output_large_source_code_page(source1, "", "Aviator D source", "aviator_d", "Name: AlienInAcornsville", "Name: lineBufferR")
            with open(dest_folder + content_folder + "all/aviator_e.html", "w") as all_file:
                output_large_source_code_page(source1, "", "Aviator E source", "aviator_e", "Name: lineBufferR", "Name: PrintTooLate")
            with open(dest_folder + content_folder + "all/aviator_f.html", "w") as all_file:
                output_large_source_code_page(source1, "", "Aviator F source", "aviator_f", "Name: PrintTooLate", "")

        if args.platform == "revs":
            with open(dest_folder + content_folder + "all/workspaces.html", "w") as all_file:
                output_large_source_code_page(source1, "", "Workspaces and configuration", "workspaces", "", "REVS MAIN GAME CODE")
            with open(dest_folder + content_folder + "all/revs_a.html", "w") as all_file:
                output_large_source_code_page(source1, "", "Revs A source", "revs_a", "REVS MAIN GAME CODE", "Name: MainDrivingLoop (Part 1 of 5)")
            with open(dest_folder + content_folder + "all/revs_b.html", "w") as all_file:
                output_large_source_code_page(source1, "", "Revs B source", "revs_b", "Name: MainDrivingLoop (Part 1 of 5)", "Name: GetColour (Part 1 of 3)")
            with open(dest_folder + content_folder + "all/revs_c.html", "w") as all_file:
                output_large_source_code_page(source1, "", "Revs C source", "revs_c", "Name: GetColour (Part 1 of 3)", "Name: ProcessOvertaking (Part 1 of 3)")
            with open(dest_folder + content_folder + "all/revs_d.html", "w") as all_file:
                output_large_source_code_page(source1, "", "Revs D source", "revs_d", "Name: ProcessOvertaking (Part 1 of 3)", "Name: token26")
            with open(dest_folder + content_folder + "all/revs_e.html", "w") as all_file:
                output_large_source_code_page(source1, "", "Revs E source", "revs_e", "Name: token26", "Name: GetWingSettings")
            with open(dest_folder + content_folder + "all/revs_f.html", "w") as all_file:
                output_large_source_code_page(source1, "", "Revs F source", "revs_f", "Name: GetWingSettings", "Name: MultiplyCoords")
            with open(dest_folder + content_folder + "all/revs_g.html", "w") as all_file:
                output_large_source_code_page(source1, "", "Revs G source", "revs_g", "Name: MultiplyCoords", "Name: xVergeRightLo")
            with open(dest_folder + content_folder + "all/revs_h.html", "w") as all_file:
                output_large_source_code_page(source1, "", "Revs H source", "revs_h", "Name: xVergeRightLo", "Name: GetTextInput")
            with open(dest_folder + content_folder + "all/revs_i.html", "w") as all_file:
                output_large_source_code_page(source1, "", "Revs I source", "revs_i", "Name: GetTextInput", "")
            with open(dest_folder + content_folder + "all/revs_silverstone.html", "w") as all_file:
                output_large_source_code_page(source_silverstone, "Silverstone", "Silverstone track data file", "revs_silverstone", "REVS SILVERSTONE TRACK SOURCE", "")
            with open(dest_folder + content_folder + "all/revs_brands_hatch.html", "w") as all_file:
                output_large_source_code_page(source_brands_hatch, "Brands Hatch", "Brands Hatch track data file", "revs_brands_hatch", "REVS BRANDS HATCH TRACK SOURCE", "")
            with open(dest_folder + content_folder + "all/revs_donington_park.html", "w") as all_file:
                output_large_source_code_page(source_donington_park, "Donington Park", "Donington Park track data file", "revs_donington_park", "REVS DONINGTON PARK TRACK SOURCE", "")
            with open(dest_folder + content_folder + "all/revs_oulton_park.html", "w") as all_file:
                output_large_source_code_page(source_oulton_park, "Oulton Park", "Oulton Park track data file", "revs_oulton_park", "REVS OULTON PARK TRACK SOURCE", "")
            with open(dest_folder + content_folder + "all/revs_snetterton.html", "w") as all_file:
                output_large_source_code_page(source_snetterton, "Snetterton", "Snetterton track data file", "revs_snetterton", "REVS SNETTERTON TRACK SOURCE", "")
            with open(dest_folder + content_folder + "all/revs_nurburgring.html", "w") as all_file:
                output_large_source_code_page(source_nurburgring, "Nürburgring", "Nürburgring track data file", "revs_nurburgring", "REVS NÜRBURGRING TRACK SOURCE", "")

        if args.platform == "lander":
            with open(dest_folder + content_folder + "all/workspaces.html", "w") as all_file:
                output_large_source_code_page(source1, "", "Workspaces and configuration", "workspaces", "", "LANDER MAIN GAME CODE")
            with open(dest_folder + content_folder + "all/lander_a.html", "w") as all_file:
                output_large_source_code_page(source1, "", "Lander A source", "lander_a", "LANDER MAIN GAME CODE", "Name: StoreParticleData")
            with open(dest_folder + content_folder + "all/lander_b.html", "w") as all_file:
                output_large_source_code_page(source1, "", "Name: StoreParticleData", "lander_b", "Name: StoreParticleData", "Name: ProjectParticleOntoScreen")
            with open(dest_folder + content_folder + "all/lander_c.html", "w") as all_file:
                output_large_source_code_page(source1, "", "Lander C source", "lander_c", "Name: ProjectParticleOntoScreen", "Name: lineJump")
            with open(dest_folder + content_folder + "all/lander_d.html", "w") as all_file:
                output_large_source_code_page(source1, "", "Lander D source", "lander_d", "Name: lineJump", "")
            with open(dest_folder + content_folder + "all/runimage.html", "w") as all_file:
                output_large_source_code_page(source_runimage, "!RunImage", "Lander !RunImage source", "lander_runimage", "LANDER !RunImage SOURCE", "")

    # Output menus
    print("\nWriting menus: ", end="", flush=True)

    with open(dest_folder + "templates_local/navigation_" + args.platform + ".php", "w") as file:
        output_menus(file)

    # Output indexes
    print("\nWriting indexes", flush=True)

    if args.platform != "lander":
        add_workspace_variables_to_indexes()
    add_entry_points_to_indexes()

    with open(dest_folder + content_folder + "indexes/subroutines.html", "w") as file:
        output_indexes(file, subroutines, versionise(html_subroutine_index_intro, platform_name), "indexes", "subroutines", "List of all subroutines", "List of all subroutines", "List of all subroutines in " + versionise("{}", platform_name), True)

    with open(dest_folder + content_folder + "indexes/variables.html", "w") as file:
        output_indexes(file, variables, versionise(html_variable_index_intro, platform_name), "indexes", "variables", "List of all variables", "List of all variables", "List of all variables in " + versionise("{}", platform_name), True)

    if args.platform != "aviator" and args.platform != "lander":
        with open(dest_folder + content_folder + "indexes/macros.html", "w") as file:
            output_indexes(file, macros, versionise(html_macro_index_intro, platform_name), "indexes", "macros", "List of all macros", "List of all macros", "List of all macros in " + versionise("{}", platform_name), False)

    if args.platform != "lander":
        with open(dest_folder + content_folder + "indexes/workspaces.html", "w") as file:
            output_indexes(file, workspaces, versionise(html_workspace_index_intro, platform_name), "indexes", "workspaces", "List of all workspaces", "List of all workspaces", "List of all workspaces in " + versionise("{}", platform_name), False)

    with open(dest_folder + content_folder + "indexes/a-z.html", "w") as file:
        output_a_z_index(file, subroutines, variables, macros, workspaces, versionise(html_az_index_intro, platform_name), "indexes", "a-z", "A-Z index of the source code", "A-Z index of the source code", "A-Z index of the source code for " + game_name)

else:

    # Comparison section
    print("\nComparison section", end="", flush=True)

    # Create folders
    create_folder(content_folder + "indexes")

    print("\nAnalysing files for comparison: ", end="", flush=True)
    analyse_files_for_compare()

    with open("debug/includes_in_versions.txt", "w") as file:
        file.write(json.dumps(includes_in_versions, indent=2, sort_keys=True))

    with open("debug/all_includes.txt", "w") as file:
        file.write(json.dumps(all_includes, indent=2, sort_keys=True))

    with open(dest_folder + content_folder + "indexes/shared_code_with_variations.html", "w") as multi_varies_page_file:
        with open(dest_folder + content_folder + "indexes/shared_code_no_variations.html", "w") as multi_same_page_file:
            with open(dest_folder + content_folder + "indexes/version_specific_code.html", "w") as mono_page_file:
                output_compares_indexes(multi_varies_page_file, multi_same_page_file, mono_page_file)

    for category in tag_categories_with_comments:
        with open(dest_folder + content_folder + "indexes/shared_code_" + category.lower() + ".html", "w") as page_file:
            output_compare_category_index(page_file, category)

    with open(dest_folder + content_folder + "indexes/shared_code_other_variations.html", "w") as page_file:
        output_compare_other_categories_index(page_file)

    # Output files with different versions
    print("\nWriting comparison pages: ", end="", flush=True)

    for include in all_includes:
        print(".", end="", flush=True)
        if len(all_includes[include]["versions"]) > 1 and all_includes[include]["multi_version"]:
            input = compare_source_folder + include
            with open(input, "r") as input_file:
                source = input_file.readlines()
                url = content_folder + all_includes[include]["stage"] + "/" + all_includes[include]["type"] + "/" + all_includes[include]["filename"] + ".html"
                output = dest_folder + url
                if os.path.exists(output):
                    print("\nERROR! File for comparison page already exists: {}".format(output))
                else:
                    create_folder(content_folder + all_includes[include]["stage"])
                    create_folder(content_folder + all_includes[include]["stage"] + "/" + all_includes[include]["type"])
                    with open(output, "w") as page_file:
                        output_compare_version_page(source, page_file, include, all_includes[include]["filename"], all_includes[include]["name"], all_includes[include]["category"])

    # Output menus
    print("\nWriting menus: ", end="", flush=True)

    with open(dest_folder + "templates_local/navigation_compare.php", "w") as file:
        output_compare_menu(file)

    print()
