import pytest

from src.classes import Category, Product


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

    def test_product_count_initialization(self, sample_category, sample_products):
        assert sample_category.product_count == len(sample_products)

    def test_category_count_increment(self):
        initial_count = Category.category_count
        products = [Product("Тест", "Тест", 100, 1)]
        category = Category("Тест", "Тест", products)
        assert Category.category_count == initial_count + 1
