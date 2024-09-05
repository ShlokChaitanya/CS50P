from twttr import shorten

def main():
    test_assert()

def test_assert():
    assert shorten("shlok chaitanya") == "shlk chtny"
    assert shorten("SHLOK CHAITANYA") == "SHLK CHTNY"
    assert shorten("shlok ch41t4nya") == "shlk ch41t4ny"
    assert shorten("h*ll@ w@r1d!!!") == "h*ll@ w@r1d!!!"
