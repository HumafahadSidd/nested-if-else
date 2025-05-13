import random
import string

# Function to get a valid word
def get_valid_word(words):
    word = random.choice(words)  
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

# Main Hangman function
def hangman():
    # Word list
    words = ["PYTHON", "DEVELOPER", "HANGMAN", "PROGRAMMING", "COMPUTER"]
    word = get_valid_word(words)
    word_letters = set(word)  # Unique letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Letters guessed by the user
    lives = 6  # Number of attempts

    while len(word_letters) > 0 and lives > 0:
        print(f"\nYou have {lives} lives left.")
        print("Used letters:", ' '.join(used_letters))
        
        # Display current word progress
        word_display = [letter if letter in used_letters else '-' for letter in word]
        print("Current word:", ' '.join(word_display))

        user_letter = input("Guess a letter: ").upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Wrong guess!")

        elif user_letter in used_letters:
            print("You already guessed that letter.")
        else:
            print("Invalid character, try again.")

    if lives == 0:
        print(f"\nYou lost! The word was {word}.")
    else:
        print(f"\nCongratulations! You guessed the word {word}.")

# Run the game
hangman()