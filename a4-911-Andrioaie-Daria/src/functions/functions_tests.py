'''
All the test functions for the functions module
'''
from src.domain.entity import initialise_participants_dictionary, add_current_list_to_history, set_current_list_to, \
    get_history_list, get_current_list, get_score1, get_score2, get_score3
from src.functions.functions import undo_last_operation, remove_participant_at_position, \
    remove_from_start_position_to_end_position, replace_old_score_with_new_score, split_command, \
    split_participant_scores, add_participant, remove_by_average_score


def test_undo_last_operation():
    '''
    Test for the undo_last_operation function
    '''
    participants_storage = initialise_participants_dictionary()
    add_current_list_to_history(participants_storage)
    set_current_list_to([0,1,2], participants_storage)
    undo_last_operation(participants_storage)
    assert len(get_current_list(participants_storage)) == 10
    assert len(get_history_list(participants_storage)) == 0



def test_add_participant():
    '''
    Test for the add_participant function
    '''

    participants_storage = initialise_participants_dictionary()

    participant_list = get_current_list(participants_storage)
    assert len(participant_list) == 10

    participant = {'problem1_score': 1, 'problem2_score': 2, 'problem3_score': 3, 'average': 2}
    add_participant(participants_storage, participant)

    participant_list = get_current_list(participants_storage)
    assert len(participant_list) == 11


def test_remove_participant_at_position():
    '''
    Test for the remove_participant_at_position function
    '''

    participant_list=[{'problem1_score': 5, 'problem2_score': 7, 'problem3_score': 6, 'average': 6}]
    remove_participant_at_position(participant_list, 0)
    assert participant_list[0]=={'problem1_score': 0, 'problem2_score': 0, 'problem3_score': 0, 'average': 0}


def test_remove_from_start_position_to_end_position():
    '''
    Test for the function remove_from_start_position_to_end_position
    '''
    participant_list = [{'problem1_score': 5, 'problem2_score': 7, 'problem3_score': 6, 'average': 6},
                        {'problem1_score': 1, 'problem2_score': 2, 'problem3_score': 3, 'average': 2},
                        {'problem1_score': 8, 'problem2_score': 10, 'problem3_score': 9, 'average': 9}]
    remove_from_start_position_to_end_position(participant_list, 0, 1)
    assert participant_list == [{'problem1_score': 0, 'problem2_score': 0, 'problem3_score': 0, 'average': 0},
                                {'problem1_score': 0, 'problem2_score': 0, 'problem3_score': 0, 'average': 0},
                                {'problem1_score': 8, 'problem2_score': 10, 'problem3_score': 9, 'average': 9}]


def test_remove_by_average_score():
    '''
    Test for the remove_by_average_score function
    '''
    participants_storage = initialise_participants_dictionary()
    list = get_current_list(participants_storage)
    remove_by_average_score('<', 10, participants_storage)
    assert get_current_list(participants_storage) == list


def test_replace_old_score_with_new_score():
    '''
    Test for the replace_old_score_with_new_score function
    '''
    participant_list = [{'problem1_score': 5, 'problem2_score': 7, 'problem3_score': 6, 'average': 6},
                        {'problem1_score': 1, 'problem2_score': 2, 'problem3_score': 3, 'average': 2},
                        {'problem1_score': 8, 'problem2_score': 10, 'problem3_score': 9, 'average': 9}]
    replace_old_score_with_new_score(participant_list, 1, 'P1', 10)
    assert participant_list == [{'problem1_score': 5, 'problem2_score': 7, 'problem3_score': 6, 'average': 6},
                                {'problem1_score': 10, 'problem2_score': 2, 'problem3_score': 3, 'average': 5},
                                {'problem1_score': 8, 'problem2_score': 10, 'problem3_score': 9, 'average': 9}]


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
