def is_solution(solution_array, list_of_numbers):
    """
    The function checks if an array is a solution to the problem.

    :param solution_array: the array containing a sequence of + and -
    :param list_of_numbers: the numbers for which the sequence of signs must give a positive result
    :return: True, if the array represents a solution, False, otherwise
    """

    # there must be as many signs as the total number of the numbers in the list - 1
    if len(solution_array) != len(list_of_numbers) - 1:
        return False

    # calculate the expression
    sum_of_numbers = list_of_numbers[0]
    for i in range(len(solution_array)):
        if solution_array[i] == '+':
            sum_of_numbers = sum_of_numbers + list_of_numbers[i+1]
        else:
            sum_of_numbers = sum_of_numbers - list_of_numbers[i+1]

    # evaluate the expression
    if sum_of_numbers > 0:
        return True


def to_string(solution_array, list_of_numbers):
    """
    The function converts a solution to a nice, readable string.

    :param solution_array: the sequence of pluses and minuses
    :param list_of_numbers: the sequence of numbers
    :return: a string having the format "a+b-c"
    """
    expression_string = ""
    for i in range(len(solution_array)):
        expression_string = expression_string + str(list_of_numbers[i]) + str(solution_array[i])

    expression_string = expression_string + str(list_of_numbers[-1])
    return expression_string
