#AL, Hangman

import random
with open("words.txt", "r") as file:
    words = file.read().splitlines()
hang_word = random.choice(words).lower()

