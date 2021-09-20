import unittest
from datetime import time

from Domain.Flight import Flight
from Repository.flight_repository import FlightsRepository
from Validators.flight_validator import FlightValidator


class TestFlightRepository(unittest.TestCase):

    def setUp(self):
        self._flight_validator = FlightValidator()
        self._flight_repository = FlightsRepository(self._flight_validator)

    def test_add_new_person(self):
        current_length_of_repo = len(self._flight_repository.current_list_of_flights)
        flight1 = Flight("RO1234", "Onesti", time(hours=12, minutes=12), "Cluj", time(hours=13, minutes=13))
        self._flight_repository.add_flight(flight1)

        self.assertEqual(len(self._flight_repository.current_list_of_flights), current_length_of_repo + 1)