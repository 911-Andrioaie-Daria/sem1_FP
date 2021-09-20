from solution import is_solution, to_string


def find_successor(partial_solution):
    """
    The function finds the successor of the last element in the list.
    By "successor" of an element we mean the next element in the list [0, +, -].

    :param partial_solution: array containing the current partial solution
    :return: True, if the last element has a successor, False, otherwise
    """
    if partial_solution[-1] == 0:
        partial_solution[-1] = '+'
        return True

    elif partial_solution[-1] == '+':
        partial_solution[-1] = '-'
        return True

    return False


def iterative_backtracking(list_of_numbers):
    """
    The function uses the concept of backtracking to search the whole space of solutions, and keeps the found solutions
    in a list that will be returned.

    :param list_of_numbers: the list of numbers for which we want to determine all the possibilities to insert between
    them the operators + and – such that by evaluating the expression the result is positive.
    :return: the resulted solutions
    """
    list_of_solutions = []
    partial_solution = [0]

    while len(partial_solution):

        current_element_has_successor = find_successor(partial_solution)

        if current_element_has_successor:
            if is_solution(partial_solution, list_of_numbers):
                printable_solution = to_string(partial_solution, list_of_numbers)
                list_of_solutions.append(printable_solution)

            elif len(partial_solution) == len(list_of_numbers) - 1:       # the solution array is full, but does not
                                                                          # represent a solution
                partial_solution.pop()
            else:
                partial_solution.append(0)                                # go to the next element in order to complete
                                                                          # the solution
        else:
            # go back with one step in the partial solution
            partial_solution.pop()

    return list_of_solutions
