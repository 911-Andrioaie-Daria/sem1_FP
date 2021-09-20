from random import choice


class GameStrategy:

    def next_move(self, game):
        """
        Return the computer's next move
        """
        raise Exception('A subclass strategy is needed in order to implement computer play!')

"""
class SimpleStrategy(GameStrategy):
    
    Class that implements a simple level of difficulty for the human player.
    
    def next_move(self, game):
        
        The function computes the next move of the computer by searching for the first available spot in a column from
        left to right.
        
        column = 0
        available_row = game.find_available_slot_in_column(column)
        while available_row < 0:
            column += 1
            available_row = game.find_available_slot_in_column(column)

        game.last_move = [available_row, column]
        game.get_game_board.make_computer_move(available_row, column)


class RandomStrategy(GameStrategy):
    
    Class that implements a medium level of difficulty for the human player.
    
    def next_move(self, game):
        
        The function generates the next move of the computer by computing the whole set of moves that could be made and
        picking one randomly.
    
        available_moves = []
        for column in range(game.get_game_board.number_of_columns):
            row = game.find_available_slot_in_column(column)
            if row >= 0:
                available_moves.append((row, column))

        move_coordinates = choice(available_moves)
        row_coordinate = move_coordinates[0]
        column_coordinate = move_coordinates[1]

        game.last_move = [row_coordinate, column_coordinate]
        game.get_game_board.make_computer_move(row_coordinate, column_coordinate)
"""

class SmartStrategy(GameStrategy):
    """
    Class that implements a hard level of difficulty for the human player.
    """

    def next_move(self, game):
        """
        The function generates the next move of the computer by computing the whole set of moves that could be made and
        for each of these moves check if it can either win or block a winning move of the human player.
        If none of these cases is encountered, it makes a random move
        """
        # SMART WAY
        available_moves = []
        for column in range(game.get_game_board.number_of_columns):
            row = game.find_available_slot_in_column(column)
            if row >= 0:
                available_moves.append((row, column))

        # check if the computer can make a winning move
        for move in available_moves:
            row_coordinate = move[0]
            column_coordinate = move[1]
            if game.check_four_in_a_line(row_coordinate, column_coordinate, '0'):  # '0' is the symbol of the computer
                game.last_move = [row_coordinate, column_coordinate]
                game.get_game_board.make_computer_move(row_coordinate, column_coordinate)
                return

        # check if the computer can block a winning move of the human
        for move in available_moves:
            row_coordinate = move[0]
            column_coordinate = move[1]
            if game.check_four_in_a_line(row_coordinate, column_coordinate, 'X'):  # 'X' is the symbol of the human
                game.last_move = [row_coordinate, column_coordinate]
                game.get_game_board.make_computer_move(row_coordinate, column_coordinate)
                return

        # if you reach this line, make a random move
        random_move = choice(available_moves)
        row_coordinate = random_move[0]
        column_coordinate = random_move[1]

        game.last_move = [row_coordinate, column_coordinate]
        game.get_game_board.make_computer_move(row_coordinate, column_coordinate)