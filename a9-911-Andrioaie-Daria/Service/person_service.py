import re

from Domain.person_entity import Person
from Service.undo_service import FunctionCall, Operation


class PersonService:
    """
    The class that implements the service of functionalities related to the list of persons
    """
    def __init__(self, person_repository, person_validator, undo_service):
        self._repository = person_repository
        self._validator = person_validator
        self._undo_service = undo_service

    @property
    def repository(self):
        return self._repository

    @property
    def validator(self):
        return self._validator

    @property
    def undo_service(self):
        return self._undo_service

    def add_person(self, list_of_person_attributes):
        """
        The method takes a list of person attributes, creates a new Person instance, validates it and passes
        it to the persons repository to be added to the list
        :param list_of_person_attributes: contains the name of the person and his or her phone number
        """

        unique_id = self.repository.current_list[-1].unique_id + 1
        name_of_person = list_of_person_attributes[0]
        phone_number_of_person = list_of_person_attributes[1]

        new_person = Person(unique_id, name_of_person, phone_number_of_person)
        self.validator.validate_person(new_person)

        self.repository.add_new_person(new_person)
        undo_function = FunctionCall(self.repository.remove_person, unique_id)
        redo_function = FunctionCall(self.repository.add_new_person, new_person)
        self.undo_service.record_operation(Operation(undo_function, redo_function))


    def remove_person(self, id_of_person):
        """
        The method searches for the person with the given id in the repository and passes the index of this person to
        the persons repository in order to perform the actual removal from the list
        :param id_of_person: integer
        """

        removed_person = self.repository.remove_person(id_of_person)

        undo_function = FunctionCall(self.repository.add_new_person, removed_person)
        redo_function = FunctionCall(self.repository.remove_person, id_of_person)
        self.undo_service.record_operation(Operation(undo_function, redo_function))

    def update_person(self, id_of_person, list_of_new_attributes):
        """
        The method creates a new Person instance having the attributes passes as parameters, validates it and passes
        the new person to the repository in order to update the person with the given id
        :param id_of_person: the id of the person who must be updated
        :param list_of_new_attributes: the new name and the new phone number of the person
        If these attributes are empty, then they are considered to be the same as in the initial version of the person
        """
        index_of_person_to_be_updated = self.repository.find_person_by_id(id_of_person)
        old_version_of_person = self.repository.get_item(index_of_person_to_be_updated)

        new_name = list_of_new_attributes[0]
        if new_name == "":
            new_name = self.repository.current_list[index_of_person_to_be_updated].name

        new_phone_number = list_of_new_attributes[1]
        if new_phone_number == "":
            new_phone_number = self.repository.current_list[index_of_person_to_be_updated].phone_number

        new_version_of_person = Person(id_of_person, new_name, new_phone_number)

        self.validator.validate_person(new_version_of_person)

        self.repository.update_person(index_of_person_to_be_updated, new_version_of_person)
        undo_function = FunctionCall(self.repository.update_person, index_of_person_to_be_updated, old_version_of_person)
        redo_function = FunctionCall(self.repository.update_person, index_of_person_to_be_updated, new_version_of_person)
        self.undo_service.record_operation(Operation(undo_function, redo_function))

    def get_all_persons(self):
        """
        Calls the repository and gets the current list of persons.
        :return: the list obtained from the rpeository
        """
        list_of_of_persons = self.repository.get_all_persons()
        return list_of_of_persons

    def search_person_by(self, search_key):
        """
                The method parses the list of persons and checks if the name or the phone number of the person matches (even
                partially) with the search key and appends this to the list of persons resulted in the search
                :param search_key: a string
                :return: the list of resulted persons
                """

        search_result = []
        for person in self.get_all_persons():
            if re.search(search_key.lower(), person.name.lower()) or re.search(search_key, person.phone_number):
                search_result.append(person)

        return search_result
