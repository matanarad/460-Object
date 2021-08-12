from Soldier import Soldier
from HovaService import HovaService
from Team import Team
from Section import Section
from Branch import Branch

soldier1 = Soldier("Matan Arad", 12344, "Private")
soldier12 = HovaService(soldier1)
soldier2 = Soldier("Matan Arad2", 12344, "Private")
soldier3 = Soldier("Matan Arad3", 12345, "Private")

team1 = Team("wings")
team2 = Team("wings1")

team1.addSoldier(soldier12)
team1.addSoldier(soldier2)
team2.addSoldier(soldier3)

section1 = Section(1)

section1.addTeam(team1)
section1.addTeam(team2)

section1.printSection()
