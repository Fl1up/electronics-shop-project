import pytest
from src.keyboard import KeyBoard

kb = KeyBoard('Dark Project KD87A', 9600, 5)


def test_language_str():
    assert str(kb) == 'Dark Project KD87A'


def test_fail():
    with pytest.raises(AssertionError):
        assert kb.language == "KZ"


