'''
This is definitely not a wordle rip-off.

** V3.0 UPDATES **
moved to objects for better modularization
affirmative answers can be either "yes" or "y" now
quit can be achieved with either "quit" or "q" now
instructions can be printed with either "instructions" or "i" now
lazily load and cache database to avoid loading before user starts game and avoid reload between
database is stripped of new line characters on load, so assigning answers andchecking guesses is
    simpler

NEXT: add 'test' function at 'ready' input
    shorter guess #
    prints answer

** CURRENT BUGS **
displays char mult times that only appears once in answer

'''

import random

# A class for lazily loading a WordWhirl database
class LazyDatabase:

    def __init__(self, file):
        self.file = file

    def get(self):
        if getattr(self, "_database", None) is None:
            with open(self.file, "r") as f:
                self._database = [word.rstrip() for word in f.readlines()]
        return self._database
            

# A class for playing Word-Whirl games
class WordWhirl:

    TITLE = "\nWelcome to Word-Whirl!"
    INSTRUCTIONS = ("\nHow it works:\n"
                "  You have 6 chances to guess the right 5-letter word\n"
                "  You'll get feedback on your guess like this:\n"
                "    uppercase letter = in answer, right spot\n"
                "    lowercase letter = in answer, wrong spot\n"
                "    dash = not in answer\n"
                "  Example: \n"
                "    answer is: 'plate'\n"
                "    you guess: 'point'\n"
                "    you'll see: 'P---t'\n"
                "  At any time, type 'quit' or 'q' to end the game\n"
                "  or type 'instructions' or 'i' to see the rules again."
                "\n")
    VICTORY_MSG = "\nThat's right! You win."
    LOSS_MSG = "\nYou ran out of guesses. The answer was "
    QUIT_MSG = "\nThanks for playing!"
    NON_ALPHA_ERROR_MSG = "\n<!> Wrong characters"
    WRONG_LENGTH_ERROR_MSG = "\n<!> Wrong length"
    NOT_A_WORD_ERROR_MSG = "\n<!> Not in database"

    AFFIRM_COMMANDS = ("yes", "y")
    QUIT_COMMANDS = ("quit", "q")
    INSTRUCTION_COMMANDS = ("instructions", "i")

    def __init__(self, database_file, max_guesses):
        self.lazy_database = LazyDatabase(database_file)
        self.max_guesses = max_guesses

    # Reset the state of this WordWhirl to be ready for a new game.
    def reset(self):
        self.current_guesses = self.max_guesses
        self.answer = random.choice(self.lazy_database.get())
        self.quit_requested = False
        self.correct_guess = False

    # Prints the remaining guesses for the current game.
    def print_current_guesses(self):
        print(f"\nGuesses remaining: {self.current_guesses}\n")

    # Prints the loss message and the correct answer.
    def print_loss_message(self):
        print(WordWhirl.LOSS_MSG + self.answer)

    # Sets the flag indicating that the user has requested to quit the game.
    def request_quit(self):
        self.quit_requested = True

    # Returns true if the user has won, lost, or quit.
    def is_game_over(self):
        return self.current_guesses <= 0 or self.quit_requested or self.correct_guess

    # Begins a new session of Word-Whirl
    # The title and instructions will be printed and the user will be asked to confirm before the
    # game begins, then the game will proceed.
    def start_session(self):
        print(WordWhirl.TITLE)
        print(WordWhirl.INSTRUCTIONS)
        ready = input("Ready to play? ").lower()
        if ready in WordWhirl.AFFIRM_COMMANDS:
            self.play_game()

    # Begins a game of World-Whirl
    # The game will proceed until the user wins, loses, or quits. If the game completes without the
    # user quitting, they will be offered another game.
    def play_game(self):
        self.reset()
        while not self.is_game_over():
            self.play_round()

        if self.correct_guess:
                print(WordWhirl.VICTORY_MSG)
        
        if self.current_guesses <= 0:
                self.print_loss_message()
        
        if self.quit_requested:
            print(WordWhirl.QUIT_MSG)
        else:
            restart = input("Play again? ").lower()
            if restart in WordWhirl.AFFIRM_COMMANDS:
                self.play_game()
            else:
                print(WordWhirl.QUIT_MSG)


    # Plays a single round of Word-Whirl
    # Prompts the user to enter a guess
    # - If the user enters "quit" the game will end
    # - If the user enters "instructions" the instructions will be printed
    # - If the user enters an invalid guess, an error message will be printed
    # - If the user guesses correctly, the game ends in victory
    # - If the user guesses incorrectly, guess feedback is printed and one guess is used
    def play_round(self):
        self.print_current_guesses()
        guess = input("Enter a guess: ").lower()
        
        if self.process_command(guess):
            return
        
        if self.check_invalid_guess(guess):
            return
        
        if self.check_winning_guess(guess):
            return
        
        self.process_guess(guess)
        
    # Checks the given command and performs it if valid, then returns True if the command was
    # valid, otherwise returns False
    def process_command(self, command):
        if command in WordWhirl.QUIT_COMMANDS:
            self.request_quit()
            return True
        
        if command in WordWhirl.INSTRUCTION_COMMANDS:
            print(WordWhirl.INSTRUCTIONS)
            return True
        
        return False
    
    # Prints a helpful error message and returns True if the given guess is invalid, otherwise
    # returns False
    def check_invalid_guess(self, guess):
        if (not guess.isalpha()):
            print(WordWhirl.NON_ALPHA_ERROR_MSG)
            return True
        
        if (len(guess) != len(self.answer)):
            print(WordWhirl.WRONG_LENGTH_ERROR_MSG)
            return True
        
        if (guess not in self.lazy_database.get()):
            print(WordWhirl.NOT_A_WORD_ERROR_MSG)
            return True
        
        return False
    
    # Sets the victory flag and returns True if the given guess was the answer, otherwise returns
    # False
    def check_winning_guess(self, guess):
        if guess == self.answer:
            self.correct_guess = True
            return True
        return False
    
    # Prints the correct letters and positions from the given guess and decrements the remaining
    # guesses
    def process_guess(self, guess):
        for i in range(len(self.answer)):
                if guess[i] == self.answer[i]:
                    print(f"{guess[i].upper()} ", end="")
                # TODO: Correctly account for words with duplicate letters
                elif guess[i] in self.answer:
                    print(f"{guess[i].lower()} ", end="")
                else:
                    print("- ", end='')
        print()
        self.current_guesses -= 1


def main():
    WordWhirl("answers.txt", max_guesses=6).start_session()

main()
