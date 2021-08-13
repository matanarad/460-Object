from KevaService import KevaService
from HovaService import HovaService
from Team import Team
from Section import Section
from Branch import Branch

soldier1 = KevaService("Soldier one", 123, "Staff Sergeant")
soldier12 = HovaService("Soldier Two", 1234, "Sergeant")
soldier2 = HovaService("Soldier three", 12345, "Private")
soldier3 = HovaService("Soldier four", 123456, "Corporal")
wingsTeam = Team("Wings")
teslaTeam = Team("Tesla")

wingsTeam.addSoldier(soldier12)
wingsTeam.addSoldier(soldier2)
teslaTeam.addSoldier(soldier3)
teslaTeam.addSoldier(soldier1)


section1 = Section(1)

section1.addTeam(teslaTeam)
section1.addTeam(wingsTeam)

brunch1 = Branch(1)
brunch1.addSection(section1)

brunch1.printHierarchy()
# soldier12.shoutedShatz(123445)
