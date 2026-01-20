import random

choices = random.choice(["rock","scissors", "paper", "lizard", "spock"])
user = str(input(print("Enter your choices, rock, scissors, paper, lizard and spock: ")))
u = True

while u == True:
    if user == "rock":
        if choices == "izard" or "scissors":
            print("You win!!")
            break
        if choices == "paper" or "spock":
            print("You lose")
            continue
        else:
            print("One more time.")
    if user == "scissors":
        if choices == "izard" or "paper":
            print("You win!!")
            break
        if choices == "rock" or "spock":
            print("You lose")
            continue
        else:
            print("One more time.")
    if user == "paper":
        if choices == "rock" or "spock":
            print("You win!!")
            break
        if choices == "scissors" or "lizard":
            print("You lose")
            continue
        else:
            print("One more time.")
    if user == "lizard":
        if choices == "spock" or "paper":
            print("You win!!")
            break
        if choices == "rock" or "scissors":
            print("You lose")
            continue
        else:
            print("One more time.")
    if user == "spock":
        if choices == "scissors" or "rock":
            print("You win!!")
            break
        if choices == "lizard" or "paper":
            print("You lose")
            continue
        else:
            print("One more time.")