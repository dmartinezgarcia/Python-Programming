# Exercise 3
#
# Change the Guess My Number so the player picks a number between 1 and 100 and the computer has to guess. Before you
# start, think about how you guess. If all goes well, try coding the game.
#

import random

max_val = 100
guesses = 100
n_found = False
number = random.randint(0, max_val)
comp_number = 0
comp_lim_a = 0
comp_lim_b = max_val

print("Guess My Number game: Guess a number between 0 and " + str(max_val) + ".")

while guesses and not n_found:
  print("Computer has " + str(guesses) + " guesses remaining.")
  comp_number = random.randint(comp_lim_a, comp_lim_b)
  response = input("Computer guessed " + str(comp_number) +". Please enter if the number is Equal, Smaller, "
                                                           "or Bigger than your number: ")
  if response == "E":
    n_found = True
  elif response == "S":
    comp_lim_a = comp_number + 1
  elif response == "B":
    comp_lim_b = comp_number - 1
  guesses -= 1

if n_found:
  print("Computer won, it guessed your number: " + str(comp_number))
else:
  print("The computer ran out of guesses, so you win.")