class Cell:
    
    def __init__(self, around_mines = 0, mine = True, fl_open = False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open 

class GamePole:

    def __init__(self, n, m):
        pass