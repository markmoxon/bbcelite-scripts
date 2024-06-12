# Generate code pages for Revs website from source code repository

echo "Clearing down website folder"

cd $BBCELITE_SCRIPTS/disassembly-website-generator
rm -fr websites/revs

echo "Generating Revs website"
python3 create-disassembly-websites.py revs

retVal=$?
if [ $retVal -ne 0 ]; then
    echo "Error generating website"
    exit $?
fi

echo "Syncing generated source to website repository"
rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/revs/ $REVS_WEBSITE_REPOSITORY/

echo "Syncing generated source to website"
rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/revs/source/ $REVS_WEBSITE/source/

echo "Copying navigation to website repository"
rsync -a $BBCELITE_SCRIPTS/disassembly-website-generator/websites/revs/templates_local/ $REVS_WEBSITE_REPOSITORY/templates_local/

echo "Copying navigation to website"
rsync -a $BBCELITE_SCRIPTS/disassembly-website-generator/websites/revs/templates_local/ $REVS_WEBSITE/templates_local/
