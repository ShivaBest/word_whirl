#!/usr/bin/env python3

#last github commit (main): Aug 19, 2023 @ 12:02 PM ET

#goal: create a wordle-like game to play in terminal

'''
** V2.1 UPDATES **
remove restart_game() function
create play_game() function
add request to start game (ready)
add option to restart game y/n (restart)
fixed bug: guess_remain = 0 was not triggering restart request
made guess_remain a local var in play_game() function
add round counting (not yet working)
fixed bug: restart game now picks new answer
fixed bug: some lines not separated by return /n
fixed bug: formatted guesses printing to same line as next statement
fixed bug (critical): now checks if guess is in database


** CURRENT BUGS **
not accepting uppercase letters
displays char mult times that only appears once in answer
incorrect 'ready' input doesn't allow new input
'quit' command doesn't always work
'''

import random
import io
import os
import time
from pathlib import Path

filepath = Path(__file__).parent / "answers.txt"
with open(filepath, "r") as f:
    print(f.name)
    database = f.readlines()

answer = random.choice(database)

affirm = ["yes", "y","Y"]

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
                "  At any time, type 'quit' to end the game\n"
                "  or type 'instructions' to see the rules again."
                "\n")

def is_alpha(guess):
    for character in guess:
        if not character.isalpha():
            return False
        return True

def play_game():
    answer = random.choice(database)
    #print(f"Answer: {answer}") # test
    guess_remain = 6 # test
    while guess_remain > 0:
        print(f"\nGuesses remaining: {guess_remain}\n")
        guess = input("Enter a guess: ")
        guess += "\n"
        if guess == answer:
            print("\nThat's right! You win.\n")
            time.sleep(1)
            restart = input("Play again? ")
            if restart in affirm:
                play_game()
        elif guess == "quit\n":
            break
        elif guess == "instructions\n":
            print(instructions)
        elif not is_alpha(guess):
            print("\n<!> Wrong characters\n", end='')
        elif len(guess) != len(answer):
            print("\n<!> Wrong length\n")
        elif guess not in database:
            print("\n<!> Not in database\n", end='')
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
        else:
            print("\nError: wrong length\n", end = '')
    else:
        print(f"\nYou ran out of guesses. The answer was '{answer}'.")
        time.sleep(1)
        restart = input("Play again? ")
        if restart in affirm:
            play_game()
    print("\n")

print(title)
print(instructions)
ready = input("Ready to play? ")
if ready in affirm:
    play_game()