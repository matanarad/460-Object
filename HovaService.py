from KevaService import KevaService
from Soldier import Soldier
from Branch import Branch


class HovaService(Soldier):

    def __init__(self, fullName, personalNumber, rank):
        super().__init__(fullName, personalNumber, rank)

    # def askForGimel(self):
    #     if self.serviceStatus is "Hova":
    #         print("ERROR Try  again later")

    def shoutedShatz(self, number):
        print(number)
        targetSoldier = Branch.soldierExistInBranch(1244)
        if targetSoldier is False:
            print("Boomerang!!!")
            return
        else:
            if Soldier.rankList.index(self.soldier.rank) <= 1:
                print("Shabat at the base")
            elif targetSoldier.rankList.index(self.soldier.rank) <= 1:
                print("Shatz received successfuly")
            elif targetSoldier.rankList.index(self.soldier.rank) > 1 and (
                                          isinstance(self, HovaService)):
                print("Error you cant do it")
            elif isinstance(self, KevaService):
                print("you'er under arrest")
