def my_func(age):
    """
        Реализация замыкания(обычная функция)

        Параметры:
            age (int) - Возраст
        Возращает:
            Внутреннюю функцию inner
        """
    name = 'Pavel'
    lastName = 'Pavlenko'
    def inner():
        """
        Замыкание: распечатывает переданные аргументы в терминале

        """
        print(f"Hello, my name is {lastName} {name}, I'm {age} years old.")
    return inner

my_func(20)()