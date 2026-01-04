# Generate code pages for The Sentinel website from source code repository

echo "Clearing down website folder"

cd $BBCELITE_SCRIPTS/disassembly-website-generator
rm -fr websites/the_sentinel

echo "Generating The Sentinel website"
python3 create-disassembly-websites.py the_sentinel

retVal=$?
if [ $retVal -ne 0 ]; then
    echo "Error generating website"
    exit $?
fi

echo "Syncing generated source to website repository"
rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/the_sentinel/ $THE_SENTINEL_WEBSITE_REPOSITORY/

echo "Syncing generated source to website"
rsync -a --delete $BBCELITE_SCRIPTS/disassembly-website-generator/websites/the_sentinel/source/ $THE_SENTINEL_WEBSITE/source/

echo "Copying navigation to website repository"
rsync -a $BBCELITE_SCRIPTS/disassembly-website-generator/websites/the_sentinel/templates_local/ $THE_SENTINEL_WEBSITE_REPOSITORY/templates_local/

echo "Copying navigation to website"
rsync -a $BBCELITE_SCRIPTS/disassembly-website-generator/websites/the_sentinel/templates_local/ $THE_SENTINEL_WEBSITE/templates_local/
