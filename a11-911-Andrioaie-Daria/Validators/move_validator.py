class MoveException(Exception):
    """
    Exception class for all errors related to a move.
    """
    def __init__(self, exception_message):
        self.message = exception_message


class MoveValidator:
    """
    Class that validates a move.
    """
    @staticmethod
    def validate_move(row, column):
        """
        A move on the coordinates (row, column) is valid if the column number is within [0, 6] and if it is not already
        full.
        :param row: the row coordinate of the move
        :param column: the column coordinate of the move

        Raises a move exception if at least one of the requirements is not satisfied.
        """
        if column <= -1 or column >= 7:
            raise MoveException('The column choice must be an integer within 1 and 7')
        if row < 0:
            raise MoveException('The column you chose is already full. Try another one.')
