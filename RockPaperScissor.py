# Rock  Paper Scissor game 

import random

print("****Rock Paper and Scissors Game****")
computer_score=0 # initial scores
user_score=0 #initial scores
No_of_ties=0 #initial score
print(""" Rules:
1. Rock vs Paper ->  Paper
2. Rock vs Scissors ->  Rock
3. Rock vs Rock -> ties
4. Paper vs Scissors -> Scissor
5. Paper vs Paper -> ties
6. Scissors vs Scissors -> ties
""")
print()
while True:
    print(""" Choices:
    1. Rock
    2.Paper
    3.Scissors       """)
    print()
    choice= int(input("Enter Your Choice from 1-3: "))
    print()
    if(choice>3 or choice<1):
        choice= int(input("enter valid input"))   

    if choice==1:
        user_choice= "Rock"
    elif choice==2:
        user_choice="Paper"
    else:
        user_choice    = "Scissors"
        
    print(f"{user_choice} is the choice of the user") 
    print()

    print("Now Computer's Turn ")
    print()
    computer= random.randint(1,3) 

    if computer==1:
        computer_choice= "Rock"
    elif computer==2:
        computer_choice="Paper"
    else:
        computer_choice    = "Scissors"

    print(f"{computer_choice} is the choice of the computer")  

    if((user_choice=="Paper" and computer_choice=="Rock") or (user_choice=="Rock" and computer_choice=="Paper")):
        print("Paper wins")
        result= "paper"
    elif((user_choice=="Scissors" and computer_choice=="Rock") or (user_choice=="Rock" and computer_choice=="Scissors")):
        print("Rock wins")
        result= "Rock"
    elif(user_choice==computer_choice):
        print("Match ties")
        result="Tie"      
    else:
        print("Scissors wins")
        result="Scissors"    

    if result=="Tie":
        No_of_ties +=1
    elif result ==user_choice:
        print("user wins")
        user_score  +=1
    else:
        print("computer wins")
        computer_score +=1   
        
    print("Scores:")
    print("Score of user are:" , user_score)         
    print("Score of computer are:" , computer_score)         
    print("Ties are:" , No_of_ties)         
       
      
    repeat= input("Do you wanna play again?")
    if repeat=="no" or  "No":
        print("Game Over!")