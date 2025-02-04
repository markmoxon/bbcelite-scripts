# Generate source repositories and code website pages from the Elite library
#
# Add a stop parameter after the command to stop after syncing source repositories, e.g. update_elite.sh stop
# Add a platform name after the command to only generate that platform, e.g. update_elite.sh cassette

platform=$1

# Generate source code from library and sync to repositories

cd $BBCELITE_SCRIPTS/elite-repository-generator
rm -fr repos
python3 create-elite-repositories.py

retVal=$?
if [ $retVal -ne 0 ]; then
    echo "Error generating repositories"
    exit $?
fi

if [[ "$platform" == "cassette" || "$platform" == "stop" || -z "$platform" ]]; then
    echo "Syncing to cassette repository"
    rsync -a --exclude ".git*" --exclude "Makefile" --delete $ELITE_LIBRARY_REPOSITORY/versions/cassette/ $ELITE_CODE_REPOSITORIES/elite-source-code-bbc-micro-cassette/
    cp -R repos/cassette/1-source-files/* $ELITE_CODE_REPOSITORIES/elite-source-code-bbc-micro-cassette/1-source-files/main-sources
    cp -R repos/cassette/2-build-files/* $ELITE_CODE_REPOSITORIES/elite-source-code-bbc-micro-cassette/2-build-files
    cp repos/cassette/Makefile $ELITE_CODE_REPOSITORIES/elite-source-code-bbc-micro-cassette/Makefile
    sed -i "" "s/Saving file 'versions\/cassette\//Saving file '/g" $ELITE_CODE_REPOSITORIES/elite-source-code-bbc-micro-cassette/3-assembled-output/compile.txt
fi

if [[ "$platform" == "disc" || "$platform" == "stop" || -z "$platform" ]]; then
    echo "Syncing to disc repository"
    rsync -a --exclude ".git*" --exclude "Makefile" --delete $ELITE_LIBRARY_REPOSITORY/versions/disc/ $ELITE_CODE_REPOSITORIES/elite-source-code-bbc-micro-disc/
    cp -R repos/disc/1-source-files/* $ELITE_CODE_REPOSITORIES/elite-source-code-bbc-micro-disc/1-source-files/main-sources
    cp -R repos/disc/2-build-files/* $ELITE_CODE_REPOSITORIES/elite-source-code-bbc-micro-disc/2-build-files
    cp repos/disc/Makefile $ELITE_CODE_REPOSITORIES/elite-source-code-bbc-micro-disc/Makefile
    sed -i "" "s/Saving file 'versions\/disc\//Saving file '/g" $ELITE_CODE_REPOSITORIES/elite-source-code-bbc-micro-disc/3-assembled-output/compile.txt
fi

if [[ "$platform" == "6502sp" || "$platform" == "stop" || -z "$platform" ]]; then
    echo "Syncing to 6502sp repository"
    rsync -a --exclude ".git*" --exclude "Makefile" --delete $ELITE_LIBRARY_REPOSITORY/versions/6502sp/ $ELITE_CODE_REPOSITORIES/elite-source-code-6502-second-processor/
    cp -R repos/6502sp/1-source-files/* $ELITE_CODE_REPOSITORIES/elite-source-code-6502-second-processor/1-source-files/main-sources
    cp -R repos/6502sp/2-build-files/* $ELITE_CODE_REPOSITORIES/elite-source-code-6502-second-processor/2-build-files
    cp repos/6502sp/Makefile $ELITE_CODE_REPOSITORIES/elite-source-code-6502-second-processor/Makefile
    sed -i "" "s/Saving file 'versions\/6502sp\//Saving file '/g" $ELITE_CODE_REPOSITORIES/elite-source-code-6502-second-processor/3-assembled-output/compile.txt
fi

if [[ "$platform" == "master" || "$platform" == "stop" || -z "$platform" ]]; then
    echo "Syncing to master repository"
    rsync -a --exclude ".git*" --exclude "Makefile" --delete $ELITE_LIBRARY_REPOSITORY/versions/master/ $ELITE_CODE_REPOSITORIES/elite-source-code-bbc-master/
    cp -R repos/master/1-source-files/* $ELITE_CODE_REPOSITORIES/elite-source-code-bbc-master/1-source-files/main-sources
    cp -R repos/master/2-build-files/* $ELITE_CODE_REPOSITORIES/elite-source-code-bbc-master/2-build-files
    cp repos/master/Makefile $ELITE_CODE_REPOSITORIES/elite-source-code-bbc-master/Makefile
    sed -i "" "s/Saving file 'versions\/master\//Saving file '/g" $ELITE_CODE_REPOSITORIES/elite-source-code-bbc-master/3-assembled-output/compile.txt
fi

if [[ "$platform" == "electron" || "$platform" == "stop" || -z "$platform" ]]; then
    echo "Syncing to electron repository"
    rsync -a --exclude ".git*" --exclude "Makefile" --delete $ELITE_LIBRARY_REPOSITORY/versions/electron/ $ELITE_CODE_REPOSITORIES/elite-source-code-acorn-electron/
    cp -R repos/electron/1-source-files/* $ELITE_CODE_REPOSITORIES/elite-source-code-acorn-electron/1-source-files/main-sources
    cp -R repos/electron/2-build-files/* $ELITE_CODE_REPOSITORIES/elite-source-code-acorn-electron/2-build-files
    cp repos/electron/Makefile $ELITE_CODE_REPOSITORIES/elite-source-code-acorn-electron/Makefile
    sed -i "" "s/Saving file 'versions\/electron\//Saving file '/g" $ELITE_CODE_REPOSITORIES/elite-source-code-acorn-electron/3-assembled-output/compile.txt
fi

if [[ "$platform" == "elite-a" || "$platform" == "stop" || -z "$platform" ]]; then
    echo "Syncing to elite-a repository"
    rsync -a --exclude ".git*" --exclude "Makefile" --delete $ELITE_LIBRARY_REPOSITORY/versions/elite-a/ $ELITE_CODE_REPOSITORIES/elite-a-source-code-bbc-micro/
    cp -R repos/elite-a/1-source-files/* $ELITE_CODE_REPOSITORIES/elite-a-source-code-bbc-micro/1-source-files/main-sources
    cp -R repos/elite-a/2-build-files/* $ELITE_CODE_REPOSITORIES/elite-a-source-code-bbc-micro/2-build-files
    cp repos/elite-a/Makefile $ELITE_CODE_REPOSITORIES/elite-a-source-code-bbc-micro/Makefile
    sed -i "" "s/Saving file 'versions\/elite-a\//Saving file '/g" $ELITE_CODE_REPOSITORIES/elite-a-source-code-bbc-micro/3-assembled-output/compile.txt
fi

if [[ "$platform" == "c64" || "$platform" == "stop" || -z "$platform" ]]; then
    echo "Syncing to c64 repository"
    rsync -a --exclude ".git*" --exclude "Makefile" --delete $ELITE_LIBRARY_REPOSITORY/versions/c64/ $ELITE_CODE_REPOSITORIES/elite-source-code-commodore-64/
    cp -R repos/c64/1-source-files/* $ELITE_CODE_REPOSITORIES/elite-source-code-commodore-64/1-source-files/main-sources
    cp -R repos/c64/2-build-files/* $ELITE_CODE_REPOSITORIES/elite-source-code-commodore-64/2-build-files
    cp repos/c64/Makefile $ELITE_CODE_REPOSITORIES/elite-source-code-commodore-64/Makefile
    sed -i "" "s/Saving file 'versions\/c64\//Saving file '/g" $ELITE_CODE_REPOSITORIES/elite-source-code-commodore-64/3-assembled-output/compile.txt
fi

if [[ "$platform" == "apple" || "$platform" == "stop" || -z "$platform" ]]; then
    echo "Syncing to apple repository"
    rsync -a --exclude ".git*" --exclude "Makefile" --delete $ELITE_LIBRARY_REPOSITORY/versions/apple/ $ELITE_CODE_REPOSITORIES/elite-source-code-apple-ii/
    cp -R repos/apple/1-source-files/* $ELITE_CODE_REPOSITORIES/elite-source-code-apple-ii/1-source-files/main-sources
    cp -R repos/apple/2-build-files/* $ELITE_CODE_REPOSITORIES/elite-source-code-apple-ii/2-build-files
    cp repos/apple/Makefile $ELITE_CODE_REPOSITORIES/elite-source-code-apple-ii/Makefile
    sed -i "" "s/Saving file 'versions\/apple\//Saving file '/g" $ELITE_CODE_REPOSITORIES/elite-source-code-apple-ii/3-assembled-output/compile.txt
fi

if [[ "$platform" == "nes" || "$platform" == "stop" || -z "$platform" ]]; then
    echo "Syncing to nes repository"
    rsync -a --exclude ".git*" --exclude "Makefile" --delete $ELITE_LIBRARY_REPOSITORY/versions/nes/ $ELITE_CODE_REPOSITORIES/elite-source-code-nes/
    cp -R repos/nes/1-source-files/* $ELITE_CODE_REPOSITORIES/elite-source-code-nes/1-source-files/main-sources
    cp -R repos/nes/2-build-files/* $ELITE_CODE_REPOSITORIES/elite-source-code-nes/2-build-files
    cp repos/nes/Makefile $ELITE_CODE_REPOSITORIES/elite-source-code-nes/Makefile
    sed -i "" "s/Saving file 'versions\/nes\//Saving file '/g" $ELITE_CODE_REPOSITORIES/elite-source-code-nes/3-assembled-output/compile.txt
fi

if [[ "$platform" == "stop" ]]; then
    echo "Stopping due to command line argument"
    exit 0
fi

# Generate websites code and sync to dev sites and staging repositories

cd $BBCELITE_SCRIPTS/disassembly-website-generator

if [[ "$platform" == "compare" ]]; then
    echo "Clearing down compare folder"
    rm -fr websites/elite/compare
else
    echo "Clearing down website folder"
    rm -fr websites/elite
fi

if [[ "$platform" == "cassette" || -z "$platform" ]]; then
    echo "Generating cassette website"
    python3 create-disassembly-websites.py cassette
fi

if [[ "$platform" == "disc" || -z "$platform" ]]; then
    echo "Generating disc website"
    python3 create-disassembly-websites.py disc
fi

if [[ "$platform" == "6502sp" || -z "$platform" ]]; then
    echo "Generating 6502sp website"
    python3 create-disassembly-websites.py 6502sp
fi

if [[ "$platform" == "master" || -z "$platform" ]]; then
    echo "Generating master website"
    python3 create-disassembly-websites.py master
fi

if [[ "$platform" == "electron" || -z "$platform" ]]; then
    echo "Generating electron website"
    python3 create-disassembly-websites.py electron
fi

if [[ "$platform" == "elite-a" || -z "$platform" ]]; then
    echo "Generating elite-a website"
    python3 create-disassembly-websites.py elite-a
fi

if [[ "$platform" == "c64" || -z "$platform" ]]; then
    echo "Generating c64 website"
    python3 create-disassembly-websites.py c64
fi

if [[ "$platform" == "apple" || -z "$platform" ]]; then
    echo "Generating apple website"
    python3 create-disassembly-websites.py apple
fi

if [[ "$platform" == "nes" || -z "$platform" ]]; then
    echo "Generating nes website"
    python3 create-disassembly-websites.py nes
fi

if [[ "$platform" == "compare" ||  -z "$platform" ]]; then
    echo "Generating compare website"
    python3 create-disassembly-websites.py compare
fi

retVal=$?
if [ $retVal -ne 0 ]; then
    echo "Error generating website"
    exit $?
fi

if [[ "$platform" == "cassette" || -z "$platform" ]]; then
    echo "Syncing cassette to website repository"
    rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/elite/cassette/ $ELITE_WEBSITE_REPOSITORY/cassette/
    echo "Syncing cassette to website"
    rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/elite/cassette/ $ELITE_WEBSITE/cassette/
fi

if [[ "$platform" == "disc" || -z "$platform" ]]; then
    echo "Syncing disc to website repository"
    rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/elite/disc/ $ELITE_WEBSITE_REPOSITORY/disc/
    echo "Syncing disc to website"
    rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/elite/disc/ $ELITE_WEBSITE/disc/
fi

if [[ "$platform" == "6502sp" || -z "$platform" ]]; then
    echo "Syncing 6502sp to website repository"
    rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/elite/6502sp/ $ELITE_WEBSITE_REPOSITORY/6502sp/
    echo "Syncing 6502sp to website"
    rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/elite/6502sp/ $ELITE_WEBSITE/6502sp/
fi

if [[ "$platform" == "master" || -z "$platform" ]]; then
    echo "Syncing master to website repository"
    rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/elite/master/ $ELITE_WEBSITE_REPOSITORY/master/
    echo "Syncing master to website"
    rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/elite/master/ $ELITE_WEBSITE/master/
fi

if [[ "$platform" == "electron" || -z "$platform" ]]; then
    echo "Syncing electron to website repository"
    rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/elite/electron/ $ELITE_WEBSITE_REPOSITORY/electron/
    echo "Syncing electron to website"
    rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/elite/electron/ $ELITE_WEBSITE/electron/
fi

if [[ "$platform" == "elite-a" || -z "$platform" ]]; then
    echo "Syncing elite-a to website repository"
    rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/elite/elite-a/ $ELITE_WEBSITE_REPOSITORY/elite-a/
    echo "Syncing elite-a to website"
    rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/elite/elite-a/ $ELITE_WEBSITE/elite-a/
fi

if [[ "$platform" == "compare" || -z "$platform" ]]; then
    echo "Syncing compare to website repository"
    rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/elite/compare/ $ELITE_WEBSITE_REPOSITORY/compare/
    echo "Syncing compare to website"
    rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/elite/compare/ $ELITE_WEBSITE/compare/
fi

if [[ "$platform" == "c64" || -z "$platform" ]]; then
    echo "Syncing c64 to website repository"
    rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/elite/c64/ $ELITE_WEBSITE_REPOSITORY/c64/
    echo "Syncing c64 to website"
    rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/elite/c64/ $ELITE_WEBSITE/c64/
fi

if [[ "$platform" == "apple" || -z "$platform" ]]; then
    echo "Syncing apple to website repository"
    rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/elite/apple/ $ELITE_WEBSITE_REPOSITORY/apple/
    echo "Syncing apple to website"
    rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/elite/apple/ $ELITE_WEBSITE/apple/
fi

if [[ "$platform" == "nes" || -z "$platform" ]]; then
    echo "Syncing nes to website repository"
    rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/elite/nes/ $ELITE_WEBSITE_REPOSITORY/nes/
    echo "Syncing nes to website"
    rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/elite/nes/ $ELITE_WEBSITE/nes/
fi

echo "Copying navigation to website repository"
rsync -a $BBCELITE_SCRIPTS/disassembly-website-generator/websites/elite/templates_local/ $ELITE_WEBSITE_REPOSITORY/templates_local/

echo "Copying navigation to website"
rsync -a $BBCELITE_SCRIPTS/disassembly-website-generator/websites/elite/templates_local/ $ELITE_WEBSITE/templates_local/
