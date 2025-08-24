class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_dict: dict) -> "Product":
        name = new_dict.get("name", "")
        description = new_dict.get("description", "")
        price = new_dict.get("price", 0.0)
        quantity = new_dict.get("quantity", 0)
        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, another: "Product") -> float:
        return self.price * self.quantity + another.price * another.quantity


class Category:
    name: str
    description: str
    __products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        self.product_count = len(products)

    def add_product(self, product: str) -> None:
        if isinstance(product, Product):
            self.__products.append(product)
            self.product_count += 1

    @property
    def products(self) -> str:
        return ", ".join(
            [f"{x.name}, {x.price} руб. Остаток: {x.quantity}" for x in self.__products]
        )

    def __str__(self) -> str:
        counter = 0
        for x in self.__products:
            counter += x.quantity
        return f"{self.name}, Количество продуктов шт.{counter}"
