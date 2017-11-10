class PartyAnimal:
    x=0

    def party(self):
        self.x=self.x+1
        print("so far",self.x)


an = PartyAnimal()
an.party()
an.party()
an.party()

PartyAnimal.party(an)
print("Class type:", type(PartyAnimal))
print("Object type:", type(an))
print("Dir:", dir(an))
print("Type of X:", type(an.x))
print("Type of Party:", type(an.party))



