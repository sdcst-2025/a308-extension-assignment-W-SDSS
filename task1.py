import random

x = random.randint(1,100)

guess = input(print("Enter your guess (1-100): "))
guesscount = 0
u = True

while u==True:
    if guess == x:
        print("You are correct.")
        print("guesscount)