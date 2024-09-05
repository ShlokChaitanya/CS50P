import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("1/2") == 50
    assert convert("84/100") == 84
    assert convert("11/100") == 11


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("4/3")
