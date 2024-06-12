# Scripts for building the bbcelite.com website and associated repositories

This repository contains Mac/Linux scripts to build the following repositories from the [Elite library repository](https://github.com/markmoxon/library-elite-beebasm):

* [BBC Micro (cassette) Elite source code](https://github.com/markmoxon/cassette-elite-beebasm)
* [BBC Micro (disc) Elite source code](https://github.com/markmoxon/disc-elite-beebasm)
* [6502 Second Processor Elite source code](https://github.com/markmoxon/6502sp-elite-beebasm)
* [BBC Master Elite source code](https://github.com/markmoxon/master-elite-beebasm)
* [Acorn Electron Elite source code](https://github.com/markmoxon/electron-elite-beebasm)
* [Elite-A source code](https://github.com/markmoxon/elite-a-beebasm)
* [NES Elite source code](https://github.com/markmoxon/nes-elite-beebasm)

It also contains scripts to generate the code sections of following websites:

* [Elite website](https://www.bbcelite.com)
* [Aviator website](https://aviator.bbcelite.com)
* [Revs website](https://revs.bbcelite.com)
* [Lander website](https://lander.bbcelite.com)

The Elite website is generated from the source code repositories listed above, while the other sites are generated from the following source code repositories:

* [Aviator source code](https://github.com/markmoxon/aviator-beebasm)
* [Revs source code](https://github.com/markmoxon/revs-beebasm)
* [Lander source code](https://github.com/markmoxon/archimedes-lander)

# Setup

## 1. Pull repositories

Create a folder for the various Elite repositories and clone them, so you have one folder containing the following repository folders:

* [library-elite-beebasm](https://github.com/markmoxon/library-elite-beebasm)
* [cassette-elite-beebasm](https://github.com/markmoxon/cassette-elite-beebasm)
* [disc-elite-beebasm](https://github.com/markmoxon/disc-elite-beebasm)
* [6502sp-elite-beebasm](https://github.com/markmoxon/6502sp-elite-beebasm)
* [master-elite-beebasm](https://github.com/markmoxon/master-elite-beebasm)
* [electron-elite-beebasm](https://github.com/markmoxon/electron-elite-beebasm)
* [elite-a-beebasm](https://github.com/markmoxon/elite-a-beebasm)
* [nes-elite-beebasm](https://github.com/markmoxon/nes-elite-beebasm)

Also clone the following repositories (they don't have to be in the same place, but can be if you like):

* [aviator-beebasm](https://github.com/markmoxon/aviator-beebasm)
* [revs-beebasm](https://github.com/markmoxon/revs-beebasm)
* [archimedes-lander](https://github.com/markmoxon/archimedes-lander)

## 2. Set environment variables

The following environment variables need to be set up for the scripts to work. They should contain the full paths of the relevant folders.

### All sites

`$BBCELITE_SCRIPTS` = this repository (i.e. bbcelite-scripts)

### Elite

`$ELITE_CODE_REPOSITORIES` = the folder containing the *-elite-beebasm repositories that we cloned above

`$ELITE_WEBSITE` = the root folder of the Elite website we want to generate

`$ELITE_WEBSITE_REPOSITORY` = a repository for tracking changes to the generated site

### Aviator

`$AVIATOR_CODE_REPOSITORY` = the path of the aviator-beebasm repository that we cloned above

`$AVIATOR_WEBSITE` = the root folder of the Aviator website we want to generate

`$AVIATOR_WEBSITE_REPOSITORY` = a repository for tracking changes to the generated site

### Revs

`$REVS_CODE_REPOSITORY` = the path of the revs-beebasm repository that we cloned above

`$REVS_WEBSITE` = the root folder of the Revs website we want to generate

`$REVS_WEBSITE_REPOSITORY` = a repository for tracking changes to the generated site

### Lander

`$LANDER_CODE_REPOSITORY` = the path of the archimedes-lander repository that we cloned above

`$LANDER_WEBSITE` = the root folder of the Lander website we want to generate

`$LANDER_WEBSITE_REPOSITORY` = a repository for tracking changes to the generated site

### Example environment variables

Here's an example setup that could be added to a .bashrc or .zshenv file:

```
export BBCELITE_SCRIPTS=~/Sites/Repositories/bbcelite-scripts

export ELITE_CODE_REPOSITORIES=/Documents/Elite/Repositories
export ELITE_WEBSITE=~/Sites/bbcelite.com
export ELITE_WEBSITE_REPOSITORY=~/Sites/staging.bbcelite.com

export AVIATOR_CODE_REPOSITORY=/Documents/Aviator/Repositories/aviator-beebasm
export AVIATOR_WEBSITE=~/Sites/aviator.bbcelite.com
export AVIATOR_WEBSITE_REPOSITORY=~/Sites/staging.aviator.bbcelite.com

export REVS_CODE_REPOSITORY=/Documents/Revs/Repositories/revs-beebasm
export REVS_WEBSITE=~/Sites/revs.bbcelite.com
export REVS_WEBSITE_REPOSITORY=~/Sites/staging.revs.bbcelite.com

export LANDER_CODE_REPOSITORY=/Documents/Lander/Repositories/archimedes-lander
export LANDER_WEBSITE=~/Sites/lander.bbcelite.com
export LANDER_WEBSITE_REPOSITORY=~/Sites/staging.lander.bbcelite.com
```

# Running the scripts

First, cd into this repository's folder:

```
cd $BBCELITE_SCRIPTS
```

Then you can generate the repositories/sites by running the relevant generate scripts. This script:

```
./generate-elite.sh
```

will update the *-elite-beebasm repositories with the latest content from the library, and will then generate the www.bbcelite.com site from the updated source code repositories.

These scripts:

```
./generate-aviator.sh
./generate-revs.sh
./generate-lander.sh
```

will generate the three *.bbcelite.com sites from the source code repositories.

---

Right on, Commanders!

_Mark Moxon_