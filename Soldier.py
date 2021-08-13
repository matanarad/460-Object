class Soldier:
    rankList = ["Private", "Corporal", "Sergeant", "Staff Sergeant"]

    def __init__(self, fullName, personalNumber, rank, kaba=None, dapar=None):
        self.fullName = fullName
        self.personalNumber = personalNumber
        self.rank = rank
        self.Kaba = kaba
        self.dapar = dapar

    def promotion(self):
        if self.rank == Soldier.rankList[len(Soldier.rankList)]:
            print("error higest rank")
        else:
            self.rank = Soldier.rankList[Soldier.rankList.index(self.rank)+1]
            print("promotion was a success")

    def askForGimel(self):
        print("you got 1 gimel")

    def printSoldier(self):
        print("Full name: " + self.fullName +
              ", Personal number: " + str(self.personalNumber) +
              ", rnak: " + self.rank)

    def officerTraining(self):
        if self.dapar is not None and self.Kaba is not None:
            if self.dapar >= 60 and self.Kaba >= 53:
                print("Suitable for taking an officers course")
            elif self.dapar >= 60 and self.Kaba < 53:
                print("Your kaba is too low")
            elif self.dapar < 60 and self.Kaba >= 53:
                print("Your dapar is too low")
            else:
                print("You do not have high enough grades")
        else:
            print("Missing data")
