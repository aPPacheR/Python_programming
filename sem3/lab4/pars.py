from contextlib import closing

from bs4 import BeautifulSoup
from urllib import request

def parse(code):
    soup = BeautifulSoup(code, "html.parser")

    weatherWhere = soup.find('span', 'temp__value temp__value_with-unit')
    city = weatherWhere.get_text() # Где показывается погода
    print(city)

    """
    degrees = soup.find('span', {'class': 'ef050'})
    degreesValue = degrees.get_text() # Градусы
    openingBracket = degrees.next_sibling.strip() # Открывающая скобка

    degreesReal = soup.find('span', {'class': 'ef051'})
    degreesValueReal = degreesReal.get_text() # Градусы по ощущениям
    closingBracket = degreesReal.next_sibling.strip() # Закрывающая скобка

    speed = soup.find('span', {'class': 'ef118'})
    speedValue = speed.get_text() # Скорость ветра
    speedText = speed.next_sibling.strip() # Единицы измерения

    print(city)
    print(typeWeather)
    print(degreesValue, openingBracket, degreesValueReal, closingBracket)
    print(speedValue, speedText)
    """


url = 'https://yandex.com.am/weather/?lat=55.75581741&lon=37.61764526'
with request.urlopen(url) as request:
    code = request.read()
parse(code)

