# Exercise 1
#
# Write a program that simulates a fortune cookie. The program should display one of five unique fortunes, at random,
# each time it's run.
#

import random

val = random.randint(1, 5)
if (val == 1):
  print("You staying in the company till the end of times.")
elif (val == 2):
  print("You will get fired from the company.")
elif (val == 3):
  print("You will find something else and leave the company.")
elif (val == 4):
  print("You will leave the company by your own.")
elif (val == 5):
  print("You will leave the company, stay here for a few months and in meanwhile you will find something else")