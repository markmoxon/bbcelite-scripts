# Scripts for generating the bbcelite.com website and associated repositories



## Purpose

This repository contains scripts that generate these repositories that contain the Elite source code for various platforms:

* [BBC Micro (cassette) Elite source code](https://github.com/markmoxon/cassette-elite-beebasm)
* [BBC Micro (disc) Elite source code](https://github.com/markmoxon/disc-elite-beebasm)
* [6502 Second Processor Elite source code](https://github.com/markmoxon/6502sp-elite-beebasm)
* [BBC Master Elite source code](https://github.com/markmoxon/master-elite-beebasm)
* [Acorn Electron Elite source code](https://github.com/markmoxon/electron-elite-beebasm)
* [Elite-A source code](https://github.com/markmoxon/elite-a-beebasm)
* [NES Elite source code](https://github.com/markmoxon/nes-elite-beebasm)

and it also contains scripts to generate the code sections of these disassembly websites:

* [Elite website](https://www.bbcelite.com)
* [Aviator website](https://aviator.bbcelite.com)
* [Revs website](https://revs.bbcelite.com)
* [Lander website](https://lander.bbcelite.com)

The Elite source code repositories are all generated from a single Elite library repository:

* [library-elite-beebasm](https://github.com/markmoxon/library-elite-beebasm)

and the Elite website is generated from both the source code repositories and the library repository.

The other three sites are generated from these source code repositories:

* [Aviator source code](https://github.com/markmoxon/aviator-beebasm)
* [Revs source code](https://github.com/markmoxon/revs-beebasm)
* [Lander source code](https://github.com/markmoxon/archimedes-lander)

I have only tested this build process on a Mac. In theory these scripts should also work in Linux, and they might also work on Windows using Git Bash or Windows Subsystem for Linux, but I haven't tried anything other than a Mac-based build.

Python 3 is required.

## Setup

The following setup will enable you to run the scripts and see them generating the source code and websites on bbcelite.com.

### 1. Clone the Elite repositories

Create a parent folder to hold the various repositories and websites that we are going to generate. This will be the folder that we set in the `$ELITE_CODE_REPOSITORIES` variable in the next step. Also, set the current directory to this folder:

```
mkdir /path/to/generated/content
cd /path/to/generated/content
```

Clone the [library-elite-beebasm](https://github.com/markmoxon/library-elite-beebasm) and [bbcelite-scripts](https://github.com/markmoxon/bbcelite-scripts )repositories into the parent folder (i.e. into `$ELITE_CODE_REPOSITORIES/library-elite-beebasm` and `$ELITE_CODE_REPOSITORIES/bbcelite-scripts`).

```
git clone https://github.com/markmoxon/library-elite-beebasm
git clone https://github.com/markmoxon/bbcelite-scripts
```

Create empty folders that will hold the generated source code repositories:

```
mkdir cassette-elite-beebasm
mkdir disc-elite-beebasm
mkdir 6502sp-elite-beebasm
mkdir master-elite-beebasm
mkdir electron-elite-beebasm
mkdir elite-a-beebasm
mkdir nes-elite-beebasm
```

Next, create folders for the website and staging website repository. These will contain identical content, but there are two of them to allow content changes to be tracked via a staging repository that is separate from the website content in the web server (as the latter mixes generated and static content). These folders can go anywhere, but for now let's put them in the same place:

```
mkdir bbcelite.com
mkdir staging.bbcelite.com
```

These folder paths will be set in the `$ELITE_WEBSITE` and `$ELITE_WEBSITE_REPOSITORY` variables in the next step.

### 2. Clone the Aviator, Revs and Lander repositories

Next, create folders for the website and staging website repository for each of the three other sites (Aviator, Revs and Lander). These folders can go anywhere, but for now let's put them in the same place:

```
mkdir aviator.bbcelite.com
mkdir staging.aviator.bbcelite.com

mkdir revs.bbcelite.com
mkdir staging.revs.bbcelite.com

mkdir lander.bbcelite.com
mkdir staging.lander.bbcelite.com
```

These folder paths will be set in the `$AVIATOR_WEBSITE`, `$AVIATOR_WEBSITE_REPOSITORY`, `$REVS_WEBSITE`, `$REVS_WEBSITE_REPOSITORY`, `$LANDER_WEBSITE` and `$LANDER_WEBSITE_REPOSITORY` variables in the next step.

Finally, clone the source code repositories for Aviator, Revs and Lander.  These folders can go anywhere, but for now let's put them in the same place:

```
git clone https://github.com/markmoxon/aviator-beebasm
git clone https://github.com/markmoxon/revs-beebasm
git clone https://github.com/markmoxon/archimedes-lander
```

### 3. Set environment variables

The following environment variables need to be set up for the scripts to work. They should contain the full paths of the relevant folders that we set up above - see the end of this section for the correct settings to use for the above setup.

#### All sites

`$BBCELITE_SCRIPTS` = this repository (i.e. bbcelite-scripts)

#### Elite

`$ELITE_CODE_REPOSITORIES` = the folder containing the *-elite-beebasm repositories that we cloned above

`$ELITE_WEBSITE` = the root folder of the Elite website we want to generate

`$ELITE_WEBSITE_REPOSITORY` = a staging repository for tracking changes to the generated site

#### Aviator

`$AVIATOR_CODE_REPOSITORY` = the path of the aviator-beebasm repository that we cloned above

`$AVIATOR_WEBSITE` = the root folder of the Aviator website we want to generate

`$AVIATOR_WEBSITE_REPOSITORY` = a staging repository for tracking changes to the generated site

#### Revs

`$REVS_CODE_REPOSITORY` = the path of the revs-beebasm repository that we cloned above

`$REVS_WEBSITE` = the root folder of the Revs website we want to generate

`$REVS_WEBSITE_REPOSITORY` = a staging repository for tracking changes to the generated site

#### Lander

`$LANDER_CODE_REPOSITORY` = the path of the archimedes-lander repository that we cloned above

`$LANDER_WEBSITE` = the root folder of the Lander website we want to generate

`$LANDER_WEBSITE_REPOSITORY` = a staging repository for tracking changes to the generated site

#### Set the environment variables

Here are the values to set for the configuration above. The easiest way to set these variables is to save the following as a file called `env.sh`, and then execute it with `source env.sh`:

```
export BBCELITE_SCRIPTS=/path/to/generated/content/bbcelite-scripts

export ELITE_CODE_REPOSITORIES=/path/to/generated/content
export ELITE_WEBSITE=/path/to/generated/content/bbcelite.com
export ELITE_WEBSITE_REPOSITORY=/path/to/generated/content/staging.bbcelite.com

export AVIATOR_CODE_REPOSITORY=/path/to/generated/content/aviator-beebasm
export AVIATOR_WEBSITE=/path/to/generated/content/aviator.bbcelite.com
export AVIATOR_WEBSITE_REPOSITORY=/path/to/generated/content/staging.aviator.bbcelite.com

export REVS_CODE_REPOSITORY=/path/to/generated/content/revs-beebasm
export REVS_WEBSITE=/path/to/generated/content/revs.bbcelite.com
export REVS_WEBSITE_REPOSITORY=/path/to/generated/content/staging.revs.bbcelite.com

export LANDER_CODE_REPOSITORY=/path/to/generated/content/archimedes-lander
export LANDER_WEBSITE=/path/to/generated/content/lander.bbcelite.com
export LANDER_WEBSITE_REPOSITORY=/path/to/generated/content/staging.lander.bbcelite.com
```

Alternatively you can add the above to your `.bashrc` or `.zshenv` file so that the variables are set for every shell that you open (if you do this, then you should close and re-open the terminal and `cd` back into the folder, to ensure that the variables are set).

### 4. Run the scripts for Elite

Now let's generate the Elite source repositories and website.

First, cd into this repository's folder as follows:

```
cd $BBCELITE_SCRIPTS
```

Now generate the repositories and website by running this script:

```
./generate-elite.sh
```

This will generate source code in each of the `*-elite-beebasm` folders using the content from the library repository, and it will then generate the code pages for the www.bbcelite.com site from the contents of those source code folders.

In other words, it will create the contents of the following repositories in the `*-elite-beebasm` folders that we created above:

* [cassette-elite-beebasm](https://github.com/markmoxon/cassette-elite-beebasm)
* [disc-elite-beebasm](https://github.com/markmoxon/disc-elite-beebasm)
* [6502sp-elite-beebasm](https://github.com/markmoxon/6502sp-elite-beebasm)
* [master-elite-beebasm](https://github.com/markmoxon/master-elite-beebasm)
* [electron-elite-beebasm](https://github.com/markmoxon/electron-elite-beebasm)
* [elite-a-beebasm](https://github.com/markmoxon/elite-a-beebasm)
* [nes-elite-beebasm](https://github.com/markmoxon/nes-elite-beebasm)

and it will create the website pages in the `bbcelite.com` and `staging.bbcelite.com` folders.

This is how I generate the source code repositories for Elite, so that updating the commentary in the library repository automatically updates the individual source code repositories.

### 5. Run the scripts for Aviator, Revs and Lander

Next, let's generate the other websites by running the relevant generate scripts.

These scripts:

```
./generate-aviator.sh
./generate-revs.sh
./generate-lander.sh
```

will generate each of the three `*.bbcelite.com` sites and corresponding staging repositories from the relevant source code repositories.

### 6. Merge the generated web content into the static website

The final step is to merge the generated website content with the static pages, such as the deep dives, homepage, images, CSS, JavaScript and so on. I have not yet released the static files to a public repository, but I plan to, at which point you will be able to generate the repositories and websites in their entirety.

---

Right on, Commanders!

_Mark Moxon_