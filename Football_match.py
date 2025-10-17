ch=""
while ch!="y":
    teamA=input("Enter 1st Team Name : ").upper()
    teamB=input("Enter 2nd Team Name : ").upper()
    print("\n")
    teamA_score=00
    teamB_score=00
    print("""
      Press 1 for Team A
      Press 2 for Team B
      Press 3 for Final Score Card and Game Ends !!! """
      )
    print("\n")
    print("\t ",teamA,"\t ", teamA_score, "\t  | | \t ",teamB,"\t ", teamB_score)
    print("\n")
    end= "y"
    while end== "y":
     choice=int(input("Choose Team, 1, 2 or 3 : "))
     if choice ==1:
            teamA_score=teamA_score+1
            print("\n")
            print("\t ",teamA,"\t ", teamA_score, "\t  | | \t ",teamB,"\t ", teamB_score)
            print("\n")
     elif choice ==2:
            teamB_score=teamB_score +1
            print("\n")
            print("\t ",teamA,"\t ", teamA_score, "\t  | | \t ",teamB,"\t ", teamB_score)
            print("\n")
     elif choice ==3:
         print("\n")
         print(" Final Score Card ")
         print("\n")
         print("\t ",teamA,"\t ", teamA_score, "\t  | | \t ",teamB,"\t ", teamB_score)
         print("\n")
         if teamA_score>teamB_score:
             print("\t",teamA, "is Winner !!")
         elif teamA_score<teamB_score:
             print("\t",teamB, "is Winner !! ")
         else:
             print("\t Match Drawn !! ")
         break
     else:
            print("\n")
            print("Please Enter 1, 2 or 3 ")
            print("\n")
    ch=input("Press y to exit or else press any key to restart :")
