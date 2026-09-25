#AL, Number Guessing Game  place a conditional in a loop

import random

current_attempts = 0

max_attempts = 6

answer = random.randint(1,100)

print(f"Hello user ! Im thinking of a number between 1 and 100, you have 6 attempts. Which number im thinking ?")

for attempt in range(1,100): 
    current_attempts += 1
    guess = int(input(f"Guess #{current_attempts}: ")) 
    if guess == answer:
        print(f"You did it in the Guess#{current_attempts}!")
    elif guess > answer :
        print("Too high!")
    elif guess < answer : 
        print("Too low!") 
    if current_attempts == max_attempts : 
        print(f"Sorry, you lost. The answer was {answer}") 


    



