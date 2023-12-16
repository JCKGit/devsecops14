import random

name = input("What is your name? ")
print("Hey, " + name + ", Time to play hangman!")

print("Start guessing...")

words = ["hangman", "python", "coffee", "master"]
secret_word = random.choice(words)

guesses = ''

turns = 10

while turns > 0:
    failed = 0

    for char in secret_word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end="")
            failed += 1

    if failed == 0:
        print("\nYou won!")
        break

    guess = input("\nGuess a character: ")

    guesses += guess

    if guess not in secret_word:
        turns -= 1
        print("Wrong")
        print("You have", turns, 'more guesses')

    if turns == 0:
        print("You Lose. The word was:", secret_word)
        break
