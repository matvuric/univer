from itertools import islice


def fib(n):
    def itr():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    g = itr()
    lst = []
    while True:
        x = next(g)
        lst.append(x)
        if x > n:
            lst.pop()
            return lst


def fib_iter(n):
    return list(islice(fib(n[-1]), 0, len(fib(n[-1]))))


class FibonacciLst:
    def __init__(self, instance):
        self.instance = instance
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                res = self.instance[self.idx]

            except IndexError:
                raise StopIteration

            if res in fib(self.instance[-1]):
                self.idx += 1
                return res

            self.idx += 1
