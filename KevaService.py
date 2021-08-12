from Soldier import Soldier


class KevaService:

    def __init__(self, soldier: Soldier, serviceStatus="Keva"):
        self.soldier = soldier
        self.serviceStatus = serviceStatus

    def askForGimel(self):
        if self.serviceStatus is "Keva":
            print("you got 10 gimel")
