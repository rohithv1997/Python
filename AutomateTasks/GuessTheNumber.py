# This is guess the number game
import random

print("Hello, what is your name?")
name = input()

print("Well, " + name + " I  am thinking of a number between 1 and 20.")
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print("Take a guess")
    guess = int(input())

    if guess == secretNumber:
        break
    elif guess < secretNumber:
        print("Your guess is too low")
    else:
        print("Your guess is too high")

if guess == secretNumber:
    print(
        "Good job, "
        + name
        + ". You guessed my number in "
        + str(guessesTaken)
        + " guesses"
    )
else:
    print("Nope. The number I was thinking was " + str(secretNumber))