from numb3rs import validate

def test_validate():
    assert validate("192.168.0.1") == True
    assert validate("300.400.500.600") == False
    assert validate('10.20.30.40') == True
    assert validate("8.8.8.8") == True
    assert validate("cat") == False
    assert validate("172.16.0.1") == True
    assert validate ('abc.def.ghi.jkl') == False
    assert validate("123.45.67.89") == True
    assert validate("10.0.0.1") == True
    assert validate("45.137.315.27") == False
    assert validate("172.16.0.1") == True
