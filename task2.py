import random

w = ["heads", "tails"]
correct = 0
incorrect = 0

while True:
    coin = random.choice(w)
    print("0:heads, 1:tails")
    guess = w[int(input("Coin Toss. Enter a number: "))]
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
        continue

#nannka busaiku na coding