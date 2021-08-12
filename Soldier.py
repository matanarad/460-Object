class Soldier:

    def __init__(self, fullName, personalNumber, rank):
        self.fullName = fullName
        self.personalNumber = personalNumber
        self.rank = rank

    def promotion(self):
        rankList = ["Private", "Corporal", "Sergeant", "Staff Sergeant"]
        if self.rank == rankList[len(rankList)]:
            print("error higest rank")
        else:
            self.rank = rankList[rankList.index(self.rank)+1]
            print("promotion was a success")

    def askForGimel(self):
        print(self.fullName + "you got 1 gimel")

    def printSoldier(self):
        print("Full name: " + self.fullName +
              ", Personal number" + self.personalNumber +
              ", rnak: " + self.rank)
