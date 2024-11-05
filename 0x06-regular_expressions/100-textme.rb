#!/usr/bin/env ruby
#project done by Eudiasnjoroge

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
