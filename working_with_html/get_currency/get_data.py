import requests
from bs4 import BeautifulSoup
from currency import Currency

def readhtml_good(url):
    return requests.get(url).text


def get_currency_data(html):
    """Из таблицы вытаскиваем требуемый параметр для конкретной валюты.
    currency_data - номер столбца в таблице, где расположен требуемый параметр."""

    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all('div')
    currencies_with_data = []
    for div in divs:
        if 'class' in div.attrs:
            if div['class'] == ["table-wrapper"]:
                for currency in div.find_all('tr'):
                    code = currency.contents[3].string
                    quantity = currency.contents[5].string
                    name = currency.contents[7].string
                    value = currency.contents[9].string
                    currencies_with_data.append(Currency(code, quantity, name, value))
    return currencies_with_data