#!/usr/bin/env python2

class Other(object):

    def implicit(self):
        print "Other::implicit()"

    def override(self):
        print "Other::override()"

    def altered(self):
        print "Other::altered()"

class Son(Other):

    def __init__(self):
        self.other = Other()

    def override(self):
        print "Son::override()"

    def altered(self):
        print "Son::altered(), before Other::altered()"
        self.other.altered()
        print "Son::altered(), after Other::altered()"

son = Son()

son.implicit()
son.override()
son.altered()
