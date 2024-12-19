import random

def choose_word():
    words = ["python", "hangman", "challenge", "programming", "developer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def play_game():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while attempts > 0 and set(word) != guessed_letters:
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again.")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! {display_word(word, guessed_letters)}")
        else:
            attempts -= 1
            guessed_letters.add(guess)
            print(f"Wrong guess! Attempts remaining: {attempts}")
            print(display_word(word, guessed_letters))

    if set(word) == guessed_letters:
        print("\nCongratulations, you've guessed the word!")
    else:
        print(f"\nGame over! The word was '{word}'.")

if __name__ == "__main__":
    play_game()
