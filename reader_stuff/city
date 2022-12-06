class City:
    def __init__(self, cityName, cityCode):
        city_name = cityName[0:1].upper() + cityName[1:].lower()  # то же самое со строкой города
        self.name = city_name
        self.code = cityCode
        # self.streets = streets

    def __eq__(self, other):
        return self.code == other.code

    def __hash__(self):
        return self.code.__hash__()
