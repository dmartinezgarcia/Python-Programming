# Exercise 1
#
# Write a program that counts for the user. Let the user enter the starting number, the ending number, and the amount
# by which to count.
#

start_number = int(input("First step, enter the starting number: "))
ending_number = int(input("Second step, enter the ending number: "))
step = int(input("Final step, now we need the amount by which to count: "))

for a in range(start_number, ending_number, step):
  print(a, end=" ")
print("")