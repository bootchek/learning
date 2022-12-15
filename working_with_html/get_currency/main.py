import time
import sys
import get_data
import json_creator

url = 'https://www.cbr.ru/currency_base/daily/'
input_file = open(sys.argv[1], "r")
codes = input_file.read().splitlines()
input_file.close()

while True:
    currencies = []
    html_string = get_data.readhtml_good(url)
    data_from_page = get_data.get_currency_data(html_string)
    for currency in data_from_page:
        if currency.code in codes:
            currencies.append(currency)
            print(currency.code, " равен ", currency.value)
    output_json = json_creator.create_json_from(currencies)
    output_file = open(sys.argv[2], 'w')
    output_file.write(output_json)
    output_file.close()
    print('\n')
    time.sleep(10)
