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
