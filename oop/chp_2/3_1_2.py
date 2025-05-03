class Shop:
    
    def __init__(self, name, goods = []):
        self.name = name
        self.goods = goods

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)

class Product:

    _id: int = 0
    name: str
    weight: float | int
    price: float | int

    def __new__(cls, *args, **kwargs):
        cls._id += 1
        instance = super().__new__(cls)
        instance._id = cls._id
        return instance
    
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, name, value):
        if not isinstance(value, self.__annotations__[name]):
            raise TypeError("Неверный тип присваиваемых данных.")
        if name in ('weight', 'price') and value < 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        if name == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, name)

shop = Shop("Балакирев и К")
book = Product("Python ООП", -100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")

    
    