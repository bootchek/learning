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


def get_currency(html, currency_code):
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all('div')
    for div in divs:
        if 'class' in div.attrs:
            if div['class'] == ["table-wrapper"]:
                for currency in div.find_all('tr'):
                    if currency.contents[3].string == currency_code:
                        order = int(currency.contents[5].string)
                        price = float(currency.contents[9].string.replace(",", "."))
                        return price/order


url = 'https://www.cbr.ru/currency_base/daily/'
while True:
    read_page = readhtml_good(url)
    for i in range(1,len(sys.argv)):
        currency = get_currency(read_page, sys.argv[i])
        print(sys.argv[i]," равен ", currency)
    print('\n')
    time.sleep(10)