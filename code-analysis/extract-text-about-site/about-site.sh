find $BBCELITE_WEBSITE/acornsoft -maxdepth 1 -name '*.html' -type f -exec perl strip_html.pl {} \; > archaeology.txt
find $BBCELITE_WEBSITE/disassembly_websites -maxdepth 1 -name '*.html' -type f -exec perl strip_html.pl {} \; > archaeology.txt
find $BBCELITE_WEBSITE/talks -maxdepth 1 -name '*.html' -type f -exec perl strip_html.pl {} \; > archaeology.txt

find $ELITE_WEBSITE/about_site -maxdepth 1 -name '*.html' -type f -exec perl strip_html.pl {} \; > elite.txt
find $ELITE_WEBSITE/alias -maxdepth 1 -name '*.html' -type f -exec perl strip_html.pl {} \; >> elite.txt
find $ELITE_WEBSITE/hacks -maxdepth 1 -name '*.html' -type f -exec perl strip_html.pl {} \; >> elite.txt

find $REVS_WEBSITE/about_site -maxdepth 1 -name '*.html' -type f -exec perl strip_html.pl {} \; > revs.txt
find $REVS_WEBSITE/alias -maxdepth 1 -name '*.html' -type f -exec perl strip_html.pl {} \; >> revs.txt

find $AVIATOR_WEBSITE/about_site -maxdepth 1 -name '*.html' -type f -exec perl strip_html.pl {} \; > aviator.txt
find $AVIATOR_WEBSITE/alias -maxdepth 1 -name '*.html' -type f -exec perl strip_html.pl {} \; >> aviator.txt

find $LANDER_WEBSITE/about_site -maxdepth 1 -name '*.html' -type f -exec perl strip_html.pl {} \; > lander.txt
find $LANDER_WEBSITE/alias -maxdepth 1 -name '*.html' -type f -exec perl strip_html.pl {} \; >> lander.txt
