from KevaService import KevaService
from HovaService import HovaService
from Team import Team
from Section import Section
from Branch import Branch

soldierKeva1 = KevaService("Soldier one", 123, "Staff Sergeant")
soldierHova1 = HovaService("Soldier Two", 1234, "Sergeant", 56, 90)
soldierHova2 = HovaService("Soldier three", 12345, "Private")
soldierKeva2 = KevaService("Soldier four", 123456, "Corporal", 50, 60)

wingsTeam = Team("Wings")
teslaTeam = Team("Tesla")
wingsTeam.addSoldier(soldierKeva1)
wingsTeam.addSoldier(soldierHova2)
teslaTeam.addSoldier(soldierHova1)
teslaTeam.addSoldier(soldierKeva2)

section1 = Section(1)
section1.addTeam(teslaTeam)
section1.addTeam(wingsTeam)

brunch1 = Branch(1)
brunch1.addSection(section1)

# brunch1.printHierarchy()
# soldier12.shoutedShatz(123445)
# soldierKeva1.askForDaysoff(25)
# soldierKeva2.officerTraining()
