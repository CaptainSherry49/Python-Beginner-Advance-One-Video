# The Perfect Guess

import random
Number = random.randint(2, 100)

Guesses = 0
user = None

while user != Number:
    user = int(input("Enter the NUmber:\n"))
    Guesses += 1
    if user > Number:
        print("Please Guess low number")
    elif user < Number:
        print("Please Guess High number")
    else:
        print("Congratulation! You Guess the Number :)")

print(f"You Guess the Number in {Guesses} Attempts")
