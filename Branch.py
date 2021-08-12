from Section import Section
from Soldier import Soldier


class Branch:
    sectionList = []

    def __init__(self, number, branchHead: Soldier = ""):
        self.number = number
        self.branchHead = branchHead

    def addSection(self, section: Section):
        self.sectionList.append(section)

    def printHierarchy(self):
        print("Branch Number: " + str(self.number))
        for section in self.sectionList:
            section.printSection()

    def soldierExistInBranch(number):
        tempSoldier = False
        for section in Branch.sectionList:
            tempSoldier = section.soldierExistInSection(number)
            if tempSoldier is not False:
                return tempSoldier
        return tempSoldier
