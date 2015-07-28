# Exercise 3
#
# Improve the Who's Your Daddy program by adding a choice that lets the user enter a name and get back a grandfather.
# Your program should still only use one dictionary of son-father pairs. Make sure to include several generations in
# your dictionary so that a match can be found.
#

# We used dictionaries for the previous exercise, so might aswell continue with that decision.

generations = [["John", "John's dad", "John's grandfather"],
               ["Chris", "Chris's dad", "Chris's grandfather"],
               ["Matthew", "Matthew's dad", "Matthew's grandfather"]]

print("This is the 'Who's your daddy?' game.")

while True:
  print("These are the following possibilities: ")
  print("\t\t 1. Check someone's family")
  print("\t\t 2. Add family")
  print("\t\t 3. Replace family")
  print("\t\t 4. Delete family")
  print("\t\t 10. Exit the game.")
  j = int(input("So, what is your option? "))

  if j == 1:
    print("You want to check someone's family.")
  elif j == 2:
    print("You want to add someone's family.")
  elif j == 3:
    print("You want to replace someone's family.")
  elif j == 4:
    print("You want to delete someone's family.")
  elif j == 10:
    print("So you want to exit the game, goodbye!")
    break
  else:
    print("Not a valid option. Please try again.")
    continue

  son_name = input("What is the name of the son? ")
  dad_name = ""
  grandfather_name = ""

  for i in range(0, len(generations)):
    if son_name == generations[i][0]:
        dad_name = generations[i][1]
        grandfather_name = generations[i][2]
        break

  if j == 1:
    if dad_name:
      print("The dad of " + son_name + " is called " + dad_name + " and the grandfather is called " + grandfather_name
          + ".")
    else:
      print("The name of the son is not registered.")
  elif j == 2:
    if dad_name:
      print("The son you entered is already registered.")
    else:
      dad_name = input("Enter the name of " + son_name + " dad: ")
      grandfather_name = input("Enter the name of " + son_name + " grandfather: ")
      generations.append([son_name, dad_name, grandfather_name])
  elif j == 3:
      if dad_name:
        dad_name = input("Enter the name of the new dad of " + son_name + ": ")
        grandfather_name = input("Enter the name of the new grandfather of " + son_name + ": ")
        generations[i][1] = dad_name
        generations[i][2] = grandfather_name
      else:
        print("The son you entered is not registered.")
  elif j == 4:
      if dad_name:
        print("Deleted son " + son_name + " and his dad " + dad_name + " and his grandfather " + grandfather_name + ".")
        del generations[i]
      else:
        print("The son you entered is not registered.")

