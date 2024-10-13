# Scripts for generating the bbcelite.com website and associated repositories

**Scripts for generating bbcelite.com** | [Static content for bbcelite.com](https://github.com/markmoxon/bbcelite-websites) | [Elite source code library](https://github.com/markmoxon/elite-source-code-library)

This repository contains scripts that use the following hand-crafted repositories:

* [Elite source code library](https://github.com/markmoxon/elite-source-code-library)
* [Aviator source code](https://github.com/markmoxon/aviator-source-code-bbc-micro)
* [Revs source code](https://github.com/markmoxon/revs-source-code-bbc-micro)
* [Lander source code](https://github.com/markmoxon/archimedes-lander)
* [Static content for bbcelite.com](https://github.com/markmoxon/bbcelite-websites)

to generate the following source code repositories:

* [BBC Micro (cassette) Elite source code](https://github.com/markmoxon/elite-source-code-bbc-micro-cassette)
* [BBC Micro (disc) Elite source code](https://github.com/markmoxon/elite-source-code-bbc-micro-disc)
* [6502 Second Processor Elite source code](https://github.com/markmoxon/elite-source-code-6502-second-processor)
* [BBC Master Elite source code](https://github.com/markmoxon/elite-source-code-bbc-master)
* [Acorn Electron Elite source code](https://github.com/markmoxon/elite-source-code-acorn-electron)
* [NES Elite source code](https://github.com/markmoxon/elite-source-code-nes)
* [Elite-A source code](https://github.com/markmoxon/elite-a-source-code-bbc-micro)

and the following websites:

* [Mark Moxon's Software Archaeology](https://www.bbcelite.com)
* [Elite on the BBC Micro and NES](https://elite.bbcelite.com)
* [Aviator on the BBC Micro](https://aviator.bbcelite.com)
* [Revs on the BBC Micro](https://revs.bbcelite.com)
* [Lander on the Acorn Archimedes](https://lander.bbcelite.com)

For details of how the site and source code repositories are built, see the [bbcelite.com website](https://www.bbcelite.com/disassembly_websites/).

## Scripts in this repository

This repository contains a number of scripts that are used to manage my source code projects. They are:

* [disassembly-website-generator](disassembly-website-generator) generates the bbcelite.com website (see below)
* [elite-repository-generator](elite-repository-generator) generates the Elite source code repositories (see below)
* [code-analysis](code-analysis) includes a number of scripts for analysing the content in my source code projects

## Running the site generation scripts

If you want to see this automatic generation working, then the following steps will enable you to set up the process on your own machine. You can then generate all the source code repositories and websites listed above, using the exact same process that I use to maintain my sites.

Note that I have only tested this build process on a Mac. In theory these scripts should also work in Linux, and they might also work on Windows using Git Bash or Windows Subsystem for Linux, but I haven't tried anything other than a Mac-based build.

Python 3 is required.

### 1. Clone the source repositories

First, we need to create a parent folder to hold the various repositories and websites that we are going to generate. The generation process will only create files within this folder, so you can clean up afterwards by simply deleting the folder and its contents.

I will refer to this path as `/path/to/websites` in the following documentation; you should change this to the actual path of the folder that you create.

Let's start by creating our parent folder and setting the current directory to this folder:

```
mkdir /path/to/websites
cd /path/to/websites
```

Next, create some folders to hold the source repositories and generated content:

```
mkdir source-repositories
mkdir generated-repositories
mkdir generated-websites
```

Then clone the static website content into the parent folder:

```
git clone https://github.com/markmoxon/bbcelite-websites
```

This will create a folder called `bbcelite-websites` that contains the static content for each of the websites. As we generate our web content, it will be copied into the relevant site folders in `bbcelite-websites` to form the finished sites.

Finally clone this repository (which contains the generation scripts) and the source code repositories into the `source-repositories` folder:

```
cd source-repositories

git clone https://github.com/markmoxon/bbcelite-scripts
git clone https://github.com/markmoxon/elite-source-code-library
git clone https://github.com/markmoxon/aviator-source-code-bbc-micro
git clone https://github.com/markmoxon/revs-source-code-bbc-micro
git clone https://github.com/markmoxon/archimedes-lander
```

We have now cloned all the source content, so let's look at the generated content next.

### 2. Create empty folders for the generated content

Start by creating empty folders in `generated-repositories` that will hold the generated source code repositories:

```
cd ../generated-repositories

mkdir elite-source-code-bbc-micro-cassette
mkdir elite-source-code-bbc-micro-disc
mkdir elite-source-code-6502-second-processor
mkdir elite-source-code-bbc-master
mkdir elite-source-code-acorn-electron
mkdir elite-source-code-nes
mkdir elite-a-source-code-bbc-micro
```

Next, create folders for the staging website repositories in the `generated-websites` folder:

```
cd ../generated-websites

mkdir staging.elite.bbcelite.com
mkdir staging.aviator.bbcelite.com
mkdir staging.revs.bbcelite.com
mkdir staging.lander.bbcelite.com
```

The idea behind the staging repositories is that they will only ever contain generated content, so we can track changes to that content easily. We want to do this when updating the generation scripts, so we can make sure our changes look correct. The complete websites will also contain this generated content, but there it's combined with the static content, so having a separate staging repository helps us keep an eye on the generated content separately, without the distraction of the static content.

### 3. Set the environment variables

Next, we set the environment variables that are needed by the generation scripts.

To do this, create a shell script called `env.sh` in our parent folder:

```
cd ..
touch env.sh
```

Open the `env.sh` file in your preferred text editor and paste in the following content, making sure to change `/path/to/websites` to the correct path for the parent folder that we created in step 1:

```
export BBCELITE_SCRIPTS=/path/to/websites/source-repositories/bbcelite-scripts
export BBCELITE_WEBSITE=/path/to/websites/bbcelite-websites/bbcelite.com

export ELITE_LIBRARY_REPOSITORY=/path/to/websites/source-repositories/elite-source-code-library
export ELITE_CODE_REPOSITORIES=/path/to/websites/generated-repositories
export ELITE_WEBSITE=/path/to/websites/bbcelite-websites/elite.bbcelite.com
export ELITE_WEBSITE_REPOSITORY=/path/to/websites/generated-websites/staging.elite.bbcelite.com

export AVIATOR_CODE_REPOSITORY=/path/to/websites/source-repositories/aviator-source-code-bbc-micro
export AVIATOR_WEBSITE=/path/to/websites/bbcelite-websites/aviator.bbcelite.com
export AVIATOR_WEBSITE_REPOSITORY=/path/to/websites/generated-websites/staging.aviator.bbcelite.com

export REVS_CODE_REPOSITORY=/path/to/websites/source-repositories/revs-source-code-bbc-micro
export REVS_WEBSITE=/path/to/websites/bbcelite-websites/revs.bbcelite.com
export REVS_WEBSITE_REPOSITORY=/path/to/websites/generated-websites/staging.revs.bbcelite.com

export LANDER_CODE_REPOSITORY=/path/to/websites/source-repositories/archimedes-lander
export LANDER_WEBSITE=/path/to/websites/bbcelite-websites/lander.bbcelite.com
export LANDER_WEBSITE_REPOSITORY=/path/to/websites/generated-websites/staging.lander.bbcelite.com
```

Now we can execute this script with the following command, to export the environment variables to the current shell:

```
source env.sh
```

[See below](#environment-variables) for more information on these environment variables, advice on automating this step, and details on how to set up a different folder structure to the all-in-one approach used in this example.

### 4. Run the generation script for Elite

Now let's generate the Elite source repositories in `generated-repositories`:

* [elite-source-code-bbc-micro-cassette](https://github.com/markmoxon/elite-source-code-bbc-micro-cassette)
* [elite-source-code-bbc-micro-disc](https://github.com/markmoxon/elite-source-code-bbc-micro-disc)
* [elite-source-code-6502-second-processor](https://github.com/markmoxon/elite-source-code-6502-second-processor)
* [elite-source-code-bbc-master](https://github.com/markmoxon/elite-source-code-bbc-master)
* [elite-source-code-acorn-electron](https://github.com/markmoxon/elite-source-code-acorn-electron)
* [elite-source-code-nes](https://github.com/markmoxon/elite-source-code-nes)
* [elite-a-source-code-bbc-micro](https://github.com/markmoxon/elite-a-source-code-bbc-micro)

and the Elite source code website in `bbcelite-websites/elite.bbcelite.com`:

* [elite.bbcelite.com](https://elite.bbcelite.com)

First, switch to the `bbcelite-scripts` repository folder:

```
cd $BBCELITE_SCRIPTS
```

Next, generate the repositories and website by running this script:

```
./generate-elite.sh
```

Note that this will take quite a while to run, but progress is shown throughout.

This script does two things:

* It generates the source code repositories in each of the empty folders in `generated-repositories`, using the content from the Elite library repository as the source.

* It generates the code pages for the Elite source code website from the contents of those newly generated source code repositories.

The script copies the generated content into both the `staging.elite.bbcelite.com` folder (where it can be tracked), and into the `elite.bbcelite.com` folder in the `bbcelite-websites` repository. Because the latter already contains the static content for the website, the end result is a complete copy of the Elite source code website, here:

`/path/to/websites/bbcelite-websites/elite.bbcelite.com`

Changing the Elite library content and re-running the generation script will automatically update both the source code repositories and the website.

### 5. Run the generation scripts for Aviator, Revs and Lander

Next, let's generate the other websites by running the relevant generate scripts. This process is a lot quicker than for Elite, as there's only one version of each game and there's no code comparision in the websites.

This command:

```
./generate-aviator.sh
```

will generate the [aviator.bbcelite.com](https://aviator.bbcelite.com) site and the corresponding staging repository, taking the source code from the [aviator-source-code-bbc-micro](https://github.com/markmoxon/aviator-source-code-bbc-micro) source code repository and creating a complete site here:

`/path/to/websites/bbcelite-websites/aviator.bbcelite.com`

Similarly, this command:

```
./generate-revs.sh
```

will generate the [revs.bbcelite.com](https://revs.bbcelite.com) site and the corresponding staging repository, taking the source code from the [revs-source-code-bbc-micro](https://github.com/markmoxon/revs-source-code-bbc-micro) source code repository and creating a complete site here:

`/path/to/websites/bbcelite-websites/revs.bbcelite.com`

and this command:

```
./generate-lander.sh
```

will generate the [lander.bbcelite.com](https://lander.bbcelite.com) site and the corresponding staging repository, taking the source code from the [archimedes-lander](https://github.com/markmoxon/archimedes-lander) source code repository and creating a complete site here:

`/path/to/websites/bbcelite-websites/lander.bbcelite.com`

The [bbcelite-websites](https://github.com/markmoxon/bbcelite-websites) repository already contains the full [www.bbcelite.com](https://www.bbcelite.com) site here:

`/path/to/websites/bbcelite-websites/bbcelite.com`

as this top-level parent domain is entirely static.

We now have all our websites fully generated, so they are ready to serve from a web server from these locations:

```
/path/to/websites/bbcelite-websites/www.bbcelite.com
/path/to/websites/bbcelite-websites/elite.bbcelite.com
/path/to/websites/bbcelite-websites/aviator.bbcelite.com
/path/to/websites/bbcelite-websites/revs.bbcelite.com
/path/to/websites/bbcelite-websites/lander.bbcelite.com
```

Let's look at how we can do that.

### 6. Serve the completed websites

The websites are designed to be served from an Apache server, but they are pretty simple, so switching to a different server should be easy.

The main requirements are:

* PHP 8
* Perl (though this is only required for the `random.cgi` script)
* Symlinks need to be followed
* `.html` files need to be interpreted using PHP
* URLs in the form `/css/yyyymmdd/` and `/javascript/yyyymmdd/` resolve to `/css/ `and `/javascript` (where `yyyymmdd` is a date like `20240607`)

The latter enables us to bypass the browser cache when assets are updated, by simply updating the date. The date of the last assets update is set in various places in the static content.

There is a `.htaccess` in each site that sets all of this up, which should be easy to tailor to your own particular web server, should you want to experiment. This file also contains various redirects that reflect the various site reorganisations over the years, and it also allows JSBeeb and Archimedes Live to run games in the browser. There's nothing particularly complicated going on; this is a relatively simple site to serve.

As all the subdomains (such as [elite.bbcelite.com](https://elite.bbcelite.com)) reuse the assets from the parent site (i.e. [www.bbcelite.com](https://www.bbcelite.com)), you will need to add symlinks as follows:

```
cd $ELITE_WEBSITE
ln -s ../bbcelite.com/css css
ln -s ../bbcelite.com/javascript javascript
ln -s ../bbcelite.com/templates templates

cd $AVIATOR_WEBSITE
ln -s ../bbcelite.com/css css
ln -s ../bbcelite.com/javascript javascript
ln -s ../bbcelite.com/templates templates

cd $REVS_WEBSITE
ln -s ../bbcelite.com/css css
ln -s ../bbcelite.com/javascript javascript
ln -s ../bbcelite.com/templates templates

cd $LANDER_WEBSITE
ln -s ../bbcelite.com/css css
ln -s ../bbcelite.com/javascript javascript
ln -s ../bbcelite.com/templates templates

cd $BBCELITE_WEBSITE
ln -s ../elite.bbcelite.com/versions versions
```

The last one allows third-party sites like JSBeeb and XR Beeb to continue to load Elite disc images from the www.bbcelite.com domain, as CORS doesn't work over a redirect. (The Elite site used to live on the www.bbcelite.com domain, but was moved to elite.bbcelite.com.)

You should now be able to serve each of the websites from their root folders in the `bbcelite-websites` folder.

## Environment variables

The following environment variables need to be set up for the scripts to work. They should contain the full paths of the relevant folders that are used by the generation process.

### All sites

`$BBCELITE_SCRIPTS` = the path of this repository (i.e. `bbcelite-scripts`)

### Software archaeology site

`$BBCELITE_WEBSITE` = the root folder of the software archaeology website we want to generate

### Elite

`$ELITE_LIBRARY_REPOSITORY` = the path of the `elite-source-code-library` repository

`$ELITE_CODE_REPOSITORIES` = the folder containing the `elite-source-code-*` folders that will contain the generated source code for all the different versions of Elite

`$ELITE_WEBSITE` = the root folder of the Elite website we want to generate

`$ELITE_WEBSITE_REPOSITORY` = a staging repository for tracking changes to the generated website content

### Aviator

`$AVIATOR_CODE_REPOSITORY` = the path of the `aviator-source-code-bbc-micro` repository that we cloned above

`$AVIATOR_WEBSITE` = the root folder of the Aviator website we want to generate

`$AVIATOR_WEBSITE_REPOSITORY` = a staging repository for tracking changes to the generated website content

### Revs

`$REVS_CODE_REPOSITORY` = the path of the `revs-source-code-bbc-micro` repository that we cloned above

`$REVS_WEBSITE` = the root folder of the Revs website we want to generate

`$REVS_WEBSITE_REPOSITORY` = a staging repository for tracking changes to the generated website content

### Lander

`$LANDER_CODE_REPOSITORY` = the path of the `archimedes-lander` repository that we cloned above

`$LANDER_WEBSITE` = the root folder of the Lander website we want to generate

`$LANDER_WEBSITE_REPOSITORY` = a staging repository for tracking changes to the generated website content

### How to set the environment variables

The environment variables can be set using the `source` approach in the above example.

Alternatively you can add the `export` commands to your `.zshenv` file so that the variables are set for every shell that you open, so you don't have to run the `source` command each time you open a new terminal.

If you do this, then after updating `.zshenv`, you should close and re-open the terminal and `cd` back into the folder, to ensure that the variables are set.

---

Right on, Commanders!

_Mark Moxon_