# word_whirl
A word guessing game playable in the terminal (so far)

REQUIREMENTS & FUNCTIONALITY
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

HOW THE GAME WORKS
You have 6 chances to guess the right 5-letter word
You'll get feedback on your guess like this:
  uppercase letter = in answer, right spot
  lowercase letter = in answer, wrong spot
  dash = not in answer
Example: if the answer is 'plate' and you guess 'point', you'll see: 'P---t'
