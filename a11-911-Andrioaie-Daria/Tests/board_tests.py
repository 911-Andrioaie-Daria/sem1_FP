import unittest

from Domain.board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self._board = Board()

    def test_getters(self):
        number_of_rows = self._board.number_of_rows
        self.assertEqual(number_of_rows, 6)

        number_of_columns = self._board.number_of_columns
        self.assertEqual(number_of_columns, 7)

    def test_slot_of_board(self):
        self._board.make_human_move(3, 4)
        slot_of_board = self._board.slot_of_board(3, 4)
        self.assertEqual(slot_of_board, 'X')

        self._board.make_computer_move(5, 6)
        slot_of_board = self._board.slot_of_board(5, 6)
        self.assertEqual(slot_of_board, '0')

    def test_printing_format(self):
        self._board.make_human_move(3, 4)
        printing_format = str(self._board)
        self.assertIsInstance(printing_format, str)