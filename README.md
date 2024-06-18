# Scripts for generating the bbcelite.com website and associated repositories

This repository contains scripts that take content from the following hand-crafted repositories:

* [Elite source code library](https://github.com/markmoxon/library-elite-beebasm)
* [Aviator source code](https://github.com/markmoxon/aviator-beebasm)
* [Revs source code](https://github.com/markmoxon/revs-beebasm)
* [Lander source code](https://github.com/markmoxon/archimedes-lander)
* [Static content for bbcelite.com](https://github.com/markmoxon/bbcelite-websites)

and generate the following source code repositories:

* [BBC Micro (cassette) Elite source code](https://github.com/markmoxon/cassette-elite-beebasm)
* [BBC Micro (disc) Elite source code](https://github.com/markmoxon/disc-elite-beebasm)
* [6502 Second Processor Elite source code](https://github.com/markmoxon/6502sp-elite-beebasm)
* [BBC Master Elite source code](https://github.com/markmoxon/master-elite-beebasm)
* [Acorn Electron Elite source code](https://github.com/markmoxon/electron-elite-beebasm)
* [Elite-A source code](https://github.com/markmoxon/elite-a-beebasm)
* [NES Elite source code](https://github.com/markmoxon/nes-elite-beebasm)

and the following websites:

* [Software Archaeology website](https://www.bbcelite.com)
* [Elite on the BBC Micro and NES](https://elite.bbcelite.com)
* [Aviator on the BBC Micro](https://aviator.bbcelite.com)
* [Revs on the BBC Micro](https://revs.bbcelite.com)
* [Lander on the Acorn Archimedes](https://lander.bbcelite.com)

So if I need to update a bit of commentary in the Elite source code, I can change the comments in just one place in the [Elite source code library](https://github.com/markmoxon/library-elite-beebasm), and then running a single script will update all the relevant Elite source code repositories, as well as all the instances of that comment in the Elite source code website. Given that the Elite website contains about 7500 cross-referenced code pages across seven versions of the game, this automated approach saves a lot of time.

## Running the scripts

If you want to see this automatic generation in action, then the following steps will enable you to set up and run the scripts, which will generate all the source code repositories and bbcelite.com websites listed above.

Note that I have only tested this build process on a Mac. In theory these scripts should also work in Linux, and they might also work on Windows using Git Bash or Windows Subsystem for Linux, but I haven't tried anything other than a Mac-based build.

Python 3 is required.

### 1. Clone the source repositories

First, we need to create a parent folder to hold the various repositories and websites that we are going to generate (the process will only create files within this folder, so you can clean up afterwards by simply deleting the folder).

I will refer to this path as `/path/to/websites` in the following documentation; you should change this to the actual path of the folder that you create.

So let's create our parent folder and set the current directory to this folder:

```
mkdir /path/to/websites
cd /path/to/websites
```

Next, create folders to hold the source repositories and generated content:

```
mkdir source-repositories
mkdir generated-repositories
mkdir generated-websites
```

First, clone the static website content into the parent folder:

```
git clone https://github.com/markmoxon/bbcelite-websites

```

Now clone this repository and the other source repositories into the `source-repositories` folder:

```
cd source-repositories

git clone https://github.com/markmoxon/bbcelite-scripts
git clone https://github.com/markmoxon/library-elite-beebasm
git clone https://github.com/markmoxon/aviator-beebasm
git clone https://github.com/markmoxon/revs-beebasm
git clone https://github.com/markmoxon/archimedes-lander
```

We have now cloned all the source content; let's now look at the generated content.

### 2. Create empty folders for the generated content

Start by creating empty folders that will hold the generated source code repositories in the `generated-repositories` folder:

```
cd ../generated-repositories

mkdir cassette-elite-beebasm
mkdir disc-elite-beebasm
mkdir 6502sp-elite-beebasm
mkdir master-elite-beebasm
mkdir electron-elite-beebasm
mkdir elite-a-beebasm
mkdir nes-elite-beebasm
```

Next, create folders for the staging website repositories in the `generated-websites` folder:

```
cd ../generated-websites
mkdir staging.elite.bbcelite.com
mkdir staging.aviator.bbcelite.com
mkdir staging.revs.bbcelite.com
mkdir staging.lander.bbcelite.com

```

The idea behind the staging repositories is that will only contain generated content, so we can track changes to generated content as we develop the scripts (this lets us check the results of changing the scripts). The complete websites will also contain this generated content, but there it's combined with the static content, so having a separate staging repository helps us manage the generated content separately from the static content.

### 3. Set the environment variables

Next, we set the environment variables that are needed by the generation scripts.

To do this, create a shell script called `env.sh` in our parent folder:

```
cd ..
touch env.sh
```

Open the `env.sh` file in your preferred text editor and paste in the following content, making sure you change `/path/to/websites` to the correct path for the parent folder that you created in step 1:

```
export BBCELITE_SCRIPTS=/path/to/websites/source-repositories/bbcelite-scripts

export ELITE_LIBRARY_REPOSITORY=/path/to/websites/source-repositories/library-elite-beebasm
export ELITE_CODE_REPOSITORIES=/path/to/websites/generated-repositories
export ELITE_WEBSITE=/path/to/websites/bbcelite-websites/elite.bbcelite.com
export ELITE_WEBSITE_REPOSITORY=/path/to/websites/generated-websites/staging.elite.bbcelite.com

export AVIATOR_CODE_REPOSITORY=/path/to/websites/source-repositories/aviator-beebasm
export AVIATOR_WEBSITE=/path/to/websites/bbcelite-websites/aviator.bbcelite.com
export AVIATOR_WEBSITE_REPOSITORY=/path/to/websites/generated-websites/staging.aviator.bbcelite.com

export REVS_CODE_REPOSITORY=/path/to/websites/source-repositories/revs-beebasm
export REVS_WEBSITE=/path/to/websites/bbcelite-websites/revs.bbcelite.com
export REVS_WEBSITE_REPOSITORY=/path/to/websites/generated-websites/staging.revs.bbcelite.com

export LANDER_CODE_REPOSITORY=/path/to/websites/source-repositories/archimedes-lander
export LANDER_WEBSITE=/path/to/websites/bbcelite-websites/lander.bbcelite.com
export LANDER_WEBSITE_REPOSITORY=/path/to/websites/generated-websites/staging.lander.bbcelite.com
```

Execute this script with the following command, to export the environment variables to the current shell:

```
source env.sh
```

[See below](#environment-variables) for information on these environment variables, advice on automating this step, and details on how to set up a different folder structure to the all-in-one approach used in this example.

### 4. Run the generation script for Elite

Now let's generate the Elite source repositories:

* [cassette-elite-beebasm](https://github.com/markmoxon/cassette-elite-beebasm)
* [disc-elite-beebasm](https://github.com/markmoxon/disc-elite-beebasm)
* [6502sp-elite-beebasm](https://github.com/markmoxon/6502sp-elite-beebasm)
* [master-elite-beebasm](https://github.com/markmoxon/master-elite-beebasm)
* [electron-elite-beebasm](https://github.com/markmoxon/electron-elite-beebasm)
* [elite-a-beebasm](https://github.com/markmoxon/elite-a-beebasm)
* [nes-elite-beebasm](https://github.com/markmoxon/nes-elite-beebasm)

and the Elite source code website:

* [elite.bbcelite.com](https://elite.bbcelite.com)

First, switch to the `bbcelite-scripts` repository folder:

```
cd $BBCELITE_SCRIPTS
```

Now generate the repositories and website by running this script (this will take quite a while to run):

```
./generate-elite.sh
```

This will generate the source code repositories in each of the empty folders in `generated-repositories`, using the content from the Elite library repository as the source.

The script also generates the code pages for the [elite.bbcelite.com](https://elite.bbcelite.com) site from the contents of those newly generated source code repositories. It copies the results into both the `staging.elite.bbcelite.com` folder, and into the `elite.bbcelite.com` folder in the `bbcelite-websites` repository. Because the latter already contains the static content for the website, the end result is a complete copy of the [elite.bbcelite.com](https://elite.bbcelite.com) website, here:

`/path/to/websites/bbcelite-websites/elite.bbcelite.com`

The generated content is copied to `staging.elite.bbcelite.com` so it can be tracked, if required.

Changing the Elite library content and re-running the generation script will automatically update both the source code repositories and the website.

### 5. Run the generation scripts for Aviator, Revs and Lander

Next, let's generate the other websites by running the relevant generate scripts.

This command:

```
./generate-aviator.sh
```

will generate the [aviator.bbcelite.com](https://aviator.bbcelite.com) site and the corresponding staging repository, taking the source code from the [aviator-beebasm](https://github.com/markmoxon/aviator-beebasm) source code repository and creating a complete site here:

`/path/to/websites/bbcelite-websites/aviator.bbcelite.com`

Similarly, this command:

```
./generate-revs.sh
```

will generate the [revs.bbcelite.com](https://revs.bbcelite.com) site and the corresponding staging repository, taking the source code from the [revs-beebasm](https://github.com/markmoxon/revs-beebasm) source code repository and creating a complete site here:

`/path/to/websites/bbcelite-websites/revs.bbcelite.com`

and this command:

```
./generate-lander.sh
```

will generate the [lander.bbcelite.com](https://lander.bbcelite.com) site and the corresponding staging repository, taking the source code from the [archimedes-lander](https://github.com/markmoxon/archimedes-lander) source code repository and creating a complete site here:

`/path/to/websites/bbcelite-websites/lander.bbcelite.com`

The bbc-websites repository already contains the full [www.bbcelite.com](https://www.bbcelite.com), so we now have all our websites fully generated, ready to serve from a web server.

### 6. Serve the completed website

The websites are designed to be served from an Apache server, but they are pretty simple, so switching to a different server should be easy.

The main requirements are:

* PHP 8
* Perl (though this is only required for the randomiser script)
* Symlinks need to be followed
* `.html` files need to be interpreted using PHP

There is a `.htaccess` in each site that sets all of this up, which should be easy to tailor to your own particular web server, should you want to experiment.

As all the *.bbcelite.com subdomains use the assets from www.bbcelite.com, you will need to add symlinks as follows:

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
```

You should now be able to serve the websites from their document roots in `bbcelite-websites'

## Environment variables

The following environment variables need to be set up for the scripts to work. They should contain the full paths of the relevant folders that are used by the generation process.

### All sites

`$BBCELITE_SCRIPTS` = the path of this repository (i.e. bbcelite-scripts)

### Elite

`$ELITE_LIBRARY_REPOSITORY` = the path of the library-elite-beebasm repository

`$ELITE_CODE_REPOSITORIES` = the folder containing the `*-elite-beebasm` folders that will contain the generated source code for all the different versions of Elite

`$ELITE_WEBSITE` = the root folder of the Elite website we want to generate

`$ELITE_WEBSITE_REPOSITORY` = a staging repository for tracking changes to the generated website content

### Aviator

`$AVIATOR_CODE_REPOSITORY` = the path of the aviator-beebasm repository that we cloned above

`$AVIATOR_WEBSITE` = the root folder of the Aviator website we want to generate

`$AVIATOR_WEBSITE_REPOSITORY` = a staging repository for tracking changes to the generated website content

### Revs

`$REVS_CODE_REPOSITORY` = the path of the revs-beebasm repository that we cloned above

`$REVS_WEBSITE` = the root folder of the Revs website we want to generate

`$REVS_WEBSITE_REPOSITORY` = a staging repository for tracking changes to the generated website content

### Lander

`$LANDER_CODE_REPOSITORY` = the path of the archimedes-lander repository that we cloned above

`$LANDER_WEBSITE` = the root folder of the Lander website we want to generate

`$LANDER_WEBSITE_REPOSITORY` = a staging repository for tracking changes to the generated website content

### How to set the environment variables

The environment variables can be set using the `source` approach in the above example.

Alternatively you can add the `export` commands to your `.zshenv` file so that the variables are set for every shell that you open, so you don>t have to run the `source` command each time you open a new terminal.

If you do this, then after updating `.zshenv`, you should close and re-open the terminal and `cd` back into the folder, to ensure that the variables are set.

---

Right on, Commanders!

_Mark Moxon_