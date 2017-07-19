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

class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, "_instance"):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance
class MyClass(Singleton):
    a = 1

a = A()
a.foo(1)
A.foo(a, 1)
a.static_foo(1)
A.static_foo(2)
