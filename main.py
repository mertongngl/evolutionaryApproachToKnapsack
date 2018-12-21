from fileOper import FileOper

from evolutionaryOper import EvolutionaryOper

files = FileOper("inputs/test1.txt")

evolutionary = EvolutionaryOper(files)

evolutionary.initialise()
eliminated_population = evolutionary.tournament_selection()
crossover_population = evolutionary.to_recombine(eliminated_population)

print(crossover_population)
print("MUTATED POPULATION:")

print(evolutionary.to_mutate(crossover_population))