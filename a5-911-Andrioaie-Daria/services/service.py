
import copy

from random import uniform

from src.domain.entity import ComplexNumber


class ComplexNumbersStorage:
    """
    Represents the storage of complex numbers, keeping both the current list and the history list of all previous
    versions of the list.
    """

    def __init__(self, initial_list):
        """
        Initialises the storage of numbers, having a current list and an empty history of lists.
        :param initial_list: the initial list of numbers, which is generated randomly
        """

        self._current_list_of_numbers = list(initial_list)
        self._history_of_lists = []

    @property
    def current_list(self):
        """
        The 'getter' of the current list in the storage of numbers
        """
        return self._current_list_of_numbers

    @property
    def history_of_lists(self):
        """
        The 'getter of the history list in the storage'
        """
        return self._history_of_lists

    @current_list.setter
    def current_list(self, new_list):
        """
        Sets the current list in the storage to a new list
        """

        self._current_list_of_numbers = copy.deepcopy(new_list)

    # should I keep this if it is not actually used?
    '''
    @history_of_lists.setter
    def history_of_lists(self, new_list):
        """
        Sets the history list in the storage to a new list
        """
        self._history_of_lists = copy.deepcopy(new_list)
    '''

    def move_current_to_history(self):
        """
        Saves a copy of the current list of numbers in the history
        """
        # copy the current list in an auxiliary one
        auxiliary_list = copy.deepcopy(self.current_list)

        # append the list at the end of the history
        self.history_of_lists.append(auxiliary_list)

    def __len__(self):
        """
        Returns the length of the current list of numbers in the storage
        """

        return len(self.current_list)

    def add_number(self, new_number):
        """
        Saves a copy of the current list in history and then
        adds a new number to the current list of numbers in the storage.
        :param new_number: the complex number to be added
        """

        # save the current version of the list
        self.move_current_to_history()

        # append the new number to the list
        self.current_list.append(new_number)

    def undo_last_operation(self):
        """
        Undoes the last operation by restoring the previous list in the current list, and removing this previous list
        fromm the history
        """

        previous_list = self._history_of_lists.pop()
        self.current_list = copy.deepcopy(previous_list)

    def filter_list_between(self, start_position,  end_position):
        """
        Filters the current list so that it only contains the numbers situated between the start position and
        the end position
        :param start_position: the beginning of the interval that is filtered
        :param end_position: the end of the interval
        """

        # save a copy if the current list
        self.move_current_to_history()
        current_length_of_list = len(self)

        # pop the first <start_position> elements from the list
        for i in range(0, start_position):
            self.current_list.pop(0)

        # pop the last elements from the list.
        for i in range(0, current_length_of_list-end_position-1):
            self.current_list.pop()


def generate_10_entries():
    """
    Randomly generates a list of 10 valid complex numbers
    :return: the generated list
    """

    list_of_numbers = []
    for i in range(0, 10):

        # generate a float number in the range [-100, 100] and round this to have only two decimal places
        real_part = uniform(-100.0, 100.0)
        real_part = round(real_part, 2)

        # the imaginary part is generated in the same way as the real part
        imaginary_part = uniform(-100.0, 100.0)
        imaginary_part = round(imaginary_part, 2)

        # create a complex number having the generated parts
        number = ComplexNumber(real_part, imaginary_part)

        # append the number to the list
        list_of_numbers.append(number)

    return list_of_numbers


def test_move_current_to_history():
    """
    Test for the move_current_to_history method
    """
    my_numbers = ComplexNumbersStorage([0, 1, 2])
    my_numbers.move_current_to_history()
    assert len(my_numbers.history_of_lists) == 1

    my_numbers.add_number(7)
    my_numbers.move_current_to_history()
    assert len(my_numbers.history_of_lists) == 2


def test_add_number():
    """
    Test for the add_number method
    """
    my_numbers = ComplexNumbersStorage([0, 1, 2])
    my_numbers.add_number(6)
    assert my_numbers.current_list == [0, 1, 2, 6]


def test_filter_list_between():
    """
    Test for the filter_list_between method
    """
    my_numbers = ComplexNumbersStorage([0, 1, 2, 3, 5])
    my_numbers.filter_list_between(1, 3)
    assert my_numbers.current_list == [1, 2, 3]


def test_undo_last_operation():
    """
    Test for the undo_last_operation method
    """
    my_numbers = ComplexNumbersStorage([0, 1, 2, 3, 5])
    my_numbers.add_number(75)
    my_numbers.filter_list_between(4, 5)

    my_numbers.undo_last_operation()
    assert my_numbers.current_list == [0, 1, 2, 3, 5, 75]

    my_numbers.undo_last_operation()
    assert my_numbers.current_list == [0, 1, 2, 3, 5]
