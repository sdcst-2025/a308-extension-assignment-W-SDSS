import random

choices = random.choice(["rock","scissors", "paper", "lizard", "spock"])
user = input(print("Enter your choices, rock, scissors, paper, lizard and spock: "))
u = True

while u == True:
    if choices == "rock":
        if user == "izard" or "scissors":
            print("You win!!")
            break
        if user == "paper" or "spock":
            print("You lose")
            continue
    if choices == "scissors":
        if user == "izard" or "paper":
            print("You win!!")
            break
        if user == "rock" or "spock":
            print("You lose")
            continue
    if choices == "paper":
        if user == "rock" or "spock":
            print("You win!!")
            break
        if user == "scissors" or "lizard":
            print("You lose")
            continue
    if choices == "lizard":
        if user == "spock" or "paper":
            print("You win!!")
            break
        if user == "rock" or "scissors":
            print("You lose")
            continue
    if choices == "spock":
        if user == "scissors" or "rock":
            print("You win!!")
            break
        if user == "lizard" or "paper":
            print("You lose")
            continue