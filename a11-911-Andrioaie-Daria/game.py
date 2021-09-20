class GameService:
    """
    The GameService class represents the service of the game with all its functionalities.
    Has a board instance, a move validator and the coordinates of the last move that was made.
    """
    def __init__(self, board, move_validator, game_strategy):
        self._board = board
        self._move_validator = move_validator
        self._strategy = game_strategy
        self._last_move = [-1, -1]     # list having two elements: the row coordinate and the column coordinate of move.

    @property
    def get_game_board(self):
        """
        Getter method for the board of the game.
        """
        return self._board


    @property
    def last_move(self):
        """
        Getter method for the coordinates of the last move on the board.
        """
        return self._last_move

    @last_move.setter
    def last_move(self, new_coordinates):
        """
        Setter method used for updating the coordinates of the last move that was made on the board.
        :param new_coordinates: list having two elements: the row coordinate and the column coordinate of the new move.
        """
        self._last_move = new_coordinates

    def make_human_move(self, users_choice_of_column):
        """
        The method finds the next available row on the given column, checks if the move at the computed position is
        valid, and if it is, it saves the coordinates of this move and passes them to the board in order to perform the
        actual move.
        :param users_choice_of_column: the column coordinate at which the user wants to place his next move.
        """
        # find the row that is available on the chosen column
        available_row = self.find_available_slot_in_column(users_choice_of_column)

        # check that the move at such coordinates is valid (the column number is in [0, 6] and the column is not already
        # full
        self._move_validator.validate_move(available_row, users_choice_of_column)

        # if the above line does not raise an error, it means that the move is valid and we have to save its coordinates
        self.last_move = [available_row, users_choice_of_column]

        # pass the coordinates to the board to make the actual move (update the internal state of the board)
        self.get_game_board.make_human_move(available_row, users_choice_of_column)

    def make_computer_move(self):
        """
        The method calls a method from the strategy in order to make a computer move
        """
        return self._strategy.next_move(self)

    def check_four_vertically(self, current_row, current_column, player_symbol):
        """
        The method checks if the last move on the board generated a vertical line of four of the same symbols
        :param current_row: the row coordinate of the last move
        :param current_column: the column coordinate of the last move
        :param player_symbol: this basically tells us who made the last move
        :return: the winner, if there is a vertical line of four symbols. None, otherwise.
        """
        same_symbol_counter = 1     # we start from the position of the last move and go vertically down, counting how
        # many symbols we found within the bounds of the board

        below_row = current_row + 1
        while below_row < 6 and same_symbol_counter < 4:
            if self.get_game_board.slot_of_board(below_row, current_column) == player_symbol:
                same_symbol_counter += 1
                below_row += 1
            else:
                break

        if same_symbol_counter == 4:   # if we found a line of four, we return the symbol of the last move
            return player_symbol

    def check_four_horizontally(self, current_row, current_column, player_symbol):
        """
        The method checks if the last move on the board generated a horizontal line of four of the same symbols, and it
        does this by counting how many symbols we have to the left of the last move and then to the right
        :param current_row: the row coordinate of the last move
        :param current_column: the column coordinate of the last move
        :param player_symbol: this basically tells us who made the last move
        :return: the winner, if there is a horizontal line of four symbols. None, otherwise.
        """
        same_symbol_counter = 1

        # count how many symbols there are to the left, within the bounds of the board
        left_column = current_column - 1
        while left_column >= 0 and same_symbol_counter < 4:
            if self.get_game_board.slot_of_board(current_row, left_column) == player_symbol:
                same_symbol_counter += 1
                left_column -= 1
            else:
                break

        # now count in the same way to the right
        if same_symbol_counter < 4:
            right_column = current_column + 1
            while right_column <= 6 and same_symbol_counter < 4:
                if self.get_game_board.slot_of_board(current_row, right_column) == player_symbol:
                    same_symbol_counter += 1
                    right_column += 1
                else:
                    break

        if same_symbol_counter == 4:    # if we found a line of four, we return the symbol of the last move
            return player_symbol

    def check_four_diagonally_to_the_left(self, current_row, current_column, player_symbol):
        """
        The method checks if the last move on the board generated a diagonal left-oriented line of four of the same
        symbols, and it does this by counting how many symbols we have going down and to the left and then going up and
        to the right of the last move.
        :param current_row: the row coordinate of the last move
        :param current_column: the column coordinate of the last move
        :param player_symbol: this basically tells us who made the last move
        :return: the winner, if there is a diagonal line of four symbols. None, otherwise.
        """
        # count how many symbols there are bottom-left, within the bounds of the board
        left_column = current_column - 1
        below_row = current_row + 1
        same_symbol_counter = 1

        while same_symbol_counter < 4 and left_column >= 0 and below_row <= 5:
            if self.get_game_board.slot_of_board(below_row, left_column) == player_symbol:
                same_symbol_counter += 1
                below_row += 1
                left_column -= 1
            else:
                break

        # now count the same way to the upper-right
        if same_symbol_counter < 4:
            right_column = current_column + 1
            above_row = current_row - 1
            while same_symbol_counter < 4 and right_column <= 6 and above_row >= 0:
                if self.get_game_board.slot_of_board(above_row, right_column) == player_symbol:
                    same_symbol_counter += 1
                    above_row -= 1
                    right_column += 1
                else:
                    break

        if same_symbol_counter == 4:
            return player_symbol

    def check_four_diagonally_to_the_right(self, current_row, current_column, player_symbol):
        """
        The method checks if the last move on the board generated a diagonal right-oriented line of four of the same
        symbols, and it does this by counting how many symbols we have going down and to the right and then going up and
        to the left of the last move.
        :param current_row: the row coordinate of the last move
        :param current_column: the column coordinate of the last move
        :param player_symbol: this basically tells us who made the last move
        :return: the winner, if there is a diagonal line of four symbols. None, otherwise.
        """
        # count how many symbols there are bottom-right, within the bounds of the board
        right_column = current_column + 1
        below_row = current_row + 1
        same_symbol_counter = 1

        while same_symbol_counter < 4 and right_column <= 6 and below_row <= 5:
            if self.get_game_board.slot_of_board(below_row, right_column) == player_symbol:
                same_symbol_counter += 1
                below_row += 1
                right_column += 1
            else:
                break

        # now count the same way to the upper-left
        if same_symbol_counter < 4:
            left_column = current_column - 1
            above_row = current_row - 1
            while same_symbol_counter < 4 and left_column >= 0 and above_row >= 0:
                if self.get_game_board.slot_of_board(above_row, left_column) == player_symbol:
                    same_symbol_counter += 1
                    above_row -= 1
                    left_column -= 1
                else:
                    break

        if same_symbol_counter == 4:
            return player_symbol

    def check_four_in_a_line(self, current_row, current_column, player_symbol):
        """
        The method checks if around a given position there exists a line of four symbols the same as the one given as a
        parameter, including the one on the current position.
        :param current_row: the row coordinate of the given position
        :param current_column: the column coordinate of the position
        :param player_symbol: a symbol of one of the players
        :return: the symbol of the player who formed four in a line or False, if there is no line of 4
        """

        # check on the diagonal to the left
        if self.check_four_diagonally_to_the_left(current_row, current_column, player_symbol) is not None:
            return player_symbol

        # check on the diagonal to the right
        if self.check_four_diagonally_to_the_right(current_row, current_column, player_symbol) is not None:
            return player_symbol

        # check horizontally
        if self.check_four_horizontally(current_row, current_column, player_symbol) is not None:
            return player_symbol

        # check vertically going down
        if self.check_four_vertically(current_row, current_column, player_symbol) is not None:
            return player_symbol

        return False

    def is_game_won(self):
        """
        The method checks if the game was won by checking if the last move generated a line of four symbols either
        horizontally, vertically or diagonally (both to the eft and to the right)
        :return: if one of the above cases is satisfied, it returns the symbol of the last move (the winner). if not,
        returns false.
        """
        row_of_last_move = self.last_move[0]
        column_of_last_move = self.last_move[1]

        # the start of the game, when the last move is initialized with [-1, -1]
        if row_of_last_move == -1 and column_of_last_move == -1:
            return False

        last_move_symbol = self.get_game_board.slot_of_board(row_of_last_move, column_of_last_move)

        return self.check_four_in_a_line(row_of_last_move, column_of_last_move, last_move_symbol)

    def is_game_draw(self):
        """
        The method checks if the game is draw, meaning that there are no more available moves to be made (all the 7
        columns are full)
        :return: True, if all columns are full. False, otherwise
        """
        for column in range(7):
            # if there is at least one column on which we can still place moves, the game can still continue
            if self.find_available_slot_in_column(column) >= 0:
                return False

        # if all columns are full, the game is draw
        return True

    def find_available_slot_in_column(self, column):
        """
        The method computes the next available spot in a column from bottom to top i.e. the lowest row in the column that
        is not yet occupied.
        """
        bottom = 5

        # the while loop stops when a free row is found or when we reached the top of the column and there are no moves
        # available on that column
        while self.get_game_board.slot_of_board(bottom, column) is not None and bottom != -1:
            bottom = bottom - 1

        return bottom
