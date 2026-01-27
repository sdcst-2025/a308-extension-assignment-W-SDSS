import random

x = random.randint(1,100)
guesscount = 0

while True:
    guess = int(input("Enter your guess (1-100): "))
    guesscount += 1
    if guess == x:
        print("You are correct!!")
        print(f"You've guessed {guesscount} times")
        break
    elif guess >= x:
        print("its too high.")
    else:
        print("its too low")
