import unittest
from datetime import date, time

from Service.undo_service import UndoService
from Service.person_service import PersonService
from Service.activity_service import ActivityService, DayWithFreeTime

"""
Here I do the testing for the person_service and activity_service
"""


class TestPersonService(unittest.TestCase):

    def setUp(self):
        undo_service = UndoService()
        self._person_service = PersonService(undo_service)

    def test_add_person(self):
        list_of_person_attributes = ['Ana Maria', '0234123456']
        self._person_service.add_person(list_of_person_attributes)

        self.assertEqual(len(self._person_service.repository), 11)

    def test_remove_person(self):
        id_of_person = 5
        self._person_service.remove_person(id_of_person)

        self.assertEqual(len(self._person_service.repository), 9)

    def test_update_person(self):
        id_of_person = 5
        list_of_person_attributes = ['Ana Maria', '0234123456']
        self._person_service.update_person(id_of_person, list_of_person_attributes)

        self.assertEqual(self._person_service.repository.current_list[4].name, 'Ana Maria')
        self.assertEqual(self._person_service.repository.current_list[4].phone_number, '0234123456')

        id_of_person = 5
        list_of_person_attributes = ["", ""]

        initial_name = self._person_service.repository.current_list[4].name
        initial_phone_number = self._person_service.repository.current_list[4].phone_number

        self._person_service.update_person(id_of_person, list_of_person_attributes)
        self.assertEqual(self._person_service.repository.current_list[4].name, initial_name)
        self.assertEqual(self._person_service.repository.current_list[4].phone_number, initial_phone_number)

    def test_get_all_persons(self):
        list_of_persons = self._person_service.get_all_persons()

        self.assertEqual(list_of_persons, self._person_service.repository.current_list)

    def test_search_by(self):
        search_key = '0234'
        resulted_persons = self._person_service.search_person_by(search_key)

        self.assertEqual(resulted_persons, self._person_service.repository.current_list)



class TestActivityService(unittest.TestCase):

    def setUp(self):
        undo_service = UndoService()
        self._activity_service = ActivityService(undo_service)

    def test_create_activity(self):
        new_activity_attributes = [[1, 2, 16], date(2020, 12, 30), time(9), time(12), 'this is a new activity', 6]
        new_activity = self._activity_service.create_activity(new_activity_attributes)

        self.assertEqual(new_activity.unique_id, 6)
        self.assertEqual(new_activity.list_of_persons, [1, 2])
        self.assertEqual(new_activity.date, date(2020, 12, 30))
        self.assertEqual(new_activity.start_time, time(9))
        self.assertEqual(new_activity.end_time, time(12))
        self.assertEqual(new_activity.description, 'this is a new activity')

    def test_add_new_activity(self):
        new_activity_attributes = [[1, 2, 16], date(2020, 12, 30), time(9), time(12), 'this is a new activity']
        self._activity_service.add_new_activity(new_activity_attributes)

        self.assertEqual(len(self._activity_service.activity_repository), 11)

    def test_remove_activity(self):
        id_of_activity = 8
        self._activity_service.remove_activity(id_of_activity)

        self.assertEqual(len(self._activity_service.activity_repository), 9)

    def test_update_activity(self):
        id_of_activity_to_be_updated = 5
        new_activity_attributes = [[], date(2020, 12, 30), time(9), time(12), ""]

        initial_description = self._activity_service.activity_repository.chronological_list[4].description
        self._activity_service.update_activity(id_of_activity_to_be_updated, new_activity_attributes)

    def test_get_all_activities(self):
        resulted_activities = self._activity_service.get_all_activities()
        self.assertEqual(resulted_activities, self._activity_service.activity_repository.chronological_list)


    def test_search_activities(self):
        search_key = '2020-12-18'
        list_of_resulted_activities = self._activity_service.search_activities(search_key)
        self.assertIsNotNone(list_of_resulted_activities)

        search_key = 'activity'
        list_of_resulted_activities = self._activity_service.search_activities(search_key)
        self.assertIsNotNone(list_of_resulted_activities)

        search_key = '10'
        list_of_resulted_activities = self._activity_service.search_activities(search_key)
        self.assertIsNotNone(list_of_resulted_activities)

    def test_get_all_activities_on_day(self):
        given_date = date(2020, 12, 8)
        list_of_resulted_activities = self._activity_service.get_all_activities_in_a_day(given_date)
        self.assertIsNotNone(list_of_resulted_activities)

    def test_get_all_activities_with_one_person(self):
        id_of_person = 3
        list_of_resulted_activities = self._activity_service.get_all_activities_with_a_person(id_of_person)
        self.assertIsNotNone(list_of_resulted_activities)

        id_of_person = 0
        list_of_resulted_activities = self._activity_service.get_all_activities_with_a_person(id_of_person)
        self.assertIsNotNone(list_of_resulted_activities)


class TestDayWithFreeTime(unittest.TestCase):

    def setUp(self):
        self._day_with_free_time = DayWithFreeTime(date(2020, 12, 1), 14)

    def test_properties(self):
        self.assertEqual(self._day_with_free_time.day, date(2020, 12, 1))
        self.assertEqual(self._day_with_free_time.free_time, 14)

        self.assertEqual(str(self._day_with_free_time), 'Day: 2020-12-01  free time: 14')



















