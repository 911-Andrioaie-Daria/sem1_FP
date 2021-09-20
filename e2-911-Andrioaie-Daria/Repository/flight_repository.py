from datetime import time

from Domain.Flight import Flight


class FileError(Exception):
    def __init__(self, message):
        self._message = message


class FlightsRepository:
    def __init__(self, flight_validator):
        self._current_list = []
        self._file_name = "input.txt"
        self.read_flights_from_file()
        self._flight_validator = flight_validator

    @property
    def current_list_of_flights(self):
        return self._current_list

    @property
    def flight_validator(self):
        return self._flight_validator

    def add_flight(self, new_flight):
        """
        Validates and appends a new Flight instance to the current list of fights
        :param new_flight: the flight that is added at the end of the list
        """
        self.flight_validator.validate(new_flight, self.current_list_of_flights)
        self.current_list_of_flights.append(new_flight)
        self.save_flights_to_file()
        return

    def remove_flight(self, flight_id):
        for flight in self.current_list_of_flights:
            if flight.unique_id == flight_id:
                self.current_list_of_flights.remove(flight)
                self.save_flights_to_file()
                return

        raise ValueError("There is no flight with the given id.")

    def read_flights_from_file(self):
        try:
            flights_file = open(self._file_name, 'rt')
            content = flights_file.readlines()
            flights_file.close()

            for line in content:
                line = line.split(',')
                unique_id = line[0]
                departure_city = line[1]

                departure_time = line[2].split(':')
                departure_hour = int(departure_time[0])
                departure_minute = int(departure_time[1])
                departure_time = time(hour=departure_hour, minute=departure_minute)

                arrival_city = line[3]

                last_attribute = line[4].split('\n')
                arrival_time = last_attribute[0]
                arrival_hour = int(arrival_time[0])
                arrival_minute = int(arrival_time[1])
                arrival_time = time(hour=arrival_hour, minute=arrival_minute)

                self.current_list_of_flights.append(Flight(unique_id, departure_city, departure_time, arrival_city,
                                                           arrival_time))

        except IOError as ioe:
            raise FileError('An error occurred!' + str(ioe))

    def save_flights_to_file(self):
        file = open(self._file_name, 'wt')
        try:
            for flight in self.current_list_of_flights:
                departure_time = str(flight.departure_time)
                departure_time = departure_time[:-3]

                arrival_time = str(flight.arrival_time)
                arrival_time = arrival_time[:-3]

                line = flight.unique_id + ',' + flight.departure_city + ',' + departure_time + ',' + \
                       flight.arrival_city + ',' + arrival_time
                file.write(line)
                file.write('\n')
            file.close()
        except Exception as exception_message:
            raise FileError(exception_message)
