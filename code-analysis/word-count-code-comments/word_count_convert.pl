#!/usr/bin/perl

use strict;
use warnings;

my $file_name = shift @ARGV;
my $word_count = 0;

open(my $file, '<', $file_name) or die $!;

while (my $line = <$file>) {
	$line =~ s#/Users/Mark/Documents/Files/Computers/[^/]+/Repositories/##g;
	$line =~ s#/1-source-files/main-sources/#\t#g;
	$line =~ s#^ +##g;
	$line =~ s# +#\t#g;
	$line =~ s#elite-a-source-code-bbc-micro\telite-6502sp#elite-source-code-6502-second-processor\telite-6502sp#g;
	print $line;
}

close($file);
