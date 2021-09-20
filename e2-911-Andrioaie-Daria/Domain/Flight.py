class FlightException(Exception):
    def __init__(self, msg):
        self._msg = msg

class Flight:

    def __init__(self, id_, departure_city, departure_time, arrival_city, arrival_time):

        self._id = id_
        self._departure_time = departure_time
        self._departure_city = departure_city
        self._arrival_time = arrival_time
        self._arrival_city = arrival_city

    @property
    def unique_id(self):
        return self._id

    @property
    def departure_time(self):
        return self._departure_time

    @property
    def departure_city(self):
        return self._departure_city

    @property
    def arrival_time(self):
        return self._arrival_time

    @property
    def arrival_city(self):
        return self._arrival_city

