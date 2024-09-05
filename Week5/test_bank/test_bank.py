from bank import value

def test_value():
    assert value("hello") == 0
    assert value("HELLO THERE") == 0
    assert value("hehehe") == 20
    assert value("How are you") == 20
    assert value("I love Python") == 100
    assert value("Shlok Chaitanya") == 100
