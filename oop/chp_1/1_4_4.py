import sys

lst_in = list(map(str.strip, sys.stdin.readlines())) 


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data: list):
        for value in data:
            self.lst_data.append(dict(zip(self.FIELDS, value.split())))

    def select(self, a, b):        
        return self.lst_data[a:b + 1]



db = DataBase()
db.insert(lst_in)