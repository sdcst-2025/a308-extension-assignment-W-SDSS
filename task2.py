import random

u = True
correct = 0
incorrect = 0

while u == True:
    coin = random.choice(["heads", "tails"])
    guess = input(print("Coin Toss. Enter your choice, heads or tails: "))
    if coin == guess:
        print("You are correct!!")
        correct += 1
        con = input(print("Do you want to go again(yes or no)?"))
        if con == "yes":
            continue
        else:
            print(f"You've correct {correct} times, and incorrect {incorrect}.")
            break
    else:
        print("You are wrong!!")
        print("Try again")
        incorrect += 1
        continue

#nannka busaiku na coding
#kirei ni suru