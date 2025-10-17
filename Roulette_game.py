# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 01:25:55 2020

@author: Bhagyesh kant
"""

def welcome():
    print('\n\t\twelcome to the Europian  roulette \n')
welcome()

def instruction():
     
     print("In Roulette we've two type of bets.\n")
     print("1. Inside bet.")
     print("2. Outside bet")
     print("\n")
     print("* Each types having 5 betting options.")
     print("\n")
     print("""\t\t\tINSIDE BETS            OUTSIDE BETS gggg
           -----------------------------------------
              1. Straight bet        1. Column bet
              2. Split bet           2. Dozen bet
              3. Street bet          3. Bet on Colour
              4. Double street bet   4. Odd & Even
              5. Corner bet          5. High & Low""")
instruction()

print("-"*80,"\n")

def Board():
    
    print('|   |||')
    print('|   | 3 | 6 | 9 | 12 | 15 | 18 | 21 | 24 | 27 | 30 | 33 | 36 | 2:1 |')
    print('|   |__|')
    print('| 0 | 2 | 5 | 8 | 11 | 14 | 17 | 20 | 23 | 26 | 29 | 32 | 35 | 2:1 |')
    print('|   |__|')
    print('|   | 1 | 4 | 7 | 10 | 13 | 16 | 19 | 22 | 25 | 28 | 31 | 34 | 2:1 |') 
    print('|   |__| ')
    print('|   |     1st 12    |     2nd 12        |       3rd  12     |') 
    print('|   |_| ')
    print('|   |   1 to 18   | Even | Red | Black | odd |   19 to 36  |')
    print('|   |__|\n')
Board()

ch="y"
while ch=="y":
 import random 

 def replace():
     print("1. Inside bet.")
     print("2. Outside bet")          
     bet_choice=int(input("Press :-"))
     if bet_choice == 1:
        print("It's an Inside betting option")
        print("""\t\t\tINSIDE BETS         
               ------------------------
                  1. Straight bet        
                  2. Split bet          
                  3. Street bet          
                  4. Double street bet 
                  5. Corner bet          """)
                  
        inbet=int(input("Press your option :-"))
         
        print("REPLACE YOUR BET!")
        rep=int(input("PRESS 1 TO REPALCE ELSE 0 TO CONTINUE!")) 
        if rep==1:
          replace() 
        else:
            if inbet==1:
             def straight_bet():
              bk=[0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
              bk=int(input("Please select number between 0 to 36 : "))
              # print("You select a numer",bk)
              comp = random.choice(range(0,36))
              print(comp)
              if (bk==comp):
                 print("congrats")
              else:
                  print("uh lost")
             straight_bet()
    
    # here are 114 split bet combinations
              
            if inbet==2:
                def split_bet():
                 cho=int(input("Please chose 1 for HORIZENTAL or 2 for VERTICAL"))
                 bk=[3,6,9,12,15,18,21,24,27,30,33]
                 bb=[]  
                 b=int(input("enter a number"))
                 if cho==1:
                   a=lambda b: str(str(b)+"," +str(b+3))  
                   bb.append(a(b))
                   print(bb)
                   comp=random.randint(0,36)
                   if a in bk:
                       print(comp,"U r winner")
                   else:
                       print(comp,"u lost")
                 if cho==2:   
                  if b not in bk:
                     a=lambda b: str(str(b)+"," +str(b+1))  
                     bb.append(a(b))
                     print(bb)
                     comp=random.choice(bk)
                     if a in bk:
                       print(comp," u r winner")
                     else:
                       print(comp," uh lost")
                  else:
                      print("Enter valid number")
                split_bet()
            #  galat h be idhar
            if inbet==3:
              def street_bet(): 
                    
                 print("Please select a number from ")
                 print("4,7,10,13,16,19,22,25,28,31,34")
            
                 bk={1,4,7,10,13,16,19,22,25,28,31,34}
                 bb=[]
                 b=int(input("enter a number"))
                 if b in bk :    
                   a=lambda b: str(str(b)+"," + str(b+1)+"," +str(b+2))  
                   bb.append(a(b))
                   print(bb)
                   comp = random.choice(range(0,36))
                   print(comp)
                   if comp in bb:
                       print("congrats")
                   else:
                       print("uh lost")
                 else:
                    print("Sorry please enter a number from above choice")
                
              street_bet()   
            
            if inbet==4:
              def Double_street_bet(): 
                print("Please select a number from")
                print("1,4,7,10,13,16,19,22,25,28,31")
                
                
                bk={1,4,7,10,13,16,19,22,25,28,31}
                bb=[]
                b=int(input("enter a number"))
                if b in bk :    
                   a=lambda b: str(str(b)+"," + str(b+1)+"," +str(b+2)+","+ str(b+3)+"," + str(b+4)+"," +str(b+5))  
                   bb.append(a(b))
                   print(bb)
                   comp = random.choice(range(0,36))
                   print(comp)
                   if comp in bb:
                       print("congrats")
                   else:
                       print("uh lost")
                else:
                    print("Sorry please enter a number from above choice")
              Double_street_bet()  
              
            if inbet==5:
              def corner_bet():
                bk={3,6,9,12,15,18,21,24,27,30,33,36}
                print("Don't Enter these numbers, given below :")
                print("3,6,9,12,15,18,21,24,27,30,33,36")
                bb=[]
                b=int(input("enter a number"))
                if b not in bk :    
                   a=lambda b: str(str(b)+"," + str(b+1)+"," +str(b+3)+"," +str(b+4))  
                   bb.append(a(b))
                   print(bb)
                   comp = random.choice(range(0,36))
                   print(comp)
                   if bb== comp:
                       print("congrats")
                   else:
                       print("uh lost")
                else:
                    print("Enter valid numbers ")     
              corner_bet()
                   
     elif bet_choice == 2:  
        print("It's an outside betting option")
        print("""\t\tOUTSIDE BETS
               ----------------------
                  1. Column bet
                  2. Dozen bet
                  3. Bet on Colour
                  4. Odd & Even
                  5. High & Low""")
        inbet=int(input("Press your option :-"))
        print("REPLACE YOUR BET!")
        rep=int(input("PRESS 1 TO REPALCE ELSE 0 TO CONTINUE!")) 
        if rep==1:
          replace() 
        else:  
            if inbet==1:
              def column_bet():
                  C1=[1 , 4 , 7 , 10 , 13 , 16 , 19 , 22 , 25 , 28 , 31 , 34 ]
                  C2=[ 2 , 5 , 8 , 11 , 14 , 17 , 20 , 23 , 26 , 29 , 32 , 35 ]
                  C3=[3 , 6 , 9 , 12 , 15 , 18 , 21 , 24 , 27 , 30 , 33 , 36]
                  C4= C1+C2+C3
                  
                  cho=int(input("Please chose column 1 , 2 , 3, or 4 (all three column) :-"))
                  if cho==1:
                    print(C1)  
                    comp = random.choice(range(0,36))
                    print(comp)
                    if comp in C1:
                       print("congrats")
                    else:
                      print("uh lost")
                  if cho==2:
                    print(C2)  
                    comp = random.choice(range(0,36))
                    print(comp)
                    if comp in C2:
                      print("congrats")
                    else:
                      print("uh lost")           
                     
                  if cho==3:
                     print(C3) 
                     comp = random.choice(range(0,36))
                     print(comp)
                     if comp in C3:
                       print("congrats")
                     else:
                       print("uh lost")      
             
                  if (cho==4):
                     comp = random.choice(range(0,36))
                     print(comp)
                     if comp in C4:
                       print("congrats")
                     else:
                       print("uh lost")  
              column_bet()
            
            if inbet==2:
              def dozen_bet():
                    ist=[1,2,3,4,5,6,7,8,9,10,11,12]
                    iind=[13,14,15,16,17,18,19,20,21,22,23,24]
                    iiird=[25,26,27,28,29,30,31,32,33,34,35,36]
                    C4= ist+iind+iiird
                    
                    cho=int(input("Please chose DOZEN 1 , 2 , 3, or 4 (all three dozen) :-"))
                    if cho==1:
                       print(ist) 
                       comp = random.choice(range(0,36))
                       print(comp)
                       if comp in ist:
                         print("congrats")
                       else:
                         print("uh lost")
                    if cho==2:
                       print(iind) 
                       comp = random.choice(range(0,36))
                       print(comp)
                       if comp in iind:
                         print("congrats")
                       else:
                         print("uh lost")           
                     
                    if cho==3:
                       print(iiird) 
                       comp = random.choice(range(0,36))
                       print(comp)
                       if comp in iiird:
                         print("congrats")
                       else:
                         print("uh lost")      
             
                    if (cho==4):
                       comp = random.choice(range(0,36))
                       print(comp)
                       if comp in C4:
                         print("congrats")
                       else:
                         print("uh lost") 
              dozen_bet()
              
            if inbet==3:
             def bet_on_color():
               red=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
               black=[2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
               C4= red+black
               
               cho=int(input("Please choose COLOUR 1 for red and 2 for black as well 3 for (both colour ) :-"))
               if cho==1:
                 print(red)
                 comp = random.choice(range(0,36))
                 print(comp)
                 if comp in red:
                       print("congrats")
                 else:
                       print("uh lost")
               if cho==2:
                 print(black)  
                 comp = random.choice(range(0,36))
                 print(comp)
                 if comp in black:
                       print("congrats")
                 else:
                       print("uh lost")   
               if (cho==3):
                 comp = random.choice(range(0,36))
                 print(comp)
                 if comp in C4:
                       print("congrats")
                 else:
                       print("uh lost")                 
             bet_on_color()    
             
            if inbet==4:
              def odd_and_even():
                odd=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
                even=[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
                C4= odd+even
                
                cho=int(input("Please choose  1 for odd and 2 for even as well 3 for (both odd and even) :-"))
                if cho==1:
                   comp = random.choice(range(0,36))
                   print(comp)
                   if comp in odd:
                       print("congrats")
                   else:
                       print("uh lost")
                if cho==2:
                   comp = random.choice(range(0,36))
                   print(comp)
                   if comp in even:
                       print("congrats")
                   else:
                       print("uh lost")   
                if (cho==3):
                   comp = random.choice(range(0,36))
                   print(comp)
                   if comp in C4:
                       print("congrats")
                   else:
                       print("uh lost")      
              odd_and_even()
        
                
            if inbet==5:
              def high_low_bet():
                high=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
                low=[19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]    
                C4= high+low
               
                cho=int(input("Please choose 1 for 1st half and 2 for 2nd half as well 3 for (both 1st and 2nd) :-"))
                if cho==1:
                    
                    comp = random.choice(range(0,36))
                    print(comp)
                    if comp in high:
                       print("congrats")
                    else:
                       print("uh lost")
                if cho==2:
                   comp = random.choice(range(0,36))
                   print(comp)
                   if comp in low:
                       print("congrats")
                   else:
                       print("uh lost")   
                if (cho==3):
                   comp = random.choice(range(0,36))
                   print(comp)
                   if comp in C4:
                       print("congrats")
                   else:
                       print("uh lost")           
        
              high_low_bet()
 replace()   
 ch=input("Press y for play further or Press n for exit :-")
