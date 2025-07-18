import random

# List of words to choose from
word_list = ["python", "apple", "hangman", "banana", "coding", "computer"]
chosen_word = random.choice(word_list)

# Initialize display with blanks
display = ['_' for _ in chosen_word]

# Number of wrong guesses allowed
max_attempts = 6
wrong_guesses = 0

# To keep track of guessed letters
guessed_letters = []

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have", max_attempts, "lives.")
print("Word:", ' '.join(display))
print()

# Main game loop
while '_' in display and wrong_guesses < max_attempts:
    guess = input(" Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single letter (a-z).")
        continue

    if guess in guessed_letters:
        print("❗ You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        # Update the display with correct guesses
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        print("✅ Good job!")
    else:
        wrong_guesses += 1
        print("❌ Wrong guess! Lives left:", max_attempts - wrong_guesses)

    # Show current word status
    print("Word:", ' '.join(display))
    print("Guessed letters:", ', '.join(guessed_letters))
    print()

# Game over conditions
if '_' not in display:
    print("🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print(" Game Over! The word was:", chosen_word)
