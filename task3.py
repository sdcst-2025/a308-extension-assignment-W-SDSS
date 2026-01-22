import random

hand = ["rock","scissors", "paper", "lizard", "spock"]

def ww(user, cp):
    if user == "rock" and (cp == "scissors" or cp == "lizard"):
        return True
    if user == "scissors" and (cp == "paper" or cp == "lizard"):
        return True
    if user == "paper" and (cp == "rock" or cp == "spock"):
        return True
    if user == "lizard" and (cp == "paper" or cp == "spock"):
        return True
    if user == "spock" and (cp == "rock" or cp == "scissors"):
        return True
    else:
        return False

while True:
    cp = random.choice(hand)
    print("0:rock, 1:scissors, 2:paper, 3:lizard, 4:spock")
    user = hand[int(input("Enter a number: "))]
    if cp == user:
        print("try again")
        continue
    elif ww(user, cp):
        print("You win")
        break
    else:
        print("You lost")
        continue

