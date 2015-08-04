# Exercise 4
#
# Create a Critter Farm program by instantiating several Critter objects and keeping track of them through a list.
# Mimic the Critter Caretaker program, but instead of requiring the user to care for a single critter, require them
# to care for an entire farm. Each menu choice should allow the user to perform some action for all of the critters (
# feed all of the critters, play with all the critters or listen to all the critters). To make the program
# interesting, give each critter random starting hunger and boredom levels.
#

import random

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        string = "Name: " + self.name + "\n"
        string += "Hunger: " + self.hunger + "\n"
        string += "Boredom: " + self.boredom + "\n"

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m

    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()

    def eat(self, food = 4):
        print("Brruppp.  Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()



def main():
    crit_list = []

    for i in range(0, 3):
        crit_name = input("What do you want to name your critter?: ")
        crit_list.append(Critter(crit_name, random.randint(1, 10), random.randint(1, 10)))

    choice = None
    while choice != "0":
        print \
        ("""
        Critter Caretaker

        0 - Quit
        1 - Listen to all your critters
        2 - Feed all of your critters
        3 - Play with all of your critters
        """)

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            for crit in crit_list:
                crit.talk()

        # feed your critter
        elif choice == "2":
            for crit in crit_list:
                crit.eat()

        # play with your critter
        elif choice == "3":
            for crit in crit_list:
                crit.play()

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.")
