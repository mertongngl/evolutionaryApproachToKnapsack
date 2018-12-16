class Item:
    weight = int()
    value = int()
    def __init__(self, weight: int, value: int):
        self.weight = weight
        self.value = value

    def get_weigth(self):
        return self.weight
    
    def get_value(self):
        return self.value