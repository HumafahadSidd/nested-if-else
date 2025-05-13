import streamlit as st
import random
import string

# Function to get a valid word
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:

        word = random.choice(words)
    return word.upper()

# Initialize session state
if 'word' not in st.session_state:
    st.session_state.word = get_valid_word(["PYTHON", "DEVELOPER", "HANGMAN", "PROGRAMMING", "COMPUTER"])
    st.session_state.word_letters = set(st.session_state.word)
    st.session_state.used_letters = set()
    st.session_state.lives = 6

# Streamlit UI
st.title("Hangman Game")
st.write("Guess the word before you run out of lives!")

# Display lives and used letters
st.write(f"**Lives Left:** {st.session_state.lives}")
st.write(f"**Used Letters:** {' '.join(st.session_state.used_letters)}")

# Display current word progress
word_display = [letter if letter in st.session_state.used_letters else '-' for letter in st.session_state.word]
st.write(f"**Current Word:** {' '.join(word_display)}")

# User input
user_letter = st.text_input("Guess a letter:", max_chars=1).upper()

if st.button("Submit Guess") and user_letter:
    alphabet = set(string.ascii_uppercase)

    if user_letter in alphabet - st.session_state.used_letters:
        st.session_state.used_letters.add(user_letter)

        if user_letter in st.session_state.word_letters:
            st.session_state.word_letters.remove(user_letter)
        else:
            st.session_state.lives -= 1
            st.write("Wrong guess!")

    elif user_letter in st.session_state.used_letters:
        st.write("You already guessed that letter.")
    else:
        st.write("Invalid character, try again.")

# Check game over conditions
if st.session_state.lives == 0:
    st.write(f"**You lost! The word was:** {st.session_state.word}")
    st.session_state.word_letters.clear()
elif not st.session_state.word_letters:
    st.write(f"**Congratulations! You guessed the word:** {st.session_state.word}")
