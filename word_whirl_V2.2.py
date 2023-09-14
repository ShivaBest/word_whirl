'''
This is definitely not a wordle rip-off.

** V2.2 UPDATES **
fixed bug to allow uppercase letters
fixed 'quit' command: program now exits from quit in either play_game or main
fixed 'ready' input: allows non-yes inputs
fixed directory problem; removed modules: io, os, path; replaced readfile logic

NEXT: add 'test' function at 'ready' input
    shorter guess #
    prints answer

** CURRENT BUGS **
play again not working: always sets answer = "petal" (?!) and keeps guess count
    over successive games --> not restarting play_game()
    maybe something to do with how read file is inside play_game()? 
    maybe read file should be a function that returns 'answer'?
displays char mult times that only appears once in answer

'''

import random
import time


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

def main():
    print(title)
    print(instructions)
    while True:
        ready = input("Ready to play? ").lower()
        if ready in "yes":
            play_game()
        elif ready == "quit":
            break
        else:
            print("Don't get ready, stay ready.")

def is_alpha(guess):
    for character in guess:
        if not character.isalpha():
            return False
        return True

def play_game():
    with open("answers.txt", "r") as f:
        #print(f"Opened file: {f}") # Test
        database = f.readlines()
    answer = random.choice(database)
    #print(f"Answer: {answer}") # Test
    guess_remain = 6
    while guess_remain > 0:
        print(f"\nGuesses remaining: {guess_remain}\n")
        guess = input("Enter a guess: ").lower()
        guess += "\n"
        if guess == answer:
            print("\nThat's right! You win.\n")
            time.sleep(1)
            restart = input("Play again? ")
            if restart.lower() in "yes":
                play_game()
        elif guess == "quit\n":
            exit()
        elif guess == "instructions\n":
            print(instructions)
        elif not is_alpha(guess):
            print("\n<!> Wrong characters\n", end='')
        elif len(guess) != len(answer):
            print("\n<!> Wrong length\n")
        elif guess not in database:
            print("\n<!> Not in database\n", end='')
        elif len(guess) == len(answer):
            print()
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
        if restart.lower() in "yes":
            play_game()
    print()

main()