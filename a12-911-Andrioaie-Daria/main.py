from random import randint
from recursive import recursive_backtracking
from iterative import iterative_backtracking


def print_iterative_solutions(list_of_numbers):
    """
    The function calls the function that solves the problem iteratively and then prints all the found solutions.

    :param list_of_numbers: the list of numbers for which we want to determine all the possibilities to insert between
    them the operators + and – such that by evaluating the expression the result is positive.
    """
    list_of_solutions = iterative_backtracking(list_of_numbers)

    number_of_solutions = len(list_of_solutions)
    if number_of_solutions == 0:
        print('There are no solutions for the given set of numbers')
    else:

        for solution in list_of_solutions:
            print(solution)
        print(str(number_of_solutions) + ' SOLUTIONS: ')
        print('\n')

    print('\n')


def print_recursive_solutions(list_of_numbers):
    """
    The function calls the function that solves the problem recursively and then prints all the found solutions.

    :param list_of_numbers: the list of numbers for which we want to determine all the possibilities to insert between
    them the operators + and – such that by evaluating the expression the result is positive.
    """
    list_of_solutions = []
    recursive_backtracking(list_of_solutions, [], list_of_numbers)

    number_of_solutions = len(list_of_solutions)
    if number_of_solutions == 0:
        print('There are no solutions for the given set of numbers')
    else:
        for solution in list_of_solutions:
            print(solution)
        print(str(number_of_solutions) + ' SOLUTIONS: ')
        print('\n')

    print('\n')


def initialise_numbers(number_of_elements):
    """
    The function computes a random sequence of natural number.

    :param number_of_elements: the total number of elements in the sequence
    :return: the sequence of numbers, represented as a list
    """
    list_of_numbers = []
    for iteration in range(number_of_elements):
        natural_number = randint(1, 100)
        list_of_numbers.append(natural_number)

    return list_of_numbers


def print_menu():
    print('1. Solve recursively.')
    print('2. Solve iteratively')
    print('3. Exit.')
    print('\n')


def start():

    available_options = {'1': print_recursive_solutions, '2': print_iterative_solutions}
    number_of_elements = int(input('Enter a natural number greater than 9: '))
    list_of_numbers = initialise_numbers(number_of_elements)

    not_finished = True
    while not_finished:

        print_menu()
        user_option = input('Enter option: ')

        if user_option in available_options:
            available_options[user_option](list_of_numbers)

        elif user_option == '3':
            not_finished = False
        else:
            print('Bad command')


start()
