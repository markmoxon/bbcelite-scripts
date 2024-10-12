
find $ELITE_CODE_REPOSITORIES/elite-source-code-bbc-micro-cassette/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec wc {} \; > temp.txt
find $ELITE_CODE_REPOSITORIES/elite-source-code-bbc-micro-disc/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec wc {} \; >> temp.txt
find $ELITE_CODE_REPOSITORIES/elite-source-code-6502-second-processor/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec wc {} \; >> temp.txt
find $ELITE_CODE_REPOSITORIES/elite-source-code-acorn-electron/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec wc {} \; >> temp.txt
find $ELITE_CODE_REPOSITORIES/elite-source-code-bbc-master/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec wc {} \; >> temp.txt
find $ELITE_CODE_REPOSITORIES/elite-a-source-code-bbc-micro/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec wc {} \; >> temp.txt
find $ELITE_CODE_REPOSITORIES/elite-source-code-nes/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec wc {} \; >> temp.txt
find $REVS_CODE_REPOSITORY/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec wc {} \; >> temp.txt
find $AVIATOR_CODE_REPOSITORY/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec wc {} \; >> temp.txt
find $LANDER_CODE_REPOSITORY/1-source-files/main-sources -maxdepth 1 -name '*.arm' -type f -exec wc {} \; >> temp.txt

perl word_count_convert.pl temp.txt > linecount.txt

find $ELITE_CODE_REPOSITORIES/elite-source-code-bbc-micro-cassette/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code.pl {} \; > temp.txt
find $ELITE_CODE_REPOSITORIES/elite-source-code-bbc-micro-disc/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code.pl {} \; >> temp.txt
find $ELITE_CODE_REPOSITORIES/elite-source-code-6502-second-processor/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code.pl {} \; >> temp.txt
find $ELITE_CODE_REPOSITORIES/elite-source-code-acorn-electron/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code.pl {} \; >> temp.txt
find $ELITE_CODE_REPOSITORIES/elite-source-code-bbc-master/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code.pl {} \; >> temp.txt
find $ELITE_CODE_REPOSITORIES/elite-a-source-code-bbc-micro/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code.pl {} \; >> temp.txt
find $ELITE_CODE_REPOSITORIES/elite-source-code-nes/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code_nes.pl {} \; >> temp.txt
find $REVS_CODE_REPOSITORY/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code.pl {} \; >> temp.txt
find $AVIATOR_CODE_REPOSITORY/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code.pl {} \; >> temp.txt
find $LANDER_CODE_REPOSITORY/1-source-files/main-sources -maxdepth 1 -name '*.arm' -type f -exec perl strip_code.pl {} \; >> temp.txt

perl word_count_convert.pl temp.txt > wordcount.txt

rm temp.txt