class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, wdth):
        if isinstance(wdth, int) and 0 <= wdth <= 10_000:
            self.__width = wdth
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, hght):
        if isinstance(hght, int) and 0 <= hght <= 10_000:
            self.__height = hght
            self.show()

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')