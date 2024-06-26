import re
import os
import ntpath


library_repository = os.environ['ELITE_LIBRARY_REPOSITORY']

# Config
dest_folder = "website/"
content_folder = "compare/"
all_version_ids = ["CASSETTE_VERSION", "ELECTRON_VERSION", "6502SP_VERSION", "DISC_VERSION", "DISC_FLIGHT", "DISC_DOCKED", "MASTER_VERSION", "NES_VERSION"]

# Regexes
re_include_directive = re.compile(r'^ *INCLUDE "(.+)"$')
re_version_if = re.compile(r'(IF|OR) _(CASSETTE_VERSION|ELECTRON_VERSION|6502SP_VERSION|DISC_VERSION|DISC_FLIGHT|DISC_DOCKED|MASTER_VERSION|NES_VERSION)')
re_version_endif = re.compile(r'^ENDIF.*$')

# Config for comparison tool
sites_to_compare = [
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/cassette/1-source-files/main-sources/",
        "source_files": ["elite-loader.asm", "elite-source.asm", "elite-bcfs.asm"],
        "do_not_expand_all_includes": ["elite-build-options.asm"],
        "this_version": [
            "CASSETTE"
        ],
        "version_key": "CASSETTE"
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/disc/1-source-files/main-sources/",
        "source_files": ["elite-loader1.asm", "elite-loader2.asm", "elite-loader3.asm", "elite-text-tokens.asm", "elite-missile.asm"],
        "do_not_expand_all_includes": ["elite-build-options.asm"],
        "this_version": [
            "DISC_VERSION"
        ],
        "version_key": "DISC_VERSION"
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/disc/1-source-files/main-sources/",
        "source_files": ["elite-source-flight.asm", "elite-ships-a.asm", "elite-ships-b.asm", "elite-ships-c.asm", "elite-ships-d.asm", "elite-ships-e.asm", "elite-ships-f.asm", "elite-ships-g.asm", "elite-ships-h.asm", "elite-ships-i.asm", "elite-ships-j.asm", "elite-ships-k.asm", "elite-ships-l.asm", "elite-ships-m.asm", "elite-ships-n.asm", "elite-ships-o.asm", "elite-ships-p.asm"],
        "do_not_expand_all_includes": ["elite-build-options.asm"],
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
        "do_not_expand_all_includes": ["elite-build-options.asm"],
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
        "do_not_expand_all_includes": ["elite-build-options.asm"],
        "this_version": [
            "6502SP"
        ],
        "version_key": "6502SP"
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/master/1-source-files/main-sources/",
        "source_files": ["elite-loader.asm", "elite-source.asm", "elite-data.asm"],
        "do_not_expand_all_includes": ["elite-build-options.asm"],
        "this_version": [
            "MASTER"
        ],
        "version_key": "MASTER"
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/electron/1-source-files/main-sources/",
        "source_files": ["elite-loader.asm", "elite-source.asm", "elite-bcfs.asm"],
        "do_not_expand_all_includes": ["elite-build-options.asm"],
        "this_version": [
            "ELECTRON"
        ],
        "version_key": "ELECTRON"
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/nes/1-source-files/main-sources/",
        "source_files": ["elite-source-bank-0.asm", "elite-source-bank-1.asm", "elite-source-bank-2.asm", "elite-source-bank-3.asm", "elite-source-bank-4.asm", "elite-source-bank-5.asm", "elite-source-bank-6.asm", "elite-source-bank-7.asm", "elite-source-header.asm", "elite-source-common.asm"],
        "do_not_expand_all_includes": ["elite-build-options.asm"],
        "this_version": [
            "NES"
        ],
        "version_key": "NES"
    }
]

# Global variables
i = 0
includes_in_versions = {}
all_includes = {}
compare_source_folder = ""
compare_do_not_expand_all_includes = []
compare_this_version = ""
compare_version_key = ""


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def analyse_files_for_compare():
    global compare_source_folder, compare_do_not_expand_all_includes, compare_this_version, compare_version_key

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
                process_compare_file(input_file, site["section_folder"] + source_file, "")


def add_compare_include(include, version, source_file, include_file, in_workspace):
    global includes_in_versions, all_includes
    multi_version = file_contains_version_ifs(include_file)

    if len(multi_version):
        version_key = version.lower().replace("disc_", "")
        if version_key in includes_in_versions:
            if include not in includes_in_versions[version_key]:
                includes_in_versions[version_key].append(include)
        else:
            includes_in_versions[version_key] = [include]

    if include in all_includes:
        if version not in all_includes[include]["versions"]:
            all_includes[include]["versions"].append(version)
    else:
        names = include.split("/")
        filename = names[4].replace(".asm", "")
        all_includes[include] = {
            "versions": [version],
            "multi_version": multi_version,
            "filename": filename,
            "type": names[3]
        }


def process_compare_file(input_file, source_file, in_workspace):
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
        elif line.startswith("IF "):
            # Other IF statement, type 1 on stack
            if_stack.append(1)
            if include_this:
                process_compare_line(input_file, line, source_file, in_workspace)
        elif re_version_endif.match(line):
            # ENDIF statement
            if_type = if_stack.pop()
            if include_this and if_type == 1:
                process_compare_line(input_file, line, source_file, in_workspace)
            if if_type == 0:
                include_this = True
        elif include_this:
            process_compare_line(input_file, line, source_file, in_workspace)


def file_contains_version_ifs(input_file):
    contains_ifs = []
    for line in input_file:
        m = re_version_if.match(line)
        if m:
            # Version IF or ELIF statement
            for version in all_version_ids:
                if version in line and version not in contains_ifs:
                    contains_ifs.append(version)
    input_file.seek(0)
    return contains_ifs


def process_compare_line(input_file, line, source_file, in_workspace):
    m = re_include_directive.match(line)
    # Exclude catlod.asm as it is purely commented-out code
    if m and "6502sp/main/subroutine/catlod.asm" not in line:
        include_filename = m.group(1)
        if path_leaf(include_filename) not in compare_do_not_expand_all_includes:
            # print("Including file: {}".format(include_filename))
            with open(compare_source_folder + include_filename, "r") as include_file:
                add_compare_include(include_filename, compare_version_key, source_file, include_file, in_workspace)
                if "/workspace/" in include_filename:
                    process_compare_file(include_file, source_file, include_filename)
                else:
                    process_compare_file(include_file, source_file, "")


# ################################# Main loop #################################

print("Analyzing files for comparison: ", end="", flush=True)
analyse_files_for_compare()

# Show files that contain version-ifs for versions that the include is not used in
print("\nFiles that might contain version-ifs that are never used: ", flush=True)
for include in all_includes:
    # if not all_includes[include]["filename"].startswith("ship_"):
    for version_if in all_includes[include]["multi_version"]:
        version_if = version_if.replace("_VERSION", "")
        if version_if == "DISC":
            if "DISC_VERSION" not in all_includes[include]["versions"]:
                if "DISC_FLIGHT" not in all_includes[include]["versions"]:
                    print("{} {}".format("Contains DISC_VERSION but isn't used in DISC_FLIGHT", include))
                if "DISC_DOCKED" not in all_includes[include]["versions"]:
                    print("{} {}".format("Contains DISC_VERSION but isn't used in DISC_DOCKED", include))
        else:
            if version_if not in all_includes[include]["versions"]:
                print("Contains {} but isn't used in {} {}".format(version_if, version_if, include))

print("Done", flush=True)
