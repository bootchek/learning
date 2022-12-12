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


url = 'https://www.cbr.ru/currency_base/daily/'
# html_reader = HtmlReader
# html_reader.HtmlReaderGood(html_reader, url, 'copy_page')
html = HtmlReader.HtmlReaderGood(HtmlReader, url)
# print(html)
soup = BeautifulSoup(HtmlReader.HtmlReaderGood(HtmlReader, url), 'html.parser')
# all_currencies = soup.find_all('tr')
all_currencies = soup('tr')
for currency in all_currencies:
    print(currency.t)
