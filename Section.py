from Team import Team
from Soldier import Soldier


class Section:

    def __init__(self, number, sectionHead: Soldier = ""):
        self.number = number
        self.sectionHead = sectionHead
        self.teamList = [Team]

    def addTeam(self, team: Team):
        self.teamList.append(team)

    def printSection(self):
        print("Section number: " + self.number)
        for team in self.teamList:
            team.printTeam()

    def soldierExistInSection(self, number):
        tempSoldier = False
        for team in self.teamList:
            tempSoldier = team.soldierExistInTeam(number)
            if tempSoldier is not False:
                return tempSoldier
        return tempSoldier
