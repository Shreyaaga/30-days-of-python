import random
number=random.randint(1,1000)
count=0
#n=int(input("enter the value of n"))
guess=int(input("Guess a number between 1 and 1000"))
while guess!=number:
    guess=int(input("Guess a number between 1 and 1000"))
    if(guess==number):
        print("You guessed it right")
        break
    elif(guess>number):
        print("too high")
        count=count+1
    elif(guess<number):
        print("too less")
        count=count+1
print("you guessed the number in",count,"counts")
