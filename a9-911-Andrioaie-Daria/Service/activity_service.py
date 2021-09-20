"""
4. activity service + test activity service
"""
import re
from datetime import date, time, timedelta

from Domain.activity_entity import Activity
from Service.undo_service import FunctionCall, Operation


class ActivityService:

    def __init__(self, activity_repository, persons_repository, activity_validator, undo_service):
        self._activity_repository = activity_repository
        self._persons_repository = persons_repository
        self._validator = activity_validator
        self._undo_service = undo_service

    @property
    def activity_repository(self):
        return self._activity_repository

    @property
    def persons_repository(self):
        return self._persons_repository

    @property
    def validator(self):
        return self._validator

    @property
    def undo_service(self):
        return self._undo_service

    def create_activity(self, new_activity_attributes):
        """
        Creates a new activity with the the list of attributes entered as a parameter
        :param new_activity_attributes: a list of the form [[list of persons], date, start_time, end_time, description]
        :return: a new instance of the Activity class
        Exception: if one of the ids in the list of persons that will participate is not valid, it simply removes this
        id from the list of person_ids
        """

        ids_of_persons_involved = new_activity_attributes[0]
        activity_date = new_activity_attributes[1]
        start_time = new_activity_attributes[2]
        end_time = new_activity_attributes[3]
        description = new_activity_attributes[4]
        unique_id = new_activity_attributes[5]

        for id_of_person in ids_of_persons_involved:
            try:
                self.persons_repository.find_person_by_id(id_of_person)
            except ValueError:
                ids_of_persons_involved.remove(id_of_person)

        new_activity = Activity(unique_id, ids_of_persons_involved, activity_date, start_time, end_time, description)
        return new_activity

    def add_new_activity(self, new_activity_attributes):
        """
        The method creates a new activity with the given attributes, validates it and passes it to repository that will
        perform the actual addition
        :param new_activity_attributes: a list of the form [[list of persons], date, start_time, end_time, description]
        """
        new_activity_attributes.append(self.activity_repository.available_id)

        new_activity = self.create_activity(new_activity_attributes)
        self.validator.validate_activity(new_activity)

        self.activity_repository.add_activity(new_activity)

        undo_function = FunctionCall(self.activity_repository.remove_activity, new_activity.unique_id)
        redo_function = FunctionCall(self.activity_repository.add_activity, new_activity)
        self.undo_service.record_operation(Operation(undo_function, redo_function))

    def remove_activity(self, id_of_activity):
        """
        The method calls the repository that will remove the activity with the given id from the current list
        of activities
        """
        removed_activity = self.activity_repository.remove_activity(id_of_activity)

        undo_function = FunctionCall(self.activity_repository.add_activity, removed_activity)
        redo_function = FunctionCall(self.activity_repository.remove_activity, id_of_activity)
        self.undo_service.record_operation(Operation(undo_function, redo_function))

    def update_activity(self, id_of_activity_to_be_updated, new_activity_attributes):
        """
        The method creates an Activity based on the list of new_activity_attributes, validates the new activity and
        passes it to the repository to perform the actual update.
        :param id_of_activity_to_be_updated: integer representing the id of the activity
        :param new_activity_attributes: a list of the form [[list of persons], date, start_time, end_time, description]
        """
        index_of_activity = self.activity_repository.find_activity_by_id(id_of_activity_to_be_updated)

        old_version_of_activity = self.activity_repository.chronological_list[index_of_activity]

        new_activity_attributes.append(id_of_activity_to_be_updated)
        new_version_of_activity = self.create_activity(new_activity_attributes)

        if not new_version_of_activity.list_of_persons:
            new_version_of_activity.list_of_persons = self.activity_repository.chronological_list[index_of_activity].list_of_persons
        if new_version_of_activity.description == "":
            new_version_of_activity.description = self.activity_repository.chronological_list[index_of_activity].description

        self.validator.validate_activity(new_version_of_activity)

        self.activity_repository.update_activity(index_of_activity, new_version_of_activity)
        undo_function = FunctionCall(self.activity_repository.update_activity, index_of_activity, old_version_of_activity)
        redo_function = FunctionCall(self.activity_repository.update_activity, index_of_activity, new_version_of_activity)
        self.undo_service.record_operation(Operation(undo_function, redo_function))

    def get_all_activities(self):
        """
        Calls the repository and returns the current list of activities
        """
        list_of_activities = self.activity_repository.get_all_activities()
        return list_of_activities

    def search_activities(self, search_key):
        """
        The method parses the list of activities and if there is a match between the search_key entered by the user and
        one of the fields date, time or description, appends the current activity to the list of resulted activities
        :param search_key: a string that can be either a whole description, date or time object or only parts of it
        :return: the list of activities that resulted during the search
        """
        resulted_activities = []

        for activity in self.get_all_activities():
            if re.search(search_key, str(activity.date)):
                resulted_activities.append(activity)
            elif re.search(search_key.lower(), activity.description.lower()):
                resulted_activities.append(activity)
            else:
                try:
                    if activity.start_time <= time(int(search_key)) <= activity.end_time:
                        resulted_activities.append(activity)
                except ValueError:
                    pass

        return resulted_activities

    def get_all_activities_in_a_day(self, user_date):
        """
        The method gets from the repository all activities that take place on a given date
        :param user_date: the date that the activities take place in
        :return: the list of activities
        """
        # check that the date is > = today
        if user_date < date.today():
            raise ValueError('The date must be today or in the future')

        # parse the list of activities until the first activity in the given day and append all the activities that come
        # afterwards and are still in the same day
        resulted_activities = []
        index = 0
        length_of_list_of_activities = len(self.get_all_activities())

        while self.get_all_activities()[index].date != user_date and index < length_of_list_of_activities:
            index = index + 1

        if index < length_of_list_of_activities:
            while self.get_all_activities()[index].date == user_date and index < length_of_list_of_activities:
                resulted_activities.append(self.get_all_activities()[index])
                index = index + 1

        # return the list
        return resulted_activities

    def get_the_busiest_days(self):
        """
        The method parses the list of activities in the repository and adds in a dictionary the date of each activity
        and the time spent for that activity. After the parsing is done, the pairs in the dictionary are added to a list
        as an instance of the DayWithFreeTime class. The list is then sorted in ascending order of the free time.
        :return: the sorted list of DayWithFreeTime objects
        """
        days_with_free_time_dictionary = {}
        resulted_days = []

        # calculate the amount of time on activities spent in each day
        for activity in self.activity_repository.get_all_activities():
            if activity.date not in days_with_free_time_dictionary:
                days_with_free_time_dictionary[activity.date] = timedelta(hours=23, minutes=59)

            days_with_free_time_dictionary[activity.date] = days_with_free_time_dictionary[activity.date] - activity.length_of_activity()

        # create an DayWithFreeTime instance for each key-value pair in the dictionary
        for day in days_with_free_time_dictionary:
            resulted_days.append(DayWithFreeTime(day, days_with_free_time_dictionary[day]))

        # sort the list in ascending order of the free time
        resulted_days.sort(key=lambda day: day.free_time)

        return resulted_days

    def get_all_activities_with_a_person(self, id_of_person):
        """
        The method parses the list of activities and appends to the list of results all activities in which the person
        with the given id will participate
        :param id_of_person: integer >= 0
        Raises an error if the id of the person is negative
        """
        if id_of_person < 0:
            raise ValueError('The id of a person should be a positive integer')

        resulted_activities = []

        if id_of_person > 0:
            for activity in self.get_all_activities():
                if id_of_person in activity.list_of_persons:
                    resulted_activities.append(activity)

        # If the id is zero, the method searches for activities that the user will do alone, without other persons
        elif id_of_person == 0:
            for activity in self.get_all_activities():
                if not activity.list_of_persons:
                    resulted_activities.append(activity)

        return resulted_activities


class DayWithFreeTime:
    """
    Data transfer object for the statistic of busiest days.
    """
    def __init__(self, date_in_the_calendar, amount_of_free_time):
        """
        :param date_in_the_calendar: instance of the date class
        :param amount_of_free_time: timedelta object representing the free time in a day
        """
        self._day = date_in_the_calendar
        self._free_time = amount_of_free_time

    @property
    def day(self):
        return self._day

    @property
    def free_time(self):
        return self._free_time

    def __str__(self):
        return 'Day: ' + str(self.day) + '  free time: ' + str(self.free_time)

