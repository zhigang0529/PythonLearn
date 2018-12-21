#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Parent:
    parentAttr = 100

    def __init__(self):
        print "call parent init"

    def parentmethod(self):
        print 'call parent method'

    def setattr(self, attr):
        Parent.parentAttr = attr

    def getattr(self):
        print "Parent attr ", Parent.parentAttr

    def __str__(self):
        return '(Parent: %s )' % (self.parentAttr)

class Child(Parent):
    def __init__(self):
        print "call sub init"

    def childmethod(self):
        print 'call sub method'


c = Child()
c.childmethod()
c.parentmethod()
c.setattr(200)
c.getattr()

par = Parent
print(par)