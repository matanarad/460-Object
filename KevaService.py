from Soldier import Soldier


class KevaService (Soldier):

    def __init__(self, fullName, personalNumber, rank):
        super().__init__(fullName, personalNumber, rank)

    # def askForGimel(self):
    #     if self.serviceStatus is "Keva":
    #         print("you got 10 gimel")
