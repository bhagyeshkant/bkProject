# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 00:23:25 2020

@author: Bhagyesh kant
"""

import time
b = 2.9
c = 0.08
def intro():
    print("\n\t\t!!!! Welcome to Advanture !!!!\n")
    time.sleep(b)
    print("""\t\t whatt... Happen...
             Were are the rest people gone... ☹️ 
             Something is wrong .....
             I have to check....
             (A door shut)
             """)
    time.sleep(b)         
    print("\t\t wha.. what happen,, Who's that..??") 
    time.sleep(b) 
    print("\t\t Oohh shit! i think i'm in a trap ")
    time.sleep(b) 
    print("\t\t There is two door i can see... ")
    time.sleep(c)
    bk=int(input("There is two door , select one of them :-"))
    if bk==1:
        door1()
    if bk==2:
        door2()
        
def door1():
    print("""\t\t Light start blinking !!!!
                  """)   
    time.sleep(b)               
    print("""\t\t I have to get out from this HELL...""")
    time.sleep(b) 
    print("\t\t yaah there is a door... no there is two door...")
    time.sleep(b)
    bk=int(input("There is two door , select one of them :-"))
    if bk==1:
        door1of1()
    if bk==2:
        door1of2()
    
def door1of1():              
    print("\t\t All the things in a room looks destroy..")
    time.sleep(b)
    print("\t\t Whatt i do...now")
    time.sleep(b)
    print("\t\t Oh God let's get out from here this place is HAUNTED...")
    time.sleep(c)
    bk=int(input("There is two door , select one of them :-"))
    if bk==1:
        door1of1of1()
    if bk==2:
        door1of1of2()
        
#siplos eye drop 
    
def door1of1of1():
    print("\t\t Again... an Again....")
    time.sleep(b)
    print("\t\t Same things... is Happening")
    time.sleep(b)
    print("\t\t I think this is a hall...")    
    time.sleep(c)
    bk=int(input("There is two door , select one of them :-"))
    if bk==1:
        win()
    if bk==2:
        creature()
    
def door1of1of2():
    print("\t\t Noooo...")
    time.sleep(b)
    print("\t\t I chose a wrong door")
    time.sleep(b)
    print()    
    bk=int(input("There is two door , select one of them :-"))
    if bk==1:
        lastroom()
    if bk==2:
        creature()
    
def door1of2():
    print("\t\t OH MY GOD....")
    time.sleep(b)
    print("\t\t All the doors look same...")  
    time.sleep(b)
    bk=int(input("There is two door , select one of them :-"))
    if bk==1:
        door1of2of1()
    if bk==2:
        door1of2of2()
    
def door1of2of1():
    print("\t\t Noooo...")
    time.sleep(b)
    print("\t\t I chose a wrong door")
    time.sleep(b)
    print()    
    bk=int(input("There is two door , select one of them :-"))
    if bk==1:
        win()
    if bk==2:
        creature()
    
def door1of2of2():
    print("\t\t whaat .... where i'm now...")
    time.sleep(b)
    print("\t\t i think i'm in a loop")
    time.sleep(b)
    print()    
    bk=int(input("There is two door , select one of them :-"))
    if bk==1:
        win()
    if bk==2:
         lastroom()
    
def door2():
    print("\t\t All the toys are broken...")  
    time.sleep(b)
    print("\t\t This room is for babiess")
    time.sleep(b)
    print()
    bk=int(input("There is two door , select one of them :-"))
    if bk==1:
        door2of1()
    if bk==2:
        door2of2()
    
def door2of1():
    print("\t\t This looks so haunted...")
    time.sleep(b)
    print("\t\t horribel paintings are ther...e !")
    time.sleep(b)
    print()
    bk=int(input("There is two door , select one of them :-"))
    if bk==1:
        door2of1of1()
    if bk==2:
        door2of1of2()
    
def door2of1of1():
    print("\t\t Noooo...")
    time.sleep(b)
    print("\t\t I chose a wrong door")
    time.sleep(b)
    print()
    bk=int(input("There is two door , select one of them :-"))
    if bk==1:
        win()
    if bk==2:
        creature()
    
def door2of1of2():
    print("\t\t I think i reached in a safe room")
    time.sleep(b)
    print("\t\t I can feel the exit point near about me..")
    time.sleep(b)
    print()    
    bk=int(input("There is two door , select one of them :-"))
    if bk==1:
        win()
    if bk==2:
        creature()
    
def door2of2():
    print("\t\t This room is quite different...")
    time.sleep(b)
    print("\t\t let's move on...")
    time.sleep(b)
    print()
    bk=int(input("There is two door , select one of them :-"))
    if bk==1:
        door2of2of1()
    if bk==2:
        door2of2of2()
    
def door2of2of1():
    print("\t\t Noooo...")
    time.sleep(b)
    print("\t\t I chose a wrong door")
    time.sleep(b)
    print()
    creature()
def door2of2of2():
    print("\t\t SOmeone is behind the door")
    time.sleep(b)
    print("\t\t One door is a safe...")
    time.sleep(b)
    bk=int(input("There is two door , select one of them :-"))
    if bk==1:
        win()
    if bk==2:
        creature()
    
def lastroom():
    print("\t\t again this is a DARK  room ....")
    time.sleep(b)
    print("\t\t take a safe door..")
    time.sleep(b)
    print() 
    bk=int(input("There is two door , select one of them :-"))
    if bk==1:
        lastroomof1()
    if bk==2:
        lastroomof2()
    
def lastroomof1():
    print("\t\t I feel afraid... to see this...")
    time.sleep(b)
    print("\t\t Help me to select the right door ... ")
    time.sleep(b)
    print() 
    bk=int(input("There is two door , select one of them :-"))
    if bk==1:
        win()
    if bk==2:
        creature()
    
def lastroomof2():
    print("\t\t Noooo...")
    time.sleep(b)
    print("\t\t I chose a wrong door")
    time.sleep(b)
    print() 
    bk=int(input("There is two door , select one of them :-"))
    if bk==1:
        win()
    if bk==2:
        creature()
    
def win():
   print("yes i escape from that house")    
    
def creature():
    print("creature has eaten your gosh...")


print()
print()
# from PIL import Image                     
# img = Image.open('Double-Scooper-by-Enrique-Hernandez.jpg')                                                           
# # img = Image.open('Double-Scooper-by-Enrique-Hernandez.jpg')
# img.show()
print()
print()
strt = input("Would you like to start the game? (Y/N): ")
if strt == "y" :
     intro()
elif strt == "n" :
     print("Maybe next time")   
    
    