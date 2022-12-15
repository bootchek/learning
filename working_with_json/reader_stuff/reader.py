import json
import os
from working_with_json.reader_stuff.city import City
from working_with_json.reader_stuff.street import Street


def read_json_data(input_filename: str) -> dict:
    """Считываем исходный json, преобразуем данные и кладём их в dict."""

    cur_path = os.path.dirname(__file__)
    new_path = '/Users/danilbuslaev/PycharmProjects/LeetCode/Practical tasks/6_merge_json/generator_stuff/'
    fhandle = open(new_path+input_filename + '.json')
    data = json.load(fhandle)
    json_dict = dict()

    for item in data:
        building = item['building']
        street = Street(item['streetName'], item['streetCode'])
        city = City(item['cityName'], item['cityCode'])

        if not city in json_dict:
            json_dict[city] = {street: [building]}
        else:
            if not street in json_dict[city]:
                json_dict[city][street] = [building]
            else:
                json_dict[city][street].append(building)
    fhandle.close()
    return json_dict
