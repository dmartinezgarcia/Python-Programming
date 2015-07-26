# Exercise 3
#
# Write a Tipper program where the user enters a restaurant bill total. The program should then display two amounts:
# - a 15 percent tip
# - a 20 percent tip
#

bill_total = float(input("Please enter the total bill amount (for example: 31.40 pounds): "))
print("The first tip (15 percent) is the following: " + str(bill_total * 0.15))
print("The second tip (20 percent) is the following: " + str(bill_total * 0.20))
