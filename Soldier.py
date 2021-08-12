class Soldier:

    def __init__(self, fullName, personalNumber, rank):
        self.fullName = fullName
        self.personalNumber = personalNumber
        self.rank = rank

    def promotion(self):
        rankList = ["Private", "Corporal", "Sergeant", "Staff Sergeant"]
        try:
            self.rank = rankList[rankList.index(self.rank)+1]
            print("promotion was success")
        except:
            print("error -> promotion was unsuccess")

    def askForGimel(self):
        print(self.fullName + "you got 1 gimel")
