#!/usr/bin/env python2

class Base(object):
    def __init__(self):
        print("Base __init__.")

class ChildA(Base):
    def __init__(self):
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        super(ChildB, self).__init__()

print ChildA()
print ChildB()

