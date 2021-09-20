#---Problem 2. Contest

# ------------------------------------------------domain section--------------------------------------------------------
#
import math

def create_participant(p1_score, p2_score, p3_score):
    '''
    Creates a dictionary containing the three scores as integers and the average score
    :param p1_score: integer in [1, 10]
    :param p2_score: integer in [1, 10]
    :param p3_score: integer in [1, 10]
    :return: the dictionary participant
    '''

    if int(p1_score) < 0 or int(p1_score) > 10:
        raise ValueError('The scores must be integers in [0, 10]')
    if int(p2_score) < 0 or int(p2_score) > 10:
        raise ValueError('The scores must be integers in [0, 10]')
    if int(p3_score) < 0 or int(p3_score) > 10:
        raise ValueError('The scores must be integers in [0, 10]')

    average_score = calculate_average(p1_score, p2_score, p3_score)
    participant = {'p1_score': p1_score, 'p2_score': p2_score, 'p3_score': p3_score, 'average': average_score}

    return participant


def calculate_average(number1, number2, number3):
    '''
    Calculates the float average between 3 integer numbers
    :param number1: integer number
    :param number2: integer number
    :param number3: integer number
    :return: float average
    '''
    average = (number1+number2+number3)/3.0
    return truncate(average, 2)



def truncate(number, decimals=0):
    '''
    Returns a value truncated to a specific number of decimal places.
    Uses the math.trunc function
    :param number: the float number that is being truncated
    :param decimals: the number of decimals that we want to keep in the number. Must be an integer
    '''
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor


def get_score1(participant):
    '''
    Returns participant's score of P1
    :param participant: the participant
    :return: score of P1
    '''
    return participant['p1_score']


def get_score2(participant):
    '''
    Returns participant's score of P2
    :param participant: the participant
    :return: score of P2
    '''
    return participant['p2_score']


def get_score3(participant):
    '''
    Returns participant's score of P3
    :param participant: the participant
    :return: score of P3
    '''
    return participant['p3_score']


def get_average_score(participant):
    '''
    Returns participant's score of P1
    :param participant: the participant
    :return: score of P1
    '''
    return participant['average']


def set_score1(participant, value_as_int):
    '''
    Sets the score of P1 to a given integer value
    :param participant: the participant
    :param value_as_int: the value to be set
    :return:
    '''
    participant['p1_score'] = int(value_as_int)

    # now the average score has changed as well, so we have to update it
    score1 = get_score1(participant)
    score2 = get_score2(participant)
    score3 = get_score3(participant)

    set_average_score(participant, calculate_average(score1, score2, score3))


def set_score2(participant, value_as_int):
    '''
    Sets the score of P2 to a given integer value
    :param participant: the participant
    :param value_as_int: the value to be set
    :return:
    '''
    participant['p2_score'] = int(value_as_int)

    # now the average score has changed as well, so we have to update it
    score1 = get_score1(participant)
    score2 = get_score2(participant)
    score3 = get_score3(participant)

    set_average_score(participant, calculate_average(score1, score2, score3))


def set_score3(participant, value_as_int):
    '''
    Sets the score of P3 to a given integer value
    :param participant: the participant
    :param value_as_int: the value to be set
    :return:
    '''
    participant['p3_score'] = int(value_as_int)

    #now the average score has changed as well, so we have to update it
    score1 = get_score1(participant)
    score2 = get_score2(participant)
    score3 = get_score3(participant)

    set_average_score(participant, calculate_average(score1, score2, score3))


def set_average_score(participant, value_as_float):
    '''
    Sets the average score to a given integer value
    :param participant: the participant
    :param value_as_float: the value to be set
    :return:
    '''
    participant['average'] = value_as_float


def set_all_scores_to(participant, value_as_int):
    '''
    Sets all the scores of a participant (P1_score, P2_score, P3_score, average) to a given integer value
    :param participant: the participant
    :param value_as_int: the value that all scores are changed to
    :return:
    '''
    set_score1(participant, value_as_int)
    set_score2(participant, value_as_int)
    set_score3(participant, value_as_int)
    set_average_score(participant, value_as_int)


def to_string(participant):
    '''
    Converts the participant entity into a readable string,
    having the format <p1_score> <p2_score> <p3_score> Average score: <average>
    :param participant: the participant
    :return: a string with all participant data
    '''
    return str(get_score1(participant)) + ' '+str(get_score2(participant)) + ' '+str(get_score3(participant)) + '  Average score: ' + str(get_average_score(participant))

#
# -------------------------------------------------------------Functionalities section--------------------------------------------------------------------------------------
#


def add_participant(participant_list, participant):
    '''
    Adds a new participant to an existing list
    :param participant_list: the list
    :param participant: the participant
    :return:
    '''
    participant_list.append(participant)


def remove_participant_at_position(participant_list, position):
    '''
    Sets to 0 the scores obtained by the participant at the given position
    :param participant_list: the list of participants
    :param position: the given position
    :return:
    '''
    position = int(position)
    if position < 0 or position >= len(participant_list):
        raise ValueError('The is no such position in the list. The position must be between 0 and '+str(len(participant_list)-1))
    set_all_scores_to(participant_list[position], 0)


def remove_from_start_position_to_end_position(participant_list, start_position, end_position):
    '''
    Sets to 0 the scores of all participants in the list from <start_position> to <end position>
    :param participant_list: the list of participants
    :param start_position: the first position to set to 0. Must be integer
    :param end_position: the last position to set to 0. Must be integer
    :return:
    '''
    start_position = int(start_position)
    end_position = int(end_position)
    if start_position < 0 or start_position >= len(participant_list):
        raise ValueError('The is no such start position in the list. The position must be between 0 and '+str(len(participant_list)-1))
    if end_position < 0 or end_position >= len(participant_list):
        raise ValueError('The is no such end position in the list. The position must be between 0 and ' + str(len(participant_list) - 1))
    if start_position > end_position:
        raise ValueError('The start position must be smaller than or equal to the end position.')
    for i in range(start_position, end_position+1):
        set_all_scores_to(participant_list[i], 0)


def replace_old_score_with_new_score(participant_list, position, problem, new_score):
    '''
    Replaces the score obtained at <problem> by the participant at position <position> with <new_score>
    :param participant_list: the list of participants
    :param position: the position of the participants  ---- integer between [0, len(participant_list))
    :param problem: to problem whose score must be replaced  ---- string 'P1' or 'P2' or 'P3'
    :param new_score: must be integer in [0, 10]
    :return:
    '''

    position = int(position)
    if position < 0 or position >= len(participant_list):
        raise ValueError('The is no such position in the list. The position must be between 0 and '+str(len(participant_list)-1))

    new_score = int(new_score)
    if new_score < 0 or new_score > 10:
        raise ValueError('The scores must be in [0, 10]')

    problem_dict = {'P1': set_score1, 'P2': set_score2, 'P3': set_score3}
    if problem in problem_dict:
        problem_dict[problem](participant_list[position], new_score)
    else:
        raise ValueError('Invalid problem parameter. The problem must be either P1, P2 or P3')


def check_for_comparison_command(participant_list, command_parameters):
    '''
    Checks if the command parameters are eligible for the command list [ < | = | > ] <score>. If so, calls the specific functions
    :param participant_list: the list
    :param command_parameters: the parameters of the command
    '''
    tokens = command_parameters.split()
    if len(tokens) != 2:
        raise ValueError('Invalid parameter count')
    tokens[1] = float(tokens[1])
    if tokens[0] == '>':
        print_participants_greater_than(participant_list, tokens[1])         #the 'greater than' case
    elif tokens[0] == '=':
        print_participants_equal_to(participant_list, tokens[1])             #the 'equal to' case
    elif tokens[0] == '<':
        print_participants_smaller_than(participant_list, tokens[1])         #the 'smaller than' case
    else:
        raise ValueError('Invalid comparison parameter')


def split_command(command):
    '''
    Splits a command into word and parameters
    :param command:
    :return: a list in which the first element is the command word and the second are the command parameters
    '''
    tokens = command.strip().split(" ", 1)
    if len(tokens) == 1:
        tokens.append('')
    return tokens


def split_participant_scores(scores_as_string):
    '''
    Splits the command parameters containing the scores and creates a new participant
    :param scores_as_string: the parameters of the user command
    :return: the scores of a new participant
    '''

    tokens = scores_as_string.split(' ')
    if len(tokens) != 3:
        raise ValueError('Invalid number of scores')
    p1_score = tokens[0]
    p2_score = tokens[1]
    p3_score = tokens[2]
    participant = create_participant(int(p1_score), int(p2_score), int(p3_score))
    return participant


#
#------------------------------------------------------------------------ UI section-------------------------------------------------------------------------
#


def add_participant_ui(participant_list, scores_as_string):
    '''
    Adds a participant to the participant list
    :param participant_list: the list
    :param scores_as_string: all three scores in one string
    '''
    participant = split_participant_scores(scores_as_string)
    add_participant(participant_list, participant)



def insert_participant_ui(participant_list, command_parameters):
    '''
    Splits the command parameters into the three scores and the position of the insertion
    :param participant_list: the list
    :param command_parameters: a string in the expected form "<score1> <score2> <score3> at <position>
    '''

    tokens=command_parameters.split(' ')
    if len(tokens)!=5:
        raise ValueError('Invalid parameter count')
    if tokens[3]!='at':
        raise ValueError('Invalid command parameters')
    if len(participant_list) < int(tokens[4]):
        raise ValueError('The list is too short at the moment')

    participant = create_participant(int(tokens[0]), int(tokens[1]), int(tokens[2]))
    position=tokens[4]

    participant_list.insert(int(position), participant)  #inserts participant on <position> in the participant_list



def remove_participant_ui(participant_list, command_parameters):
    '''
    Checks for the command cases "remove <position>" and "remove <start_position> to <end_position>" and calls the specific function of each case
    :param participant_list: the list of participants
    :param command_parameters: the parameters of the command entered by the user
    :return:
    '''
    tokens=command_parameters.split(' ')
    if len(tokens)==1:
        remove_participant_at_position(participant_list, tokens[0])
    elif len(tokens)==3 and tokens[1]=='to':
        remove_from_start_position_to_end_position(participant_list, tokens[0], tokens[2])
    else:
        raise ValueError('Invalid parameters for performing the remove command')



def replace_participant_ui(participant_list, command_parameters):
    '''
    Checks if the command parameters ar in the format <position> <P1 | P2 | P3> with <new score> and directs to the specific function
    :param participant_list:
    :param command_parameters:
    :return:
    '''
    tokens=command_parameters.split(' ')
    if len(tokens)==4 and tokens[2]=='with':
        replace_old_score_with_new_score(participant_list, tokens[0], tokens[1], tokens[3])
    else:
        raise ValueError('Invalid parameters for the replace command. The command must have the format replace <position> <P1 | P2 | P3> with <new score>')


def print_list_ui(participant_list, command_parameters):
    '''
    Handles all the cases in which the command word is 'list'
    :param participant_list: the list of participants
    :param command_parameters: the parameters of the command
    :return:
    '''
    if command_parameters=='':
        print_list(participant_list)
    elif command_parameters=='sorted':
        print_list_sorted(participant_list)
    else:
        check_for_comparison_command(participant_list, command_parameters)




def print_participants_greater_than(participant_list, comparing_number):
    '''
    Displays all the participants whose average score is greater than a certain number
    :param participant_list: the list of participants
    :param comparing_number: the number to which all participants' average score is compared to
    '''
    check=False
    for participant in participant_list:
        if get_average_score(participant)>comparing_number:
            check=True
            print('Participant '+to_string(participant))

    if check==False:
        print('The are no participants whose average score is greater than '+str(comparing_number))


def print_participants_equal_to(participant_list, comparing_number):
    '''
    Displays the participants whose average score is equal to a given number
    :param participant_list: the list of participants
    :param comparing_number: the number to which all participants' average score is being compared to
    :return:
    '''

    check=False
    for participant in participant_list:
        if get_average_score(participant)==comparing_number:
            check=True
            print('Participant ' + to_string(participant))

    if check==False:
        print('There are no participants whose average score is equal to '+str(comparing_number))



def print_participants_smaller_than(participant_list, comparing_number):
    '''
    Displays the participants whose average score is smaller than a given number
    :param participant_list: the list of participants
    :param comparing_number: the number to which all participants' average score is being compared to (as float)
    :return:
    '''

    check = False
    for participant in participant_list:
        if get_average_score(participant)<comparing_number:
            check = True
            print('Participant ' + to_string(participant))

    if check == False:
        print('There are no participants whose average score is smaller than '+str(comparing_number))


def print_list(participant_list):
    '''
    Displays each participant in format: Participant i: score1 score2 score3  Average score: average
    :param participant_list:
    :return:
    '''
    for i in range(0, len(participant_list)):
        print('Participant '+str(i)+': '+to_string(participant_list[i]))


def print_list_sorted(participant_list):
    '''
    Prints the list of participants into the descending order depending on the average score
    :param participant_list: the list
    :return:
    '''
    ordered_list = participant_list.copy()

    #selection sort algorithm applied on a copy of the original list
    length = len(ordered_list)
    for i in range(0, length-1):
        for j in range(i+1, length):
            if get_average_score(ordered_list[i]) < get_average_score(ordered_list[j]):
                auxiliary_dict = ordered_list[i].copy()
                ordered_list[i] = ordered_list[j].copy()
                ordered_list[j] = auxiliary_dict.copy()

    print('Participants displayed in descendant order of their average score:')
    print_list(ordered_list)


def print_commands():
    print('Hello! :)')
    print('These are your commands:')
    print('     add <P1 score> <P2 score> <P3 score>')
    print('     insert <P1 score> <P2 score> <P3 score> at <position>')
    print('     remove <position>')
    print('     remove <start position> to <end position>')
    print('     replace <position> <P1 | P2 | P3> with <new score>')
    print('     list')
    print('     list sorted')
    print('     list [ < | = | > ] <score>')
    print("\n")


def start():

    command_dict={'add': add_participant_ui, 'insert': insert_participant_ui, 'remove': remove_participant_ui, 'replace': replace_participant_ui, 'list': print_list_ui}

    participant_list=[]
    test_init(participant_list)

    print_commands()

    finished = False
    while not finished:
        user_command=input('Enter command: ')

        command_word, command_params = split_command(user_command)

        if command_word in command_dict:
            try:
                command_dict[command_word](participant_list, command_params)
            except ValueError as ve:
                print(str(ve))

        elif command_word=='exit':
            print('bye, bye!')
            finished = True

        else:
            print('Wrong command. Try again')


#
# -------------------------------------------------------------------Test functions-----------------------------------------------------------------------------------------
#


def test_init(test_list):
    test_list.append(create_participant(9,7,6))
    test_list.append(create_participant(9, 2, 9))
    test_list.append(create_participant(1, 4, 7))
    test_list.append(create_participant(7, 2, 5))
    test_list.append(create_participant(10, 7, 7))
    test_list.append(create_participant(9, 8, 3))
    test_list.append(create_participant(6, 10, 9))
    test_list.append(create_participant(9, 9, 5))
    test_list.append(create_participant(9, 8, 6))
    test_list.append(create_participant(3, 5, 6))


def test_calculate_average():
    '''
    test function for calculate_average
    '''
    score1 = 9
    score2 = 7
    score3 = 8
    average_score = calculate_average(score1, score2, score3)
    assert average_score == 8

    score1 = 3
    score2 = 5
    score3 = 6
    average_score=calculate_average(score1, score2, score3)
    assert average_score == 4.66


def test_create_participant():
    '''
    Test function for create_participant
    '''
    participant = create_participant(1, 2, 3)
    assert participant=={'p1_score': 1, 'p2_score': 2, 'p3_score': 3, 'average': 2}


def test_truncate():
    '''
    Test for truncate function
    '''
    number = truncate(12.235, 1)
    assert number == 12.2

    number = truncate(6, 0)
    assert number == 6


def test_add_participant():
    '''
    Test for the add_participant function
    '''

    participant_list = [{'p1_score': 5, 'p2_score': 7, 'p3_score': 6, 'average': 6}]
    participant = {'p1_score': 1, 'p2_score': 2, 'p3_score': 3, 'average': 2}
    add_participant(participant_list, participant)
    assert participant_list == [{'p1_score': 5, 'p2_score': 7, 'p3_score': 6, 'average': 6} , {'p1_score': 1, 'p2_score': 2, 'p3_score': 3, 'average': 2}]


def test_remove_participant_at_position():
    '''
    Test for the remove_participant_at_position function
    '''

    participant_list=[{'p1_score': 5, 'p2_score': 7, 'p3_score': 6, 'average': 6}]
    remove_participant_at_position(participant_list, 0)
    assert participant_list[0]=={'p1_score': 0, 'p2_score': 0, 'p3_score': 0, 'average': 0}


def test_remove_from_start_position_to_end_position():
    '''
    Test for the function remove_from_start_position_to_end_position
    '''
    participant_list = [{'p1_score': 5, 'p2_score': 7, 'p3_score': 6, 'average': 6},
                        {'p1_score': 1, 'p2_score': 2, 'p3_score': 3, 'average': 2},
                        {'p1_score': 8, 'p2_score': 10, 'p3_score': 9, 'average': 9}]
    remove_from_start_position_to_end_position(participant_list, 0, 1)
    assert participant_list == [{'p1_score': 0, 'p2_score': 0, 'p3_score': 0, 'average': 0},
                                {'p1_score': 0, 'p2_score': 0, 'p3_score': 0, 'average': 0},
                                {'p1_score': 8, 'p2_score': 10, 'p3_score': 9, 'average': 9}]


def test_replace_old_score_with_new_score():
    '''
    Test for the replace_old_score_with_new_score function
    '''
    participant_list = [{'p1_score': 5, 'p2_score': 7, 'p3_score': 6, 'average': 6},
                        {'p1_score': 1, 'p2_score': 2, 'p3_score': 3, 'average': 2},
                        {'p1_score': 8, 'p2_score': 10, 'p3_score': 9, 'average': 9}]
    replace_old_score_with_new_score(participant_list, 1, 'P1', 10)
    assert participant_list == [{'p1_score': 5, 'p2_score': 7, 'p3_score': 6, 'average': 6},
                                {'p1_score': 10, 'p2_score': 2, 'p3_score': 3, 'average': 5},
                                {'p1_score': 8, 'p2_score': 10, 'p3_score': 9, 'average': 9}]

def test_check_for_comparison_command():
    '''
    Test for the function check_for_comparison_command.
    Not entirely sure how to do this. :/
    '''
    pass

def test_split_command():

    command = "add 15"
    command_word, command_params = split_command(command)
    assert command_word=="add"
    assert command_params=="15"

    command='exit'
    command_word, command_params=split_command(command)
    assert command_word=='exit'
    assert command_params==''


def test_split_participant_scores():
    participant = split_participant_scores("10 9 8")
    assert get_score1(participant)== 10
    assert get_score2(participant)==9
    assert get_score3(participant)==8



start()









