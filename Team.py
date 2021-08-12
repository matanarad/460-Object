from Soldier import Soldier


class Team:

    def __init__(self, teamName, teamLeader: Soldier = ""):
        self.teamName = teamName
        self.teamLeader = teamLeader
        self.soldiersList = []

    def addSoldier(self, soldier: Soldier):
        self.soldiersList.append(soldier)
        print(len(self.soldiersList))

    def freeSoldier(self, soldier: Soldier):
        self.soldiersList.remove(soldier)
        print("release was a success")

    def printTeam(self):
        print("Team name: " + self.teamName)
        for soldier in self.soldiersList:
            soldier.printSoldier()

    def soldierExistInTeam(self, number):
        for soldier in self.soldiersList:
            if soldier.personalNumber == number:
                return soldier
        return False
