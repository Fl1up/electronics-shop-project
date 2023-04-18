import pytest
from src.item import Item
from src.phone import Phone

item1 = Item("Смартфон", 10000, 20)
phone1 = Phone("iPhone 14", 120_000, 5, 2)


def test_calculate_total_price():
    with pytest.raises(AssertionError):
        assert item1.price == float


def test_apply_discount():
    assert item1.apply_discount() == None


def test_string_to_number():
    assert Item.string_to_number(5) != str


def test_repr():
    assert type(repr(item1)) == str


def test_str():
    assert type(str(item1)) == str


def test_add():
    assert isinstance(phone1, Item) == True


def test_affiliation():
    assert issubclass(Phone, Item) == True


def test_false_add():
    with pytest.raises(NameError):
        assert isinstance(phone1, pups) == False
