### Class and Object
class PartyAnimal:  # Class
    x = 0

    def Party(self):
        self.x = self.x + 1
        print("So far", self.x)


an = PartyAnimal()
an.Party()
an.Party()
an.Party()

print("Type", type(an))  # Type of attribute
print("Dir:", dir(an))  # Functions Available


###Constructor and Destructor
class PartyAnimal:
    x = 0

    def __init__(self):
        print("I am self Constructed")

    def Party(self):
        self.x = self.x + 1
        print("So Far", self.x)

    def __del__(self):
        print("I am Destructed", self.x)


an = PartyAnimal()
an.Party()
an.Party()
an = 42
print('an contains: ', an)


### Instance Variables
class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, z):
        self.name = z
        print(self.name, "Constructed")

    def Party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)


s = PartyAnimal("Sally")
s.Party()
j = PartyAnimal("Jim")
j.Party()
s.Party()


### Object Inheritance
class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, z):
        self.name = z
        print(self.name, "Constructed")

    def Party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)


class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.Party()
        print(self.name, "points", self.points)


print("=======================================")
s = PartyAnimal("Sally")
s.Party()
j = FootballFan("Jim")
j.Party()
j.touchdown()
