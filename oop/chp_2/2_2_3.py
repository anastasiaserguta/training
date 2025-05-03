class StackObj:
    
    def __init__(self, data):
        self.__data = data
        self.__next = None

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
    
    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj):
        if self.last:
            self.last.next = obj
        self.last = obj
        if self.top is None:
            self.top = obj

    def pop(self):
        pre_last = self.top
        if pre_last is None:
            return
        while pre_last and pre_last.next != self.last:
            pre_last = pre_last.next
        if pre_last:
            pre_last.next = None
        last = self.last
        self.last = pre_last
        if self.last is None:
            self.top = None
        
        return last

    def get_data(self):
        res = []
        obj = self.top
        while obj:
            res.append(obj.data)
            obj = obj.next
        return res


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()    # ['obj1', 'obj2']
print(res)
