import requests
from bs4 import BeautifulSoup

def readhtml_good(url):
    return requests.get(url).text


def get_currency_parametr_from_column(html, currency_code, column):
    """Из таблицы вытаскиваем требуемый параметр для конкретной валюты.
    currency_data - номер столбца в таблице, где расположен требуемый параметр."""

    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all('div')
    for div in divs:
        if 'class' in div.attrs:
            if div['class'] == ["table-wrapper"]:
                for currency in div.find_all('tr'):
                    if currency.contents[3].string == currency_code:
                        return currency.contents[column].string