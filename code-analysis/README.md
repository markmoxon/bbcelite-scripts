# Code analaysis scripts for the bbcelite.com website and associated repositories

This folder contains a number of scripts that I use to manage the content in my source code repositories and websites.

For these scripts to work, you need to have set up the environment variables described in the [bbcelite-scripts README](../README.md).

Note that I have only tested these scripts on a Mac. In theory they should also work in Linux, and they might also work on Windows using Git Bash or Windows Subsystem for Linux, but I haven't tried anything other than a Mac-based build.

## Code images

The [code-images](code-images) folder contains a Python script to generate visual images that contain the binaries from my disassembly projects.

To run the script, change directory into `code-images` and run the script like this:

```
cd code-images
python3 image.py
```

This will generate PNG images of the assembled binaries in the source code repositories.

For the script to work, you will need Python 3 with the Pillow library installed. You can install Pillow with the following:

```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```

## Text extractor: About site

The [extract-text-about-site](extract-text-about-site) folder contains a Perl script to extract the text from the about site sections of all the bbcelite.com sites. The text is saved into a text file, one per site, that can then be put through a spell checker.

To run the script, change directory into `extract-text-about-site` and run the script like this:

```
cd extract-text-about-site
./about-site.sh
```

For the script to work, you will need Perl installed.

## Text extractor: Code comments

The [extract-text-code-comments](extract-text-code-comments) folder contains a Perl script to extract the text of the code comments from all the source code repositories. The text is saved into a text file, one per site, that can then be put through a spell checker.

To run the script, change directory into `extract-text-code-comments` and run the script like this:

```
cd extract-text-code-comments
./code-comments.sh
```

For the script to work, you will need Perl installed.

## Text extractor: Deep dives

The [extract-text-deep-dives](extract-text-deep-dives) folder contains a Perl script to extract the text from the deep dive sections of all the bbcelite.com sites. The text is saved into a text file, one per site, that can then be put through a spell checker.

To run the script, change directory into `extract-text-deep-dives` and run the script like this:

```
cd extract-text-deep-dives
./deep-dives.sh
```

For the script to work, you will need Perl installed.


---

Right on, Commanders!

_Mark Moxon_