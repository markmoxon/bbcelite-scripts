import re
import os
import ntpath


# Environment variables
library_repository = os.environ['ELITE_LIBRARY_REPOSITORY']

# Config
sites = [
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/cassette/1-source-files/main-sources/",
        "source_files": ["elite-loader.asm", "elite-source.asm", "elite-bcfs.asm", "elite-disc.asm", "elite-readme.asm"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/cassette/1-source-files/",
        "this_version": [
            "_CASSETTE_VERSION"
        ],
        "replacements": [
            ('SAVE "versions/cassette/', 'SAVE "'),
            ('INCBIN "versions/cassette/', 'INCBIN "'),
            ('INCLUDE "versions/cassette/1-source-files/main-sources/elite-build-options.asm"', 'INCLUDE "1-source-files/main-sources/elite-build-options.asm"'),
            ('PUTFILE "versions/cassette/', 'PUTFILE "')
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/cassette/2-build-files/",
        "source_files": ["elite-checksum.py", "crc32.py"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/cassette/2-build-files/",
        "this_version": [
            "_CASSETTE_VERSION"
        ],
        "replacements": [
            ('open("versions/cassette/', 'open("')
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/cassette/",
        "source_files": ["Makefile"],
        "do_not_expand_includes": [],
        "dest_folder": "repos/cassette/",
        "this_version": [
            "_CASSETTE_VERSION"
        ],
        "replacements": [
            ('versions/cassette/', ''),
            ('_cassette', ''),
            ('b2-cassette', 'b2'),
            ('PHONY:uef-cassette', 'PHONY:uef'),
            ('uef-cassette: cassette', 'uef: all'),
            ('variant-cassette', 'variant'),
            ('cassette:', 'all:'),
            (':cassette', ':all')
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/disc/1-source-files/main-sources/",
        "source_files": ["elite-text-tokens.asm", "elite-missile.asm", "elite-loader1.asm", "elite-loader2.asm", "elite-loader3.asm", "elite-loader-sideways-ram.asm", "elite-source-flight.asm", "elite-ships-a.asm", "elite-ships-b.asm", "elite-ships-c.asm", "elite-ships-d.asm", "elite-ships-e.asm", "elite-ships-f.asm", "elite-ships-g.asm", "elite-ships-h.asm", "elite-ships-i.asm", "elite-ships-j.asm", "elite-ships-k.asm", "elite-ships-l.asm", "elite-ships-m.asm", "elite-ships-n.asm", "elite-ships-o.asm", "elite-ships-p.asm", "elite-disc.asm", "elite-readme.asm"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/disc/1-source-files/",
        "this_version": [
            "_DISC_VERSION",
            "_DISC_FLIGHT"
        ],
        "replacements": [
            ('SAVE "versions/disc/', 'SAVE "'),
            ('INCBIN "versions/disc/', 'INCBIN "'),
            ('INCLUDE "versions/disc/1-source-files/main-sources/elite-build-options.asm"', 'INCLUDE "1-source-files/main-sources/elite-build-options.asm"'),
            ('PUTFILE "versions/disc/', 'PUTFILE "')
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/disc/2-build-files/",
        "source_files": ["elite-checksum.py", "crc32.py"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/disc/2-build-files/",
        "this_version": [
            "_DISC_VERSION",
            "_DISC_FLIGHT"
        ],
        "replacements": [
            ('open("versions/disc/', 'open("')
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/disc/1-source-files/main-sources/",
        "source_files": ["elite-source-docked.asm"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/disc/1-source-files/",
        "this_version": [
            "_DISC_VERSION",
            "_DISC_DOCKED"
        ],
        "replacements": [
            ('SAVE "versions/disc/', 'SAVE "'),
            ('INCBIN "versions/disc/', 'INCBIN "'),
            ('INCLUDE "versions/disc/1-source-files/main-sources/elite-build-options.asm"', 'INCLUDE "1-source-files/main-sources/elite-build-options.asm"'),
            ('PUTFILE "versions/disc/', 'PUTFILE "')
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/disc/",
        "source_files": ["Makefile"],
        "do_not_expand_includes": [],
        "dest_folder": "repos/disc/",
        "this_version": [
            "_DISC_VERSION",
            "_DISC_FLIGHT"
        ],
        "replacements": [
            ('versions/disc/', ''),
            ('_disc', ''),
            ('b2-disc', 'b2'),
            ('variant-disc', 'variant'),
            ('disc:', 'all:'),
            (':disc', ':all')
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/6502sp/1-source-files/main-sources/",
        "source_files": ["elite-loader1.asm", "elite-loader2.asm", "elite-source.asm", "elite-bcfs.asm", "elite-z.asm", "elite-disc.asm", "elite-readme.asm", "elite-checksum.asm"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/6502sp/1-source-files/",
        "this_version": [
            "_6502SP_VERSION"
        ],
        "replacements": [
            ('SAVE "versions/6502sp/', 'SAVE "'),
            ('INCBIN "versions/6502sp/', 'INCBIN "'),
            ('INCLUDE "versions/6502sp/1-source-files/main-sources/elite-build-options.asm"', 'INCLUDE "1-source-files/main-sources/elite-build-options.asm"'),
            ('PUTFILE "versions/6502sp/', 'PUTFILE "')
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/6502sp/2-build-files/",
        "source_files": ["elite-checksum.py", "crc32.py"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/6502sp/2-build-files/",
        "this_version": [
            "_6502SP_VERSION"
        ],
        "replacements": [
            ('open("versions/6502sp/', 'open("')
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/6502sp/",
        "source_files": ["Makefile"],
        "do_not_expand_includes": [],
        "dest_folder": "repos/6502sp/",
        "this_version": [
            "_6502SP_VERSION"
        ],
        "replacements": [
            ('versions/6502sp/', ''),
            ('_6502sp', ''),
            ('b2-6502sp', 'b2'),
            ('variant-6502sp', 'variant'),
            ('6502sp:', 'all:'),
            (':6502sp', ':all')
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/master/1-source-files/main-sources/",
        "source_files": ["elite-loader.asm", "elite-data.asm", "elite-source.asm", "elite-disc.asm", "elite-readme.asm"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/master/1-source-files/",
        "this_version": [
            "_MASTER_VERSION"
        ],
        "replacements": [
            ('SAVE "versions/master/', 'SAVE "'),
            ('INCBIN "versions/master/', 'INCBIN "'),
            ('INCLUDE "versions/master/1-source-files/main-sources/elite-build-options.asm"', 'INCLUDE "1-source-files/main-sources/elite-build-options.asm"'),
            ('PUTFILE "versions/master/', 'PUTFILE "')
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/master/2-build-files/",
        "source_files": ["elite-checksum.py", "crc32.py"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/master/2-build-files/",
        "this_version": [
            "_MASTER_VERSION"
        ],
        "replacements": [
            ('open("versions/master/', 'open("')
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/master/",
        "source_files": ["Makefile"],
        "do_not_expand_includes": [],
        "dest_folder": "repos/master/",
        "this_version": [
            "_MASTER_VERSION"
        ],
        "replacements": [
            ('versions/master/', ''),
            ('_master', ''),
            ('b2-master', 'b2'),
            ('variant-master', 'variant'),
            ('master:', 'all:'),
            (':master', ':all')
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/electron/1-source-files/main-sources/",
        "source_files": ["elite-loader.asm", "elite-source.asm", "elite-bcfs.asm", "elite-disc.asm", "elite-readme.asm"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/electron/1-source-files/",
        "this_version": [
            "_ELECTRON_VERSION"
        ],
        "replacements": [
            ('SAVE "versions/electron/', 'SAVE "'),
            ('INCBIN "versions/electron/', 'INCBIN "'),
            ('INCLUDE "versions/electron/1-source-files/main-sources/elite-build-options.asm"', 'INCLUDE "1-source-files/main-sources/elite-build-options.asm"'),
            ('PUTFILE "versions/electron/', 'PUTFILE "')
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/electron/2-build-files/",
        "source_files": ["elite-checksum.py", "crc32.py"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/electron/2-build-files/",
        "this_version": [
            "_ELECTRON_VERSION"
        ],
        "replacements": [
            ('open("versions/electron/', 'open("')
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/electron/",
        "source_files": ["Makefile"],
        "do_not_expand_includes": [],
        "dest_folder": "repos/electron/",
        "this_version": [
            "_ELECTRON_VERSION"
        ],
        "replacements": [
            ('versions/electron/', ''),
            ('_electron', ''),
            ('PHONY:uef-cassette', 'PHONY:uef'),
            ('uef-electron: electron', 'uef: all'),
            ('variant-electron', 'variant'),
            ('electron:', 'all:'),
            (':electron', ':all')
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/elite-a/1-source-files/main-sources/",
        "source_files": ["elite-text-tokens.asm", "elite-missile.asm", "elite-source-flight.asm", "elite-ships-a.asm", "elite-ships-b.asm", "elite-ships-c.asm", "elite-ships-d.asm", "elite-ships-e.asm", "elite-ships-f.asm", "elite-ships-g.asm", "elite-ships-h.asm", "elite-ships-i.asm", "elite-ships-j.asm", "elite-ships-k.asm", "elite-ships-l.asm", "elite-ships-m.asm", "elite-ships-n.asm", "elite-ships-o.asm", "elite-ships-p.asm", "elite-ships-q.asm", "elite-loader.asm", "elite-disc.asm", "elite-readme.asm"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/elite-a/1-source-files/",
        "this_version": [
            "_ELITE_A_VERSION",
            "_ELITE_A_FLIGHT"
        ],
        "replacements": [
            ('SAVE "versions/elite-a/', 'SAVE "'),
            ('INCBIN "versions/elite-a/', 'INCBIN "'),
            ('INCLUDE "versions/elite-a/1-source-files/main-sources/elite-build-options.asm"', 'INCLUDE "1-source-files/main-sources/elite-build-options.asm"'),
            ('PUTFILE "versions/elite-a/', 'PUTFILE "')
        ],
        "that_version": [
            "_DISC_VERSION",
            "_DISC_FLIGHT"
        ],
        "disable_diffs_for_whole_routine": [
            "library/disc/loader3/subroutine/elite_loader_part_2_of_3.asm",
            "library/disc/loader3/subroutine/elite_loader_part_3_of_3.asm"
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/elite-a/2-build-files/",
        "source_files": ["elite-checksum.py", "crc32.py"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/elite-a/2-build-files/",
        "this_version": [
            "_ELITE_A_VERSION",
            "_ELITE_A_FLIGHT"
        ],
        "replacements": [
            ('open("versions/elite-a/', 'open("')
        ],
        "that_version": [
            "_DISC_VERSION",
            "_DISC_FLIGHT"
        ],
        "disable_diffs_for_whole_routine": [
            "library/disc/loader3/subroutine/elite_loader_part_2_of_3.asm",
            "library/disc/loader3/subroutine/elite_loader_part_3_of_3.asm"
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/elite-a/1-source-files/main-sources/",
        "source_files": ["elite-ships-r.asm"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/elite-a/1-source-files/",
        "this_version": [
            "_ELITE_A_VERSION",
            "_ELITE_A_FLIGHT",
            "_ELITE_A_SHIPS_R"
        ],
        "replacements": [
            ('SAVE "versions/elite-a/', 'SAVE "'),
            ('INCBIN "versions/elite-a/', 'INCBIN "'),
            ('INCLUDE "versions/elite-a/1-source-files/main-sources/elite-build-options.asm"', 'INCLUDE "1-source-files/main-sources/elite-build-options.asm"'),
            ('PUTFILE "versions/elite-a/', 'PUTFILE "')
        ],
        "that_version": [
            "_DISC_VERSION",
            "_DISC_FLIGHT"
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/elite-a/1-source-files/main-sources/",
        "source_files": ["elite-ships-s.asm"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/elite-a/1-source-files/",
        "this_version": [
            "_ELITE_A_VERSION",
            "_ELITE_A_FLIGHT",
            "_ELITE_A_SHIPS_S"
        ],
        "replacements": [
            ('SAVE "versions/elite-a/', 'SAVE "'),
            ('INCBIN "versions/elite-a/', 'INCBIN "'),
            ('INCLUDE "versions/elite-a/1-source-files/main-sources/elite-build-options.asm"', 'INCLUDE "1-source-files/main-sources/elite-build-options.asm"'),
            ('PUTFILE "versions/elite-a/', 'PUTFILE "')
        ],
        "that_version": [
            "_DISC_VERSION",
            "_DISC_FLIGHT"
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/elite-a/1-source-files/main-sources/",
        "source_files": ["elite-ships-t.asm"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/elite-a/1-source-files/",
        "this_version": [
            "_ELITE_A_VERSION",
            "_ELITE_A_FLIGHT",
            "_ELITE_A_SHIPS_T"
        ],
        "replacements": [
            ('SAVE "versions/elite-a/', 'SAVE "'),
            ('INCBIN "versions/elite-a/', 'INCBIN "'),
            ('INCLUDE "versions/elite-a/1-source-files/main-sources/elite-build-options.asm"', 'INCLUDE "1-source-files/main-sources/elite-build-options.asm"'),
            ('PUTFILE "versions/elite-a/', 'PUTFILE "')
        ],
        "that_version": [
            "_DISC_VERSION",
            "_DISC_FLIGHT"
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/elite-a/1-source-files/main-sources/",
        "source_files": ["elite-ships-u.asm"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/elite-a/1-source-files/",
        "this_version": [
            "_ELITE_A_VERSION",
            "_ELITE_A_FLIGHT",
            "_ELITE_A_SHIPS_U"
        ],
        "replacements": [
            ('SAVE "versions/elite-a/', 'SAVE "'),
            ('INCBIN "versions/elite-a/', 'INCBIN "'),
            ('INCLUDE "versions/elite-a/1-source-files/main-sources/elite-build-options.asm"', 'INCLUDE "1-source-files/main-sources/elite-build-options.asm"'),
            ('PUTFILE "versions/elite-a/', 'PUTFILE "')
        ],
        "that_version": [
            "_DISC_VERSION",
            "_DISC_FLIGHT"
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/elite-a/1-source-files/main-sources/",
        "source_files": ["elite-ships-v.asm"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/elite-a/1-source-files/",
        "this_version": [
            "_ELITE_A_VERSION",
            "_ELITE_A_FLIGHT",
            "_ELITE_A_SHIPS_V"
        ],
        "replacements": [
            ('SAVE "versions/elite-a/', 'SAVE "'),
            ('INCBIN "versions/elite-a/', 'INCBIN "'),
            ('INCLUDE "versions/elite-a/1-source-files/main-sources/elite-build-options.asm"', 'INCLUDE "1-source-files/main-sources/elite-build-options.asm"'),
            ('PUTFILE "versions/elite-a/', 'PUTFILE "')
        ],
        "that_version": [
            "_DISC_VERSION",
            "_DISC_FLIGHT"
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/elite-a/1-source-files/main-sources/",
        "source_files": ["elite-ships-w.asm"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/elite-a/1-source-files/",
        "this_version": [
            "_ELITE_A_VERSION",
            "_ELITE_A_FLIGHT",
            "_ELITE_A_SHIPS_W"
        ],
        "replacements": [
            ('SAVE "versions/elite-a/', 'SAVE "'),
            ('INCBIN "versions/elite-a/', 'INCBIN "'),
            ('INCLUDE "versions/elite-a/1-source-files/main-sources/elite-build-options.asm"', 'INCLUDE "1-source-files/main-sources/elite-build-options.asm"'),
            ('PUTFILE "versions/elite-a/', 'PUTFILE "')
        ],
        "that_version": [
            "_DISC_VERSION",
            "_DISC_FLIGHT"
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/elite-a/1-source-files/main-sources/",
        "source_files": ["elite-source-docked.asm"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/elite-a/1-source-files/",
        "this_version": [
            "_ELITE_A_VERSION",
            "_ELITE_A_DOCKED"
        ],
        "replacements": [
            ('SAVE "versions/elite-a/', 'SAVE "'),
            ('INCBIN "versions/elite-a/', 'INCBIN "'),
            ('INCLUDE "versions/elite-a/1-source-files/main-sources/elite-build-options.asm"', 'INCLUDE "1-source-files/main-sources/elite-build-options.asm"'),
            ('PUTFILE "versions/elite-a/', 'PUTFILE "')
        ],
        "that_version": [
            "_DISC_VERSION",
            "_DISC_DOCKED"
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/elite-a/1-source-files/main-sources/",
        "source_files": ["elite-source-encyclopedia.asm"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/elite-a/1-source-files/",
        "this_version": [
            "_ELITE_A_VERSION",
            "_ELITE_A_ENCYCLOPEDIA"
        ],
        "replacements": [
            ('SAVE "versions/elite-a/', 'SAVE "'),
            ('INCBIN "versions/elite-a/', 'INCBIN "'),
            ('INCLUDE "versions/elite-a/1-source-files/main-sources/elite-build-options.asm"', 'INCLUDE "1-source-files/main-sources/elite-build-options.asm"'),
            ('PUTFILE "versions/elite-a/', 'PUTFILE "')
        ],
        "that_version": [
            "_DISC_VERSION",
            "_DISC_DOCKED"
        ],
        "disable_diffs_for_whole_routine": [
            "library/enhanced/main/variable/tkn1.asm"
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/elite-a/1-source-files/main-sources/",
        "source_files": ["elite-6502sp-io-processor.asm"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/elite-a/1-source-files/",
        "this_version": [
            "_ELITE_A_VERSION",
            "_ELITE_A_6502SP_IO"
        ],
        "replacements": [
            ('SAVE "versions/elite-a/', 'SAVE "'),
            ('INCBIN "versions/elite-a/', 'INCBIN "'),
            ('INCLUDE "versions/elite-a/1-source-files/main-sources/elite-build-options.asm"', 'INCLUDE "1-source-files/main-sources/elite-build-options.asm"'),
            ('PUTFILE "versions/elite-a/', 'PUTFILE "')
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/elite-a/1-source-files/main-sources/",
        "source_files": ["elite-6502sp-parasite.asm"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/elite-a/1-source-files/",
        "this_version": [
            "_ELITE_A_VERSION",
            "_ELITE_A_6502SP_PARA"
        ],
        "replacements": [
            ('SAVE "versions/elite-a/', 'SAVE "'),
            ('INCBIN "versions/elite-a/', 'INCBIN "'),
            ('INCLUDE "versions/elite-a/1-source-files/main-sources/elite-build-options.asm"', 'INCLUDE "1-source-files/main-sources/elite-build-options.asm"'),
            ('PUTFILE "versions/elite-a/', 'PUTFILE "')
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/elite-a/",
        "source_files": ["Makefile"],
        "do_not_expand_includes": [],
        "dest_folder": "repos/elite-a/",
        "this_version": [
            "_ELITE_A_VERSION"
        ],
        "replacements": [
            ('versions/elite-a/', ''),
            ('_elite-a', ''),
            ('b2-elite-a', 'b2'),
            ('variant-elite-a', 'variant'),
            ('elite-a:', 'all:'),
            (':elite-a', ':all')
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/c64/1-source-files/main-sources/",
        "source_files": ["elite-firebird.asm", "elite-gma1.asm", "elite-gma2.asm", "elite-gma3.asm", "elite-loader.asm", "elite-data.asm", "elite-sprites.asm", "elite-source.asm", "elite-readme.asm", "elite-checksum.asm", "elite-send.asm"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/c64/1-source-files/",
        "this_version": [
            "_C64_VERSION"
        ],
        "replacements": [
            ('SAVE "versions/c64/', 'SAVE "'),
            ('INCBIN "versions/c64/', 'INCBIN "'),
            ('INCLUDE "versions/c64/1-source-files/main-sources/elite-build-options.asm"', 'INCLUDE "1-source-files/main-sources/elite-build-options.asm"'),
            ('PUTFILE "versions/c64/', 'PUTFILE "')
        ],
        "code_style": "6502"
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/c64/2-build-files/",
        "source_files": ["elite-checksum.py", "crc32.py"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/c64/2-build-files/",
        "this_version": [
            "_C64_VERSION"
        ],
        "replacements": [
            ('open("versions/c64/', 'open("')
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/c64/",
        "source_files": ["Makefile"],
        "do_not_expand_includes": [],
        "dest_folder": "repos/c64/",
        "this_version": [
            "_C64_VERSION"
        ],
        "replacements": [
            ('versions/c64/', ''),
            ('_c64', ''),
            ('variant-c64', 'variant'),
            ('c64:', 'all:'),
            (':c64', ':all')
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/apple/1-source-files/main-sources/",
        "source_files": ["elite-bcfs.asm", "elite-mover.asm", "elite-loader.asm", "elite-data.asm", "elite-source.asm", "elite-transfer.asm", "elite-readme.asm", "elite-checksum.asm"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/apple/1-source-files/",
        "this_version": [
            "_APPLE_VERSION"
        ],
        "replacements": [
            ('SAVE "versions/apple/', 'SAVE "'),
            ('INCBIN "versions/apple/', 'INCBIN "'),
            ('INCLUDE "versions/apple/1-source-files/main-sources/elite-build-options.asm"', 'INCLUDE "1-source-files/main-sources/elite-build-options.asm"'),
            ('PUTFILE "versions/apple/', 'PUTFILE "')
        ],
        "code_style": "6502"
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/apple/2-build-files/",
        "source_files": ["elite-checksum.py", "crc32.py"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/apple/2-build-files/",
        "this_version": [
            "_APPLE_VERSION"
        ],
        "replacements": [
            ('open("versions/apple/', 'open("')
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/apple/",
        "source_files": ["Makefile"],
        "do_not_expand_includes": [],
        "dest_folder": "repos/apple/",
        "this_version": [
            "_APPLE_VERSION"
        ],
        "replacements": [
            ('versions/apple/', ''),
            ('versions\\apple\\', ''),
            ('_apple', ''),
            ('variant-apple', 'variant'),
            ('apple:', 'all:'),
            (':apple', ':all')
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/nes/1-source-files/main-sources/",
        "source_files": ["elite-source-bank-0.asm", "elite-source-bank-1.asm", "elite-source-bank-2.asm", "elite-source-bank-3.asm", "elite-source-bank-4.asm", "elite-source-bank-5.asm", "elite-source-bank-6.asm", "elite-source-bank-7.asm", "elite-source-header.asm", "elite-source-common.asm"],
        "do_not_expand_includes": ["elite-build-options.asm", "elite-source-common.asm", "elite-source-bank-0.asm", "elite-source-bank-1.asm", "elite-source-bank-2.asm", "elite-source-bank-3.asm", "elite-source-bank-4.asm", "elite-source-bank-5.asm", "elite-source-bank-6.asm", "elite-source-bank-7.asm"],
        "dest_folder": "repos/nes/1-source-files/",
        "this_version": [
            "_NES_VERSION"
        ],
        "replacements": [
            ('SAVE "versions/nes/', 'SAVE "'),
            ('INCBIN "versions/nes/', 'INCBIN "'),
            ('INCLUDE "versions/nes/1-source-files/main-sources/elite-build-options.asm"', 'INCLUDE "1-source-files/main-sources/elite-build-options.asm"'),
            ('INCLUDE "versions/nes/1-source-files/main-sources/elite-bank-options.asm"', 'INCLUDE "1-source-files/main-sources/elite-bank-options.asm"'),
            ('INCLUDE "versions/nes/1-source-files/main-sources/elite-source-common.asm"', 'INCLUDE "1-source-files/main-sources/elite-source-common.asm"'),
            ('INCLUDE "versions/nes/1-source-files/main-sources/elite-source-bank-0.asm"', 'INCLUDE "1-source-files/main-sources/elite-source-bank-0.asm"'),
            ('INCLUDE "versions/nes/1-source-files/main-sources/elite-source-bank-1.asm"', 'INCLUDE "1-source-files/main-sources/elite-source-bank-1.asm"'),
            ('INCLUDE "versions/nes/1-source-files/main-sources/elite-source-bank-2.asm"', 'INCLUDE "1-source-files/main-sources/elite-source-bank-2.asm"'),
            ('INCLUDE "versions/nes/1-source-files/main-sources/elite-source-bank-3.asm"', 'INCLUDE "1-source-files/main-sources/elite-source-bank-3.asm"'),
            ('INCLUDE "versions/nes/1-source-files/main-sources/elite-source-bank-4.asm"', 'INCLUDE "1-source-files/main-sources/elite-source-bank-4.asm"'),
            ('INCLUDE "versions/nes/1-source-files/main-sources/elite-source-bank-5.asm"', 'INCLUDE "1-source-files/main-sources/elite-source-bank-5.asm"'),
            ('INCLUDE "versions/nes/1-source-files/main-sources/elite-source-bank-6.asm"', 'INCLUDE "1-source-files/main-sources/elite-source-bank-6.asm"'),
            ('INCLUDE "versions/nes/1-source-files/main-sources/elite-source-bank-7.asm"', 'INCLUDE "1-source-files/main-sources/elite-source-bank-7.asm"'),
            ('PUTFILE "versions/nes/', 'PUTFILE "')
        ],
        "code_style": "6502"
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/nes/2-build-files/",
        "source_files": ["crc32.py"],
        "do_not_expand_includes": ["elite-build-options.asm"],
        "dest_folder": "repos/nes/2-build-files/",
        "this_version": [
            "_NES_VERSION"
        ],
        "replacements": [
            ('open("versions/nes/', 'open("')
        ]
    },
    {
        "source_folder": library_repository + "/",
        "section_folder": "versions/nes/",
        "source_files": ["Makefile"],
        "do_not_expand_includes": [],
        "dest_folder": "repos/nes/",
        "this_version": [
            "_NES_VERSION"
        ],
        "replacements": [
            ('versions/nes/', ''),
            ('_nes', ''),
            ('variant-nes', 'variant'),
            ('nes:', 'all:'),
            (':nes', ':all')
        ]
    }
]

remove_lines = [
    "_CASSETTE_VERSION      = (_VERSION = 1)",
    "_DISC_VERSION          = (_VERSION = 2)",
    "_6502SP_VERSION        = (_VERSION = 3)",
    "_MASTER_VERSION        = (_VERSION = 4)",
    "_ELECTRON_VERSION      = (_VERSION = 5)",
    "_ELITE_A_VERSION       = (_VERSION = 6)",
    "_NES_VERSION           = (_VERSION = 7)",
    "_C64_VERSION           = (_VERSION = 8)",
    "_APPLE_VERSION         = (_VERSION = 9)",
    "_DISC_DOCKED           = FALSE",
    "_DISC_FLIGHT           = FALSE",
    "_ELITE_A_DOCKED        = FALSE",
    "_ELITE_A_FLIGHT        = FALSE",
    "_ELITE_A_SHIPS_R       = FALSE",
    "_ELITE_A_SHIPS_S       = FALSE",
    "_ELITE_A_SHIPS_T       = FALSE",
    "_ELITE_A_SHIPS_U       = FALSE",
    "_ELITE_A_SHIPS_V       = FALSE",
    "_ELITE_A_SHIPS_W       = FALSE",
    "_ELITE_A_ENCYCLOPEDIA  = FALSE",
    "_ELITE_A_6502SP_PARA   = FALSE",
    "_ELITE_A_6502SP_IO     = FALSE",
    "_DISC_DOCKED           = TRUE",
    "_DISC_FLIGHT           = TRUE",
    "_ELITE_A_DOCKED        = TRUE",
    "_ELITE_A_FLIGHT        = TRUE",
    "_ELITE_A_SHIPS_R       = TRUE",
    "_ELITE_A_SHIPS_S       = TRUE",
    "_ELITE_A_SHIPS_T       = TRUE",
    "_ELITE_A_SHIPS_U       = TRUE",
    "_ELITE_A_SHIPS_V       = TRUE",
    "_ELITE_A_SHIPS_W       = TRUE",
    "_ELITE_A_ENCYCLOPEDIA  = TRUE",
    "_ELITE_A_6502SP_PARA   = TRUE",
    "_ELITE_A_6502SP_IO     = TRUE"
]

re_include = re.compile(r'^ *INCLUDE "(.+)"$')
re_if = re.compile(r'(IF|OR) (NOT\()?_(CASSETTE_VERSION|6502SP_VERSION|DISC_VERSION|DISC_FLIGHT|DISC_DOCKED|MASTER_VERSION|ELECTRON_VERSION|NES_VERSION|C64_VERSION|APPLE_VERSION|ELITE_A_VERSION|ELITE_A_DOCKED|ELITE_A_FLIGHT|ELITE_A_ENCYCLOPEDIA|ELITE_A_6502SP_PARA|ELITE_A_6502SP_IO|ELITE_A_SHIPS_R|ELITE_A_SHIPS_S|ELITE_A_SHIPS_T|ELITE_A_SHIPS_U|ELITE_A_SHIPS_V|ELITE_A_SHIPS_W)')
re_endif = re.compile(r'^ENDIF.*$')
re_comment = re.compile(r'^\\ \*{78}$')
re_deleted_include = re.compile(r'^\\INCLUDE "(.+)"$')
re_moved_include = re.compile(r'^\\\\INCLUDE "(.+)"$')
re_name = re.compile(r'^\\(       Name): (.+)$')

previous_line_was_blank = False
that_version = []
this_version = []

added_code_start = "                        \\ --- Mod: Code added for Elite-A: -------------------->\n"
added_code_end = "                        \\ --- End of added code ------------------------------->\n"

deleted_code_start = "                        \\ --- Mod: Code removed for Elite-A: ------------------>\n"
deleted_code_end = "                        \\ --- End of removed code ----------------------------->\n"

amended_code_start = "                        \\ --- Mod: Code removed for Elite-A: ------------------>\n"
amended_code_middle = "                        \\ --- And replaced by: -------------------------------->\n"
amended_code_end = "                        \\ --- End of replacement ------------------------------>\n"

added_routine_start = "                        \\ --- Mod: Code added for Elite-A: -------------------->\n"
added_routine_end = "                        \\ --- End of added code ------------------------------->\n"

deleted_routine_start = "                        \\ --- Mod: Code removed for Elite-A: ------------------>\n"
deleted_routine_end = "                        \\ --- End of removed code ----------------------------->\n"
deleted_subtitle = ", Removed\n"

moved_routine_start = "                        \\ --- Mod: Code moved for Elite-A: -------------------->\n"
moved_routine_end = "                        \\ --- End of moved code ------------------------------->\n"
moved_subtitle = ", Moved\n"


def create_folder(name):
    if not os.path.isdir(name):
        os.mkdir(name)


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def should_we_show_this(condition, versions):
    show_this = False
    for version in versions:
        if version in condition:
            show_this = True
    if "NOT(" in condition:
        show_this = not show_this
    return show_this


def comment_out_line(line):
    if re_include.match(line):
        return line
    # if "  \\" in line:
    #     return "\\ " + line.replace("  \\", "\\", 1)
    # elif line.strip() == "":
    #     return "\\\n"
    # else:
    #     return "\\ " + line.replace(" \\", "\\", 1)
    if line[0] == ' ':
        return "\\" + line[1:]
    if " \\" in line:
        return "\\" + line.replace(" \\", "\\", 1)
    else:
        return "\\" + line


def remove_commentary(line):
    return re.sub(r'( +)\\(.*)$', '', line)


def start_header(header, input_file, i, comment_this, comment_all):
    write_line(output_file, header, source_file, False, False)


def end_header(header, input_file, i, comment_this, comment_all):
    write_line(output_file, header, source_file, False, False)


def process_file(input_file, source_file, parent_file, comment_all, wrap_whole_include, deleted_include, moved_include, disable_wrapping):
    global this_version, that_version
    if_stack = []
    include_this = True
    include_that = False
    in_header = False
    this_version_condition_already_met = False
    that_version_condition_already_met = False
    whole_include_start_header_added = False
    comment_this = comment_all
    input_file = input_file.readlines()
    for i in range(len(input_file)):
        line = input_file[i]
        m = re_comment.match(line)
        if m:
            in_header = not in_header

        m = re_if.search(line)
        if m:
            # Version IF or ELIF statement
            if that_version and not in_header and not wrap_whole_include:
                if line.startswith("ELIF "):
                    if_type = if_stack[0]
                    if if_type == 0:
                        if include_this and (include_this != include_that):
                            end_header(added_code_end, input_file, i, comment_this, comment_all)
                        if include_that and (include_this != include_that):
                            end_header(deleted_code_end, input_file, i, comment_this, comment_all)

            include_this = should_we_show_this(line, this_version)

            if that_version and not in_header and not wrap_whole_include:
                if that_version_condition_already_met:
                    # We already output something for this IF block, so skip all the ELIFs
                    include_that = False
                else:
                    include_that = should_we_show_this(line, that_version)
                if include_that and (include_this != include_that):
                    that_version_condition_already_met = True
                    if not comment_this:
                        comment_this = True
                    start_header(deleted_code_start, input_file, i, comment_this, comment_all)
            if this_version_condition_already_met:
                # We already output something for this IF block, so skip all the ELIFs
                include_this = False
            if include_this:
                this_version_condition_already_met = True
                if that_version and (not in_header) and (include_this != include_that) and not wrap_whole_include:
                    comment_this = False
                    start_header(added_code_start, input_file, i, comment_this, comment_all)
            # Version IF statement, type 0 on stack
            if line.startswith("IF "):
                if_stack.append(0)
        elif line.startswith("IF "):
            # Other IF statement, type 1 on stack
            if in_header:
                print("\nERROR: IF...ENDIF found in header in {}".format(parent_file))
            if_stack.append(1)
            if include_this or include_that:
                process_line(output_file, input_file, parent_file, line, source_file, comment_this, comment_all)
        elif re_endif.match(line):
            # ENDIF statement
            if_type = if_stack.pop()
            if if_type == 1:
                if include_this or include_that:
                    process_line(output_file, input_file, parent_file, line, source_file, comment_this, comment_all)
            if if_type == 0:
                if that_version and not in_header and not wrap_whole_include:
                    if include_this and (include_this != include_that):
                        end_header(added_code_end, input_file, i, comment_this, comment_all)
                    if include_that and (include_this != include_that):
                        end_header(deleted_code_end, input_file, i, comment_this, comment_all)
                    comment_this = False
                    include_that = False
                include_this = True
                this_version_condition_already_met = False
                that_version_condition_already_met = False
        elif include_this or include_that:
            # Normal line
            if deleted_include and re_name.match(line):
                line = line.strip() + deleted_subtitle
            elif moved_include and re_name.match(line):
                line = line.strip() + moved_subtitle
            process_line(output_file, input_file, parent_file, line, source_file, comment_this, comment_all)
        if wrap_whole_include and not in_header and not whole_include_start_header_added and not disable_wrapping:
            whole_include_start_header_added = True
            write_line(output_file, "\n", source_file, False, False)
            # Add wrapper to start of whole routine
            if deleted_include:
                start_header(deleted_routine_start, input_file, i, comment_this, comment_all)
                comment_all = True
                this_version, that_version = that_version, this_version
            elif moved_include:
                start_header(moved_routine_start, input_file, i, comment_this, comment_all)
                comment_all = True
                this_version, that_version = that_version, this_version
            else:
                start_header(added_routine_start, input_file, i, comment_this, comment_all)

    if wrap_whole_include and whole_include_start_header_added:
        # Add wrapper to end of whole routine
        if deleted_include:
            comment_all = False
            this_version, that_version = that_version, this_version
            end_header(deleted_routine_end, input_file, i, comment_this, comment_all)
        elif moved_include:
            comment_all = False
            this_version, that_version = that_version, this_version
            end_header(moved_routine_end, input_file, i, comment_this, comment_all)
        else:
            end_header(added_routine_end, input_file, i, comment_this, comment_all)
        write_line(output_file, "\n", source_file, False, False)


def process_line(output_file, input_file, parent_file, line, source_file, comment_this, comment_all):
    m = re_include.match(line)
    n = re_deleted_include.match(line)
    o = re_moved_include.match(line)
    if m:
        include_filename = m.group(1)
        if path_leaf(include_filename) not in do_not_expand_includes:
            # print("Including file: {}".format(include_filename))
            with open(source_folder + include_filename, "r") as include_file:
                if that_version:
                    if include_filename in disable_diffs_for_whole_routine:
                        process_file(include_file, source_file, include_filename, comment_this, wrap_whole_include=True, deleted_include=False, moved_include=False, disable_wrapping=True)
                    else:
                        wrap_subroutine = ("elite-a/" in include_filename) and ("workspace/" not in include_filename) and ("workspace/" not in parent_file or ("workspace/" in parent_file and "variable/" not in include_filename)) and ("subroutine/" in include_filename or "variable/" in include_filename)
                        process_file(include_file, source_file, include_filename, comment_this, wrap_whole_include=wrap_subroutine, deleted_include=False, moved_include=False, disable_wrapping=False)
                else:
                    process_file(include_file, source_file, include_filename, comment_this, wrap_whole_include=False, deleted_include=False, moved_include=False, disable_wrapping=False)
        else:
            write_line(output_file, line, source_file, comment_this, comment_all)
    elif n:
        if that_version:
            include_filename = n.group(1)
            if path_leaf(include_filename) not in do_not_expand_includes:
                # print("Including deleted include: {}".format(include_filename))
                with open(source_folder + include_filename, "r") as include_file:
                    process_file(include_file, source_file, include_filename, comment_all=False, wrap_whole_include=True, deleted_include=True, moved_include=False, disable_wrapping=False)
    elif o:
        if that_version:
            include_filename = o.group(1)
            if path_leaf(include_filename) not in do_not_expand_includes:
                # print("Including moved include: {}".format(include_filename))
                with open(source_folder + include_filename, "r") as include_file:
                    process_file(include_file, source_file, include_filename, comment_all=False, wrap_whole_include=True, deleted_include=False, moved_include=True, disable_wrapping=False)
    else:
        write_line(output_file, line, source_file, comment_this, comment_all)


def write_line(output_file, line, source_file, comment_this, comment_all):
    global previous_line_was_blank
    if source_file.endswith(".asm"):
        if comment_this or comment_all:
            line = comment_out_line(line)
        length = len(line.strip("\n"))
        if not previous_line_was_blank or length > 0:
            if not remove_this_line(line):
                output_file.append(do_replacements(line))
                if length == 0:
                    previous_line_was_blank = True
                else:
                    previous_line_was_blank = False
    else:
        output_file.append(do_replacements(line))


def remove_this_line(line):
    for removal in remove_lines:
        if removal in line:
            return True
    return False


def do_replacements(line):
    for (search, replacement) in replacements:
        line = line.replace(search, replacement)
    return line


def tidy_diff_blocks(input):
    output = []
    buffer_add = []
    buffer_delete = []
    buffer_move = []
    processing_add = False
    processing_delete = False
    processing_move = False
    i = 0
    while i < len(input):
        line = input[i]

        if line.strip() == "" and (not processing_add) and (not processing_delete) and (not processing_move) and (i + 1 < len(input)) and (input[i + 1] == added_code_start or input[i + 1] == deleted_code_start or input[i + 1] == moved_routine_start):
            # Blank line between consecutive diff blocks
            pass

        elif line.strip() != "" and (not processing_add) and (not processing_delete) and (not processing_move) and (i + 1 < len(input)) and line != added_code_start and line != deleted_code_start and line != moved_routine_start:
            # End of consecutive diff blocks, so we output them

            # Check for blocks that contain identical code (ignoring commentary and blank lines)
            match = False
            if len(buffer_delete) > 0 or len(buffer_add) > 0:
                match = True
                j = 0
                k = 0
                while j < len(buffer_delete) or k < len(buffer_add):
                    if j < len(buffer_delete):
                        del_line = remove_commentary(buffer_delete[j])
                    else:
                        del_line = "\\"
                    if k < len(buffer_add):
                        add_line = remove_commentary(comment_out_line(buffer_add[k]))
                    else:
                        add_line = "\\"
                    if j < len(buffer_delete) and del_line.strip() == "\\":
                        j += 1
                        continue
                    if k < len(buffer_add) and add_line.strip() == "\\":
                        k += 1
                        continue
                    if del_line != add_line:
                        match = False
                        break
                    j += 1
                    k += 1

            if match:
                # Diffs contain the same code, so output the Elite-A code rather than a diff
                for newline in buffer_add:
                    add_line_to_buffer(output, newline)

            else:
                # Output both diffs, as they aren't duplicates
                before = []
                after = []
                if buffer_delete and buffer_add:
                    shrink_diffs(buffer_delete, buffer_add, before, after, output)
                for moved_line in before:
                    add_line_to_buffer(output, moved_line)
                if buffer_delete:
                    add_line_to_buffer(output, "\n")
                    if buffer_add:
                        output.append(amended_code_start)
                    else:
                        output.append(deleted_code_start)
                    add_line_to_buffer(output, "\n")
                    if buffer_delete[0].strip() == "\\":
                        buffer_delete = buffer_delete[1:]
                    if buffer_delete and buffer_delete[-1].strip() == "\\":
                        buffer_delete.pop()
                    for newline in buffer_delete:
                        add_line_to_buffer(output, newline)
                    add_line_to_buffer(output, "\n")
                    if buffer_add:
                        output.append(amended_code_middle)
                        add_line_to_buffer(output, "\n")
                    else:
                        output.append(deleted_code_end)
                    add_line_to_buffer(output, "\n")
                if buffer_add:
                    if not buffer_delete:
                        add_line_to_buffer(output, "\n")
                        output.append(added_code_start)
                        add_line_to_buffer(output, "\n")
                    for newline in buffer_add:
                        add_line_to_buffer(output, newline)
                    add_line_to_buffer(output, "\n")
                    if buffer_delete:
                        output.append(amended_code_end)
                    else:
                        output.append(added_code_end)
                    add_line_to_buffer(output, "\n")
                if buffer_move:
                    output.append(moved_routine_start)
                    add_line_to_buffer(output, "\n")
                    if buffer_move[0].strip() == "\\":
                        buffer_move = buffer_move[1:]
                    if buffer_move and buffer_move[-1].strip() == "\\":
                        buffer_move.pop()
                    for newline in buffer_move:
                        add_line_to_buffer(output, newline)
                    add_line_to_buffer(output, "\n")
                    output.append(moved_routine_end)
                    add_line_to_buffer(output, "\n")
                for moved_line in after:
                    add_line_to_buffer(output, moved_line)

            buffer_delete = []
            buffer_add = []
            buffer_move = []

        if line == added_code_start:
            processing_add = True

        elif line == deleted_code_start:
            processing_delete = True

        elif line == moved_routine_start:
            processing_move = True

        elif line == added_code_end:
            processing_add = False

        elif line == deleted_code_end:
            processing_delete = False

        elif line == moved_routine_end:
            processing_move = False

        elif processing_add:
            add_line_to_buffer(buffer_add, line)

        elif processing_delete:
            add_line_to_buffer(buffer_delete, line)

        elif processing_move:
            add_line_to_buffer(buffer_move, line)

        else:
            add_line_to_buffer(output, line)

        i += 1

    return output


def add_line_to_buffer(buffer, line):
    if len(buffer) > 0 and line.strip() == "":
        if buffer[-1].strip() != "":
            buffer.append(line)
    elif len(buffer) > 0 and line.strip() == "\\":
        if buffer[-1].strip() != "\\":
            buffer.append(line)
    else:
        buffer.append(line)


def shrink_diffs(buffer_delete, buffer_add, before, after, output):
    shrink_from_start(buffer_delete, buffer_add, before, output)
    buffer_delete.reverse()
    buffer_add.reverse()
    shrink_from_start(buffer_delete, buffer_add, after, output)
    buffer_delete.reverse()
    buffer_add.reverse()
    after.reverse()


def shrink_from_start(buffer_delete, buffer_add, before_or_after, output):
    # output.append("buffer_delete:\n")
    # for b in buffer_delete:
    #     output.append(b)
    # output.append("buffer_add:\n")
    # for b in buffer_add:
    #     output.append(b)
    min_length = min(len(buffer_delete), len(buffer_add))
    i = 0
    matched_all_lines = True
    while i < min_length:
        # output.append("Checking line " + str(i) + "\n")
        # output.append(buffer_delete[i])
        # output.append(comment_out_line(buffer_add[i]))
        if buffer_delete[i] != comment_out_line(buffer_add[i]):
            # output.append("NO MATCH on line " + str(i) + "\n")
            matched_all_lines = False
            if i > 0:
                if buffer_add[i - 1].strip() == "":
                    move_lines_out_of_top(i, buffer_delete, buffer_add, before_or_after, output)
                else:
                    # output.append("Looking backwards from " + str(i) + " for blank line:\n")
                    for j in range(i, 0, -1):
                        # output.append("Checking line " + str(j) + " for blanks\n")
                        if buffer_add[j].strip() == "" and j > 0:
                            # output.append("Line " + str(j) + " is blank\n")
                            move_lines_out_of_top(j, buffer_delete, buffer_add, before_or_after, output)
                            break
            break
        i += 1
    if matched_all_lines:
        move_lines_out_of_top(i, buffer_delete, buffer_add, before_or_after, output)


def move_lines_out_of_top(i, buffer_delete, buffer_add, before, output):
    # output.append("Moving first " + str(i) + " lines \n")
    # output.append("BEFORE buffer_delete:\n")
    # for b in buffer_delete:
    #     output.append(b)
    # output.append("BEFORE buffer_add:\n")
    # for b in buffer_add:
    #     output.append(b)
    before.extend(buffer_add[0:i])
    del buffer_add[:i]
    del buffer_delete[:i]
    # output.append("AFTER buffer_delete:\n")
    # for b in buffer_delete:
    #     output.append(b)
    # output.append("AFTER buffer_add:\n")
    # for b in buffer_add:
    #     output.append(b)


def code_style_6502(line):
    line = re.sub(r"&([0-9A-Fx]+)\b", r"$\1", line)
    line = re.sub(r"^\\", ";", line)
    line = re.sub(r"^([^\\]+ )\\", r"\1;", line)
    line = re.sub(r"^([^\\]+'\\'[^\\]+ )\\", r"\1;", line)
    return line


create_folder("repos")

create_folder("repos/cassette")
create_folder("repos/disc")
create_folder("repos/6502sp")
create_folder("repos/master")
create_folder("repos/electron")
create_folder("repos/elite-a")
create_folder("repos/c64")
create_folder("repos/apple")
create_folder("repos/nes")

create_folder("repos/cassette/1-source-files")
create_folder("repos/disc/1-source-files")
create_folder("repos/6502sp/1-source-files")
create_folder("repos/master/1-source-files")
create_folder("repos/electron/1-source-files")
create_folder("repos/elite-a/1-source-files")
create_folder("repos/c64/1-source-files")
create_folder("repos/apple/1-source-files")
create_folder("repos/nes/1-source-files")

create_folder("repos/cassette/2-build-files")
create_folder("repos/disc/2-build-files")
create_folder("repos/6502sp/2-build-files")
create_folder("repos/master/2-build-files")
create_folder("repos/electron/2-build-files")
create_folder("repos/elite-a/2-build-files")
create_folder("repos/c64/2-build-files")
create_folder("repos/apple/2-build-files")
create_folder("repos/nes/2-build-files")

print("Generating source files: ", end="", flush=True)

for site in sites:
    source_folder = site["source_folder"]
    section_folder = site["section_folder"]
    source_files = site["source_files"]
    do_not_expand_includes = site["do_not_expand_includes"]
    dest_folder = site["dest_folder"]
    this_version = site["this_version"]
    replacements = site["replacements"]
    if "that_version" in site:
        that_version = site["that_version"]
    else:
        that_version = []
    if "disable_diffs_for_whole_routine" in site:
        disable_diffs_for_whole_routine = site["disable_diffs_for_whole_routine"]
    else:
        disable_diffs_for_whole_routine = []
    if "code_style" in site:
        code_style = site["code_style"]
    else:
        code_style = "bbc"

    for source_file in source_files:
        input = source_folder + section_folder + source_file

        with open(input, "r") as input_file:
            output = dest_folder + source_file
            print(".", end="", flush=True)

            output_file = []
            process_file(input_file, source_file, parent_file="", comment_all=False, wrap_whole_include=False, deleted_include=False, moved_include=False, disable_wrapping=False)
            if that_version and source_file.endswith(".asm"):
                output_file = tidy_diff_blocks(output_file)
            with open(output, "w") as file_to_write:
                for line in output_file:
                    if code_style == "6502":
                        line = code_style_6502(line)
                    file_to_write.write(line)

print()
