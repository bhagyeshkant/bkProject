# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 10:56:40 2020

@author: Bhagyesh kant
"""

import pandas as pd
li=[["Abhiyuday","1","yes"],["Utpal","2","yes"],["Deepak","3","yes"],["Taushif","4","yes"],["Bhagyesh","5","yes"],["Ritik","6","no"]]
li=pd.DataFrame(li,index=["std1","std2","std3","std4","std5","std6"],columns=["Name","Rollno","Hostel"])
#li=pd.DataFrame(li)
print(li,"\n")
li["cpp"]=[35,30,32,33,29,39]
print(li)
print(li.loc["std1"])
print(li.iloc[1:])
