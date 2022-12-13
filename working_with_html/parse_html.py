import urllib.request
import ssl
import requests
from bs4 import BeautifulSoup
import time
import sys


def readhtml_bad(url, output_filename):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urllib.request.urlopen(url, context=ctx).read()
    fhand = open(output_filename + '.html', 'wb')
    fhand.write(html)
    fhand.close()


def readhtml_good(url):
    return requests.get(url).text


def get_currency_data(html, currency_code, currency_data):
    """Из таблицы вытаскиваем требуемый параметр для конкретной валюты.
    currency_data - номер столбца в таблице, где расположен требуемый параметр."""

    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all('div')
    for div in divs:
        if 'class' in div.attrs:
            if div['class'] == ["table-wrapper"]:
                for currency in div.find_all('tr'):
                    if currency.contents[3].string == currency_code:
                        return currency.contents[currency_data+1].string


url = 'https://www.cbr.ru/currency_base/daily/'
input_file = open(sys.argv[1], "r")

for code in input_file:
    print(code.rstrip('\n'))
while True:
    read_page = readhtml_good(url)
    for i in range(1, len(sys.argv)):
        currency = get_currency_data(read_page, sys.argv[i])
        print(sys.argv[i], " равен ", currency)
    print('\n')
    time.sleep(10)
