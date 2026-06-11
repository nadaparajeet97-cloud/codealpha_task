import random
 
#  hangman game 

# List of predefined words
words = ["python", "computer", "program", "coding", "hangman"]

# Select a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

# Display hidden word
display_word = ["_"] * len(word)

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")

while wrong_guesses < max_wrong_guesses and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        print("Wrong!")
        wrong_guesses += 1

# Game result
if "_" not in display_word:
    print("\n Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)