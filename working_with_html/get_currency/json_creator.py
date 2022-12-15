import json
from json import JSONEncoder

class Mapper(JSONEncoder):
    def default(self, o):
        return o.__dict__


def create_json_from(json_dict: dict) -> str:
    """Считывыем словарь и преобразуем к виду json"""

    return json.dumps(json_dict, indent=2, cls=Mapper, ensure_ascii=False)