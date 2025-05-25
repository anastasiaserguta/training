class Book:

    def __init__(self, title = '', author = '', pages = 0, year = 0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    @staticmethod
    def __excep():
        raise TypeError("Неверный тип присваиваемых данных.")

    def __setattr__(self, name, value):
        if name == 'title' and isinstance(value, str):
            object.__setattr__(self, name, value)
        elif name == 'author' and isinstance(value, str):
            object.__setattr__(self, name, value)
        elif name == 'pages' and isinstance(value, int):
            object.__setattr__(self, name, value)
        elif name == 'year' and isinstance(value, int):
            object.__setattr__(self, name, value)
        else:
            self.__excep()

book = Book()
book.author = 'Сергей Балакирев'
book.title = 'Python ООП'
book.pages = 123
book.year = 2022
