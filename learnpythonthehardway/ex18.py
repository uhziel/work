#!/usr/bin/env python2

def hello(arg1, arg2):
    print "hello, arg1:%s, arg2:%s" % (arg1, arg2)

def hello_again(*args):
    arg1, arg2 = args
    print "hello, arg1:%s, arg2:%s" % (arg1, arg2)

hello("zhu", "lei")
hello_again("zhu", "peng")
