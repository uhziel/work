#!/usr/bin/env python2

from sys import argv

scipt, src_file, dest_file = argv
open(dest_file, 'w').write(open(src_file).read())
