#!/usr/bin/perl

use strict;
use warnings;

my $file_name = shift @ARGV;
my $word_count = 0;

open(my $file, '<', $file_name) or die $!;

while (my $line = <$file>) {
    if ($line !~ m#<\?php# && $line !~ m#\?># && $line !~ m#include\(# && $line !~ m#include_once\(# && $line !~ m#page_header\(#) {
        $line =~ s#</a>#</a> #g;
        $line =~ s#<a class="next"# <a class="next"#g;
        $line =~ s#&nbsp;# #g;
        $line =~ s#&amp;#&#g;
        $line =~ s#<br/># #g;
        $line =~ s#<br /># #g;
        $line =~ s#</td><td#</td> <td#g;
        $line =~ s#</th><th#</th> <th#g;
        $line =~ s#</li><li#</li> <li#g;
        $line =~ s#<[^>]+>##g;
        $line =~ s#&lt;#<#g;
        $line =~ s#&gt;#>#g;
        print $line;
    }
}

close($file);
