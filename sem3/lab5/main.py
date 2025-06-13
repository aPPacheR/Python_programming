import random

class RandomNumberIterator:
    def __init__(self, n_len, start_range, end_range):
        self.__idx = 0
        self.n_len = n_len
        self.start_range = start_range
        self.end_range = end_range

    def __iter__(self):
        return self

    def __next__(self):
        if self.__idx < self.n_len:
            self.__idx += 1
            return random.randint(self.start_range, self.end_range)
        else:
            raise StopIteration

def RandomNumberGenerator(n_len, start_range, end_range):
    counter = 0
    while counter < n_len:
        counter += 1
        yield random.randint(start_range, end_range)

def FibGenerator1(n):
    x1 = 0
    x2 = 1
    for _ in range(n):
        yield x1
        x1, x2 = x2, x1 + x2

def FibGenerator2(n):
    for element in FibGenerator1(n):
        yield element + 10

class CountriesAndCities:
    def __init__(self, countries_and_cities, cities_where):
        self.countries_and_cities = countries_and_cities
        self.cities_where = cities_where
        self.countries = list(self.countries_and_cities.keys())
        self.current_index = 0
        self.current_city_index = 0
        self.current_city_where_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_index < len(self.countries):
            country = self.countries[self.current_index]
            cities = self.countries_and_cities[country]

            city = cities[self.current_city_index]
            self.current_city_index += 1

            if self.current_city_index >= len(cities):
                self.current_index += 1
                self.current_city_index = 0

            if city in self.cities_where:
                return city, country

        raise StopIteration

print("1.1")
for __element in RandomNumberIterator(10, 0, 100):
    print(__element)
print()

print("1.2")
for el1 in RandomNumberGenerator(10, 0, 100):
    print(el1)
print()

print("1.3")
for el2 in FibGenerator2(10):
    print(el2)
print()

countries_and_cities = {
    "Россия": ["Москва", "Санкт-Петербург", "Новосибирск"],
    "США": ["Нью-Йорк", "Лос-Анджелес", "Чикаго"],
    "Франция": ["Париж", "Марсель", "Лион"]
}

cities_where = {"Санкт-Петербург", "Чикаго", "Москва"}

print("1.4")
for city, county in CountriesAndCities(countries_and_cities, cities_where):
    print(f"{city} in {county}")
