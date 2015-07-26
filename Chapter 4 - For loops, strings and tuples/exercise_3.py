# Exercise
#
# Improve "Word Jumble" so that each word is paired with a hint. The player should be able to see the hint if he or
# she is stuck. The player should be able to see the hint if he or she is stuck. Add scoring system that rewards
# players who solve a jumble without asking for the hint.
#

# Word Jumble
#
# The computer picks a random word and then "jumbles" it.
# The player has to guess the original word.
#

import random

# Create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
# The hint appears after five unsuccessful attempts
HINTS = ("A programming language.",
         "The name of this game.",
         "Something that is simple to do.",
         "Something that is not simple to do.",
         "When someone asks you a question it is polite to...",
         "A musical instrument.")

# Pick one word randomly from the sequence
i = random.randrange(len(WORDS))
word = WORDS[i]
hint = HINTS[i]

# Score variable
score = 0

# Create a variable to use later to see if the guess is correct
correct = word

# Create a jumbled version of the word
jumble = ""

while word:
  position = random.randrange(len(word))
  jumble += word[position]
  word = word[:position] + word[(position + 1):]

# Start the game
print(
"""
        Welcome to the Word Jumble!

    Unscramble the letters to make a word.
 (Press the enter key at the prompt to quit.)
"""
)
print("The jumble is: ", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
  score -= 1
  print("Sorry, that's not it.")
  if score == -5:
    score -= 25
    print("Do you need help? This is the hint: " + hint)
  guess = input("Your guess: ")

if guess == correct:
  score += 50
  print("That's it! You guessed it!\n")
else:
  print("You gave up!\n")

print("Your final score is: " + str(score) + " points. Thanks for playing.")
input("\n\nPress the enter key to exit.")