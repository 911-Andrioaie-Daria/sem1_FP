from Domain.board import Board
from Service.game import GameService
from Service.strategy import SmartStrategy
from UI.console import UI
from Validators.move_validator import MoveValidator

game_board = Board()
move_validator = MoveValidator()
game_strategy = SmartStrategy()
game_service = GameService(game_board, move_validator, game_strategy)
console_UI = UI(game_service)

console_UI.start()