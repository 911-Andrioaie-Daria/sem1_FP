class FlightService:
    def __init__(self, flight_repository):
        self._flight_repository = flight_repository

    @property
    def flight_repository(self):
        return self._flight_repository

    def get_all_flights(self):
        return self.flight_repository.current_list_of_flights

    def add_flight(self, new_flight):
        """
        The method takes a new Flight instance and passes it to the flights repository to be added to the list
        :param new_flight: Flight instance which is not yet validated.
        """
        self.flight_repository.add_flight(new_flight)

    def delete_flight(self, flight_id):
        self.flight_repository.remove_flight(flight_id)

    def list_of_airports_decreasing_by_activity(self):
        resulted_airports = []
        flights = self.get_all_flights()
        airports = {}
        for flight in flights:
            if flight.departure_city not in airports:
                airports[flight.departure_city] = 1
            else:
                airports[flight.departure_city] += 1

            if flight.arrival_city not in airports:
                airports[flight.arrival_city] = 1
            else:
                airports[flight.departure_city] += 1

        for airport in airports:
            resulted_airports.append(AirportActivity(airport, airports[airport]))

        # sort the list in ascending order of the free time
        resulted_airports.sort(key=lambda airport1: airport1.activity, reverse=True)

        return resulted_airports

    def intervals_with_no_airborne(self):
        sorted_list_of_intervals = []
        copy_of_flights = self.get_all_flights()
        copy_of_flights.sort(key=lambda flight: flight.departure_time)

        for index in range(len(copy_of_flights)-1):
            pass

class AirportActivity:
    def __init__(self, airport_city, activity):
        self._airport = airport_city
        self._activity = activity

    @property
    def airport(self):
        return self._airport

    @property
    def activity(self):
        return self._activity

    def __str__(self):
        return 'Airport: ' + self.airport + '  Activity: ' + str(self.activity)


