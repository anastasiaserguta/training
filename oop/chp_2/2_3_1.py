class FloatValue:

    def __set_name__(self, owner, name):
        self.name = '_' + name

    @staticmethod
    def __is_valid(value):
        if not isinstance(value, float):
            raise TypeError("Присваивать можно только вещественный тип данных.")
        return True
    
    def __set__(self, instance, value):
        if self.__is_valid(value):
            setattr(instance, self.name, value)
    
    def __get__(self, instance, owner):
        return getattr(instance, self.name)

class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value

class TableSheet:

    def __init__(self, n, m):
        self.cells = [[Cell() for _ in range(m)] for _ in range(n)]

table = TableSheet(5, 3)
start_value = 1.0
for i in range(5):
    for j in range(3):
        table.cells[i][j].value = start_value
        start_value += 1



