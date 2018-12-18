from fileOper import FileOper

from evolutionaryOper import EvolutionaryOper

files = FileOper("inputs/test1.txt")

evolutionary = EvolutionaryOper(files)

evolutionary.initialise()
print(evolutionary.tournament_selection())