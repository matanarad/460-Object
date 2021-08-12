class Soldier:
    rankList = ["Private", "Corporal", "Sergeant", "Staff Sergeant"]

    def __init__(self, fullName, personalNumber, rank):
        self.fullName = fullName
        self.personalNumber = personalNumber
        self.rank = rank

    def promotion(self):
        if self.rank == Soldier.rankList[len(Soldier.rankList)]:
            print("error higest rank")
        else:
            self.rank = Soldier.rankList[Soldier.rankList.index(self.rank)+1]
            print("promotion was a success")

    def askForGimel(self):
        print(self.fullName + "you got 1 gimel")

    def printSoldier(self):
        print("Full name: " + self.fullName +
              ", Personal number: " + str(self.personalNumber) +
              ", rnak: " + self.rank)
