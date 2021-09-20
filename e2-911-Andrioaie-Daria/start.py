from Repository.flight_repository import FlightsRepository
from Service.flight_service import FlightService
from Validators.flight_validator import FlightValidator
from ui.ui import ConsoleUI


def start_program():
    flight_validator = FlightValidator()
    flight_repository = FlightsRepository(flight_validator)

    flight_service = FlightService(flight_repository)

    console = ConsoleUI(flight_service)
    console.start()


start_program()
