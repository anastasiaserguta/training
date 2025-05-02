class Point:
    
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y

class Rectangle:
    
    def __init__(self, x1, y1, x2 = 0, y2 = 0):
        self.__sp = x1 if isinstance(x1, Point) else Point(x1, y1)
        self.__ep = y1 if isinstance(y1, Point) else Point(x2, y2)

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__sp
    
    def draw(self):
        print(f'Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}')

rect = Rectangle(0, 0, 20, 34)
print(rect.get_coords())
print(rect.draw())