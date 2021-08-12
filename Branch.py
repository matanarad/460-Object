from Section import Section
from Soldier import Soldier


class Branch:

    def __init__(self, number, branchHead: Soldier = ""):
        self.number = number
        self.branchHead = branchHead
        self.sectionList = []

    def addSection(self, section: Section):
        self.sectionList.append(section)

