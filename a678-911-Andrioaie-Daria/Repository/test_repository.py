import unittest
from datetime import date, time

from Repository.person_repository import PersonRepository
from Domain.person_entity import Person

from Repository.activity_repository import ActivityRepository
from Domain.activity_entity import Activity, ActivityException

"""
Here I implement the tests for person repository and activity repository
"""


class TestPersonRepository(unittest.TestCase):

    def setUp(self):
        self._person_repository = PersonRepository()

    def test_add_new_person(self):
        person1 = Person(12, 'Ana Maria', '0234000000')
        self._person_repository.add_new_person(person1)

        self.assertEqual(len(self._person_repository), 11)

    def test_remove_person(self):
        index_of_the_person_to_be_removed = 1
        self._person_repository.remove_person(index_of_the_person_to_be_removed)

        self.assertEqual(len(self._person_repository), 9)

    def test_update_person(self):
        new_version_of_person = Person(12, 'Ana Maria', '0234000000')
        index_of_person_to_be_updated = 1

        self._person_repository.update_person(index_of_person_to_be_updated, new_version_of_person)
        self.assertEqual(self._person_repository.current_list[index_of_person_to_be_updated], new_version_of_person)

    def test_find_person_by_id(self):

        # this should create no trouble
        id_of_person = 9
        index_of_person = self._person_repository.find_person_by_id(id_of_person)

        # the id must raise a ValueError
        try:
            id_of_person = -2
            index_of_person = self._person_repository.find_person_by_id(id_of_person)
        except ValueError:
            pass

        # the id does not exist
        try:
            id_of_person = 50
            index_of_person = self._person_repository.find_person_by_id(id_of_person)
        except ValueError:
            pass

        self.assertEqual(index_of_person, 8)

    def test_get_all_persons(self):
        list_of_persons = self._person_repository.get_all_persons()
        self.assertEqual(list_of_persons, self._person_repository.current_list)


class TestActivityRepository(unittest.TestCase):

    def setUp(self):
        self._activity_repository = ActivityRepository()
        my_list_of_activities = [
            Activity(1, [1, 2, 3], date(2020, 12, 15), time(9), time(12), 'this is the first activity'),
            Activity(2, [], date(2020, 12, 16), time(9), time(12), 'this is the first activity'),
            Activity(3, [1, 3, 5, 9], date(2020, 12, 17), time(9), time(12), 'this is the first activity'),
            Activity(4, [10], date(2020, 12, 18), time(9), time(12), 'this is the first activity'),
            Activity(5, [3], date(2020, 12, 19), time(9), time(12), 'this is the first activity'),
            Activity(6, [], date(2020, 12, 20), time(9), time(12), 'this is the first activity'),
            Activity(7, [2], date(2020, 12, 21), time(9), time(12), 'this is the first activity'),
            Activity(8, [], date(2020, 12, 22), time(9), time(12), 'this is the first activity'),
            Activity(9, [1], date(2020, 12, 23), time(9), time(12), 'this is the first activity'),
            Activity(10, [5, 7, 3], date(2020, 12, 24), time(9), time(12), 'this is the first activity')]
        self._activity_repository.chronological_list = my_list_of_activities
        self._activity_repository.available_id = 11

    def test_add_activity(self):
        activity1 = Activity(11, [1, 2, 3], date(2020, 12, 26), time(9), time(12), 'this is a new activity')
        self._activity_repository.add_activity(activity1)

        self.assertEqual(len(self._activity_repository), 11)

        # this should raise an Activity exception, since it is during the same time as activity 1
        activity2 = Activity(12, [1, 2, 3], date(2020, 12, 15), time(10), time(11), 'this is a new activity')
        try:
            self._activity_repository.add_activity(activity2)
        except ActivityException:
            pass

        activity3 = Activity(13, [1, 2, 3], date(2020, 12, 25), time(10), time(11), 'this is a new activity')
        self._activity_repository.add_activity(activity3)

        activity4 = Activity(14, [1, 2, 3], date(2020, 12, 1), time(10), time(11), 'this is a new activity')
        self._activity_repository.add_activity(activity4)

        activity5 = Activity(15, [1, 2, 3], date(2020, 12, 1), time(6), time(8), 'this is a new activity')
        self._activity_repository.add_activity(activity5)

        activity6 = Activity(16, [1, 2, 3], date(2020, 12, 1), time(8), time(9), 'this is a new activity')
        self._activity_repository.add_activity(activity6)

        activity7 = Activity(17, [1, 2, 3], date(2020, 12, 1), time(20), time(21), 'this is a new activity')
        self._activity_repository.add_activity(activity7)


    def test_find_activity_by_id(self):
        id_of_activity = -2
        try:
            self._activity_repository.find_activity_by_id(id_of_activity)
        except ActivityException:
            pass

        id_of_activity = 50
        try:
            self._activity_repository.find_activity_by_id(id_of_activity)
        except ActivityException:
            pass

        id_of_activity = 7
        index_of_activity = self._activity_repository.find_activity_by_id(id_of_activity)
        self.assertEqual(index_of_activity, 6)


    def test_remove_activity(self):
        id_of_activity = 6
        self._activity_repository.remove_activity(id_of_activity)
        self.assertEqual(len(self._activity_repository), 9)

    def test_update_activity(self):
        index_of_activity = 9
        new_version_of_activity = Activity(10, [], date(2020, 12, 24), time(9), time(12), 'this is the updated activity')
        self._activity_repository.update_activity(index_of_activity, new_version_of_activity)
        self.assertEqual(self._activity_repository.chronological_list[index_of_activity].description, 'this is the updated activity')

        index_of_activity = 8
        new_version_of_activity = Activity(10, [], date(2020, 12, 21), time(9), time(12),
                                           'this is the updated activity')
        try:
            self._activity_repository.update_activity(index_of_activity, new_version_of_activity)
        except ActivityException:
            pass

    def test_get_all_activities(self):
        list_of_activities = self._activity_repository.get_all_activities()
        self.assertEqual(list_of_activities, self._activity_repository.chronological_list)