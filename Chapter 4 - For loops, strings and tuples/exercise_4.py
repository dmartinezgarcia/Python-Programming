# Exercise 4
#
# Create a game where the computer picks a random word and the player has to guess the word. THe computer tells the
# player how many letters are in the word. Then the player gets five chances to ask if a letter is in the word. The
# computer can only respond with "yes" or "no". Then, the player must guess the word.
#

import random

words = ("sarcophage", "book", "computer", "laptop", "desk", "chair")
word_index = random.randint(0, len(words) - 1)
TOTAL_ATTEMPTS = 50
win = False

print("The word chosen by the computer has " + str(len(words[word_index])) + " characters.")

# Create the word disc vars
word_disc_0 = ""
word_disc_1 = ""
for i in words[word_index]:
  word_disc_0 += "_"
  word_disc_1 += "_"

for i in range(1, TOTAL_ATTEMPTS + 1, 1):
  if "_" not in word_disc_1:
    win = True
    break
  else:
    print("These are your results so far: " + word_disc_1)

  print("This is attempt number " + str(i) + " out of " + str(TOTAL_ATTEMPTS) + " .")
  letter = input("Please enter a letter, or the full word: ").lower()

  if letter == words[word_index].lower():
    win = True
    break
  elif len(letter) != 1 or letter < "a" or letter > "z":
    print("Invalid input, or you didn't discover the word.")
  elif letter in word_disc_1:
    print("You've already discovered this letter.")
  elif letter in words[word_index].lower():
    print("Good, you discovered a letter.")
    word_disc_0 = word_disc_1
    word_disc_1 = ""
    for j in range(0, len(words[word_index])):
      if words[word_index][j] == letter and word_disc_0[j] == "_":
        word_disc_1 += letter
      elif word_disc_0[j] != "_":
        word_disc_1 += word_disc_0[j]
      else:
        word_disc_1 += "_"
  else:
    print("Letter not found.")

if win:
  print("Well done, you defeated the computer. The word you discovered is: " + words[word_index])
else:
  print("You lost, computer won, the word was: " + words[word_index])