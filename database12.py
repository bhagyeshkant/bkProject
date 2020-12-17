# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 10:42:37 2020

@author: Bhagyesh kant
"""

import mysql.connector
db = mysql.connector.connect( host = "localhost",user = "root",password = "123",database="infogain")
cursor = db.cursor()
#sql = "CREATE TABLE employee (NAME varchar(25),FATHER_NAME varchar(25),MANAGER varchar(25)) "
inst= """INSERT into employee (NAME ,FATHER_NAME ,MANAGER ) """
val= [("BK","NKM","AM"),("HERO","SAKTIMAN","BAHUBALI")]

cursor.executemany(inst,val)
db.commit()
print("List of tables: ")
cursor.execute("SHOW TABLES")
q3="select * from employee"
db.execute()
a=db.fetchall()
# mc.execute("show databases")
for i in a:
    print(i)
print(cursor.fetchall())

db.close()