"""
1. build person class + test_person_class + exception class

2. build PersonValidator + test_person_validator

"""


class PersonException(Exception):
    """
    Exception class for errors related to a person.
    """
    def __init__(self, exception_message):
        self.message = exception_message


class Person:
    """
    The class of a Person entity.
    """
    def __init__(self, person_unique_id, name, phone_number):

        self.__unique_id = person_unique_id
        self._name = name
        self._phone_number = phone_number

    @property
    def unique_id(self):
        return self.__unique_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    def __str__(self):
        return 'id: ' + str(self.unique_id) + ' name: ' + self.name + '      phone number: ' + str(self.phone_number)


class PersonValidator:
    """
    Class that validates a Person instance
    Name -> must be non empty string of letter with two nouns, the first and the last name
    ID -> must be a positive integer
    phone number -> must be a string of 10 digits
    """

    def validate_id(self, unique_id):
        """validate the id"""

        if not (isinstance(unique_id, int) and unique_id > 0):
            raise PersonException('The unique ID must be a positive integer')

    def validate_name(self, person_name):
        """validate the name"""

        if not isinstance(person_name, str):
            raise PersonException('The name must be a string.')
        person_name = person_name.strip()

        number_of_spaces = 0
        for character in person_name:
            if character != ' ':
                if not character.isalpha():
                    raise PersonException('1. The name must only contain letters and whitespaces')
            else:
                number_of_spaces = number_of_spaces + 1

        if number_of_spaces != 1:
            raise PersonException('The name must contain 2 nouns.')

    def validate_phone_number(self, phone_number):
        """validate the phone number"""

        if len(phone_number) != 10:
            raise PersonException('The phone number must have 10 digits')
        for digit in phone_number:
            if not digit.isnumeric():
                raise PersonException('The phone number must only contain digits')

    def validate_person(self, person):
        self.validate_id(person.unique_id)
        self.validate_name(person.name)
        self.validate_phone_number(person.phone_number)


