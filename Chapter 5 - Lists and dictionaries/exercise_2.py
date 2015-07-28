# Exercise 2
#
# Write a character creator program for a role-playing game. The player should be given a pool of 30 points to spend
# on four attributes: Strength, Health, Wisdom and Dexterity. The player should be able to spend points from the pool
# on any attribute and should also be able to take points from an attribute and put them back into the pool.
#

import random

traits = {"Strength": 5, "Health": 5, "Wisdom": 5, "Dexterity": 5}
points = 30

while True:
  print("These are your character traits: ")
  print("\t\t Strength  " + str(traits["Strength"]))
  print("\t\t Health    " + str(traits["Health"]))
  print("\t\t Wisdom    " + str(traits["Wisdom"]))
  print("\t\t Dexterity " + str(traits["Dexterity"]))

  if points:
    print("You still have " + str(points) + " points left.")
  else:
    if input("There are no points left, type F to exit character creation.") == "F":
      break

  while True:
    trait = input("Which trait you wish to modify? ")
    if trait not in traits:
      print("Entered trait invalid. Please try again.")
      continue
    break

  value = int(input("Enter a positive number to increment the trait, negative to decrease it: "))
  if value > 0:
    if value > points:
      print("Not enough points.")
    else:
      traits[trait] += value
      points -= value
  elif value < 0:
    value = abs(value)
    if value > traits[trait]:
      value = traits[trait]
    traits[trait] -= value
    points += value

print("Your character has been created!")