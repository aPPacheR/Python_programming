from gen_fib import my_genn


def test_fib_3():
    gen = my_genn()
    assert gen.send(3) == [0, 1, 1]


def test_fib_5():
    gen = my_genn()
    assert gen.send(5) == [0, 1, 1, 2, 3]


def test_fib_0():
    gen = my_genn()
    assert gen.send(0) == []


def test_fib_1():
    gen = my_genn()
    assert gen.send(1) == [0]


def test_fib_8():
    gen = my_genn()
    assert gen.send(8) == [0, 1, 1, 2, 3, 5, 8, 13]
