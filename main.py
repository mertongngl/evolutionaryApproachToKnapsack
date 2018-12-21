from fileOper import FileOper

from evolutionaryOper import EvolutionaryOper

files = FileOper("inputs/test1.txt")

evolutionary = EvolutionaryOper(files)

best_ones = list()
worst_ones = list()

evolutionary.initialise()
survivors = evolutionary.get_population()
print(survivors)
for i in range(files.get_iteration()):
    eliminated_population = evolutionary.tournament_selection(survivors)
    crossover_population = evolutionary.to_recombine(eliminated_population)
    mutated_population = evolutionary.to_mutate(crossover_population)
    survivors = evolutionary.survival_select(survivors,mutated_population)
    best_ones.append(survivors[0])
    worst_ones.append(survivors[-1])

print("BEST :" , " \n" , best_ones)
print("WORST :"," \n",worst_ones)