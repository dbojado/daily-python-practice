#Guessing Number Game
#Guess number (1 - 10) until you are right
#Program will tell you how many times you guessed 

import random

number = random.randint(1,10)
guess = 0
count = 0


while guess != number and guess != "exit":
    guess = input("What's your guess? ")
    
    if guess == "exit":
        break
    
    guess = int(guess)
    count += 1
    
    if guess < number:
        print("Too low!\n")
    elif guess > number:
        print("Too high!\n")
    else:
        print("Congrats! You got it! And it only took you",count,"tries!\n")