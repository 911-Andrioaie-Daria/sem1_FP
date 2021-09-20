"""
3. Persons_repo + test_persons_repo + test_init (to add 10 persons at program start-up
    add, remove, update methods
"""
import re
import copy
import random

from Domain.person_entity import Person


def initialise_persons():
    """
    Randomly generates 10 valid Person instances.
    """
    list_of_persons = []

    list_of_surnames = ['Elliot', 'Collins', 'Baker', 'Allen', 'Adams', 'Smith', 'Harris', 'Johnson', 'Lee']
    list_of_forenames = ['Emily', 'Ben', 'Avery', 'Austin', 'Dorothy', 'Posie', 'Manilla', 'Jessica', 'Cole', 'Marc']

    for i in range(0, 10):
        person_id = i + 1

        person_surname = random.choice(list_of_surnames)
        person_forename = random.choice(list_of_forenames)
        person_name = person_forename + ' ' + person_surname

        phone_number = '0234' + str(random.randint(100, 999)) + str(random.randint(100, 999))

        new_person = Person(person_id, person_name, phone_number)
        list_of_persons.append(new_person)

    return list_of_persons


class PersonRepository:
    """
    The class which holds the list of persons and methods that can be done on the list of persons
    """
    def __init__(self):
        self._current_list_of_persons = initialise_persons()

    @property
    def current_list(self):
        return self._current_list_of_persons

    @current_list.setter
    def current_list(self, new_list):
        self._current_list_of_persons = copy.deepcopy(new_list)

    def __len__(self):
        return len(self.current_list)

    def add_new_person(self, new_person):
        """
        Appends a new Person instance to the current list of persons
        :param new_person: the person that is added at the end of the list
        :return:
        """
        self.current_list.append(new_person)

    def remove_person(self, id_of_person):
        """
        Removes from the list the Person instance with the given id
        :param id_of_person:
        """
        person_index = self.find_person_by_id(id_of_person)
        return self._current_list_of_persons.pop(person_index)

    def update_person(self, index_of_person, new_version_of_person):
        """
        Updates the person on the position 'index_of_person' in the list with a new version
        :param index_of_person: the position of the person whose data is being updated
        :param new_version_of_person: a Person instance having the required updates
        """
        self.current_list[index_of_person] = new_version_of_person

    def find_person_by_id(self, id_of_person):
        """
        Searches the list for a Person instance having the id passed as parameter and returns the index of this Person
        in the list
        :param id_of_person: integer
        errors: ValueError if the id couldn't be found in the list or if it is negative
        """
        if id_of_person < 0:
            raise ValueError('The id must be a positive integer')
        for index in range(0, len(self.current_list)):
            if id_of_person == self.current_list[index].unique_id:
                return index
        raise ValueError('The person does not exist in your list')

    def get_all_persons(self):
        """
        Returns the current list of persons
        :return:
        """
        return self.current_list

    def get_item(self, index_in_list):
        return self.current_list[index_in_list]

