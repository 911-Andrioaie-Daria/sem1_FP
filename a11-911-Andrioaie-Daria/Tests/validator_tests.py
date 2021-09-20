import unittest

from Validators.move_validator import MoveValidator, MoveException


class TextMoveValidator(unittest.TestCase):
    def setUp(self):
        self._validator = MoveValidator()

    def test_move_validator(self):
        # the column check raises an exception, so the row check is not reached
        try:
            self._validator.validate_move(3, -1)
        except MoveException:
            pass

        try:
            self._validator.validate_move(-1, 3)
        except MoveException:
            pass
