# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 10:21:59 2020

@author: Bhagyesh kant
"""

import mysql.connector

myconn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123",
  database="bhagyesh"
)

mc = myconn.cursor()
#query="CREATE TABLE utpals (name VARCHAR(255), address VARCHAR(255))"
#mc.execute(query)
q2="show tables"
q3="insert into customers(name,address)"
value=["Utpal","Laptajang"]
mc.execute(q3,value)
print(q3)
