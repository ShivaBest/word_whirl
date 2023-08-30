#!/usr/bin/env python3
import random
import io
import os
from pathlib import Path

#last github commit (main): Aug 19, 2023 @ 12:02 PM ET

#goal: create a wordle-like game to play in terminal

'''
REQUIREMENTS & TASKS
x 0.0 print rules at start of game
0.1 restart game
0.2 reset guess_remain and answer at start of new game

x 1.0 choose a random 5-letter word from a database/array
x 1.1 don't print answer to terminal
x 1.2 call from a large database

x 2.0 get 5-letter string input from user
x 2.1 accept only letter character inputs
2.2 accept letters in any case
x 2.3 check if input == answer
x 2.4 convert/get each char from input to char
x 2.5 check if input includes chars from answer
x 2.6 display assessment of input with uppercase, lowercase, and "-"
2.7 display all guesses so far before asking for next input

x 3.0 allow 6 guesses
x 3.1 track number of guesses remaining
x 3.2 display number of guesses remaining before each new guess
3.3 remember previous guesses (in an array or set of variables?) in assessed format
3.4 display previous guesses in assessed format for easier reading

** TASK LIST **
ask to restart game if correct answer or guess_remain = 0
if restart game, print intro (title, guess_remain, CTA "instructions" option)
create command to print instructions
if guess_remain = 0, print message f"You ran out of guesses. The answer was {answer}"
create command to print answer ("test")

** V2.0 UPDATES **
adding f strings instead of concatenations
lowercasing incorrect entry responses (eg "Wrong answer," "Wrong length")
added restart_game() function -- not tested!!

** BUGS **
restart game doesn't reset guess_remain
restart game doesn't reset answer
cannot enter uppercase letters
guesses not in database are not triggering error (eg: "radia")
displays char mult times that only appears once in answer

'''

filepath = Path(__file__).parent / "answers.txt"
with open(filepath, "r") as f:
    print(f.name)
    database = f.readlines()

answer = random.choice(database)
answer = answer.rstrip()
print("Answer: " + answer)
#print("Length: " + str(len(answer)))

guess_remain = 6

restart_ans = ["yes", "y","Y"]

title = "\nWelcome to Word-Whirl!"

instructions = ("\nHow it works:\n"
                "  You have 6 chances to guess the right 5-letter word\n"
                "  You'll get feedback on your guess like this:\n"
                "    uppercase letter = in answer, right spot\n"
                "    lowercase letter = in answer, wrong spot\n"
                "    dash = not in answer\n"
                "  Example: \n"
                "    answer is: 'plate'\n"
                "    you guess: 'point'\n"
                "    you'll see: 'P---t'\n"
                "\n")

def is_alpha(guess):
    for character in guess:
        if not character.isalpha():
            return False
        return True

def restart_game():
    guess_remain = 0

print(title)
print(instructions)

while guess_remain > 0: # make this function "play_game()"
    print(f"Guesses remaining: {guess_remain}")
    guess = input("Enter a guess: ")
    if guess == answer:
        print("\nThat's right! You win.\n")
        restart = input("Play again? ")
        if restart in restart_ans:
            print("This is working")
        else:    
            break
    elif not is_alpha(guess):
        print("\nWrong characters", end='')
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
        if guess == "quit":
            break
        else:
            print("\nWrong length", end='')
    elif not guess in database: 
        print("\nThat's not in the database", end='')
    else:
        print(f"You ran out of guesses. The answer was {answer}.") # not triggering when guess_remain = 0
        restart = input("Play again? ")
            # logic for restart
    print("\n")