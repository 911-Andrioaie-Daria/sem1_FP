from datetime import datetime, timedelta


class FlightException(Exception):
    """
    Exception class for errors related to a person.
    """
    def __init__(self, exception_message):
        self.message = exception_message


class FlightValidator:
    def validate(self, flight, already_existing_flights):
        for existing_flight in already_existing_flights:
            if existing_flight.unique_id == flight.unique_id:
                raise FlightException("The ID is not unique.")

        departure_time = datetime.combine(datetime.today(), flight.departure_time)
        arrival_time = datetime.combine(datetime.today(), flight.arrival_time)

        flight_length = arrival_time - departure_time
        if flight_length > timedelta(minutes=90) or flight_length < timedelta(minutes=15):
            raise FlightException("Flight times are between 15 and 90 minutes")

        for existing_flight in already_existing_flights:
            if existing_flight.departure_city == flight.departure_city and existing_flight.departure_time == flight.departure_time:
                raise FlightException("An airport can handle a single operation")

            if existing_flight.arrival_city == flight.departure_city and existing_flight.arrival_time == flight.departure_time:
                raise FlightException("An airport can handle a single operation")

            if existing_flight.departure_city == flight.arrival_city and existing_flight.departure_time == flight.arrival_time:
                raise FlightException("An airport can handle a single operation")

            if existing_flight.arrival_city == flight.arrival_city and existing_flight.arrival_time == flight.arrival_time:
                raise FlightException("An airport can handle a single operation")