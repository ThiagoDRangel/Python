import random

WORDS = [
    "cat",
    "elephant",
    "dog",
    "monkey",
    "duck",
    "chameleon",
    "bear",
    "moose",
    "rooster",
]

MAX_ATTEMPTS = 3

def draw_secret_word(words):
    secret_word = random.choice(words)
    scrambled_word = "".join(random.sample(secret_word, len(secret_word)))
    return secret_word, scrambled_word

def collect_guesses(secret_word):
    guesses = [input("Guess the word: ") for _ in range(MAX_ATTEMPTS)]
    return guesses

def check_game_result(secret_word, guesses):
    result = "You win" if secret_word in guesses else "You lose"
    print(f"{result}: {secret_word}")

if __name__ == "__main__":
    secret_word, scrambled_word = draw_secret_word(WORDS)
    print(f"Scrambled word is {scrambled_word}")
    guesses = collect_guesses(secret_word)
    check_game_result(secret_word, guesses)
