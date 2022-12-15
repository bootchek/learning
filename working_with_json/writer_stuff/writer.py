import json
from json import JSONEncoder
from working_with_json.writer_stuff.street import Street
from working_with_json.writer_stuff.city import City
from working_with_json.writer_stuff.country import Country

class Mapper(JSONEncoder):
    def default(self, o):
        return o.__dict__


def create_json_from(json_dict: dict) -> str:
    """Считывыем словарь и преобразуем к виду json"""
    cities = []
    for city in json_dict:
        streets = []
        for street in json_dict[city]:
            buildings = json_dict[city][street]
            streets.append(Street(street, buildings))
        cities.append(City(city, streets))

    return json.dumps(Country(cities), indent=2, cls=Mapper)
