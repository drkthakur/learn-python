class PartyAnimal:
    x=0

    def __init__(self):
        print("I'm initialized!")

    def party(self):
        self.x = self.x+1
        print("so far:", self.x)

    def __del__(self):
        print("I'm destroyed !")


an = PartyAnimal()
an.party()
an.party()

an=42

print("an contains", an)