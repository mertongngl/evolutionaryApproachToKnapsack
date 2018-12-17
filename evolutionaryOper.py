from fileOper import FileOper
from item import Item

class EvolutionaryOper:
    __files = object()
    __population = list()
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
        i_random = 0 # iterator for random list
        item_list = self.__create_item()

        for i in range(self.__files.get_population_size()):
            gen = ''
            sum_of_weight = 0
            sum_of_value = 0
            for j in range(len(item_list)):
                if(random_list[i_random % random_list_len] < 0.5):
                    gen += '0'
                else:
                    gen += '1'
                    sum_of_value += item_list[j].get_value()
                    sum_of_weight += item_list[j].get_weigth()
                i_random += 1
            if(sum_of_weight > self.__files.get_bag_size()):
                sum_of_value = 0
            self.__population.append((gen, sum_of_value))
            
    def get_population(self):
        return self.__population

    def evaluate(self, individual: tuple):
        item_list = self.__create_item()
        sum_of_weight = 0
        sum_of_value = 0
        for i in len(individual[0]):
            if(individual[0][i] == '1'):
                sum_of_value += item_list[i].get_value()
                sum_of_weight += item_list[i].get_weigth()
        if(sum_of_weight > self.__files.get_bag_size()):
            sum_of_value = 0
        return (individual[0], sum_of_value)
        