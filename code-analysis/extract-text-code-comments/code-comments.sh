find $ELITE_CODE_REPOSITORIES/cassette-elite-beebasm/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code.pl {} \; > elite.txt
find $ELITE_CODE_REPOSITORIES/disc-elite-beebasm/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code.pl {} \; >> elite.txt
find $ELITE_CODE_REPOSITORIES/6502sp-elite-beebasm/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code.pl {} \; >> elite.txt
find $ELITE_CODE_REPOSITORIES/electron-elite-beebasm/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code.pl {} \; >> elite.txt
find $ELITE_CODE_REPOSITORIES/master-elite-beebasm/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code.pl {} \; >> elite.txt
find $ELITE_CODE_REPOSITORIES/elite-a-beebasm/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code.pl {} \; >> elite.txt
find $ELITE_CODE_REPOSITORIES/nes-elite-beebasm/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code_nes.pl {} \; >> elite.txt

find $REVS_CODE_REPOSITORY/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code.pl {} \; > revs.txt

find $AVIATOR_CODE_REPOSITORY/1-source-files/main-sources -maxdepth 1 -name '*.asm' -type f -exec perl strip_code.pl {} \; > aviator.txt

find $LANDER_CODE_REPOSITORY/1-source-files/main-sources -maxdepth 1 -name '*.arm' -type f -exec perl strip_code.pl {} \; > lander.txt
