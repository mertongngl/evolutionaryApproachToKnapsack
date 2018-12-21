from fileOper import FileOper
from item import Item
from math import ceil

class EvolutionaryOper:
    __files = object()
    __population = list()
    __i_random = int()
    __random_list_len = int()
    def __init__(self, files: FileOper):
        self.__files = files
        self.__i_random = 0
        self.__random_list_len = len(files.get_random_list())

    def __create_item(self):
        item_list = list()
        for i in range(len(self.__files.get_value_list())):
            item_list.append(Item(self.__files.get_weight_list()[i], self.__files.get_value_list()[i]))
        return item_list

    def initialise(self):
        random_list = self.__files.get_random_list()
        item_list = self.__create_item()
        for i in range(self.__files.get_population_size()):
            gen = ''
            for j in range(len(item_list)):
                if(random_list[self.__i_random % self.__random_list_len] < 0.5):
                    gen += '0'
                else:
                    gen += '1'
                self.__i_random += 1
            self.__population.append(self.__evaluate((gen, 0)))
            
    def get_population(self):
        return self.__population

    def __evaluate(self, individual: tuple):
        item_list = self.__create_item()
        sum_of_weight = 0
        sum_of_value = 0
        for i in range(len(individual[0])):
            if(individual[0][i] == '1'):
                sum_of_value += item_list[i].get_value()
                sum_of_weight += item_list[i].get_weigth()
        if(sum_of_weight > self.__files.get_bag_size()):
            sum_of_value = 0
        return (individual[0], sum_of_value)
        
    def __get_index(self, random_value: float):
        return ceil(random_value * float(self.__files.get_population_size()))

    def tournament_selection(self, population: list):
        chosen_ind = list()
        new_population = list()
        random_list = self.__files.get_random_list()
        self.__random_list_len = len(random_list)
        for i in range(self.__files.get_population_size()):
            chosen_ind = list()
            for j in range(self.__files.get_k()):
                chosen_ind.append(population[self.__get_index(random_list[self.__i_random % self.__random_list_len]) - 1])
                self.__i_random += 1
            chosen_ind.sort(key=lambda tup: tup[1])
            new_population.append(chosen_ind[-1])
        return new_population

    def __recombine(self, parent1: tuple, parent2: tuple):
        random_list = self.__files.get_random_list()
        random_list_len = len(random_list)
        parent1_gen = parent1[0]
        parent2_gen = parent2[0]
        index = self.__get_index(random_list[self.__i_random % random_list_len])
        child1 = parent1_gen[0:index] + parent2_gen[index:] 
        child2 = parent2_gen[0:index] + parent1_gen[index:]
        self.__i_random += 1
        return self.__evaluate((child1, 0)), self.__evaluate((child2, 0))

    def to_recombine(self, population: list):
        crossover_population = list()
        for i in range(0,len(population),2):
            child1, child2 = self.__recombine(population[i], population[i+1])
            crossover_population.extend([child1, child2])
        return crossover_population

    def to_mutate(self, population: list):
        mutated_population = list()
        for item in population:
            mutated_population.append(self.__mutate(item))
        return mutated_population

    def __mutate(self, individual: tuple):
        random_list = self.__files.get_random_list()
        random_list_len = len(random_list)
        mutation_chance = self.__files.get_mutaition_chance()
        gen = individual[0]
        new_gen = ""
        for i in range(len(gen)):
            if(random_list[self.__i_random % random_list_len] >= mutation_chance):
                new_gen += gen[i]
            else:
                if(int(gen[i])):
                    new_gen += '0'
                else:
                    new_gen += '1'
            self.__i_random += 1

        return self.__evaluate((new_gen, 0))
        
    def survival_select(self, crossover_population: list, mutated_population: list):
        survival_population = crossover_population
        survival_population.extend(mutated_population)
        survival_population.sort(key=lambda tup: tup[1])
        survival_population.reverse()
        return survival_population[:self.__files.get_population_size()]