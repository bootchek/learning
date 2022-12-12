import urllib.request
import ssl
import requests
from bs4 import BeautifulSoup
import time

def readhtml_bad(url, output_filename):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urllib.request.urlopen(url, context=ctx).read()
    fhand = open(output_filename+'.html', 'wb')
    fhand.write(html)
    fhand.close()


def readhtml_good(url):
    return requests.get(url).text
    # with open(output_filename+'.html', 'w') as output_file:
    #     output_file.write(r.text)


def getCurrency(html, currency_string):
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all('div')
    for tag in divs:
        if 'class' in tag.attrs:
            if tag['class'] == ["table-wrapper"]:
                for currency in tag.find_all('tr'):
                    if currency.contents[3].string == currency_string:
                        return currency.contents[9].string

url = 'https://www.cbr.ru/currency_base/daily/'
while True:
    read_page = readhtml_good(url)
    currency = getCurrency(read_page, 'USD')
    print(currency)
    time.sleep(300)