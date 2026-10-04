#AL, Hangman

import random

with open("words.txt", "r") as file:
    words = file.read().splitlines()

hang_word = random.choice(words).lower()


try:
    with open("stats.txt", "r") as stats:
        stats1 = stats.read()

        if len(stats1) == 0:
            wins = 0
            losses = 0
        else:
            lines = stats1.split("\n")
            line_1 = lines[0]
            line_2 = lines[1]

            wins = int(line_1.split(":")[1])
            losses = int(line_2.split(":")[1])

except:
    wins = 0
    losses = 0


wrong_guesses = 0


def hangman(wrong_guesses):
    if wrong_guesses == 0:
        print("  +---+")
        print("  |   |")
        print("      |")
        print("      |")
        print("      |")
        print("=========")

    if wrong_guesses == 1:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print("      |")
        print("      |")
        print("=========")

    if wrong_guesses == 2:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print("  |   |")
        print("      |")
        print("=========")

    if wrong_guesses == 3:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|   |")
        print("      |")
        print("=========")

    if wrong_guesses == 4:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\\  |")
        print("      |")
        print("=========")

    if wrong_guesses == 5:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\\  |")
        print(" /    |")
        print("      |")
        print("=========")

    if wrong_guesses == 6:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\\  |")
        print(" / \\  |")
        print("      |")
        print("=========")


guessed_letters = []


def display_word_function(hang_word):
    display_word = ""

    for letter in hang_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    return display_word


def stupid_proof_guess():
    while True:
        guess = input("Guess a letter: ")

        if guess.isalpha() and len(guess) == 1:
            return guess.lower()
        else:
            print("Learn how to play hangman >:/")


wrong_letters = []


def stupid_proof_play_again():
    while True:
        play_again = input(
            "Do you want to play again User? (Y)es or (N)o: "
        ).lower()

        if play_again == "y" or play_again == "n":
            return play_again
        else:
            print("...Okey...")


while True:
    hangman(wrong_guesses)
    print(display_word_function(hang_word))
    print("Wrong guesses:", wrong_letters)

    guess = stupid_proof_guess()

    if guess not in guessed_letters:
        guessed_letters.append(guess)

        if guess not in hang_word:
            wrong_letters.append(guess)
            wrong_guesses += 1

    if display_word_function(hang_word).replace(" ", "") == hang_word:
        print("Yay, you won!")
        wins += 1

        play_again = stupid_proof_play_again()

        if play_again == "y":
            hang_word = random.choice(words).lower()
            wrong_guesses = 0
            guessed_letters = []
            wrong_letters = []
        else:
            break

    elif wrong_guesses == 6:
        print(f"Sorry, you lost! The word was {hang_word}")
        losses += 1

        play_again = stupid_proof_play_again()

        if play_again == "y":
            hang_word = random.choice(words).lower()
            wrong_guesses = 0
            guessed_letters = []
            wrong_letters = []
        else:
            break


with open("stats.txt", "w") as stats:
    stats.write(f"wins:{wins}\n")
    stats.write(f"losses:{losses}")

