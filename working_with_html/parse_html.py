import urllib.request
import ssl
import requests
from bs4 import BeautifulSoup

class HtmlReader:
    def HtmlReaderBad(self, url, output_filename):
        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        html = urllib.request.urlopen(url, context=ctx).read()
        fhand = open(output_filename+'.html', 'wb')
        fhand.write(html)
        fhand.close()


    def HtmlReaderGood(self, url):
        return requests.get(url).text
        # with open(output_filename+'.html', 'w') as output_file:
        #     output_file.write(r.text)


    def getCurrency(self, html, currency_string):
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.find_all('div')
        for tag in tags:
            if 'class' in tag.attrs:
                if tag['class'] == ["table-wrapper"]:
                    for currency in tag.find_all('tr'):
                        if currency.contents[3].string == currency_string:
                            return currency.contents[9].string

url = 'https://www.cbr.ru/currency_base/daily/'
page = HtmlReader
read_page = page.HtmlReaderGood(page, url)
currency = page.getCurrency(page, read_page, 'EUR')
print(currency)