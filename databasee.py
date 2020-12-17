# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 11:09:01 2020

@author: Bhagyesh kant
"""

a=[]
for i in range(2,21):
   if i%2==0:
      print(i)
      a.append(i)
      print(a)      
class vehchel:
    def __init__(self, speed, milaze):
        self.speed = speed
        self.milaze = milaze

p1 = vehchel(120,25)

print(p1.speed,"km/hr")
print(p1.milaze,"km/ltr")      
def add(*args):
    c=0
    for i in args:
        c=c+i
    return c   