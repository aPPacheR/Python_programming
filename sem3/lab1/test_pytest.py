from main import calculate

def test_plus():
    assert calculate(999, 1, '+') == 1000

def test_minus():
    assert calculate(1, 1, '-') == 0

def test_divide():
    assert calculate(2, 1, '/') == 2

def test_multy():
    assert calculate(2,0, '*') == 0
