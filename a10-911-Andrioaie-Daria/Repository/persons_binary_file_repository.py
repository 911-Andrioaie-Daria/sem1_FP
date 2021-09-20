from Repository.person_repository import PersonRepository, PersonRepositoryException
import pickle


class PersonBinaryFileRepositoryException(PersonRepositoryException):
    def __init__(self, message):
        super().__init__(message)


class PersonsBinaryFileRepository(PersonRepository):
    def __init__(self, file_name='persons.pickle'):
        super().__init__()
        self._file_name = file_name
        self._load_from_binary_file()

    def add_new_person(self, new_person):
        super().add_new_person(new_person)
        self._save_to_binary_file()

    def remove_person(self, id_of_person):
        removed_person = super().remove_person(id_of_person)
        self._save_to_binary_file()

        return removed_person

    def update_person(self, index_of_person, new_version_of_person):
        super().update_person(index_of_person, new_version_of_person)
        self._save_to_binary_file()

    def _save_to_binary_file(self):
        binary_file = open(self._file_name, 'wb')
        try:
            pickle.dump(self.current_list, binary_file)
            binary_file.close()
        except Exception as exception_message:
            raise PersonBinaryFileRepositoryException(str(exception_message))

    def _load_from_binary_file(self):
        """
        Load data from file
        We assume file-saved data is valid
        """
        try:
            binary_file = open(self._file_name, 'rb')
            self.current_list = pickle.load(binary_file)
            binary_file.close()
        except EOFError:
            return
        except Exception as exception_message:
            raise PersonBinaryFileRepositoryException(str(exception_message))
