class RadiusVector2D:

    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x = 0, y = 0):
        self.__x = 0
        self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, value):
        return type(value) in (int, float) and cls.MIN_COORD <= value <= cls.MAX_COORD

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, new_x):
        if self.__check_value(new_x):
            self.__x = new_x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, new_y):
        if self.__check_value(new_y):
            self.__y = new_y

    @staticmethod
    def norm2(vector):
        return vector.x ** 2 + vector.y ** 2

