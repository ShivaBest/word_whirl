#!/usr/bin/env python3
import random
import io
import os
from pathlib import Path

#goal: create a wordle-like game to play in terminal

'''
REQUIREMENTS & TASKS
0.0 print rules at start of game
0.1 reset guess_remain and answer at start of new game

1.0 choose a random 5-letter word from a database/array
1.1 don't print answer to terminal (return from function)
1.2 call from a large database

2.0 get 5-letter string input from user
2.1 accept only letter character inputs
2.2 accept letters in any case
2.3 check if input == answer
2.4 convert/get each char from input to char
2.5 check if input includes chars from answer
2.6 display assessment of input with uppercase, lowercase, and "-"
2.7 display all guesses so far before asking for next input

3.0 allow 6 guesses
3.1 track number of guesses remaining
3.2 display number of guesses remaining before each new guess
3.3 remember previous guesses (in an array or set of variables?) in assessed format
3.4 display previous guesses in assessed format for easier reading

extended version (roadmap)
    remember up to 4 player names
    track scores across multiple rounds
    remember previous answers and don't repeat

BUGS 
cannot enter uppercase letters
guesses not in database are not triggering error (eg: "radia")
'''

filepath = Path(__file__).parent / "answers.txt"
with open(filepath, "r") as f:
    print(f.name)
    database = f.readlines()

answer = random.choice(database)
answer = answer.rstrip()
#print("Answer: " + answer)
#print("Length: " + str(len(answer)))

guess_remain = 6

def is_alpha(guess):
    for character in guess:
        if not character.isalpha():
            return False
        return True

print("\nWELCOME TO WORD-WHIRL!")
print("HOW IT WORKS")
print("  You have 6 chances to guess the right 5-letter word")
print("  You'll get feedback on your guess like this:")
print("    uppercase letter = in answer, right spot")
print("    lowercase letter = in answer, wrong spot")
print("    dash = not in answer")
print("  Example: if the answer is 'plate' and you guess 'point', you'll see: 'P---t' ")
print("\n")

while guess_remain > 0:
    print("Guesses remaining: " + str(guess_remain))
    guess = input("Enter a guess: ")
    if guess == answer:
        print("\nRIGHT ANSWER. YOU WIN.\n")
        break
    elif not is_alpha(guess):
        print("\nWRONG CHARACTERS", end='')
    elif len(guess) == len(answer):
        print("\n")
        for i in range(len(answer)):
            if guess[i] == answer[i]:
                print(guess[i].upper() + " ", end='')
            elif guess[i] in answer:
                print(guess[i].lower() + " ", end='')
            else:
                print("-" + " ", end='')
        guess_remain -= 1
    elif len(guess) != len(answer):
        print("\nWRONG LENGTH", end='')
    elif not guess in database: 
        print("\nNOT IN DATABASE", end='')
    print("\n")
