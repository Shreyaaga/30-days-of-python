import random

choices = ['rock', 'paper', 'scissors']
index=random.randint(0,2)

comp_choice =choices[index]
user_choice=input("enter your choice as rock,paper or scissors:")

if (comp_choice==user_choice):
    print("Tie game")
    print("user chosed:",user_choice)
    print("computer chosed:",comp_choice)
elif (comp_choice=='rock' and user_choice=='paper'):
    print("user chosed:",user_choice)
    print("computer chosed:",comp_choice)
    print("user wins")
elif (comp_choice=='rock' and user_choice=='scissors'):
    print("user chosed:",user_choice)
    print("computer chosed:",comp_choice)
    print("computer wins")
elif (comp_choice=='paper' and user_choice=='rock'):
    print("user chosed:",user_choice)
    print("computer chosed:",comp_choice)
    print("computer wins")
elif (comp_choice=='paper' and user_choice=='scissors'):
    print("user chosed:",user_choice)
    print("computer chosed:",comp_choice)
    print("user wins")
elif (comp_choice=='scissors' and user_choice=='paper'):
    print("user chosed:",user_choice)
    print("computer chosed:",comp_choice)
    print("computer wins")
elif (comp_choice=='scissors' and user_choice=='rock'):
    print("user chosed:",user_choice)
    print("computer chosed:",comp_choice)
    print("user wins")
else:
    print("wrong input !! please enter all the charecters in lower case")




