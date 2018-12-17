class Item:
    __weight = int()
    __value = int()
    def __init__(self, weight: int, value: int):
        self.__weight = weight
        self.__value = value

    def get_weigth(self):
        return self.__weight
    
    def get_value(self):
        return self.__value