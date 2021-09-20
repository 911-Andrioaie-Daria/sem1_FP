from Repository.activity_repository import ActivityRepository, ActivityRepositoryException
import pickle


class ActivityBinaryFileRepositoryException(ActivityRepositoryException):
    def __init__(self, message):
        super().__init__(message)


class ActivityBinaryFileRepository(ActivityRepository):
    def __init__(self, file_name='activities.pickle'):
        super().__init__()
        self._file_name = file_name
        self._load_from_binary_file()

    def add_activity(self, new_activity):
        super().add_activity(new_activity)
        self._save_to_binary_file()

    def remove_activity(self, id_of_activity):
        super().remove_activity(id_of_activity)
        self._save_to_binary_file()

    def update_activity(self, index_of_activity, new_version_of_activity):
        super().update_activity(index_of_activity, new_version_of_activity)
        self._save_to_binary_file()

    def _save_to_binary_file(self):
        binary_file = open(self._file_name, 'wb')
        try:
            pickle.dump(self.chronological_list, binary_file)
            binary_file.close()
        except Exception as exception_message:
            raise ActivityBinaryFileRepositoryException(str(exception_message))


    def _load_from_binary_file(self):
        """
        Load data from file
        We assume file-saved data is valid
        """
        binary_file = open(self._file_name, 'rb')  # read text
        try:
            self.chronological_list = pickle.load(binary_file)
            binary_file.close()
        except EOFError:
            return
        except Exception as exception_message:
            raise ActivityBinaryFileRepositoryException(str(exception_message))