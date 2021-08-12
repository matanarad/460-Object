from Soldier import Soldier


class Team:

    def __init__(self, teamName, teamLeader: Soldier = ""):
        self.teamName = teamName
        self.teamLeader = teamLeader
        self.soldiersList = []

    def addSoldier(self, soldier: Soldier):
        self.soldiersList.append(soldier)

    def freeSoldier(self, soldier: Soldier):
        self.soldiersList.remove(soldier)
        print("release was a success")
