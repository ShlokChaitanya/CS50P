from seasons import minutes

def test_date():
    assert minutes(365) == "Five hundred twenty-five thousand, six hundred minutes"
    assert minutes(10477) == "Fifteen million, eighty-six thousand, eight hundred eighty minutes"
    assert minutes(60) == "Eighty-six thousand, four hundred minutes"
    assert minutes(1000000) == "One billion, four hundred forty million minutes"
    assert minutes(8760) == "Twelve million, six hundred fourteen thousand, four hundred minutes"
