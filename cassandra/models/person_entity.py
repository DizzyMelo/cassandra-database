import datetime
from models.location_entity import LocationEntity

class PersonEntity():
    def __init__(self, first_name: str, last_name: str, date_of_birth: datetime.datetime, place_of_birth: LocationEntity) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.place_of_birth = place_of_birth