from random import randint

class Line:
    def __init__(self, a = 0, b = 0, c = 0, d = 0):
        self.sp = (a, b)
        self.ep = (c, d)

class Rect:
    def __init__(self, a = 0, b = 0, c = 0, d = 0):
        self.sp = (a, b)
        self.ep = (c, d)

class Ellipse:
    def __init__(self, a = 0, b = 0, c = 0, d = 0):
        self.sp = (a, b)
        self.ep = (c, d)

elements = []

for _ in range(217):
    a, c = randint(1, 10), randint(1, 10)
    b, d = randint(1, 10), randint(1, 10)
    elements.append((Line(a, b, c, d), Rect(a, b, c, d), Ellipse(a, b, c, d))[randint(0, 2)])
    

for obj in elements:
    if isinstance(obj, Line):
        obj.sp = (0, 0)
        obj.ep = (0, 0)

