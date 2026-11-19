
from even_odd import check_even_odd

def test_even_number():
    assert check_even_odd(10) == "even"

def test_odd_number():
    assert check_even_odd(7) == "odd"

def test_zero():
    assert check_even_odd(0) == "even"
