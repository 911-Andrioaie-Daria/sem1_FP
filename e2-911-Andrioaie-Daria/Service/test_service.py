import unittest
from datetime import time

from Domain.Flight import Flight
from Repository.flight_repository import FlightsRepository
from Service.flight_service import FlightService
from Validators.flight_validator import FlightValidator


class TestFlightService(unittest.TestCase):

    def setUp(self):
        flight_validator = FlightValidator()
        flight_repository = FlightsRepository(flight_validator)

        self._flights_service = FlightService(flight_repository)

    def test_add_flight(self):
        current_length_of_repo = len(self._flights_service.get_all_flights())
        flight1 = Flight("RO1234", "Onesti", time(hours=12, minutes=12), "Cluj", time(hours=13, minutes=13))
        self._flights_service.add_flight(flight1)

        self.assertEqual(len(self._flights_service.get_all_flights()), current_length_of_repo+1)