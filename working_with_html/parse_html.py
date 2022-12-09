import urllib.request
import ssl
import requests

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


    def HtmlReaderGood(self, url, output_filename):
        r = requests.get(url)
        with open(output_filename+'.html', 'w') as output_file:
            output_file.write(r.text)


url = 'https://www.cbr.ru/currency_base/daily/'
html_reader = HtmlReader
html_reader.HtmlReaderGood(html_reader, url, 'copy_page')