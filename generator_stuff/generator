import random
import string
import json
import os


def create_json(output_filename, number_of_objects):
    json_list = list()
    for i in range(number_of_objects):
        element = {
            "cityName": ''.join(random.choice(string.ascii_lowercase) for i in range(10)),
            "cityCode": random.randint(1, 100),
            "streetName": ''.join(random.choice(string.ascii_lowercase) for i in range(10)),
            "streetCode": random.randint(1, 100),
            "building": random.randint(1, 100)
        }
        json_list.append(element)

    cur_path = os.path.dirname(__file__)
    new_path = cur_path+'/'
    with open(new_path+output_filename + '.json', "w") as outfile:
        json.dump(json_list, outfile, indent=2)
