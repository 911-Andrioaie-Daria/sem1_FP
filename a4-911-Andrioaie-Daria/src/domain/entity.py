"""
Domain file includes code for entity management
entity = number, transaction, expense etc.
"""
import copy
import math


def truncate(number, decimals=0):
    """
    Returns a value truncated to a specific number of decimal places.
    Uses the math.trunc function
    :param number: the float number that is being truncated
    :param decimals: the number of decimals that we want to keep in the number. Must be an integer
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor


def calculate_average(number1, number2, number3):
    """
    Calculates the float average between 3 integer numbers
    :param number1: integer number
    :param number2: integer number
    :param number3: integer number
    :return: float average
    """

    average = (number1+number2+number3)/3.0
    return truncate(average, 2)


def create_participant(problem1_score, problem2_score, problem3_score):
    """
    Creates a dictionary containing the three scores as integers and the average score
    :param problem1_score: integer in [1, 10]
    :param problem2_score: integer in [1, 10]
    :param problem3_score: integer in [1, 10]
    :return: the dictionary participant
    """

    if int(problem1_score) < 0 or int(problem1_score) > 10:
        raise ValueError('The scores must be integers in [0, 10]')
    if int(problem2_score) < 0 or int(problem2_score) > 10:
        raise ValueError('The scores must be integers in [0, 10]')
    if int(problem3_score) < 0 or int(problem3_score) > 10:
        raise ValueError('The scores must be integers in [0, 10]')

    average_score = calculate_average(problem1_score, problem2_score, problem3_score)
    participant = {'problem1_score': problem1_score, 'problem2_score': problem2_score, 'problem3_score': problem3_score,
                   'average': average_score}

    return participant


def test_init(test_list):
    """
    Adds ten new participants to the list
    """

    test_list.append(create_participant(9, 7, 6))
    test_list.append(create_participant(9, 2, 9))
    test_list.append(create_participant(1, 4, 7))
    test_list.append(create_participant(7, 2, 5))
    test_list.append(create_participant(10, 7, 7))
    test_list.append(create_participant(9, 8, 3))
    test_list.append(create_participant(6, 10, 9))
    test_list.append(create_participant(9, 9, 5))
    test_list.append(create_participant(9, 8, 6))
    test_list.append(create_participant(3, 5, 6))


def initialise_participants_dictionary():
    """
    Initialises a storage entity for the list of participants as a dictionary containing history_list and current list
    history_list is a list containing all the previous lists after each modification
    current_list is the list of participants in its current form
    """

    participants_dictionary = {'history_list': [], 'current_list': []}
    test_init(participants_dictionary['current_list'])

    return participants_dictionary


def get_current_list(participants_storage):
    """
    Returns the list of participants at the current moment
    :param participants_storage: a dictionary containing the history_list and the current_list
    """
    return participants_storage['current_list']


def get_history_list(participants_storage):
    """
    Returns the history list containing all the previous lists of participants
    :param participants_storage: a dictionary containing the history_list and the current_list
    """

    auxiliary_list = list(participants_storage['history_list'])
    return auxiliary_list
    # return participants['history_list']


def set_history_list_to(new_list, participants_storage):
    """
    Updates the history list with another list
    :param new_list: the list that the history list is set to
    :param participants_storage: a dictionary containing the history_list and the current_list
    """

    participants_storage['history_list'] = list(new_list)


def add_current_list_to_history(participants_storage):
    """
    Adds the current list of participants to the history of lists
    :param participants_storage: a dictionary containing the history_list and the current_list
    """

    history = get_history_list(participants_storage)
    current_list = get_current_list(participants_storage)
    
    auxiliary_list = list(current_list)
    history.append(copy.deepcopy(auxiliary_list))
    # history.append(current_list)
    set_history_list_to(history, participants_storage)


def set_current_list_to(new_list, participants_storage):
    """
    Sets the currents list of participants to a new list
    :param new_list: the list that the current list is set to
    :param participants_storage: a dictionary containing the history_list and the current_list
    """

    participants_storage['current_list'] = list(new_list)


def get_previous_list_from_history(participants_storage):
    """
    Returns the last list in the history of lists.
    :param participants_storage: a dictionary containing the history_list and the current_list
    """
    history_list = get_history_list(participants_storage)
    return history_list[-1]


def remove_last_list_from_history(participants_storage):
    """
    Removes the last list from the history of lists
    :param participants_storage: a dictionary containing the history_list and the current_list
    """

    history_list = get_history_list(participants_storage)
    del history_list[-1]
    set_history_list_to(history_list, participants_storage)


def get_score1(participant):
    """
    Returns participant's score of P1
    :param participant: the participant
    :return: score of P1
    """
    return participant['problem1_score']


def get_score2(participant):
    """
    Returns participant's score of P2
    :param participant: the participant
    :return: score of P2
    """
    return participant['problem2_score']


def get_score3(participant):
    """
    Returns participant's score of P3
    :param participant: the participant
    :return: score of P3
    """
    return participant['problem3_score']


def get_average_score(participant):
    """
    Returns participant's score of P1
    :param participant: the participant
    :return: score of P1
    """
    return participant['average']


def set_score1(participant, value_as_int):
    """
    Sets the score of problem1 of participant to a given integer value
    :param participant: the participant whose score is updated
    :param value_as_int: the value to be set
    """
    participant['problem1_score'] = int(value_as_int)

    # now the average score has changed as well, so we have to update it
    score1 = get_score1(participant)
    score2 = get_score2(participant)
    score3 = get_score3(participant)

    set_average_score(participant, calculate_average(score1, score2, score3))


def set_score2(participant, value_as_int):
    """
    Sets the score of problem2 of a participant to a given integer value
    :param participant: the participant whose score is updated
    :param value_as_int: the value to be set
    """
    participant['problem2_score'] = int(value_as_int)

    # now the average score has changed as well, so we have to update it
    score1 = get_score1(participant)
    score2 = get_score2(participant)
    score3 = get_score3(participant)

    set_average_score(participant, calculate_average(score1, score2, score3))


def set_score3(participant, value_as_int):
    """
    Sets the score of problem 3 of a participant to a given integer value
    :param participant: the participant whose score is updated
    :param value_as_int: the value to be set
    """
    participant['problem3_score'] = int(value_as_int)

    # now the average score has changed as well, so we have to update it
    score1 = get_score1(participant)
    score2 = get_score2(participant)
    score3 = get_score3(participant)

    set_average_score(participant, calculate_average(score1, score2, score3))


def set_average_score(participant, value_as_float):
    """
    Sets the average score of a participant to a given integer value
    :param participant: the participant whose score is updated
    :param value_as_float: the value to be set
    """
    participant['average'] = value_as_float


def set_all_scores_to(participant, value_as_int):
    """
    Sets all the scores of a participant (problem1_score, problem2_score, problem3_score, average) to a given integer
    :param participant: the participant whose scores are updated
    :param value_as_int: the value that all scores are changed to. must be integer in [0, 10]
    """

    set_score1(participant, value_as_int)
    set_score2(participant, value_as_int)
    set_score3(participant, value_as_int)
    set_average_score(participant, value_as_int)


def to_string(participant):
    """
    Converts the participant entity into a readable string,
    having the format <p1_score> <p2_score> <p3_score> Average score: <average>
    :return: a string with all participant data
    """
    return str(get_score1(participant)) + ' '+str(get_score2(participant)) + ' '+str(get_score3(participant)) + '  Average score: ' + str(get_average_score(participant))
