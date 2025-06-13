# Функция для вычисления расчета остатка вещества
def calculate_remainder(N0, t, t1_2):
    return N0 * (1/2) ** (t / t1_2)

def curried_calculate(t1_2):
    """
    Каррированная функция: фиксирует t1_2 и возвращающает новую функцию

    Параметры:
        t1_2 - параметр функции, который нужно зафиксировать
    """

    # Функция для вычисления расчета остатка вещества с фиксированным периодом полураспада
    def decay_fixed(N0, t):
        return calculate_remainder(N0, t, t1_2)
    return decay_fixed

# Словарь с изотопами и их периодами полураспада (в минутах)
isotopes = {
    "131I": 8, # Йод
    "133Xe": 5.3, # Ксенон
    "99Mo": 2.8 # Молибден
}

# Создание нового словаря с каррированными функциями
curried_isotopes = {isotope: curried_calculate(t1_2) for isotope, t1_2 in isotopes.items()}

N0 = 100
t = 100

# Цикл по словарю с каррированными функциями
for isotope, func in curried_isotopes.items():
    result = func(N0, t)
    print(f"{isotope}: осталось {result} единиц вещества.")
