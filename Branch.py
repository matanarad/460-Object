from Section import Section
from Soldier import Soldier


class Branch:

    def __init__(self, number, branchHead: Soldier = ""):
        self.number = number
        self.branchHead = branchHead
        self.sectionList = [Section]

    def addSection(self, section: Section):
        self.sectionList.append(section)

    def printHierarchy(self):
        print("Branch Number: " + self.number)
        for section in self.sectionList:
            section.printSection()

    def soldierExistInBranch(self, number):
        tempSoldier = False
        for section in self.sectionList:
            tempSoldier = section.soldierExistInSection(number)
            if tempSoldier is not False:
                return tempSoldier
        return tempSoldier
