class Cart:

    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        del self.goods[indx]

    def get_list(self):
        goods = [f'{good.name}: {good.price}' for good in self.goods]
        return goods

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

class Table(Product):
    pass

class TV(Product):
    pass

class Notebook(Product):
    pass

class Cup(Product):
    pass

cart = Cart()
cart.add(TV('Samsung', 1000))
cart.add(TV('LG', 1500))
cart.add(Table('black', 50))
cart.add(Notebook('Samsung', 2000))
cart.add(Notebook('Xiaomi', 1000))
cart.add(Cup('tiny', 2))

print(cart.get_list())