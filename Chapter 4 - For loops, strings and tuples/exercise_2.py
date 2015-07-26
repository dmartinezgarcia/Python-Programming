# Exercise 2
#
# Create a program that gets a message from the user and then prints it out backwards.
#

text = input("So, what is your text that shall be printed backwards?")

for a in range(len(text) - 1, -1, -1):
  print(text[a], end = "")
print("")