import random

# Sample list of 6-letter words for demo (can be expanded)
WORDS = [
    "planet", "friend", "stream", "bottle", "animal",
    "circle", "flight", "garden", "orange", "silver",
    "forest", "market", "bridge", "castle", "flight"
]

def choose_word():
    return random.choice(WORDS).lower()

def get_feedback(secret, guess):
    feedback = ["Wrong"] * 6
    secret_list = list(secret)
    guess_list = list(guess)

    # First pass: correct letters in correct position
    for i in range(6):
        if guess_list[i] == secret_list[i]:
            feedback[i] = "Correct"
            secret_list[i] = None  # Mark this letter as used
            guess_list[i] = None

    # Second pass: similar letters in wrong position
    for i in range(6):
        if guess_list[i] is not None and guess_list[i] in secret_list:
            feedback[i] = "Similar"
            secret_list[secret_list.index(guess_list[i])] = None

    return feedback

def wordle():
    secret_word = choose_word()
    attempts = 6

    print("Welcome to Wordle! Guess the 6-letter word.")
    # Uncomment for testing: print(f"(Secret word is: {secret_word})")

    for attempt in range(1, attempts + 1):
        while True:
            guess = input(f"Attempt {attempt}/{attempts}: ").lower()
            if len(guess) != 6 or not guess.isalpha():
                print("Please enter a valid 6-letter word.")
            else:
                break

        feedback = get_feedback(secret_word, guess)
        print("Feedback:", feedback)

        if guess == secret_word:
            print(f"Congratulations! You guessed the word '{secret_word}' correctly.")
            return

    print(f"Sorry, you did not guess the word. It was '{secret_word}'.")

if __name__ == "__main__":
    wordle()
