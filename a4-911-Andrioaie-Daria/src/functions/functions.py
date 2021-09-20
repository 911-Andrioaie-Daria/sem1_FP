"""
Functions that implement program features. They should call each other, or other functions from the domain
"""
from src.domain.entity import set_all_scores_to, set_score1, set_score2, set_score3, create_participant, get_score1, \
    get_score2, get_score3, get_average_score, truncate, add_current_list_to_history, get_current_list, \
    set_current_list_to, remove_last_list_from_history, get_previous_list_from_history


def add_participant(participants_storage, participant):
    """
    Adds a new participant to the current list of participants
    :param participants_storage: a dictionary containing the history_list and the current_list
    :param participant: the new participant to be added
    """

    # save the last version of the list, by moving it to history
    add_current_list_to_history(participants_storage)

    # modify the list by appending a new participant
    participant_list = get_current_list(participants_storage)
    participant_list.append(participant)

    # update the current list of participants with the modified list
    set_current_list_to(participant_list, participants_storage)


def remove_participant_at_position(position, participants_storage):
    """
    Sets to 0 the scores obtained by the participant at the given position
    :param participants_storage: a dictionary containing the history_list and the current_list
    :param position: the given position
    """

    participant_list = get_current_list(participants_storage)

    # the position of removal must be an integer within the length of the current list of participants
    position = int(position)
    if position < 0 or position >= len(participant_list):
        raise ValueError('The is no such position in the list. The position must be between 0 and ' +
                         str(len(participant_list)-1))

    # move the last list to history
    add_current_list_to_history(participants_storage)

    # modify the current list and update in in the participants storage
    set_all_scores_to(participant_list[position], 0)
    set_current_list_to(participant_list, participants_storage)


def remove_from_start_position_to_end_position(start_position, end_position, participants_storage):
    """
    Sets to 0 the scores of all participants in the list between <start_position> to <end position>

    :param start_position: the first position to set to 0. Must be an integer
    :param end_position: the last position to set to 0. Must be an integer
    :param participants_storage: a dictionary containing the history_list and the current_list
    """

    participant_list = get_current_list(participants_storage)

    # both positions must be integers
    start_position = int(start_position)
    end_position = int(end_position)

    # both positions must be within the length of the current list of participants
    if start_position < 0 or start_position >= len(participant_list):
        raise ValueError('The is no such start position in the list. The position must be between 0 and ' +
                         str(len(participant_list)-1))
    if end_position < 0 or end_position >= len(participant_list):
        raise ValueError('The is no such end position in the list. The position must be between 0 and ' +
                         str(len(participant_list) - 1))

    # the start position must be smaller than the end position
    if start_position > end_position:
        raise ValueError('The start position must be smaller than or equal to the end position.')

    # make a copy of the current list by moving it to history
    add_current_list_to_history(participants_storage)

    # modify the current list and update it in the storage of participants
    for i in range(start_position, end_position+1):
        set_all_scores_to(participant_list[i], 0)
    set_current_list_to(participant_list, participants_storage)


def remove_by_average_score(relational_operator, comparing_number, participants_storage):
    """
    Participants whose average score are greater, equal-to or smaller than the comparing_number are set to 0

    :param relational_operator: can be either '<', '=', '>'
    :param comparing_number: the number that average scores are being compared to
    :param participants_storage: a dictionary containing the history of lists and the current_list
    """

    comparing_number = float(comparing_number)
    participant_list = get_current_list(participants_storage)

    check = False

    if relational_operator == '<':
        for participant in participant_list:
            if get_average_score(participant) < comparing_number:
                check = True
                set_all_scores_to(participant, 0)

    if relational_operator == '=':
        for participant in participant_list:
            if get_average_score(participant) == comparing_number:
                check = True
                set_all_scores_to(participant, 0)

    if relational_operator == '>':
        for participant in participant_list:
            if get_average_score(participant) > comparing_number:
                check = True
                set_all_scores_to(participant, 0)

    if not check:
        raise ValueError('There are no participants to be removed')

    else:
        # make a copy of the last list by moving it to history and update the current list in the participants storage
        add_current_list_to_history(participants_storage)
        set_current_list_to(participant_list, participants_storage)


def calculate_average_between(start_position, end_position, current_participant_list):
    """
    Calculates the average of the average scores for participants between the start position and the end position
    in the current list of participants

    :param start_position: the start of the interval of positions whose average is calculated
    :param end_position: the end of the interval of positions whose average is calculated
    :param current_participant_list: the current list of participants
    """

    # both positions must be an integer
    start_position = int(start_position)
    end_position = int(end_position)

    # both positions must be within the length of the current list of participants
    if start_position < 0 or start_position >= len(current_participant_list):
        raise ValueError('The is no such start position in the list. The position must be between 0 and ' + str(
            len(current_participant_list) - 1))
    if end_position < 0 or end_position >= len(current_participant_list):
        raise ValueError('The is no such end position in the list. The position must be between 0 and ' + str(
            len(current_participant_list) - 1))

    # the start position must not be greater than the end_position
    if start_position > end_position:
        raise ValueError('The start position must be smaller than or equal to the end position.')

    # calculate the average score of participants within the given interval
    sum_of_averages = 0
    number_of_participants_within_the_interval = end_position - start_position + 1

    for i in range(start_position, end_position+1):
        sum_of_averages = sum_of_averages + get_average_score(current_participant_list[i])
    average = sum_of_averages/number_of_participants_within_the_interval

    return truncate(average, 2)


def calculate_minimum_between(start_position, end_position, current_participant_list):
    """
    Calculates the minimum average score of participants between the start_position and end_position
    in the current list of participants

    :param start_position: the start of the interval of positions whose average is calculated
    :param end_position: the end of the interval of positions whose average is calculated
    :param current_participant_list: the current list of participants
    """

    # both positions must be an integer
    start_position = int(start_position)
    end_position = int(end_position)

    # both positions must be within the length of the current list of participants
    if start_position < 0 or start_position >= len(current_participant_list):
        raise ValueError('The is no such start position in the list. The position must be between 0 and ' + str(
            len(current_participant_list) - 1))
    if end_position < 0 or end_position >= len(current_participant_list):
        raise ValueError('The is no such end position in the list. The position must be between 0 and ' + str(
            len(current_participant_list) - 1))

    # the start position must not be greater than the end_position
    if start_position > end_position:
        raise ValueError('The start position must be smaller than or equal to the end position.')

    # calculate the minimum average score of participants within the given interval
    minimum_average = 10

    for i in range(start_position, end_position+1):

        current_participant_average = get_average_score(current_participant_list[i])
        if current_participant_average < minimum_average:
            minimum_average = current_participant_average

    return minimum_average


def replace_old_score_with_new_score(participants_storage, position, problem, new_score):
    """
    Replaces the score obtained at one of the problems by the participant at position <position> with a new_score

    :param participants_storage: a dictionary containing the history_list and the current_list
    :param position: the position of the participant -> integer within the length of the current list of participants
    :param problem: to problem whose score must be replaced  -> string: 'P1' or 'P2' or 'P3'
    :param new_score: must be integer in [0, 10]
    """

    participant_list = get_current_list(participants_storage)

    # the position must be an integer within the current list of participants
    position = int(position)
    if position < 0 or position >= len(participant_list):
        raise ValueError('The is no such position in the list. The position must be between 0 and ' +
                         str(len(participant_list)-1))

    # the score must be an integer in [0, 10]
    new_score = int(new_score)
    if new_score < 0 or new_score > 10:
        raise ValueError('The scores must be in [0, 10]')

    problem_dict = {'P1': set_score1, 'P2': set_score2, 'P3': set_score3}

    # the problem must be either 'P1', 'P2' or 'P3'
    if problem in problem_dict:

        # make a copy of the last list by moving it to history
        add_current_list_to_history(participants_storage)

        # modify the current list of participants accordingly
        problem_dict[problem](participant_list[position], new_score)

        # update the current list in the storage of participants
        set_current_list_to(participant_list, participants_storage)
    else:
        raise ValueError('Invalid problem parameter. The problem must be either P1, P2 or P3')


def sort_list_by(key, current_participant_list):
    """
    Sorts the current list of participants in descending order regarding a given key

    :param key: must be either 'P1', 'P2', 'P3' or 'average'
    :param current_participant_list: the list that is being sorted
    :return: the sorted list
    """

    key_dict = {'P1': get_score1, 'P2': get_score2, 'P3': get_score3, 'average': get_average_score}
    ordered_list = current_participant_list.copy()

    # the selection sort algorithm is applied on a copy of the original list
    length = len(ordered_list)
    for i in range(0, length - 1):
        for j in range(i + 1, length):
            if key_dict[key](ordered_list[i]) < key_dict[key](ordered_list[j]):
                auxiliary_dict = ordered_list[i].copy()
                ordered_list[i] = ordered_list[j].copy()
                ordered_list[j] = auxiliary_dict.copy()

    return ordered_list


def split_command(command):
    """
    Splits the command entered by the user into a command_word and command_parameters
    :param command: the command typed by the user
    :return: a list in which the first element is the command word and the second are the command parameters
    """

    command_as_units = command.strip().split(" ", 1)

    if len(command_as_units) == 1:
        command_as_units.append('')
    return command_as_units


def split_participant_scores(scores_as_string):
    """
    Splits the command parameters containing the scores and creates a new participant
    :param scores_as_string: the parameters of the user command
    :return: a new participant with the given scores
    """

    command_as_units = scores_as_string.split(' ')
    if len(command_as_units) != 3:
        raise ValueError('Invalid number of scores')
    problem1_score = command_as_units[0]
    problem2_score = command_as_units[1]
    problem3_score = command_as_units[2]
    participant = create_participant(int(problem1_score), int(problem2_score), int(problem3_score))
    return participant


def undo_last_operation(participants_storage):
    """
    Reverses the last operation that modified program data.
    """

    # gets the last list from the history
    previous_participant_list = get_previous_list_from_history(participants_storage)

    # sets the current list to be the previous one
    set_current_list_to(previous_participant_list, participants_storage)

    # removes the last list from the history of the lists
    remove_last_list_from_history(participants_storage)
