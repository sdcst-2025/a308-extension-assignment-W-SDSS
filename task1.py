import random

x = random.randint(1,100)
guesscount = 0

while True:
    guess = int(input("Enter your guess (1-100): "))
    if guess == x:
        print("You are correct!!")
        print(f"You've guessed {guesscount} times")
        break
    elif guess >= x:
        print("its too high.")
        guesscount += 1
        continue
    else:
        print("its too low")
        guesscount += 1
        continue

#1 no sa demo, its too high ni shiterukedo daijyoubuka
#diagram wo kaku