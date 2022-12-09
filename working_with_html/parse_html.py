import urllib.request
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.cbr.ru/currency_base/daily/'
html = urllib.request.urlopen(url, context=ctx).read()
fhand = open('copy_of_the_page.html', 'wb')
fhand.write(html)
fhand.close()