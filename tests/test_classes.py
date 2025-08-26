import pytest

from src.classes import Category, LawnGrass, Product, Smartphone

# mypy: ignore-errors


@pytest.fixture
def product_cucumber() -> Product:
    return Product("Огурец", "Зеленый овощ", 120.5, 5)


def test_init(product_cucumber):
    assert product_cucumber.name == "Огурец"
    assert product_cucumber.description == "Зеленый овощ"
    assert product_cucumber.price == 120.5
    assert product_cucumber.quantity == 5


def test_category_initialization():
    product1 = Product("Ноутбук", "Мощный игровой ноутбук", 999.99, 5)
    product2 = Product("Телефон", "Смартфон с хорошей камерой", 699.99, 10)

    electronics = Category("Электроника", "Техника для дома", [product1, product2])

    assert electronics.name == "Электроника"
    assert electronics.product_count == 2
    assert electronics.category_count == 1
    assert electronics.product_count == 2


class TestProduct:
    @pytest.fixture
    def sample_product(self):
        return Product("Телефон", "Смартфон", 50000.0, 10)

    @pytest.fixture
    def product_dict(self):
        return {
            "name": "Ноутбук",
            "description": "Игровой",
            "price": 80000.0,
            "quantity": 5,
        }

    def test_product_initialization(self, sample_product):
        assert sample_product.name == "Телефон"
        assert sample_product.description == "Смартфон"
        assert sample_product.price == 50000.0
        assert sample_product.quantity == 10

    def test_price_setter_positive(self, sample_product):
        sample_product.price = 45000.0
        assert sample_product.price == 45000.0

    def test_price_setter_negative(self, sample_product, capsys):
        sample_product.price = -100.0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert sample_product.price == 50000.0  # Цена не изменилась

    def test_new_product_classmethod(self, product_dict):
        product = Product.new_product(product_dict)
        assert product.name == "Ноутбук"
        assert product.description == "Игровой"
        assert product.price == 80000.0
        assert product.quantity == 5

    def test_private_price_access(self, sample_product):
        with pytest.raises(AttributeError):
            sample_product.__price


class TestCategory:
    @pytest.fixture
    def sample_products(self):
        return [
            Product("Телефон", "Смартфон", 50000.0, 10),
            Product("Ноутбук", "Игровой", 80000.0, 5),
        ]

    @pytest.fixture
    def sample_category(self, sample_products):
        Category.category_count = 0  # Сброс счетчика перед тестом
        return Category("Электроника", "Техника", sample_products)

    def test_category_initialization(self, sample_category, sample_products):
        assert sample_category.name == "Электроника"
        assert sample_category.description == "Техника"
        assert len(sample_category._Category__products) == 2
        assert Category.category_count == 1

    def test_add_product(self, sample_category):
        new_product = Product("Планшет", "Графический", 30000.0, 8)
        initial_count = sample_category.product_count
        sample_category.add_product(new_product)
        assert sample_category.product_count == initial_count + 1
        assert len(sample_category._Category__products) == 3

    def test_products_property(self, sample_category):
        products_str = sample_category.products
        assert "Телефон, 50000.0 руб. Остаток: 10" in products_str
        assert "Ноутбук, 80000.0 руб. Остаток: 5" in products_str

    def test_private_products_access(self, sample_category):
        with pytest.raises(AttributeError):
            sample_category.__products

    def test_product_count_initialization(
        self, sample_category, sample_products
    ) -> None:
        assert sample_category.product_count == len(sample_products)

    def test_category_count_increment(self) -> None:
        initial_count = Category.category_count
        products = [Product("Тест", "Тест", 100, 1)]
        Category("Тест", "Тест", products)
        assert Category.category_count == initial_count + 1


def testing_15_1():
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства "
        "жизни",
        [product1, product2, product3],
    )
    text_for_1_product = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    text_for_category = "Смартфоны, Количество продуктов шт.27"
    text_for_product = [
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5",
        "Iphone 15, 210000.0 руб. Остаток: 8",
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14",
    ]
    summ_of_products_1_2 = 2580000.0
    summ = product1 + product2
    assert text_for_category == str(category1)
    assert text_for_product == category1.products
    assert summ_of_products_1_2 == summ
    assert str(product1) == text_for_1_product


@pytest.fixture
def product_smartphone() -> Smartphone:
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


def test_smartphone(product_smartphone):
    assert product_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert product_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert product_smartphone.price == 180000.0
    assert product_smartphone.quantity == 5
    assert product_smartphone.efficiency == 95.5
    assert product_smartphone.model == "S23 Ultra"
    assert product_smartphone.memory == 256
    assert product_smartphone.color == "Серый"


@pytest.fixture
def product_grass() -> LawnGrass:
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


def test_grass(product_grass):
    assert product_grass.name == "Газонная трава"
    assert product_grass.description == "Элитная трава для газона"
    assert product_grass.price == 500.0
    assert product_grass.quantity == 20
    assert product_grass.country == "Россия"
    assert product_grass.germination_period == "7 дней"
    assert product_grass.color == "Зеленый"


def testing_16_1() -> None:
    grass1 = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    grass2 = LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    smartphone2 = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )

    grass_sum = grass1 + grass2
    smartphone_sum = smartphone1 + smartphone2
    assert smartphone_sum == 2580000.0
    assert grass_sum == 16750.0


def error_invalid_sum():
    grass1 = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )

    with pytest.raises(TypeError):
        smartphone1 + grass1


def error_invalid_add():

    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    smartphone2 = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )
    category_smartphones = Category(
        "Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2]
    )
    with pytest.raises(TypeError):
        category_smartphones.add_product("Not a product")


def test_16_2(capsys):

    Product("Test Product", "Test Description", 100.0, 5)
    captured = capsys.readouterr()
    output = captured.out.strip()

    # Проверяем вывод
    assert output == "(Product('Test Product', 'Test Description', 5)"
