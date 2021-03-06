import timeit
from fileOper import FileOper

from evolutionaryOper import EvolutionaryOper

import matplotlib as mpl

mpl.use("agg")

import matplotlib.pyplot as plt

start = timeit.default_timer()

files = FileOper("inputs/test1.txt")

evolutionary = EvolutionaryOper(files)

best_ones = list()
avg = list()
worst_ones = list()

evolutionary.initialise()
survivors = evolutionary.get_population()
print(survivors)
for i in range(files.get_iteration()):
    eliminated_population = evolutionary.tournament_selection(survivors)
    crossover_population = evolutionary.to_recombine(eliminated_population)
    mutated_population = evolutionary.to_mutate(crossover_population)
    survivors = evolutionary.survival_select(survivors,mutated_population)
    best_ones.append(survivors[0][1])
    worst_ones.append(survivors[-1][1])
    avg.append((sum([j for i,j in survivors])/float(len(survivors))))
    

stop = timeit.default_timer()


gen = range(0,files.get_iteration())
plt.plot(gen,avg,label='Ortalama')
plt.plot(gen,worst_ones,label='En küçük')
plt.plot(gen,best_ones,label='En büyük')
plt.xlabel('Nesil')
plt.ylabel('Fitness')
plt.legend(loc='upper right')
plt.savefig("./myOutputs/out1.png")



print("Time: " + str(stop - start))