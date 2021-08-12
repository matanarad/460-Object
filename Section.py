from Team import Team
from Soldier import Soldier


class Section:

    def __init__(self, number, sectionHead: Soldier = ""):
        self.number = number
        self.sectionHead = sectionHead
        self.teamList = []

    def addTeam(self, team: Team):
        self.teamList.append(team)

