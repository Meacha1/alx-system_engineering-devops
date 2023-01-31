#!/usr/bin/env ruby

regex = /School/

if ARGV[0] =~ regex
  puts "School"
else
  puts "Nothing"
end
