find $ELITE_WEBSITE/deep_dives -maxdepth 1 -name '*.html' -type f -exec perl word_count_html.pl {} \; | sort -Vr > wordcount.txt

find $REVS_WEBSITE/deep_dives -maxdepth 1 -name '*.html' -type f -exec perl word_count_html.pl {} \; | sort -Vr >> wordcount.txt

find $AVIATOR_WEBSITE/deep_dives -maxdepth 1 -name '*.html' -type f -exec perl word_count_html.pl {} \; | sort -Vr >> wordcount.txt

find $LANDER_WEBSITE/deep_dives -maxdepth 1 -name '*.html' -type f -exec perl word_count_html.pl {} \; | sort -Vr >> wordcount.txt
