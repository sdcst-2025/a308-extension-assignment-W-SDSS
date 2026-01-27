import random

correct = 0
incorrect = 0

while True:
    coin = random.randint(0, 1)
    guess = int(input("0:heads, 1:tails"))
    if coin == guess:
        print("You are correct!!")
        correct += 1
        con = input("Do you want to go again(yes or no)?")
        if con == "yes":
            continue
        else:
            print(f"You've correct {correct} times, and incorrect {incorrect}.")
            break
    else:
        print("You are wrong!!")
        print("Try again")
        incorrect += 1