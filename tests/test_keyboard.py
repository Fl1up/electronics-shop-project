import pytest

from src.keyboard import Keyboard

kb = Keyboard('Dark Project KD87A', 9600, 5)
def test_language_str():
    assert str(kb) == 'Dark Project KD87A'

def test_fail():
    with pytest.raises(AttributeError):
        assert kb.language() == "EM"