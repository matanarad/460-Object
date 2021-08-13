from KevaService import KevaService
from Soldier import Soldier
from Branch import Branch


class HovaService(Soldier):

    def __init__(self, fullName, personalNumber, rank, kaba=None, dapar=None):
        super().__init__(fullName, personalNumber, rank, kaba, dapar)
        self.daysoff = 20

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

    def askForDayoff(self, days):
        if self.daysoff - days > 0:
            self.daysoff = self.daysoff - days
            print("Your vacation has been approved")
            print("You have {} days left".format(self.daysoff))
        else:
            print("You dont have enough days off")
            print("Number of days off left is: {}".format(self.daysoff))
