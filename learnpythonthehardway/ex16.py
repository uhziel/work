#!/usr/bin/env python2

from sys import argv

script, filename = argv

print "truncate %s, cancel hit CTRL-C, ok hit RETURN." % filename
txt = open(filename, 'w')
txt.truncate()
txt.write(raw_input("your words: "))
txt.close()
