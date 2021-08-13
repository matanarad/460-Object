from Soldier import Soldier


class KevaService (Soldier):

    def __init__(self, fullName, personalNumber, rank):
        super().__init__(fullName, personalNumber, rank)

    def askForGimel(self):
        print("you got 10 gimel")
