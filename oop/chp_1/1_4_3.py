import sys

class StreamData:

    def create(self, fields: tuple, lst_values: list):
        if len(fields) == len(lst_values):
            for index, field in enumerate(fields):
                setattr(self, field, lst_values[index])
            return True
        else: 
            return False


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        print(sd.__dict__)
        return sd, res
    
sr = StreamReader()
data, result = sr.readlines()
print(result)