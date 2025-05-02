class StackObj:
    
    def __init__(self, data, next = None):
        self.__data = data
        self.__next = next

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, nxt):
        if isinstance(nxt, StackObj) or nxt is None:
            self.__next = nxt

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, dt):
        self.__data = dt

class Stack:
    
    def __init__(self, top = None):
        self.top = top

    def push(self, obj):
        self.top = obj
        obj.next = obj


    
