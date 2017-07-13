# !/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'wtq'

class A(object):
    def __init__(self):
        self.a = 1
    def foo(self, x):
        print "excuting foo(%s, %s)"%(self, x)

    @classmethod
    def class_foo(cls, x):
        print "exceting class_foo(%s, %s)"%(cls, x)

    @staticmethod
    def static_foo(x):
        print "excuting static_foo(%s)"%x

a = A()
a.foo(1)
A.foo(a, 1)
a.static_foo(1)
A.static_foo(2)
