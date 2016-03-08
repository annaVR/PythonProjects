__author__ = 'anna'
# Critter Farm
# A virtual pet farm to care for

class Critter(object):
    """A virtual pet"""
    farm=list()


    def __init__(self, name, hunger, boredom):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        Critter.farm.append(self)
        print("The farm:", Critter.farm)

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
    import random
    farm=Critter.farm
    item=int()
    for item in range(0, 4):
        crit = Critter(input("Name:"), random.randrange(0, 5), random.randrange(0,6))
        print(crit.name, crit.hunger, crit.boredom)

    choice = None
    while choice != "0":
        print \
        ("""
        Critter Caretaker

        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            for crit in Critter.farm:
                crit.talk()

        # feed your critter
        elif choice == "2":
            for crit in Critter.farm:
                crit.eat()

        # play with your critter
        elif choice == "3":
            for crit in Critter.farm:
                crit.play()

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.")