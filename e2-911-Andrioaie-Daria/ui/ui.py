from datetime import time

from Domain.Flight import Flight


class ConsoleUI:
    def __init__(self, flight_service):
        self.__flight_service = flight_service


    @property
    def flight_service(self):
        return self.__flight_service

    def print_menu(self):
        print("1. Add flight")
        print("2. Delete flight")
        print("3. List the airports, in decreasing order of activity.")
        print("4. List the time intervals during which no flights are airborne, in decreasing order of their length")
        print("5. List all time intervals during which the maximum number of flights are airborne ")
        print("0. exit")
        print('\n')

    def __print_list(self, objects):
        for object in objects:
            print(object)

    def add_flight_ui(self):
        flight_id = input("ID: ")
        departure_city = input("Departure city: ")
        departure_hour = int(input("Departure hour: "))
        departure_minute = int(input("Departure minute: "))
        departure_time = time(hour=departure_hour, minute=departure_minute)
        arrival_city = input("Arrival city: ")
        arrival_hour = int(input("Arrival hour: "))
        arrival_minute = int(input("Arrival minute: "))
        arrival_time = time(hour=arrival_hour, minute= arrival_minute)


        new_flight = Flight(flight_id, departure_city, departure_time, arrival_city, arrival_time)
        self.flight_service.add_flight(new_flight)
        print("The flight was added.")

    def delete_flight_ui(self):
        flight_id = input("Enter the flight id: ")
        self.flight_service.delete_flight(flight_id)
        print("The flight was deleted")

    def list_airports_decreasing_by_activity_ui(self):
        resulted_list_of_airports = self.flight_service.list_of_airports_decreasing_by_activity()
        print("AIRPORTS: ")
        print('\n')
        self.__print_list(resulted_list_of_airports)

    def list_time_intervals_with_no_flights_airborne(self):
        resulted_intervals = self.flight_service.intervals_with_no_airborne()
        self.__print_list(resulted_intervals)

    def list_time_intervals_with_maximum_flights_airborne_ui(self):
        pass

    def start(self):
        user_options = {1: self.add_flight_ui, 2: self.delete_flight_ui, 3: self.list_airports_decreasing_by_activity_ui,
                        4: self.list_time_intervals_with_no_flights_airborne,
                        5: self.list_time_intervals_with_maximum_flights_airborne_ui}

        self.print_menu()
        while True:
            user_option = int(input("Enter option: "))
            try:
                if user_option in user_options:
                    user_options[user_option]()
                elif user_option == 0:
                    print("Bye bye!")
                    break
                else:
                    print("The given option is not valid.")
            except Exception as exception_message:
                print("Errors:")
                print(exception_message)

