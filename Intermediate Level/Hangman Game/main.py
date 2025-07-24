import random, sys, hangman_stages

words = ["python", "hangman", "challenge", "programming", "developer"]

def select_word():
    return random.choice(words)

def print_secret_word(secret_word, guessed_letters):
    display = [letter if letter in guessed_letters else '_' for letter in secret_word]
    print(" ".join(display))

def guess_letter():
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Only single letters are allowed. Unable to continue...")
        sys.exit()
    return guess

def is_guess_in_secret_word(guess, secret_word):
    return guess in secret_word

print("Welcome to Hangman! Let's see if you can guess this word!\n")
secret_word = select_word()
guessed_letters = []
remaining_attempts = 6

while remaining_attempts > 0:
    guess = guess_letter()

    if guess in guessed_letters:
        print(f"You've already guessed the letter '{guess}'.")
        continue

    guessed_letters.append(guess)

    if is_guess_in_secret_word(guess, secret_word):
        print(f"Yes! The letter '{guess}' is part of the word.")
    else:
        print(f"No! The letter '{guess}' is not part of the word.")
        remaining_attempts -= 1

    print(hangman_stages.get_hangman_stage(remaining_attempts))
    print_secret_word(secret_word, guessed_letters)

    if all(letter in guessed_letters for letter in secret_word):
        print("🎉 Congratulations, you guessed the word!")
        break
else:
    print(f"😵 Game over! The word was '{secret_word}'.")