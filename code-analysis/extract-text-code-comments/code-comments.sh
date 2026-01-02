find $ELITE_CODE_REPOSITORIES/elite-source-code-bbc-micro-cassette/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code.pl {} \; > elite.txt
find $ELITE_CODE_REPOSITORIES/elite-source-code-bbc-micro-disc/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code.pl {} \; >> elite.txt
find $ELITE_CODE_REPOSITORIES/elite-source-code-6502-second-processor/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code.pl {} \; >> elite.txt
find $ELITE_CODE_REPOSITORIES/elite-source-code-acorn-electron/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code.pl {} \; >> elite.txt
find $ELITE_CODE_REPOSITORIES/elite-source-code-commodore-64/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code_nes.pl {} \; >> elite.txt
find $ELITE_CODE_REPOSITORIES/elite-source-code-apple-ii/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code_nes.pl {} \; >> elite.txt
find $ELITE_CODE_REPOSITORIES/elite-source-code-bbc-master/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code.pl {} \; >> elite.txt
find $ELITE_CODE_REPOSITORIES/elite-a-source-code-bbc-micro/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code.pl {} \; >> elite.txt
find $ELITE_CODE_REPOSITORIES/elite-source-code-nes/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code_nes.pl {} \; >> elite.txt

find $REVS_CODE_REPOSITORY/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code.pl {} \; > revs.txt

find $AVIATOR_CODE_REPOSITORY/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code.pl {} \; > aviator.txt

find $THE_SENTINEL_CODE_REPOSITORY/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code.pl {} \; > the-sentinel.txt

find $LANDER_CODE_REPOSITORY/1-source-files/main-sources -maxdepth 1 -name '*.arm' -type f -exec perl strip_code.pl {} \; > lander.txt
