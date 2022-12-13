import time
import sys
import get_data
from currency import Currency
import json_creator

url = 'https://www.cbr.ru/currency_base/daily/'
input_file = open(sys.argv[1], "r")

while True:
    json_list = []
    read_page = get_data.readhtml_good(url)
    for code in input_file:
        code = code.rstrip('\n')
        quantity = get_data.get_currency_parametr_from_column(read_page, code, 5)
        name = get_data.get_currency_parametr_from_column(read_page, code, 7)
        value = get_data.get_currency_parametr_from_column(read_page, code, 9)
        json_list.append(Currency(code, quantity, name, value))
        print(code, " равен ", value)
    output_json = json_creator.create_json_from(json_list)
    output_file = open(sys.argv[2] + 'output.json', 'w')
    output_file.write(output_json)
    output_file.close()
    print('\n')

    time.sleep(10)
