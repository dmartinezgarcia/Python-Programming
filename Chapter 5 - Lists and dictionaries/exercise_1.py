# Exercise 1
#
# Create a program that prints a list of words in random order. The program should print all the words and not repeat
# any.
#

import random

list = ["make", "sure", "include", "several", "generations"]

print("Beginning of the list.\n")

while len(list):
  i = random.randrange(len(list))
  print(list[i], end = "|")
  del list[i]

print("\n\nEnd of the list.\n")