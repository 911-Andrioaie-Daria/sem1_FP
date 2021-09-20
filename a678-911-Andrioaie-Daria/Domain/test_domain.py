import unittest
from datetime import date, time

from Domain.activity_entity import Activity, ActivityValidator, ActivityException
from Domain.person_entity import Person, PersonValidator, PersonException


class TestPerson(unittest.TestCase):

    def test_person(self):

        #test the constuctor
        new_person = Person(12, 'Ana Maria', '0234000000')
        self.assertEqual(new_person.unique_id, 12)
        self.assertEqual(new_person.name, 'Ana Maria')
        self.assertEqual(new_person.phone_number, '0234000000')

        #name setter
        new_person.name = 'John Smith'
        self.assertEqual(new_person.name, 'John Smith')

        #phone number setter
        new_person.phone_number = '0234'
        self.assertEqual(new_person.phone_number, '0234')


class TestPersonValidator(unittest.TestCase):

    def test_person_validator(self):
        validator = PersonValidator()

        # valid object
        person1 = Person(12, 'John Smith', '0764309596')
        validator.validate_person(person1)

        # id is negative
        person2 = Person(-1, 'John Smith', '0234000000')
        try:
            validator.validate_person(person2)
        except PersonException:
            pass

        # the name is not a string
        person3 = Person(3, 123, '0234000000')
        try:
            validator.validate_person(person3)
        except PersonException:
            pass

        # the name has characters other than letters
        person4 = Person(4, '$£ Ben', '0234000000')
        try:
            validator.validate_person(person4)
        except PersonException:
            pass

        # the name does not have 2 nouns
        person5 = Person(4, 'John', '0234123456')
        try:
            validator.validate_person(person5)
        except PersonException:
            pass

        # the phone number is not 10 digits long
        person6 = Person(4, 'James Smith', '1234')
        try:
            validator.validate_person(person6)
        except PersonException:
            pass

        # the phone number contains characters other than digits
        person7 = Person(4, 'James Smith', '@123000@@@')
        try:
            validator.validate_person(person7)
        except PersonException:
            pass


class TestActivity(unittest.TestCase):

    def test_activity(self):

        # the constructor
        new_activity = Activity(12, [1, 2, 3], date(2020, 11, 25), time(16, 30), time(20), 'This is an activity I created.')
        self.assertEqual(new_activity.unique_id, 12)
        self.assertEqual(new_activity.list_of_persons, [1, 2, 3])
        self.assertEqual(new_activity.date, date(2020, 11, 25))
        self.assertEqual(new_activity.start_time, time(16, 30))
        self.assertEqual(new_activity.end_time, time(20))
        self.assertEqual(new_activity.description, 'This is an activity I created.')

        # the str method
        printed_format = str(new_activity)
        self.assertEqual(printed_format, 'id: 12' + '\npersons: 1, 2, 3' + '\ndate: 2020-11-25' + '\nstart: 16:30:00' +
                         ' end: 20:00:00' + '\ndescription: This is an activity I created.')

        # the setters
        new_activity.list_of_persons = []
        self.assertEqual(new_activity.list_of_persons, [])

        new_activity.date = date(2020, 12, 1)
        self.assertEqual(new_activity.date, date(2020, 12, 1))

        new_activity.start_time = time(12)
        self.assertEqual(new_activity.start_time, time(12))

        new_activity.end_time = time(16)
        self.assertEqual(new_activity.end_time, time(16))

        new_activity.description = 'new description'
        self.assertEqual(new_activity.description, 'new description')

        printed_format = str(new_activity)
        self.assertEqual(printed_format, 'id: 12' + '\npersons: nobody' + '\ndate: 2020-12-01' + '\nstart: 12:00:00' +
                         ' end: 16:00:00' + '\ndescription: new description')


class TestActivityValidator(unittest.TestCase):

    def test_activity_validator(self):

        trustworthy_validator = ActivityValidator()

        # this activity should make no trouble
        activity1 = Activity(12, [1], date(2020, 11, 30), time(12, 30), time(15, 30), 'alabalaportocala')
        trustworthy_validator.validate_activity(activity1)

        # the id field must not be empty
        activity2 = Activity("", [], date(2020, 11, 1), time(12, 30), time(9), "")
        try:
            trustworthy_validator.validate_activity(activity2)
        except ActivityException:
            pass

        # the id must be a positive integer
        activity9 = Activity(-12, [1], date(2020, 11, 30), time(12, 30), time(15, 30), 'alabalaportocala')
        try:
            trustworthy_validator.validate_activity(activity9)
        except ActivityException:
            pass

        # the list of ids of persons must only contain integers
        activity3 = Activity(12, ['@:{'], date(2020, 11, 30), time(12, 30), time(15, 30), 'alabalaportocala')
        try:
            trustworthy_validator.validate_activity(activity3)
        except ActivityException:
            pass

        # the date field should not be empty
        activity4 = Activity(12, [1], "", time(12, 30), time(15, 30), 'alabalaportocala')
        try:
            trustworthy_validator.validate_activity(activity4)
        except ActivityException:
            pass

        # the date field should have the type date
        activity5 = Activity(12, [1], 2020, time(12, 30), time(15, 30), 'alabalaportocala')
        try:
            trustworthy_validator.validate_activity(activity5)
        except ActivityException:
            pass

        # the date cannot be in the past
        activity10 = Activity(12, [1], date(2020, 8, 1), time(12, 30), time(15, 30), 'alabalaportocala')
        try:
            trustworthy_validator.validate_activity(activity10)
        except ActivityException:
            pass

        # the start time field should not be empty
        activity6 = Activity(12, [1], date(2020, 11, 30), "", time(15, 30), 'alabalaportocala')
        try:
            trustworthy_validator.validate_activity(activity6)
        except ActivityException:
            pass

        # the start time must be before the end time
        activity7 = Activity(12, [1], date(2020, 11, 30), time(12), time(9), 'alabalaportocala')
        try:
            trustworthy_validator.validate_activity(activity7)
        except ActivityException:
            pass

        # the description field should not be empty
        activity8 = Activity(12, [1], date(2020, 11, 30), time(12, 30), time(15, 30), "")
        try:
            trustworthy_validator.validate_activity(activity8)
        except ActivityException:
            pass