import texttable


class Board:
    """
    Class that represents the 6 x 7 board of the game, in the form of a matrix.
    """
    def __init__(self):
        self._number_of_rows = 6
        self._number_of_columns = 7
        self._representation_of_data = [[None for column in range(self._number_of_columns)] for row in range(self._number_of_rows)]

    @property
    def number_of_rows(self):
        """
        Getter method for the number of rows.
        """
        return self._number_of_rows

    @property
    def number_of_columns(self):
        """
        Getter method for the number of columns.
        """
        return self._number_of_columns

    def slot_of_board(self, index_of_row, index_of_column):
        """
        Getter method for a single slot of the board.
        :param index_of_row: represents the coordinate of the row.
        :param index_of_column: represents the coordinate of the column.
        :return: the element that is to be found at the given coordinates.
        """
        return self._representation_of_data[index_of_row][index_of_column]

    def make_human_move(self, row_coordinate, column_coordinate):
        """
        The method makes a human move by placing on the board the symbol 'X' at the coordinates (row, column).
        """
        self._representation_of_data[row_coordinate][column_coordinate] = 'X'

    def make_computer_move(self, row_coordinate, column_coordinate):
        """
        The method makes a computer move by placing on the board the symbol '0' at the coordinates (row, column).
        """
        self._representation_of_data[row_coordinate][column_coordinate] = '0'

    def __str__(self):
        """
        The method 'converts' the internal representation of the board into a readable format that will be used for
        printing.
        It uses the module 'texttable' and creates a table with 7 columns and progressively adds the rows to the table.
        :return: the board in the form of a nice, readable table.
        """
        table = texttable.Texttable()
        table.header(['1', '2', '3', '4', '5', '6', '7'])
        for row in range(self.number_of_rows):
            row_data = []

            for index in self._representation_of_data[row]:
                if index is None:
                    row_data.append(' ')
                elif index == 'X' or index == '0':
                    row_data.append(index)
            table.add_row(row_data)

        return table.draw()
