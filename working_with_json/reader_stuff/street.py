class Street:
    def __init__(self, streetName, streetCode):
        street_name = streetName[0:1].upper() + streetName[
                                                        1:].lower()  # исходную строку приводим к целевому виду (первая заглавная)
        self.name = street_name
        self.code = streetCode
        # self.buildings = buildings

    def __eq__(self, other):
        return self.code == other.code

    def __hash__(self):
        return self.code.__hash__()
