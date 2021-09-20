from Domain.person_entity import Person
from Repository.person_repository import PersonRepository, PersonRepositoryException


class PersonTextFileRepositoryException(PersonRepositoryException):
    def __init__(self, message):
        super().__init__(message)


class PersonTextFileRepository(PersonRepository):
    def __init__(self, file_name='persons.txt'):
        super().__init__()
        self._file_name = file_name
        self._load_from_text_file()

    def add_new_person(self, new_person):
        super().add_new_person(new_person)
        self._save_to_text_file()

    def remove_person(self, id_of_person):
        super().remove_person(id_of_person)
        self._save_to_text_file()

    def update_person(self, index_of_person, new_version_of_person):
        super().update_person(index_of_person, new_version_of_person)
        self._save_to_text_file()

    def _save_to_text_file(self):
        file = open(self._file_name, 'wt')
        try:
            for person in self.current_list:
                line = str(person.unique_id) + ';' + person.name + ';' + person.phone_number
                file.write(line)
                file.write('\n')
            file.close()
        except Exception as exception_message:
            raise PersonTextFileRepositoryException(exception_message)

    def _load_from_text_file(self):
        """
        Load data from file
        We assume file-saved data is valid
        """
        try:
            file = open(self._file_name, 'rt')  # read text
            lines = file.readlines()
            file.close()

            for line in lines:
                line = line.split(';')
                unique_id = int(line[0])

                name = line[1]
                phone_number = line[2].split('\n')

                super().add_new_person(Person(unique_id, name, phone_number))

        except IOError as error_message:
            raise PersonTextFileRepositoryException(error_message)
