# Exercise 2
#
# Modify the Guess My Number chapter project from Chapter 3 by reusing the function ask_number().
#

import random

def ask_number(question, low, high, step = 1):
  """
  Ask for a number within a range.
  :param question: Question to ask.
  :param low: Lowest number.
  :param high: Highest number.
  :param step: Step value
  :return: Number entered by the user.
  """
  response = None
  while response not in range(low, high, step):
    response = int(input(question))
  return response

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# Set the initial values
the_number = random.randint(1, 100)
guess = ask_number("Take a guess: ", 1, 100)
tries = 1

# Guessing loop
while guess != the_number:
  if guess > the_number:
    print("Lower...")
  else:
    print("Higher...")
  guess = ask_number("Take a guess: ", 1, 100)
  tries += 1

print("You guessed it! The number was", the_number)
print("And it only took you", tries, "tries!\n")