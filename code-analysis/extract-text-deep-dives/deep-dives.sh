find $ELITE_WEBSITE/deep_dives -maxdepth 1 -name '*.html' -type f -exec perl strip_html.pl {} \; > elite.txt

find $REVS_WEBSITE/deep_dives -maxdepth 1 -name '*.html' -type f -exec perl strip_html.pl {} \; > revs.txt

find $AVIATOR_WEBSITE/deep_dives -maxdepth 1 -name '*.html' -type f -exec perl strip_html.pl {} \; > aviator.txt

find $LANDER_WEBSITE/deep_dives -maxdepth 1 -name '*.html' -type f -exec perl strip_html.pl {} \; > lander.txt
