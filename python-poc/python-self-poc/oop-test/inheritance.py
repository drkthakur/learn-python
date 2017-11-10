class PartyAnimal:
    x=0

    def party(self):
        self.x=self.x+1
        print("so far",self.x)


class CricketFan(PartyAnimal):
    points = 0

    def six(self):
        self.points = self.points+6
        self.party()
        print(self.points)


j = CricketFan()
j.six()

