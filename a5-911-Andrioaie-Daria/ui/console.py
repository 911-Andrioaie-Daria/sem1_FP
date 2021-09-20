"""
    This module implements the UI class.
"""
from src.domain.entity import ComplexNumber
from src.services.service import generate_10_entries, ComplexNumbersStorage

"""
1. Complex numbers
Manage a list of complex numbers in a+bi form and provide the user the following features:

    -> Add a number. The number is read from the console.
    -> Display the list of numbers. 
    -> Filter the list so that it contains only the numbers between indices start and end,
       where these values are read from the console.
    ->Undo the last operation that modified program data. This step can be repeated.
"""


def print_menu():
    """
    Prints all the options available to the user.
    """
    print('Hello :)')
    print('These are your available options:')
    print('     1: Add a new number to the list')
    print('     2: Display your list of numbers')
    print('     3: Filter the list so that it contains only the numbers between two indices.')
    print('     4: Undo the last operation that modified the list')
    print('     5. Exit')
    print('\n')


class UI:
    """
    The UI class
    """

    def __init__(self):
        """
        The constructor generates a list of 10 random entries and initialises the storage of complex numbers
        """

        default_list = generate_10_entries()
        self.numbers_storage = ComplexNumbersStorage(default_list)

    def read_new_number(self):
        """
        Reads the real part and the imaginary part of a new complex number
        :return: the complex number having these real and imaginary parts
        """

        real_part = input('Enter the real part of your number: ')
        imaginary_part = input('Enter the imaginary part of your number: ')

        return ComplexNumber(real_part, imaginary_part)

    def add_number_ui(self):
        """
        Reads a new complex number from the console and calls the non-ui function that implements the addition
        of this number to the current list of numbers.
        """
        # read new number
        new_number = self.read_new_number()

        # perform the actual addition
        self.numbers_storage.add_number(new_number)
        print("Successfully added number.")
        print('\n')

    def display_numbers_ui(self):
        """
        If the current list of numbers is non-empty, it displays the numbers of this list. Otherwise, it prints
        a message for the user.
        """

        # the case in which the the history list is empty
        if len(self.numbers_storage) == 0:
            print('The list is empty. Try adding some numbers first')

        # the case in which it is non-empty
        else:
            for i in self.numbers_storage.current_list:
                print(i)
        print('\n')

    def filter_list_between_two_indices_ui(self):
        """
        Reads two indices, start and end position and calls the function that filters the current list so that
        it only contains the numbers situated between indices start and end.
        """

        # read the input data from the user
        start_position = int(input('Enter the starting position: '))
        end_position = int(input('Enter the ending position: '))

        # both the start and the end position must be within the length of the current list
        if start_position < 0 or start_position >= len(self.numbers_storage):
            raise ValueError(' The two indices must be within the length of the current list. Try again')

        if end_position < 0 or end_position >= len(self.numbers_storage):
            raise ValueError(' The two indices must be within the length of the current list. Try again')

        # The start indices must be smaller or equal than the end indices
        if start_position > end_position:
            raise ValueError(' The start indices must be smaller or equal than the end indices. Try again')

        self.numbers_storage.filter_list_between(start_position, end_position)

        print('Successfully filtered the list')
        print('\n')

    def undo_last_operation_ui(self):
        """
        Undoes the last operation that modified the current list of numbers.
        There must be previous versions of the current list in history in order to perform the undo.
        """

        if len(self.numbers_storage.history_of_lists) > 0:
            self.numbers_storage.undo_last_operation()
            print('Successfully undone')
        else:
            print('Undo is not available at the moment. Try making some changes to your list first')
        print('\n')

    def start(self):
        """
        Start of the UI is here.
        """
        print_menu()
        menu_dictionary = {'1': self.add_number_ui, '2': self.display_numbers_ui,
                           '3': self.filter_list_between_two_indices_ui, '4': self.undo_last_operation_ui}

        not_finished = True

        while not_finished:

            user_option = input('Please enter your choice: ')

            # one of the options 'add', 'display', 'filter' or 'undo'
            if user_option in menu_dictionary:
                try:
                    menu_dictionary[user_option]()
                except ValueError as ve:
                    print(str(ve))

            # the 'exit' option. The program stops when the user chooses this option
            elif user_option == '5':
                print('Bye, bye! :)')
                not_finished = False

            # any user option that is not valid
            else:
                print('You might want to try again')


MyComplexNumbers = UI()
MyComplexNumbers.start()
