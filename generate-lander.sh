# Generate code pages for Lander website from source code repository

echo "Clearing down website folder"

cd $BBCELITE_SCRIPTS/disassembly-website-generator
rm -fr websites/lander

echo "Generating Lander website"
python3 create-disassembly-websites.py lander

retVal=$?
if [ $retVal -ne 0 ]; then
    echo "Error generating website"
    exit $?
fi

echo "Syncing generated source to website repository"
rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/lander/ $LANDER_WEBSITE_REPOSITORY/

echo "Syncing generated source to website"
rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/lander/source/ $LANDER_WEBSITE/source/

echo "Copying navigation to website"
cp $BBCELITE_SCRIPTS/disassembly-website-generator/websites/lander/templates_local/navigation_* $LANDER_WEBSITE/templates_local/
