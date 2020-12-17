# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 11:05:22 2020

@author: Bhagyesh kant
"""

import mysql.connector
db = mysql.connector.connect( host = "localhost",user = "root",password = "123")
cursor = db.cursor()
crt="CREATE DATABASE project"
cursor.execute(crt)
crtt="CREATE TABLE hospital (ID int,NAME varchar(25),BED int)"
crtt2="CREATE TABLE doctor (ID int,NAME varchar(25),EXPERIENCE int, SPECALITY varchar,SALARY int)"
inst=""" "INSERT into hospital (ID,NAME,BED) VALUES (1234,"PMCH",5000),(1235,"AIIMS",4500),(1236,"AAROGYA"1200),(1237,"VASUNDHRA",2000),(1238,"PARAS",3600)"""
