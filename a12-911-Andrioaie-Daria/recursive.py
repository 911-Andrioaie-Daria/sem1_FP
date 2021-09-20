from solution import is_solution, to_string


def recursive_backtracking(solutions, partial_solution, list_of_numbers):
    """
    The function uses the concept of backtracking to search the whole space of solutions, and keeps the found solutions
    in a list.
    :param solutions: the resulted solutions
    :param list_of_numbers: the list of numbers for which we want to determine all the possibilities to insert between
    them the operators + and – such that by evaluating the expression the result is positive.
    """

    signs = ['+', '-']

    partial_solution.append(0)

    if len(partial_solution) == len(list_of_numbers):  # the solution exceeds the number of elements and it's time to stop
        return

    for sign in signs:
        partial_solution[-1] = sign

        if is_solution(partial_solution, list_of_numbers):
            printable_solution = to_string(partial_solution, list_of_numbers)
            solutions.append(printable_solution)

        # go the the next element of the solution
        recursive_backtracking(solutions, partial_solution, list_of_numbers)
        partial_solution.pop()

