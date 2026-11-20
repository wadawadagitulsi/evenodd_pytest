from evenodd import evenodd
def evenodd(num):
    return num % 2 == 0
def test_even():
    assert evenodd(2) == True
def test_odd():
    assert evenodd(5) == False