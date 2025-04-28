class Money:

    def __init__(self, money = 0):
        self.money = money

class Point:
    
    def __init__(self, x, y, color = 'black'):
        self.x = x
        self.y = y
        self.color = color

start_point = 1
points = []

for i in range(1000):
    points.append(Point(start_point, start_point)) if i != 1 else points.append(Point(start_point, start_point, 'yellow'))
    start_point += 2