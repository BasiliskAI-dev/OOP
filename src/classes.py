from abc import ABC, abstractmethod


class BaseClass(ABC):

    @abstractmethod
    def __init__(self, name: str, description: str, quantity: int, price: float):
        self.name = name
        self.description = description
        self.quantity = quantity
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self._price = price

    @classmethod
    @abstractmethod
    def new_product(cls, new_dict: dict) -> "Product":
        pass

    @abstractmethod
    def price(self) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, another: "Product") -> float:
        pass


class MixinLog:

    def __init__(self, name: str, description: str, quantity: int, price: float):
        super().__init__(name, description, quantity, price)
        print(self.__repr__())

    def __repr__(self) -> str:
        return f"({self.__class__.__name__}('{self.name}', '{self.description}', {self.quantity})"


class Product(MixinLog, BaseClass):
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        super().__init__(name, description, quantity, price)
        self.__price = price

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
        if type(self) is type(another):
            return self.price * self.quantity + another.price * another.quantity
        else:
            raise TypeError


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

    def add_product(self, product: Product) -> None:
        if isinstance(product, Product):
            self.__products.append(product)
            self.product_count += 1
        else:
            raise TypeError

    @property
    def products(self) -> list:
        return [
            f"{x.name}, {x.price} руб. Остаток: {x.quantity}" for x in self.__products
        ]

    def __str__(self) -> str:
        counter = 0
        for x in self.__products:
            counter += x.quantity
        return f"{self.name}, Количество продуктов шт.{counter}"

    def middle_price(self) -> float:
        average = 0
        average_list = [x.price for x in self.__products]
        for x in average_list:
            average += x
        try:
            middle = average / len(average_list)
            return round(middle, 2)
        except ZeroDivisionError:
            raise ZeroDivisionError(
                "Количество товаров не может быть ноль в категории. Перепроверьте исходные данные"
            )


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
