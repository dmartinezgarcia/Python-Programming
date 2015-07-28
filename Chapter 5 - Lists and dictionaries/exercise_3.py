# Exercise 3
#
# Write a Who's Your Daddy? program that lets the user enter the name of a male and produces the name of his father.
# (You can use celebrities, fictional characters or even historical figures for fun). Allow the user to add,
# replace and delete son-father pairs.
#

# We used dictionaries for the previous exercise, let's use lists for this one, although the exercise entirely
# suggests to use dictionaries.

generations = [["John", "John's dad"], ["Chris", "Chris's dad"], ["Matthew", "Matthew's dad"]]

print("This is the 'Who's your daddy?' game.")

while True:
  print("These are the following possibilities: ")
  print("\t\t 1. Check someone's dad")
  print("\t\t 2. Add son-father pair")
  print("\t\t 3. Replace son-father pair")
  print("\t\t 4. Delete son-father pair")
  print("\t\t 10. Exit the game.")
  j = int(input("So, what is your option? "))

  if j == 1:
    print("You want to check someone's dad.")
  elif j == 2:
    print("You want to add someone's dad.")
  elif j == 3:
    print("You want to replace someone's dad.")
  elif j == 4:
    print("You want to delete someone's dad.")
  elif j == 10:
    print("So you want to exit the game, goodbye!")
    break
  else:
    print("Not a valid option. Please try again.")
    continue

  son_name = input("What is the name of the son? ")
  dad_name = ""

  for i in range(0, len(generations)):
    if son_name == generations[i][0]:
        dad_name = generations[i][1]
        break

  if j == 1:
    if dad_name:
      print("The dad of " + son_name + " is called " + dad_name + ".")
    else:
        print("The name of the son is not registered.")
  elif j == 2:
    if dad_name:
      print("The son you entered is already registered.")
    else:
      dad_name = input("Enter the name of " + son_name + " dad: ")
      generations.append([son_name, dad_name])
  elif j == 3:
      if dad_name:
        dad_name = input("Enter the name of the new dad of " + son_name + ": ")
        generations[i][1] = dad_name
      else:
        print("The son you entered is not registered.")
  elif j == 4:
      if dad_name:
        print("Deleted son " + son_name + " and his dad " + dad_name + " successfully.")
        del generations[i]
      else:
        print("The son you entered is not registered.")

