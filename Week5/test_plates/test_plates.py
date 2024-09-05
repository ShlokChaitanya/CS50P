from plates import is_valid


def test_plates():
    assert is_valid("CS") == True
    assert is_valid("50") == False
    assert is_valid("ABCD01") == False
    assert is_valid("HICS50") == True
    assert is_valid("HEYCS50") == False
    assert is_valid("ABC123") == True
    assert is_valid("ABC12D") == False
    assert is_valid("Hello!") == False
