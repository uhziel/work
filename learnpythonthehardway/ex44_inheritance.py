#!/usr/bin/env python2

class Dad(object):

    def implicit(self):
        print "Dad::implicit()"

    def override(self):
        print "Dad::override()"

    def altered(self):
        print "Dad::altered()"

class Son(Dad):

    def override(self):
        print "Son::override()"

    def altered(self):
        print "Son::altered(), before Dad::altered()"
        super(Son, self).altered()
        print "Son::altered(), after Dad::altered()"

dad = Dad()
son = Son()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
