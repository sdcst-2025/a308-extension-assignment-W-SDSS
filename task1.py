import random

x = random.randint(1,100)
guesscount = 0
u = True

while u==True:
    guess = input(print("Enter your guess (1-100): "))
    guess = int(guess)
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

#korede iinoka no kakunin
#1 no sa demo, its too high ni shiterukedo daijyoubuka
#diagram wo kaku

#Enter your guess (1-100): None   to deru     None nannde