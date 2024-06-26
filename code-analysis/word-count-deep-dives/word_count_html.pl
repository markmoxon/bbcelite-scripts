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
        $line =~ s#<[^>]+>##g;
        $line =~ s#&lt;#<#g;
        $line =~ s#&gt;#>#g;
        $word_count += scalar(split(/\s+/, $line));
    }
}

# Calculated after removing goat soup breakdown
if ($file_name =~ m#extended_system_descriptions#) {
    $word_count -= 13685;
}

# Calculated after removing code snippets
if ($file_name =~ m#backporting_the_flicker-free_algorithm#) {
    $word_count -= 6133;
}

$file_name =~ s#$ENV{ELITE_WEBSITE}#elite.bbcelite.com#;
$file_name =~ s#$ENV{AVIATOR_WEBSITE}#aviator.bbcelite.com#;
$file_name =~ s#$ENV{REVS_WEBSITE}#revs.bbcelite.com#;
$file_name =~ s#$ENV{LANDER_WEBSITE}#lander.bbcelite.com#;

close($file);
print $word_count . "\t" . $file_name . "\n";
