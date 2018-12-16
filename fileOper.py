class FileOper:
    __path = ""
    __lines = list()
    __flag = True # If it reads file, __flag becomes False
    def __init__(self, path: str ):
        self.__path = path
    
    def  __open_file(self):
        with open(self.__path, 'r') as f:
            for line in f:
                self.__lines.append(line.replace('\n','').split(','))
        self.__flag = False


    def get_random_list(self):
        if self.__flag:
            self.__open_file()
        return list(map(float, self.__lines[0]))

    def get_population_size(self):
        if self.__flag:
            self.__open_file()
        return int(self.__lines[1][0])

    def get_k(self):
        if self.__flag:
            self.__open_file()
        return int(self.__lines[2][0])
    
    def get_mutaition_chance(self):
        if self.__flag:
            self.__open_file()
        return float(self.__lines[3][0])

    def get_iteration(self):
        if self.__flag:
            self.__open_file()
        return int(self.__lines[4][0])

    def get_bag_size(self):
        if self.__flag:
            self.__open_file()
        return int(self.__lines[5][0])

    def get_weight(self):
        if self.__flag:
            self.__open_file()
        return list(map(int, self.__lines[6]))
    
    def get_value(self):
        if self.__flag:
            self.__open_file()
        return list(map(int, self.__lines[7]))
    