class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, __price, quantity):
        self.name = name
        self.description = description
        self.__price = __price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_dict):
        cls.name = new_dict.get("name")
        cls.description = new_dict.get("description")
        cls.__price = new_dict.get("price")
        cls.quantity = new_dict.get("quantity")
        return cls(cls.name, cls.description, cls.__price, cls.quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Category:
    name: str
    description: str
    __products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name, description, __products):
        self.name = name
        self.description = description
        self.__products = __products
        Category.category_count += 1
        self.product_count = len(__products)

    def add_product(self, product):
        self.__products.append(product)
        self.product_count += 1

    @property
    def products(self):
        return ", ".join(
            [f"{x.name}, {x.price} руб. Остаток: {x.quantity}" for x in self.__products]
        )
