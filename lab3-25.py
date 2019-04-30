#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:20:27 2019

@author: root
"""

class ExampleClass(object):
    """
    this class is an example
    """
    
    def _init_(self,a,b):
        self.a=a
        self.b=b
    
    def set_sum(self):
         """
         this function addds a and b together
         """
        #a+b
        self.sum=self.a+self.b
        
        
example1= ExampleClass(2,4)
example2=ExampleClass(b=5,a=7)
print (example1.a)
print (example2.A)
example1.set_sum()
print(example1.sum)


type(example1)