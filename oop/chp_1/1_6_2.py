class SingletonFive:

    __total_cls_num = 0
    __current_cls = None

    def __new__(cls, *args, **kwargs):
        if cls.__total_cls_num < 5:
            cls.__total_cls_num += 1
            cls.__current_cls = super().__new__(cls)
        return cls.__current_cls
        
    def __init__(self, name):
        self.name = name
        


objs = [SingletonFive(str(n)) for n in range(10)]
print([id(x) for x in objs])