#!/usr/bin/perl

use strict;
use warnings;

my $file_name = shift @ARGV;
my $word_count = 0;

open(my $file, '<', $file_name) or die $!;

while (my $line = <$file>) {
    if ($line =~ /\\ / && $line =~ /[^ *-\\\n]/) {
        $line =~ s#^[^\\]*\\ *##g;
        $line =~ s#^\.[^\\]+##g;
        $word_count += scalar(split(/\s+/, $line));
    }
}

close($file);
print $word_count . "\t" . $file_name . "\n";
