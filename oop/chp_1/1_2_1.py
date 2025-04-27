class DataBase:
    pk = 1
    title = "Классы и объекты"
    author = "Сергей Балакирев"
    views = 14356
    comments = 12

class Goods:
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024

Goods.price = 2048
Goods.inflation = 100

class Car:
    pass

setattr(Car, 'model', 'Тойота')
setattr(Car, 'color', 'Розовый')
setattr(Car, 'number', 'П111УУ77')

print(Car.__dict__['color'])

class Notes:
    uid = 1005435
    title = "Шутка"
    author = "И.С. Бах"
    pages = 2

print(getattr(Notes, 'author'))

class Dictionary:
    rus = "Питон"
    eng = "Python"

print(getattr(Dictionary, 'rus_word', False))