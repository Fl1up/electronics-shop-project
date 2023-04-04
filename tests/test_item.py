import pytest

from src.item import Item

item1 = Item("Смартфон", 10000, 20)

def test_calculate_total_price():
    with pytest.raises(AssertionError):
        assert item1.price == float

def test_apply_discount():
    assert item1.apply_discount() == None
