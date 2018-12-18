from fileOper import FileOper
from item import Item
from math import ceil

class EvolutionaryOper:
    __files = object()
    __population = list()
    __i_random = 0
    def __init__(self, files: FileOper):
        self.__files = files

    def __create_item(self):
        item_list = list()
        for i in range(len(self.__files.get_value_list())):
            item_list.append(Item(self.__files.get_weight_list()[i], self.__files.get_value_list()[i]))
        return item_list

    def initialise(self):
        random_list = self.__files.get_random_list()
        random_list_len = len(random_list)
        item_list = self.__create_item()
        for i in range(self.__files.get_population_size()):
            gen = ''
            for j in range(len(item_list)):
                if(random_list[self.__i_random % random_list_len] < 0.5):
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
        return ceil(random_value * float(self.__files.get_population_size())) - 1

    def tournament_selection(self):
        chosen_ind = list()
        new_population = list()
        random_list = self.__files.get_random_list()
        random_list_len = len(random_list)
        for i in range(self.__files.get_population_size()):
            chosen_ind = list()
            for j in range(self.__files.get_k()):
                chosen_ind.append(self.__population[self.__get_index(random_list[self.__i_random % random_list_len])])
                self.__i_random += 1
            chosen_ind.sort(key=lambda tup: tup[1])
            new_population.append(chosen_ind[-1])
        return new_population