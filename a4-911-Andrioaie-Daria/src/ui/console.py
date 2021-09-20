"""
This is the user interface module. These functions call functions from the domain and functions module.
"""
from src.domain.entity import create_participant, get_average_score, to_string, get_current_list, \
    initialise_participants_dictionary, add_current_list_to_history, set_current_list_to, get_history_list
from src.functions.functions import split_command, split_participant_scores, add_participant, \
    remove_participant_at_position, remove_from_start_position_to_end_position, replace_old_score_with_new_score, \
    remove_by_average_score, calculate_average_between, calculate_minimum_between, undo_last_operation, sort_list_by


def add_new_participant_ui(participants_storage, scores_as_string):
    """
    Adds a new participant to the current participant list

    :param participants_storage: a dictionary containing the history_list and the current_list of participants
    :param scores_as_string: all three scores in one string
    """
    participant = split_participant_scores(scores_as_string)
    add_participant(participants_storage, participant)


def insert_new_participant_at_position_ui(participants_storage, insert_command_parameters):
    """
    Inserts the scores of a new participant at a given position
    by splitting the command parameters into the three scores and the position of insertion

    :param participants_storage: a dictionary containing the history_list and the current_list of participants
    :param insert_command_parameters: a string in the expected form "<score1> <score2> <score3> at <position>"
    """

    participant_list = get_current_list(participants_storage)

    command_as_units = insert_command_parameters.split(' ')

    # length of command parameters must be 5 in order to be eligible for the "insert <score1> <score2> <score3> at
    # <position>" command
    if len(command_as_units) != 5:
        raise ValueError('Invalid parameter count')

    score1 = command_as_units[0]
    score2 = command_as_units[1]
    score3 = command_as_units[2]
    word = command_as_units[3]
    insertion_position = command_as_units[4]

    if word != 'at':
        raise ValueError('The command must have the format insert <score1> <score2> <score3> at <position>')

    if len(participant_list) < int(insertion_position):
        raise ValueError('The list is too short at the moment')

    participant = create_participant(int(score1), int(score2), int(score3))

    add_current_list_to_history(participants_storage)

    # inserts participant on <insertion_position> in the participant_list
    participant_list.insert(int(insertion_position), participant)

    set_current_list_to(participant_list, participants_storage)


def remove_participant_ui(participants_storage, remove_command_parameters):
    """
    Handles all the cases in which the command entered by the user starts with 'remove'
    by checking for the command cases "remove <position>", "remove <start_position> to <end_position>",
    "remove [ < | = | > ] <score>"
    and calls the specific function that implements each case

    :param participants_storage: a dictionary containing the history_list and the current_list
    :param remove_command_parameters: the parameters of the command entered by the user
    """

    command_as_units = remove_command_parameters.split(' ')

    # the "remove <position>" case
    if len(command_as_units) == 1:      # length must be one because the only command parameter is <position>
        position = command_as_units[0]
        remove_participant_at_position(position, participants_storage)

    # the "remove <start_position> to <end_position>" case

    # length must be 3 because there are two positions and the word 'to' in the middle
    elif len(command_as_units) == 3 and command_as_units[1] == 'to':
        start_position = command_as_units[0]
        end_position = command_as_units[2]
        remove_from_start_position_to_end_position(start_position, end_position, participants_storage)

    # the "remove [ < | = | > ] <score>" case

    # length must be 2 because there are only two parameters that this case takes
    elif len(command_as_units) == 2:
        relational_operator = command_as_units[0]
        score = int(command_as_units[1])
        if relational_operator == '<' or relational_operator == '=' or relational_operator == '>':
            remove_by_average_score(relational_operator, score, participants_storage)
    else:
        raise ValueError('Invalid parameters for performing the remove command')


def replace_participant_score_with_new_score_ui(participants_storage, parameters_of_replace_command):
    """
    Checks if the command parameters are in the format "<position> <P1 | P2 | P3> with <new score>"
    and directs to the function that implements this case.
    Otherwise, raises an error

    :param participants_storage: a dictionary containing the history_list and the current_list of participants
    :param parameters_of_replace_command: the parameters of the command entered by the user
    """

    command_as_units = parameters_of_replace_command.split(' ')

    # the 'replace <position> <P1 | P2 | P3> with <new score>' scenario
    if len(command_as_units) == 4 and command_as_units[2] == 'with':
        position = int(command_as_units[0])
        problem = command_as_units[1]
        new_score = int(command_as_units[3])
        replace_old_score_with_new_score(participants_storage, position, problem, new_score)

    else:
        raise ValueError('Invalid parameters for the replace command. '
                         'The command must have the format replace <position> <P1 | P2 | P3> with <new score>')
    print('\n')


def print_list_of_participants_ui(participants_storage, command_parameters):
    """
    Handles all the cases in which the command word is 'list':
        -'list'
        -'list sorted'
        -'list [ < | = | > ] <score>'

    :param participants_storage: a dictionary containing the history_list and the current_list of participants
    :param command_parameters: the parameters of the command
    """

    # the 'list' command
    if command_parameters == '':
        print_list_of_participants(participants_storage)

    # the 'list sorted' command
    elif command_parameters == 'sorted':
        print_list_of_participants_sorted(participants_storage)

    # the 'list [ < | = | > ] <score>' command
    else:
        check_for_print_participants_compared_to_command(participants_storage, command_parameters)


def print_list_of_participants(participants_storage):
    """
    Displays each participant in the current list in the format: Participant i: score1 score2 score3
    Average score: average

    :param participants_storage: a dictionary containing the history_list and the current_list of participants
    """

    participant_list = get_current_list(participants_storage)
    for i in range(0, len(participant_list)):
        print('Participant '+str(i)+': '+to_string(participant_list[i]))
    print('\n')


def print_list_of_participants_sorted(participants_storage):
    """
    Prints the list of participants into the descending order depending on the average score

    :param participants_storage: a dictionary containing the history_list and the current_list of participants
    """

    participant_list = get_current_list(participants_storage)

    ordered_list = sort_list_by('average', participant_list)

    print('Participants displayed in descendant order of their average score:')
    for i in range(0, len(ordered_list)):
        print('Participant '+str(i)+': '+to_string(ordered_list[i]))
    print('\n')


def check_for_print_participants_compared_to_command(participants_storage, print_command_parameters):
    """
    Checks if the command parameters are eligible for the command "list [ < | = | > ] <score>". If so, calls
    the specific function that implements this case.

    :param participants_storage: a dictionary containing the history_list and the current_list of participants
    :param print_command_parameters: the parameters of the command entered by the user
    """

    command_as_units = print_command_parameters.split()

    # the length of the command must be two, since it should only contain a relational operator and a number
    if len(command_as_units) != 2:
        raise ValueError('Invalid parameter count')

    relational_operator = command_as_units[0]
    comparing_number = float(command_as_units[1])

    compare_list = ['<', '=', '>']

    if relational_operator in compare_list:
        print_participants_compared_to(comparing_number, relational_operator, participants_storage)
    else:
        raise ValueError('Invalid comparison parameter')


def print_participants_compared_to(number, relational_operator, participants_storage):
    """
    Prints all the participants whose average score is smaller-than, equal-to or greater-than a <number>, depending
    on the relational operator given as a parameter

    :param number: the number that participants' average score is being compared to
    :param relational_operator: either '<', '=' or '>'
    :param participants_storage: a dictionary containing the history_list and the current_list of participants
    """
    check = False
    participant_list = get_current_list(participants_storage)

    if relational_operator == '<':
        for participant in participant_list:
            if get_average_score(participant) < number:
                check = True
                print('Participant ' + to_string(participant))

    elif relational_operator == '=':
        for participant in participant_list:
            if get_average_score(participant) == number:
                check = True
                print('Participant ' + to_string(participant))

    elif relational_operator == '>':
        for participant in participant_list:
            if get_average_score(participant) > number:
                check = True
                print('Participant ' + to_string(participant))

    if not check:
        print('The are no participants whose average score is '+relational_operator + ' ' + str(number))
    print('\n')


def print_average_score_from_start_to_end(participants_storage, average_command_parameters):
    """
    Checks if the user command is eligible for the format "avg <start_position> to <end_position>"
    and prints the average of the average scores of all participants between these 2 positions
    
    :param participants_storage: a dictionary containing the history_list and the current_list of participants
    :param average_command_parameters: the parameters of the command entered by the user
    """

    command_as_units = average_command_parameters.split()

    start_position = command_as_units[0]
    word = command_as_units[1]
    end_position = command_as_units[2]

    # the "avg <position> to <position>" command
    if len(command_as_units) == 3 and word == 'to':

        participant_list = get_current_list(participants_storage)
        average = calculate_average_between(start_position, end_position, participant_list)
        print('The average score is: '+str(average))

    else:
        raise ValueError('The command must have the format "avg <position> to <position>"')

    print('\n')


def print_minimum_score_from_start_to_end(participants_storage, minimum_command_parameters):
    """
    Checks if the command is eligible for the format "min <position> to <position>"
    and prints the minimum average score of all participants between these 2 positions

    :param participants_storage: a dictionary containing the history_list and the current_list of participants
    :param minimum_command_parameters: the parameters of the command entered by the user
    """

    command_as_units = minimum_command_parameters.split()

    start_position = command_as_units[0]
    word = command_as_units[1]
    end_position = command_as_units[2]

    # the "min <position> to <position>" command
    if len(command_as_units) == 3 and word == 'to':

        participant_list = get_current_list(participants_storage)
        minimum = calculate_minimum_between(start_position, end_position, participant_list)
        print('The minimum average score is: ' + str(minimum))

    else:
        raise ValueError('The command must have the format min <position> to <position>')
    print('\n')


def establish_podium(participants_storage, top_command_parameters):
    """
    Checks if the command is eligible for either of the formats "top <number>" or "top <number> <P1 | P2 | P3>"
    and calls the specific functions that implement each case

    :param participants_storage: a dictionary containing the history_list and the current_list of participants
    :param top_command_parameters: the parameters of the command entered by the user
    """

    command_as_units = top_command_parameters.split()

    # the "top <number>" command
    if len(command_as_units) == 1:

        podium_length = command_as_units[0]
        print_top_participants_regarding_average(podium_length, participants_storage)

    # the "top <number> <P1 | P2 | P3>" command
    elif len(command_as_units) == 2:

        podium_length = command_as_units[0]
        problem = command_as_units[1]
        print_top_regarding_problem_score(podium_length, problem, participants_storage)

    else:
        raise ValueError('The command must have either of the format top <number> or top <number> <P1 | P2 | P3>')
    print('\n')


def print_top_participants_regarding_average(podium_length, participants_storage):
    """
    Prints the top <number> participants in descending order of their average score.

    :param podium_length: the amount of participants that the top should display -> integer
    :param participants_storage: a dictionary containing the history_list and the current_list of participants
    """

    podium_length = int(podium_length)
    participant_list = get_current_list(participants_storage)

    if podium_length not in range(0, len(participant_list) + 1):
        raise ValueError('The podium length must be within the length of the list')

    ordered_list = sort_list_by('average', participant_list)

    print('The top ' + str(podium_length) + ' participants with the highest average score are:')
    for i in range(0, podium_length):
        print(to_string(ordered_list[i]))
    print('\n')


def print_top_regarding_problem_score(podium_length, problem, participants_storage):
    """
    Prints the top <number> participants in descending order of their <problem> score

    Command must have the format: top <number> <P1 | P2 | P3>

    :param podium_length: must be an integer within the length of the current list of participants
    :param problem: must be either 'P1', 'P2' or 'P3'
    :param participants_storage: a dictionary containing the history_list and the current_list of participants
    """

    podium_length = int(podium_length)
    participant_list = get_current_list(participants_storage)

    if podium_length not in range(0, len(participant_list) + 1):
        raise ValueError('The podium length must be within the length of the list')

    if problem == 'P1' or problem == 'P2' or problem == 'P3':

        ordered_list = sort_list_by(problem, participant_list)

        print('The top ' + str(podium_length) + ' participants with the highest ' + problem + ' score are:')
        for i in range(0, podium_length):
            print(to_string(ordered_list[i]))
    else:
        raise ValueError('Invalid parameter for the top command')
    print('\n')


def undo_last_operation_ui(participants_storage, command=''):
    """
    Reverses the last operation that modified program data.
    When there are no operations to be reversed, raises a value error.

    :param participants_storage: a dictionary containing the history_list and the current_list
    :param command: is not actually used, it is only there because other functions in the UI need it
    """

    if len(get_history_list(participants_storage)) == 0:
        raise ValueError('No more undo s. You have reached the initial list')

    undo_last_operation(participants_storage)

    print('Successfully undone :)')
    print('\n')


def print_commands():
    print('Hello! :)')
    print('These are your commands:')
    print('     add <P1 score> <P2 score> <P3 score>')
    print('     insert <P1 score> <P2 score> <P3 score> at <position>')
    print("\n")
    print('     remove <position>')
    print('     remove <start position> to <end position>')
    print('     remove[ < | = | >] < score >')
    print('     replace <position> <P1 | P2 | P3> with <new score>')
    print("\n")
    print('     list')
    print('     list sorted')
    print('     list [ < | = | > ] <score>')
    print("\n")
    print('     avg <position> to <position>')
    print('     min <position> to <position>')
    print("\n")
    print('     top <number>')
    print('     top <number> <P1 | P2 | P3>')
    print("\n")
    print('     undo')
    print("\n")


def start():

    command_dict = {'add': add_new_participant_ui, 'insert': insert_new_participant_at_position_ui,
                    'remove': remove_participant_ui, 'replace': replace_participant_score_with_new_score_ui,
                    'list': print_list_of_participants_ui, 'avg': print_average_score_from_start_to_end,
                    'min': print_minimum_score_from_start_to_end,
                    'top': establish_podium, 'undo': undo_last_operation_ui}

    participants_storage = initialise_participants_dictionary()

    print_commands()

    finished = False
    while not finished:
        user_command = input('Enter command: ')

        command_word, command_parameters = split_command(user_command)

        if command_word in command_dict:
            try:
                command_dict[command_word](participants_storage, command_parameters)
            except ValueError as ve:
                print(str(ve))

        elif command_word == 'exit':
            print('bye, bye!')
            finished = True

        else:
            print('Wrong command. Try again')
