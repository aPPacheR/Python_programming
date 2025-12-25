import functools

def fib_elem_gen():
    """Генератор, возвращающий элементы ряда Фибоначчи"""
    a = 0
    b = 1

    while True:
        yield a
        res = a + b
        a = b
        b = res


def my_genn():
    """Сопрограмма, возвращающая список чисел Фибоначчи"""
    while True:
        n = yield  # получаем n через send
        fib_gen = fib_elem_gen()
        result = []

        for _ in range(n):
            result.append(next(fib_gen))

        yield result


def fib_coroutine(g):
    """Декоратор для автоматического запуска корутины"""
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        gen.send(None)  # запуск корутины
        return gen
    return inner


my_genn = fib_coroutine(my_genn)


class FibonacchiLst:

    def __init__(self, instance):
        self.instance = instance
        self.idx = 0
        self.fib_set = self._make_fib_set(max(instance))

    def _make_fib_set(self, max_value):
        """Создаём множество чисел Фибоначчи до max_value"""
        fibs = {0, 1}
        a, b = 0, 1
        while b <= max_value:
            a, b = b, a + b
            fibs.add(b)
        return fibs

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.idx >= len(self.instance):
                raise StopIteration

            value = self.instance[self.idx]
            self.idx += 1

            if value in self.fib_set:
                return value


if __name__ == "__main__":
    print("Демонстрация работы сопрограммы Фибоначчи\n")

    # Создаём и автоматически запускаем корутину
    gen = my_genn()

    print("Отправляем n = 5")
    result = gen.send(5)
    print("Результат:", result, "\n")

    print("Демонстрация работы итератора FibonacchiLst\n")

    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    print("Исходный список:")
    print(lst, "\n")

    fib_iter = FibonacchiLst(lst)

    print("Элементы списка, принадлежащие ряду Фибоначчи:")

    for value in fib_iter:
        print(value, end=" ")

    print()



