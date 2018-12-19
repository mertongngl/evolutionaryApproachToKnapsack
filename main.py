from fileOper import FileOper

from evolutionaryOper import EvolutionaryOper

files = FileOper("inputs/test1.txt")

evolutionary = EvolutionaryOper(files)

evolutionary.initialise()
print(evolutionary.tournament_selection())

print(evolutionary.recombine(('00000010100001000010000', 72), ('00101000010000100000010', 90)))