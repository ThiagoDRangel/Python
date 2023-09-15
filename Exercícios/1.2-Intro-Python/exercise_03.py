import random

MAX_ATTEMPTS = 3

def retrieve_words(file):
    return [word.strip() for word in file]

def draw_secret_word(words):
    secret_word = random.choice(words)
    scrambled_word = "".join(random.sample(secret_word, len(secret_word)))
    return secret_word, scrambled_word

def collect_guesses(secret_word):
    for attempt in range(MAX_ATTEMPTS):
        guess = input("Guess the word: ")
        if guess == secret_word:
            print(f"You win: the secret word is {secret_word}")
            return
    print(f"You lose: the secret word is {secret_word}")

if __name__ == "__main__":
    with open("words.txt") as file:
        words = retrieve_words(file)
    secret_word, scrambled_word = draw_secret_word(words)
    print(f"Scrambled word is {scrambled_word}")
    collect_guesses(secret_word)
