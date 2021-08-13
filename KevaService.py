from Soldier import Soldier


class KevaService (Soldier):

    def __init__(self, fullName, personalNumber, rank, kaba=None, dapar=None):
        super().__init__(fullName, personalNumber, rank, kaba, dapar)
        self.daysoff = 30

    def askForGimel(self):
        print("you got 10 gimel")

    def askForDayoff(self, days):
        if self.daysoff - days > 0:
            self.daysoff = self.daysoff - days
            print("Your vacation has been approved")
            print("You have {} days left".format(self.daysoff))
        else:
            print("You dont have enough days off")
            print("Number of days off left is: {}".format(self.daysoff))
