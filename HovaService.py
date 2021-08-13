from KevaService import KevaService
from Soldier import Soldier
from Branch import Branch


class HovaService(Soldier):

    def __init__(self, fullName, personalNumber, rank):
        super().__init__(fullName, personalNumber, rank)

    def askForGimel(self):
        print("ERROR Try  again later")

    def shoutedShatz(self, number):
        targetSoldier = Branch.soldierExistInBranch(number)
        if targetSoldier is False:
            print("Boomerang!!!")
            return
        else:
            if Soldier.rankList.index(self.rank) <= 1:
                print("Shabat at the base")
            elif targetSoldier.rankList.index(targetSoldier.rank) <= 1:
                print("Shatz received successfuly")
            elif targetSoldier.rankList.index(targetSoldier.rank) > 1 and (
                                              isinstance(targetSoldier,
                                                         HovaService)):
                print("Error you cant do it")
            elif isinstance(targetSoldier, KevaService):
                print("you'er under arrest")
