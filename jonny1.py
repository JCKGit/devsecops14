import random

def choose_word():
    words = ["python", "hangman", "programming", "developer", "computer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    max_attempts = 6
    guessed_letters = []
    word_to_guess = choose_word()
    attempts_left = max_attempts

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while attempts_left > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts_left -= 1
            print(f"Incorrect! Attempts left: {attempts_left}")
        else:
            print("Correct!")

        current_display = display_word(word_to_guess, guessed_letters)
        print(current_display)

        if "_" not in current_display:
            print("Congratulations! You guessed the word.")
            break

    if attempts_left == 0:
        print(f"Sorry, you ran out of attempts. The word was: {word_to_guess}")

if _name_ == "__main__":
    hangman()