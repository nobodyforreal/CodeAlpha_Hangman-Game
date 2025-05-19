import random

def hangman():
    word_list = ["python", "hangman", "challenge", "programming", "developer", "nvidia", "openai"]
    word = random.choice(word_list).lower()
    word_letters = set(word)
    guessed_letters = set()
    lives = 4

    print("Welcome to Hangman!")

    while len(word_letters) > 0 and lives > 0:
        print(f"\nYou have {lives} lives left.")
        print("Guessed letters: ", " ".join(guessed_letters))
        
        # Display current word with underscores for unguessed letters
        display_word = [letter if letter in guessed_letters else '_' for letter in word]
        print("Current word: ", " ".join(display_word))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            lives -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")

    if lives == 0:
        print(f"\nYou died! The word was '{word}'. Better luck next time.")
    else:
        print(f"\nCongratulations! You guessed the word '{word}' correctly!")

if __name__ == "__main__":
    hangman()
