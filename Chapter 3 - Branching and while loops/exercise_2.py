# Exercise 2
#
# Write a program that flips a coin 100 times and then tells you the number of heads and tails.
#

import random

heads = 0
tails = 0
count = 0

while (count < 100):
  if (random.randint(0, 1)):
    heads += 1
  else:
    tails += 1
  count += 1

print("Number of heads: " + str(heads) + "\nNumber of tails: " + str(tails))