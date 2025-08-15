class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_dict):
        name = new_dict.get("name")
        description = new_dict.get("description")
        price = new_dict.get("price")
        quantity = new_dict.get("quantity")
        return cls(name, description, price, quantity)

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

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        self.product_count = len(products)

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            self.product_count += 1

    @property
    def products(self):
        return ", ".join(
            [f"{x.name}, {x.price} руб. Остаток: {x.quantity}" for x in self.__products]
        )

