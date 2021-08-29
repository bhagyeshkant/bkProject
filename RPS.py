# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 10:58:57 2020

@author: Bhagyesh kant
"""

#import mysql.connector
import random

games=0
p1win=0
p2win=0
cop=0
print("   ________ WELCOME TO _________")
print("~~~~~~~ ROCK PAPER SCISSOR ~~~~~~~~")

mode1=int(input("-- ** (1) for Normal play (2) for Battel play ** --"))
mode = int(input('-- ** (1) Vs. Computer (2) Vs. Second player ** --'))

choices = ['r','p','s']
chi="y"

# print("'CREATE YOUR BATTEL \nENTER NUMBER OF MATCH YOU WANT '")

# game=int(input(" ~Please Enter Number Of Match You Want To Play ~"))

p1=input("Please enter name of first player : ").upper()
#p2=input("Please enter name of second player : ").upper()

if mode1==1:
  if mode==1:
    while chi=="y":
      p1c=input("player1 enter your choice :-")
     
      comp=random.choice(choices)

      if(p1c=="r" or p1c=="s" or p1c=="p") and (comp=="r" or comp=="s" or comp=="p"):
     
         if (p1c=="r" and comp=="s") or (p1c== "p" and comp== "r") or (p1c=="s" and comp== "p"):
              print("Choice of computer",comp)
              print("The winner of this battel is :",p1)
              p1win=p1win+1
              print("THE POINT ",p1," is ",p1win)
         elif (comp=="r" and p1c =="s") or (comp == "p" and p1c =="r") or (comp=="s" and p1c== "p") :
              print("Choice of computer",comp)
              print("The winner of this battel is : computer")
              cop=cop+1
              print("THE POINT ",p1," is ",p1win)
         else:
              print("Choice of computer",comp)
              print("ooohhh this is a DRAW")
              print("------------------------------------")
         print("SCORE OF PLAYER1 ->",p1win)  
         print("SCORE OF COMPUTTER ->",cop)     
      chi=input("PLEASE ENTER 'y' FOR PLAY AGAIN ELSE 'n' FOR EXIT -->")
    
    if (cop==p1win)  :
       print("SCORE OF PLAYER1 ->",p1win)  
       print("SCORE OF COMPUTTER ->",cop)  
       print("\n")
       print("``````````````````````````````")       
       print("  !!!   THIS IS A TIE   !!!   ")
       print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,") 
   
    elif (cop<p1win) :
       print("SCORE OF PLAYER1 ->",p1win)  
       print("SCORE OF COMPUTTER ->",cop)  
       print("\n") 
       print("`````````````````````````````````````````````")       
       print("  !!!   WINNER OF THIS BATTEL PLAYER   !!!   ")
       print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,") 
   
    elif (cop>p1win) :
       print("SCORE OF PLAYER1 ->",p1win)  
       print("SCORE OF COMPUTTER ->",cop)  
       print("\n") 
       print("```````````````````````````````````````````````")       
       print("  !!!   WINNER OF THIS BATTEL COMPUTER   !!!   ")
       print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")    
        
    
  if mode==2:
    p2=input("Please enter name of second player : ").upper()  
    while chi=="y":
      p1c=input("player1 enter your choice :-")
      p2c=input("player2 enter your choice :-")
      
      if(p1c=="r" or p1c=="s" or p1c=="p") and (p2c=="r" or p2c=="s" or p2c=="p"):
     
        if (p1c=="r" and p2c =="s") or (p1c == "p" and p2c == "r") or (p1c=="s" and p2c== "p"):
           print("The winner of this battel is :",p1)
           p1win=p1win+1
           print("THE POINT ",p1," is ",p1win)
        elif (p2c=="r" and p1c =="s") or (p2c == "p" and p1c =="r") or (p2c=="s" and p1c== "p") :
           print("The winner of this battel is :",p2)
           p2win=p2win+1
           print("THE POINT ",p2," is ",p2win)
        else:
           print("ooohhh this is a DRAW")
           print("------------------------------------")
        print("SCORE OF PLAYER1 ->",p1win)  
        print("SCORE OF PLAYER2 ->",p2win)    
      chi=input("PLEASE ENTER 'y' FOR PLAY AGAIN ELSE 'n' FOR EXIT -->")   
   
    if (p2win==p1win)  :
       print("SCORE OF ",p1 ,"->",p1win)  
       print("SCORE OF ",p2 ,"->",p2win)  
       print("\n")
       print("``````````````````````````````")       
       print("  !!!   THIS IS A TIE   !!!   ")
       print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")   
   

 
    elif p2win>p1win :
       print("SCORE OF ",p1 ,"->",p1win)  
       print("SCORE OF ",p2 ,"->",p2win)  
       print("\n") 
       print("```````````````````````````````````````````````")       
       print("  !!!   WINNER OF THIS BATTEL PLAYER2   !!!   ")
       print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,") 

    elif p2win<p1win :
       print("SCORE OF ",p1 ,"->",p1win)  
       print("SCORE OF ",p2 ,"->",p2win)  
       print("\n") 
       print("```````````````````````````````````````````````")       
       print("  !!!   WINNER OF THIS BATTEL PLAYER1  !!!   ")
       print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
    
    
    
if mode1==2:
   print("'CREATE YOUR BATTEL \nENTER NUMBER OF MATCH YOU WANT '")
   game=int(input(" ~Please Enter Number Of Match You Want To Play ~"))
   if mode == 1: 
      while games<game:  
         games=games+1  
     
         p1c=input("Please enter your choice Player1:-").lower() 
         comp = random.choice(choices)
         if(p1c=="r" and comp=="s"):
             p1win=p1win+1
             print("THE WINNER OF THIS MATCH IS",p1,p1c,"beats ",comp)
             print(p1win," point for -->",p1)
         elif(p1c=="s" and comp=="p"):
             p1win=p1win+1
             print("THE WINNER OF THIS MATCH IS",p1,p1c,"beats ",comp)
         elif(p1c=="p" and comp=="r"):
             p1win=p1win+1
             print("THE WINNER OF THIS MATCH IS",p1,p1c,"beats ",comp)
         elif(p1c=="r" and comp=="p"):
             cop=cop+1
             print("THE WINNER OF THIS MATCH IS",comp,"beats ",p1c)
         elif(p1c=="p" and comp=="s"):
             cop=cop+1
             print("THE WINNER OF THIS MATCH IS",comp,"beats ",p1c) 
         elif(p1c=="s" and comp=="r"):
             cop=cop+1
             print("THE WINNER OF THIS MATCH IS",comp,"beats ",p1c)   
         else: 
             print("Oops ! the match is tie.  \U0001f600","COMPUTER :-",cop,p1,p1win)
         print("SCORE OF PLAYER1 ->",p1win)  
         print("SCORE OF COMPUTTER ->",cop)       
  
      if (cop==p1win):
           print("SCORE OF PLAYER1 ->",p1win)  
           print("SCORE OF COMPUTTER ->",cop)  
           print("\n")
           print("``````````````````````````````")       
           print("  !!!   THIS IS A TIE   !!!   ")
           print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,") 
   
      elif cop<p1win :
           print("SCORE OF PLAYER1 ->",p1win)  
           print("SCORE OF COMPUTTER ->",cop)  
           print("\n") 
           print("`````````````````````````````````````````````")       
           print("  !!!   WINNER OF THIS BATTEL PLAYER   !!!   ")
           print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,") 
   
      elif cop>p1win :
          print("SCORE OF PLAYER1 ->",p1win)  
          print("SCORE OF COMPUTTER ->",cop)  
          print("\n") 
          print("```````````````````````````````````````````````")       
          print("  !!!   WINNER OF THIS BATTEL COMPUTER   !!!   ")
          print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")    
  
    
   if mode==2 :
      p2=input("Please enter name of second player : ").upper()
      
      while games<game:
         p1c=input("Please enter your choice Player1:-").lower()     
         p2c=input("Please enter your choice Player2 :-").lower() 
         games=games+1 
           
         if(p1c=="r" and p2c=="s"):
             p1win=p1win+1
             print("THE WINNER OF THIS MATCH IS",p1,p1c,"beats ",p2c)
         elif(p1c=="s" and p2c=="p"):
             p1win=p1win+1
             print("THE WINNER OF THIS MATCH IS",p1,p1c,"beats ",p2c)
         elif(p1c=="p" and p2c=="r"):
             p1win=p1win+1
             print("THE WINNER OF THIS MATCH IS",p1,p1c,"beats ",p2c)
         elif(p1c=="r" and p2c=="p"):
             p2win=p2win+1
             print("THE WINNER OF THIS MATCH IS",p2,p2c,"beats ",p1c)
         elif(p1c=="p" and p2c=="s"):
             p2win=p2win+1
             print("THE WINNER OF THIS MATCH IS",p2,p2c,"beats ",p1c) 
         elif(p1c=="s" and p2c=="r"):
             p2win=p2win+1
             print("THE WINNER OF THIS MATCH IS",p2,p2c,"beats ",p1c)   
         else:
             print("Oops ! the match is tie.  \U0001f600")
             
         print("SCORE OF PLAYER2 ->",p2win) 
         print("SCORE OF PLAYER1 ->",p1win)  
         print("\n")
   
         if (p2win==p1win)  :
             print("SCORE OF ",p1 ,"->",p1win)  
             print("SCORE OF ",p2 ,"->",p2win)  
             print("\n")
             print("``````````````````````````````")       
             print("  !!!   THIS IS A TIE   !!!   ")
             print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")   
   
         elif p2win>p1win :
             print("SCORE OF ",p1 ,"->",p1win)  
             print("SCORE OF ",p2 ,"->",p2win)  
             print("\n") 
             print("```````````````````````````````````````````````")       
             print("  !!!   WINNER OF THIS BATTEL PLAYER2   !!!   ")
             print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,") 

         elif p1win>p2win :
             print("SCORE OF ",p1 ,"->",p1win)  
             print("SCORE OF ",p2 ,"->",p2win)  
             print("\n") 
             print("```````````````````````````````````````````````")       
             print("  !!!   WINNER OF THIS BATTEL PLAYER1  !!!   ")
             print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")

# # name=""
# # score=[p1win]
# db = mysql.connector.connect( host = "localhost",user = "root",password = "123")
# cursor = db.cursor()
# cursor.execute("CREATE DATABASE mydatabase")
# crtt="CREATE TABLE Stats (NAME varchar(25),SCORE int)"
# cursor.execute(crtt)
# inst="""INSERT into Stats (NAME , SCORE ) values (p1,p1win) """
# cursor.execute(inst)    
# db.commit()        
# for i in cursor:
#     print(i)