import pytest
from um import count


def test_input():
    assert count("Um, code in Python.") == 1
    assert count("um") == 1
    assert count("hello world") == 0
    assert count("yummy") == 0
    assert count("Um, thanks, um...") == 2
    assert count("Um?") == 1
