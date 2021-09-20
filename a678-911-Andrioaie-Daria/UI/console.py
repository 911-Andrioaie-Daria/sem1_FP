from datetime import date, time

from Domain.activity_entity import ActivityException
from Domain.person_entity import PersonException
from Service.activity_service import ActivityService
from Service.person_service import PersonService
from Service.undo_service import UndoService


def print_menu():
    """
    Prints all the options available to the user.
    """
    print('Hello :)')
    print('These are your available options:')
    print('     1: Add a new friend to the list')
    print('     2: Remove a friend from the list')
    print("     3: Update a friend's data.")
    print("     4: Display your list of friends")
    print("     5: Search for persons based on their name or phone number.")
    print('     6: Add a new activity in your planner')
    print('     7: Remove an activity from the planner')
    print("     8: Update an activity.")
    print("     9: Display your list of activities")
    print('     10: Search for activities based on their date, time or description')
    print('     11: List all activities taking place in a given day')
    print('     12: List busiest days.')
    print('     13: List all activities in which a specific person will participate ')
    print('     14: Undo last operation.')
    print('     15: Redo undone operation')
    print('     16: Exit')
    print('\n')


def read_new_friend_data():
    """
    The function reads the attributes of a new person as a list
    :return: the list of attributes
    """
    new_friend_data = [(input('First name and last name: ')), (input('Phone number: '))]
    return new_friend_data


def read_new_activity_data():
    """
    The function reads the attributes of a new activity as a list
    :return: the list of attributes
    """
    ids_of_persons_involved = input('Enter the ids of persons you want to involve in your activity: ').split()

    ids_of_persons_involved = [int(person_id) for person_id in ids_of_persons_involved]
    new_activity_data = [ids_of_persons_involved,
                         date(int(input('Enter year: ')), int(input('Enter month:')), int(input('Enter day: '))),
                         time(int(input('Enter start hour: ')), int(input('Enter start minute: '))),
                         time(int(input('Enter end hour: ')), int(input('Enter end minute: '))),
                         input('Enter description: ')]
    return new_activity_data


class ConsoleUI:

    def __init__(self):
        self._undo_service = UndoService()
        self._persons_service = PersonService(self.undo_service)
        self._activity_service = ActivityService(self.undo_service)

    @property
    def persons_service(self):
        return self._persons_service

    @property
    def activity_service(self):
        return self._activity_service

    @property
    def undo_service(self):
        return self._undo_service

    def add_new_friend_ui(self):
        """
        The method reads the data of a new friend and passes this to the service in order to perform the addition to the list.
        """
        new_friend_data = read_new_friend_data()
        self.persons_service.add_person(new_friend_data)
        print('Successfully added new friend. :)')

    def remove_friend_ui(self):
        """
        The method removes a friend from the list of friends based on their unique ID.
        Reads the ID from the console and passes it to the service to perform the removal.
        """
        id_of_person_to_be_removed = int(input('Enter the ID of the person you want to remove: '))
        self.persons_service.remove_person(id_of_person_to_be_removed)
        print('Successfully removed person.')

    def update_friend_ui(self):
        """
        The method reads the ID of a person and a list containing the new data with which the person will be updated
        and passes this id and data to the service in order perform the update.
        """

        id_of_person_to_be_updated = int(input('Enter the ID of the person whose data you want to update: '))
        new_attributes_of_person = read_new_friend_data()
        self.persons_service.update_person(id_of_person_to_be_updated, new_attributes_of_person)
        print('Successfully updated person data.')

    def display_list_of_friends_ui(self):
        """
        The method prints all the persons in the current list of persons.
        """
        list_of_persons = self.persons_service.get_all_persons()
        for person in list_of_persons:
            print(person)

    def search_for_persons_ui(self):
        """
        The method reads a search key entered by the user and will pass this to the service to search for persons whose
        data match (even partially) with this key. The service will return a list of persons who resulted in the search
        and print this list.
        :return:
        """
        search_key = input("Enter the name or a phone number that you want to search by: ")
        search_result = self.persons_service.search_person_by(search_key)

        if not search_result:
            print("No matches found")
        else:
            for person in search_result:
                print(person)

    def add_new_activity_ui(self):
        """
        The method reads all the required data of a new activity in the form of a list and passes this data to the
        service in order to perform the addition.
        """

        new_activity_attributes = read_new_activity_data()
        self.activity_service.add_new_activity(new_activity_attributes)
        print('Successfully added new activity.')

    def remove_activity_ui(self):
        """
        The method reads the id of the activity that will be removed and passes this id to the service that will perform
        the removal.
        """

        id_of_activity_to_be_removed = int(input('Enter the id of the activity you want to remove: '))
        self.activity_service.remove_activity(id_of_activity_to_be_removed)
        print('Successfully removed activity')

    def update_activity_ui(self):
        """
        The method reads the ID of an activity and a list containing the new data with which the activity will be updated
        and passes this id and data to the service in order perform the update.
        """

        id_of_activity_to_be_updated = int(input('Enter the id pf the activity you want to update: '))

        new_activity_attributes = read_new_activity_data()

        self.activity_service.update_activity(id_of_activity_to_be_updated, new_activity_attributes)
        print('Successfully updated.')

    def display_list_of_activities_ui(self):
        """
        The method prints all the activities in the current list of activities.
        """
        list_of_activities = self.activity_service.get_all_activities()
        for activity in list_of_activities:
            print(activity)
            print('\n')

    def search_activity_ui(self):
        """
        The method reads as an input a string containing either a date, time or a description and passes  this to the service,
        that will return a list of activities resulted while searching
        :return:
        """
        search_key = input("Enter the date, time or description that you want to search by: ")

        search_result = self.activity_service.search_activities(search_key)

        if not search_result:
            print('No matches found')
        else:
            for activity in search_result:
                print(activity)
                print('\n')

    def show_activities_on_specific_day_ui(self):
        """
        The method prints the activities that take place in a day entered by the user, in the order of their start time.
        """
        # read date
        given_date = date(int(input('Enter the year: ')), int(input('Enter the month: ')), int(input('Enter the day: ')))

        # call method from activity service that returns a list of activities
        resulted_activities = self.activity_service.get_all_activities_in_a_day(given_date)

        # print the activities in the returned list
        if not resulted_activities:
            print('There are no activities taking place in the given date.')
        else:
            for activity in resulted_activities:
                print(activity)
                print('\n')

    def show_busiest_days_ui(self):
        """
        The method calls the service which provides the list of upcoming dates with activities, sorted in descending
        order of the free time and prints this list
        """
        list_of_busiest_days = self.activity_service.get_the_busiest_days()
        for day in list_of_busiest_days:
            print(day)

    def show_all_activities_with_a_person_ui(self):
        """
        The methods reads the id of a person and list all upcoming activities to which the person will participate.
        """
        id_of_person = int(input('Enter the id of the person: '))
        resulted_activities = self.activity_service.get_all_activities_with_a_person(id_of_person)

        if not resulted_activities:
            print('The person is not involved in any activity for now.')
        else:
            for activity in resulted_activities:
                print(activity)
                print('\n')

    def undo_operation_ui(self):
        if self.undo_service.undo_operation():
            print('Undone successfully.')
        else:
            print('There are no more operations that can be undone.')

    def redo_operation_ui(self):
        if not self.undo_service.redo_operation():
            print('There are no operations that can be redone.')
        else:
            print('Redone successfully')

    def start(self):

        print_menu()
        person_options = {'1': self.add_new_friend_ui, '2': self.remove_friend_ui,
                          '3': self.update_friend_ui, '4': self.display_list_of_friends_ui,
                          '5': self.search_for_persons_ui}
        activity_options = {'6': self.add_new_activity_ui, '7': self.remove_activity_ui,
                            '8': self.update_activity_ui, '9': self.display_list_of_activities_ui,
                            '10': self.search_activity_ui}

        statistics_options = {'11': self.show_activities_on_specific_day_ui, '12': self.show_busiest_days_ui,
                              '13': self.show_all_activities_with_a_person_ui}

        undo_options = {'14': self.undo_operation_ui, '15': self.redo_operation_ui}

        not_finished = True
        while not_finished:
            user_option = input('Please enter your option: ')

            if user_option in person_options:
                try:
                    person_options[user_option]()
                except PersonException as error_message:
                    print(error_message)
                except ValueError as error_message:
                    print(error_message)

            elif user_option in activity_options:
                try:
                    activity_options[user_option]()
                except ActivityException as error_message:
                    print(error_message)
                except ValueError as error_message:
                    print(error_message)

            elif user_option in statistics_options:
                try:
                    statistics_options[user_option]()
                except Exception as error_message:
                    print(error_message)

            elif user_option in undo_options:
                undo_options[user_option]()

            elif user_option == '16':
                print('bye, bye')
                not_finished = False

            else:
                print('Unavailable option. Try again')
