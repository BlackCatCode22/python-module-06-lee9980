# Anthony Silva
# 3/26/2025
# CIT 95

class PartyAnimal:

    def __init__ (self, z) :
        self.x = 0
        self.name = z
        print(self.name, "constructed")

    def party(self) :
        self.x = self.x + 1
        print(self.name, "party count", self.x)

a = PartyAnimal("Sally")
a.party()
j = PartyAnimal("Jim")

j.party()
a.party()