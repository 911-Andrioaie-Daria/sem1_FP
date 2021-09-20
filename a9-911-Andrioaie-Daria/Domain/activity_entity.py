from datetime import time, date, timedelta, datetime

import copy


class ActivityException(Exception):
    """
    Exception class for errors related to an activity.
    """
    def __init__(self, error_message):
        self.message = error_message


class Activity:
    """
    The class of activity entity.
    """
    def __init__(self, unique_id, list_of_persons_involved, calendaristic_date, start_time, end_time, description):
        """
        :param unique_id: a string of digits
        :param list_of_persons_involved: list of ids of Person instances
        :param calendaristic_date: uses the class date(year, month, day)
        :param start_time: the time of the start of the activity
        :param end_time: the time of the end of an activity
        """
        self.__unique_id = unique_id
        self._list_of_persons = list_of_persons_involved
        self._date = calendaristic_date
        self._start_time = start_time
        self._end_time = end_time
        self._description = description

    @property
    def unique_id(self):
        return self.__unique_id

    @property
    def list_of_persons(self):
        return self._list_of_persons

    @list_of_persons.setter
    def list_of_persons(self, new_list):
        self._list_of_persons = copy.deepcopy(new_list)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, new_date):
        self._date = new_date

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, new_time):
        self._start_time = new_time

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, new_time):
        self._end_time = new_time

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_description):
        self._description = new_description

    def length_of_activity(self):
        end_date_time = datetime.combine(self.date, self.end_time)
        start_date_time = datetime.combine(self.date, self.start_time)

        return end_date_time - start_date_time

    def __str__(self):
        """

        """
        string_of_ids_of_persons = ""
        for id_of_person in self.list_of_persons:
            string_of_ids_of_persons = string_of_ids_of_persons + str(id_of_person) + ', '

        if string_of_ids_of_persons == "":
            string_of_ids_of_persons = string_of_ids_of_persons + "nobody"
        else:
            string_of_ids_of_persons = string_of_ids_of_persons[:-2]

        return 'id: ' + str(self.unique_id) + '\npersons: ' + string_of_ids_of_persons + '\ndate: ' + \
               str(self.date) + '\nstart: ' + str(self.start_time) + ' end: ' + str(self.end_time) + '\ndescription: ' \
               + self.description


class ActivityValidator:
    """
    The class validates an activity.
    """

    def validate_id(self, unique_id):
        """
        The id must be a non-empty string of digits
        """
        if unique_id == "":
            raise ActivityException('The id should not be empty')

        if not isinstance(unique_id, int) or unique_id < 0:
            raise ActivityException('The id must be an integer')

    def validate_list_of_persons_involved(self, list_of_persons):
        """
        The list of persons must only have Person instances (this can be empty).
        Raises Activity exception otherwise.
        """
        for id_of_person in list_of_persons:
            if not isinstance(id_of_person, int):
                raise ActivityException('The list of ids of persons should only contain ids of existent persons.')

    def validate_date(self, activity_date):
        """
        The date must be today or in the future (field non empty).
        """
        if activity_date == "":
            raise ActivityException('The date field cannot be empty.')
        if not isinstance(activity_date, date):
            raise ActivityException('The date should have the specific format')
        if activity_date < date.today():
            raise ActivityException('You should stop living in the past :) try adding activities in the near future. '
                                    'Today is ' + str(date.today()))

    def validate_time(self, start_time, end_time):
        """
        Fields are not empty.
        The end time must be greater than the start time (field non empty)
        """
        if start_time == "" or end_time == "":
            raise ActivityException('You must complete both the start time and the end time of your activity')

        if end_time <= start_time:
            raise ActivityException('The ending time can only be after the start time.')

    def validate_description(self, activity_description):
        """
        The description is a non-empty string
        """
        if activity_description == "":
            raise ActivityException('Description field cannot be empty')

    def validate_activity(self, activity):
        self.validate_id(activity.unique_id)
        self.validate_list_of_persons_involved(activity.list_of_persons)
        self.validate_date(activity.date)
        self.validate_time(activity.start_time, activity.end_time)
        self.validate_description(activity.description)

