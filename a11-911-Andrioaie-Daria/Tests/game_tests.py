import unittest

from Domain.board import Board
from Service.game import GameService
from Service.strategy import SmartStrategy
from Validators.move_validator import MoveValidator


class TestGameService(unittest.TestCase):
    def setUp(self):
        game_board = Board()
        move_validator = MoveValidator()
        game_strategy = SmartStrategy()
        self._game_service = GameService(game_board, move_validator, game_strategy)

    def test_getters(self):
        board = self._game_service.get_game_board
        self.assertIsInstance(board, Board)

        last_move = self._game_service.last_move
        self.assertEqual(last_move, [-1, -1])

    def test_setters(self):
        self._game_service.last_move = [3, 4]
        last_move = self._game_service.last_move
        self.assertEqual(last_move, [3, 4])

    def test_make_human_move(self):
        self._game_service.make_human_move(1)
        last_move = self._game_service.last_move
        self.assertEqual(last_move, [5, 1])

    def test_make_computer_move(self):
        self._game_service.make_computer_move()
        last_move = self._game_service.last_move
        row_coordinate_of_last_move = last_move[0]
        self.assertEqual(row_coordinate_of_last_move, 5)

    def test_is_game_won(self):
        # initial state of the game. of course the game is not yet won
        self.assertFalse(self._game_service.is_game_won())

        # enter the while loop that checks moves horizontally
        self._game_service.make_human_move(2)
        self._game_service.make_human_move(5)
        self._game_service.make_human_move(3)
        self._game_service.make_human_move(4)
        self.assertTrue(self._game_service.is_game_won())

        # enter the while loop that checks moves vertically
        self._game_service.make_human_move(3)
        self._game_service.make_human_move(3)
        self._game_service.make_human_move(3)
        self.assertTrue(self._game_service.is_game_won())

        # enter the while loop that checks moves diagonally to the left
        self._game_service.make_human_move(2)
        self._game_service.make_human_move(2)
        self._game_service.make_human_move(1)
        self._game_service.make_human_move(1)
        self._game_service.make_human_move(0)
        self.assertTrue(self._game_service.is_game_won())

        # enter the while loop that checks diagonally to the right
        self._game_service.make_human_move(4)
        self._game_service.make_human_move(4)
        self._game_service.make_human_move(5)
        self._game_service.make_human_move(6)
        self.assertTrue(self._game_service.is_game_won())

    def test_is_game_draw(self):
        self.assertFalse(self._game_service.is_game_draw())

        for i in range(42):
            self._game_service.make_computer_move()
        self.assertTrue(self._game_service.is_game_draw())

