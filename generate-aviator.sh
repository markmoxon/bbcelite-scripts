# Generate code pages for Aviator website from source code repository

echo "Clearing down website folder"

cd $BBCELITE_SCRIPTS/disassembly-website-generator
rm -fr websites/aviator

echo "Generating Aviator website"
python3 create-disassembly-websites.py aviator

retVal=$?
if [ $retVal -ne 0 ]; then
    echo "Error generating website"
    exit $?
fi

echo "Syncing generated source to website repository"
rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/aviator/ $AVIATOR_WEBSITE_REPOSITORY/

echo "Syncing generated source to website"
rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/aviator/source/ $AVIATOR_WEBSITE/source/

echo "Copying navigation to website"
cp $BBCELITE_SCRIPTS/disassembly-website-generator/websites/aviator/templates_local/navigation_* $AVIATOR_WEBSITE/templates_local/
