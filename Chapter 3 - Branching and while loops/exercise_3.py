# Exercise 3
#
# Modify the Guess My Number game so that the player has a limited number of guesses. If the player fails to guess in
# time, the program should display an appropriately chastising message.
#

import random

max_val = 100
guesses = 5
n_found = False
number = random.randint(0, max_val)
user_number = 0

print("Guess My Number game: Guess a number between 0 and " + str(max_val) + ".")

while guesses and not n_found:
  print("You have " + str(guesses) + " guesses remaining.")
  user_number = int(input("Please enter your guess: "))
  if user_number == number:
    n_found = True
  elif user_number < number:
    print("Try a bigger number.")
  elif user_number > number:
    print("Try a smaller number.")
  guesses -= 1

if n_found:
  print("Congratulations, you found the number!!!!!!!")
else:
  print("You ran out of guesses.")
  print("The number was: " + str(number))
  print("You didn't find the number, better luck next time.")