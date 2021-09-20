"""
3. activity repository + test activity repository + initialise_activities
"""
import copy
from random import randint, sample, choice
from datetime import date, time, timedelta

from Domain.activity_entity import Activity, ActivityException


def initialise_10_activities():
    """
    The function randomly generates a list of 10 valid Activity instances in 10 consecutive days.
    :return: the list of activities
    """

    list_of_descriptions = ['movies', 'jog in the park', 'read ten pages', 'dinner in town', 'yoga session',
                            'study session', 'choir rehearsals']

    list_of_activities = []
    for index in range(0, 10):
        unique_id = index + 1

        number_of_persons = randint(0, 10)
        persons_involved_in_activity = sample(range(1, 11), number_of_persons)

        date_of_activity = date.today() + timedelta(days=index)

        start_hour = randint(0, 22)
        start_of_activity = time(start_hour)

        end_hour = randint(start_hour+1, 23)
        end_of_activity = time(end_hour)
        description = choice(list_of_descriptions)

        new_activity = Activity(unique_id, persons_involved_in_activity, date_of_activity, start_of_activity,
                                end_of_activity, description)
        list_of_activities.append(new_activity)

    return list_of_activities


class ActivityRepository:

    def __init__(self):
        self._chronological_list_of_activities = initialise_10_activities()
        self._available_id = 11

    @property
    def chronological_list(self):
        return self._chronological_list_of_activities

    @chronological_list.setter
    def chronological_list(self, new_list):
        self._chronological_list_of_activities = copy.deepcopy(new_list)

    @property
    def available_id(self):
        return self._available_id

    @available_id.setter
    def available_id(self, new_value):
        self._available_id = new_value

    def __len__(self):
        return len(self.chronological_list)

    def find_available_gap_in_list(self, new_activity):
        """
        The method performs a binary search on the list of activities sorted chronologically in order to find
        an activity in the same day as the new activity that is to be added.

        Case 1: if there are no activities in the same day, it means that the new activity will not overlap with
        anything and the function returns the index where it should be added among the other activities

        Case 2: if there are activities in the same day, we move backwards in the list to the first activity in the day
        and check if there is a gap of free time between two consecutive activities.
        If the gap was found, it returns the index where the activity should be inserted.
        If it wasn't found, it means that the new activity overlaps with some other existing activity and an
        ActivityException is raised.

        :param new_activity: the activity for which we want to find and available gap in the list
        :return: the index of the position where the activity can be inserted in the list
        """
        day_of_activity = new_activity.date

        start_index = 0
        end_index = len(self.chronological_list)-1
        found_activity_in_the_given_day = False

        while start_index <= end_index and not found_activity_in_the_given_day:

            middle_of_list = (start_index + end_index) // 2

            if self.chronological_list[middle_of_list].date == day_of_activity:
                found_activity_in_the_given_day = True
            elif self.chronological_list[middle_of_list]. date < day_of_activity:
                start_index = middle_of_list + 1
            elif self.chronological_list[middle_of_list].date > day_of_activity:
                end_index = middle_of_list - 1

        # if there are no activities in the same day, it means that the new activity will not overlap with anything
        # and the function returns the index where it should be added among the other activities
        if not found_activity_in_the_given_day:

            # before the first activity
            if day_of_activity < self.chronological_list[0].date:
                return 0
            # after the last activity
            elif day_of_activity > self.chronological_list[-1].date:
                return len(self.chronological_list)
            # somewhere in the middle
            else:
                return end_index

        # if there are activities in the same day, we move backwards in the list to the first activity in the day
        else:
            insertion_index = 0
            current_index = middle_of_list
            found_gap = False

            while self.chronological_list[current_index].date == day_of_activity:
                current_index = current_index - 1
            current_index = current_index + 1

            # case 1:  the new activity ends before the first activity in the day starts
            if new_activity.end_time <= self.chronological_list[current_index].start_time:
                found_gap = True
                insertion_index = current_index

            # case 2: the new activity can be fitted between two activities in the same day
            while not found_gap and current_index < len(self.chronological_list)-1 and self.chronological_list[current_index + 1].date == day_of_activity:
                if new_activity.start_time >= self.chronological_list[current_index].end_time and \
                        new_activity.end_time <= self.chronological_list[current_index+1].start_time:
                    found_gap = True
                    insertion_index = current_index + 1
                else:
                    current_index = current_index + 1
            # case 3: the new activity starts after the end of the last activity in the day
            if not found_gap:
                if self.chronological_list[current_index].end_time <= new_activity.start_time:
                    found_gap = True
                    insertion_index = current_index + 1

            # final conclusion:
            if found_gap:
                return insertion_index
            else:
                raise ActivityException('You are busy during that time. Try clearing up the desired interval or finding'
                                        'another time for your activity.')

    def add_activity(self, new_activity):
        """
        The method finds the index where the new activity can be inserted in the list of activities and perform the
        insertion at this index
        :param new_activity:
        """
        insertion_index = self.find_available_gap_in_list(new_activity)
        self.chronological_list.insert(insertion_index, new_activity)

        # if add was done successfully, the available id is incremented
        self._available_id = self._available_id + 1

    def find_activity_by_id(self, id_of_activity):
        """
        The method searches for the position in the list of the activity with the given index.
        :return: the index of the activity in the list
        :error: Raises Activity exception in case that the activity with the given ID is not in the list
        """
        if id_of_activity < 0:
            raise ActivityException('The id of an activity is a positive integer')
        for index in range(0, len(self.chronological_list)):
            if id_of_activity == self.chronological_list[index].unique_id:
                return index
        raise ActivityException('The activity with the given id is not in your planner')

    def remove_activity(self, id_of_activity):
        """
        The method finds the index where the activity with the given is in the list and removes the activity at this
        index in the list
        """
        index_of_activity = self.find_activity_by_id(id_of_activity)
        return self.chronological_list.pop(index_of_activity)

    def update_activity(self, index_of_activity, new_version_of_activity):
        """
        The method updates an activity at the given index in the list with a new version of the activity

        If the new activity is at a different time from the old version of activity, the program tries to find
        an available gap of free time among the other activities. If there is no gap available, then the activity
        remains unchanged
        """
        old_version_of_activity = self.chronological_list[index_of_activity]

        if old_version_of_activity.date != new_version_of_activity.date or old_version_of_activity.start_time != new_version_of_activity.start_time or old_version_of_activity.end_time:
            try:
                self.chronological_list.pop(index_of_activity)
                insertion_index = self.find_available_gap_in_list(new_version_of_activity)
                self.chronological_list.insert(insertion_index, new_version_of_activity)

            except ActivityException:
                self.chronological_list.insert(index_of_activity, old_version_of_activity)

        else:
            # the list of persons and the description are updated
            old_version_of_activity.list_of_persons = new_version_of_activity.list_of_persons
            old_version_of_activity.description = new_version_of_activity.description

    def get_all_activities(self):
        """
        Returns the list of activities from the repository
        """
        return self.chronological_list
