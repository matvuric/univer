import gen_fib


def test_fib_1():
    assert gen_fib.fib(1) == [0, 1, 1]


def test_fib_2():
    assert gen_fib.fib(2) == [0, 1, 1, 2]


def test_fib_3():
    assert gen_fib.fib(0) == [0]


def test_fib_4():
    assert gen_fib.fib(40) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_fib_lst_1():
    assert list(gen_fib.FibonacciLst(range(0))) == []


def test_fib_lst_2():
    assert list(gen_fib.FibonacciLst(range(1))) == [0]


def test_fib_lst_3():
    assert list(gen_fib.FibonacciLst(range(4))) == [0, 1, 2, 3]


def test_fib_lst_4():
    assert list(gen_fib.FibonacciLst(range(40))) == [0, 1, 2, 3, 5, 8, 13, 21, 34]


if __name__ == '__main__':
    test_fib_1()
    test_fib_2()
    test_fib_3()
    test_fib_4()
    test_fib_lst_1()
    test_fib_lst_2()
    test_fib_lst_3()
    test_fib_lst_4()
