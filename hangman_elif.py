import time
import random

# Welcoming the user
name = input("What is your name? ")
print("Hello, " + name + ", Time to play hangman!")

# Wait for 1 second
time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

# Set the secret word
words = ["secret", "word", "hangman"]
secret_word = random.choice(words)

# Create a variable with an empty value for guesses
guesses = ''

# Determine the number of turns
turns = 10

# Create a while loop to check if the turns are more than zero
while turns > 0:
    # Make a counter that starts with zero
    failed = 0

    # Display the current state of the word
    for char in secret_word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end="")
            failed += 1

    # Check if the player has guessed all the letters
    if failed == 0:
        print("\nYou won!")
        break

    # Ask the user to guess a character
    guess = input("\nGuess a character: ")

    # Update the player's guesses
    guesses += guess

    # Check if the guess is not found in the secret word
    if guess not in secret_word:
        turns -= 1
        print("Wrong")
        print("You have", turns, 'more guesses')

        # Check if the turns are equal to zero
        if turns == 0:
            print("You Lose. The word was:", secret_word)
            break
    elif guess in secret_word:
        print("Good guess!")

# The game is finished