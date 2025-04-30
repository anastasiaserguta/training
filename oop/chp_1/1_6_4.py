class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def clone(self):
        new_obj = Point(self.x, self.y)
        return new_obj
    
pt = Point(3, 4)
pt_clone = pt.clone()

print(id(pt), id(pt_clone))