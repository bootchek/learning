import time
import sys
import get_data
from currency import Currency
import json_creator

url = 'https://www.cbr.ru/currency_base/daily/'
input_file = open(sys.argv[1], "r")
codes = input_file.read().splitlines()
input_file.close()

while True:
    json_list = []
    read_page = get_data.readhtml_good(url)
    data_from_page = get_data.get_currency_data(read_page)
    for currency in data_from_page:
        if currency.code in codes:
            json_list.append(currency)
            print(currency.code, " равен ", currency.value)
    output_json = json_creator.create_json_from(json_list)
    output_file = open(sys.argv[2], 'w')
    output_file.write(output_json)
    output_file.close()
    print('\n')
    time.sleep(10)
