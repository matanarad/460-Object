from Soldier import Soldier
from Branch import Branch


class HovaService:

    def __init__(self, soldier: Soldier, serviceStatus="Hova"):
        self.soldier = soldier
        self.serviceStatus = serviceStatus

    def askForGimel(self):
        if self.serviceStatus is "Hova":
            print("ERROR Try again later")

    def shoutedShatz(self, number):
        targetSoldier = Branch.soldierExistInBranch(number)
        if targetSoldier is False:
            print("Boomerang!!!")
            return
        else:
            if Soldier.rankList.index(self.soldier.rank) <= 1:
                print("Shabat at the base")
            elif targetSoldier.rankList.index(self.soldier.rank) <= 1:
                print("Shatz received successfuly")
            elif targetSoldier.rankList.index(self.soldier.rank) > 1 and True:
            # חייל חובה
                print("Error you cant do it")
            elif True:
                print("you'er under arrest")
                 # חייל קבע
