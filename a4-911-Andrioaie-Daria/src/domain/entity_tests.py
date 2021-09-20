"""
All the test functions for the entity module
"""
from src.domain.entity import initialise_participants_dictionary, calculate_average, create_participant, truncate, \
    add_current_list_to_history, set_current_list_to, get_history_list, set_history_list_to, \
    get_previous_list_from_history, remove_last_list_from_history, get_current_list


def test_initialise_participants_dictionary():
    """
    Test for the initialise_participants_dictionary function
    """

    participants = initialise_participants_dictionary()
    assert participants['history_list'] == []
    assert len(participants['current_list']) == 10


def test_add_current_list_to_history():
    """
    Test for the add_current_list_to_history function
    """

    participants = initialise_participants_dictionary()
    add_current_list_to_history(participants)

    history = get_history_list(participants)

    assert len(history) == 1


def test_calculate_average():
    """
    Test function for calculate_average function
    """

    score1 = 9
    score2 = 7
    score3 = 8
    average_score = calculate_average(score1, score2, score3)
    assert average_score == 8

    score1 = 3
    score2 = 5
    score3 = 6
    average_score = calculate_average(score1, score2, score3)
    assert average_score == 4.66


def test_create_participant():
    """
    Test function for create_participant
    """

    participant = create_participant(1, 2, 3)
    assert participant == {'problem1_score': 1, 'problem2_score': 2, 'problem3_score': 3, 'average': 2}


def test_truncate():
    """
    Test for truncate function
    """

    number = truncate(12.235, 1)
    assert number == 12.2

    number = truncate(6, 0)
    assert number == 6


def test_set_history_list_to():
    """
    Test for the set_history_list_to function
    """

    participants = initialise_participants_dictionary()
    add_current_list_to_history(participants)
    set_current_list_to([0, 1, 2], participants)
    add_current_list_to_history(participants)
    assert len(get_history_list(participants)) == 2

    set_history_list_to([[0, 1, 2]], participants)
    assert len(get_history_list(participants)) == 1


def test_remove_last_list_from_history():
    """
    Test for the remove_last_list_from_history function
    """

    participants = initialise_participants_dictionary()

    set_current_list_to([0, 1, 2], participants)
    add_current_list_to_history(participants)
    remove_last_list_from_history(participants)

    assert get_history_list(participants) == []


def test_set_current_list_to():
    """
    Test for the set_current_list_to function
    """

    participants = initialise_participants_dictionary()
    set_current_list_to([0, 1, 2, 3, 4, 5], participants)
    current = get_current_list(participants)
    assert current == [0, 1, 2, 3, 4, 5]


def test_get_previous_list_from_history():
    """
    Test for the get_previous_list_from_history function
    """

    participants = initialise_participants_dictionary()
    add_current_list_to_history(participants)

    set_current_list_to([0, 1, 2], participants)
    add_current_list_to_history(participants)

    last_list = get_previous_list_from_history(participants)

    assert len(last_list) == 3
