from datetime import date, time

from Domain.activity_entity import Activity
from Repository.activity_repository import ActivityRepository, ActivityRepositoryException


class ActivityTextFileRepositoryException(ActivityRepositoryException):
    def __init__(self, message):
        super().__init__(message)


class ActivityTextFileRepository(ActivityRepository):
    def __init__(self, file_name='activities.txt'):
        super().__init__()
        self._file_name = file_name
        self._load_from_text_file()

    def add_activity(self, new_activity):
        super().add_activity(new_activity)
        self._save_to_text_file()

    def remove_activity(self, id_of_activity):
        removed_activity = super().remove_activity(id_of_activity)
        self._save_to_text_file()

        return removed_activity

    def update_activity(self, index_of_activity, new_version_of_activity):
        super().update_activity(index_of_activity, new_version_of_activity)
        self._save_to_text_file()

    def _save_to_text_file(self):
        file = open(self._file_name, 'wt')
        try:
            for activity in self.chronological_list:
                string_list_of_persons = ""
                for person_id in activity.list_of_persons:
                    string_list_of_persons = string_list_of_persons + str(person_id) + " "
                line = str(activity.unique_id) + ';' + string_list_of_persons + ';' + str(activity.date) + ';' + \
                       str(activity.start_time) + ';' + str(activity.end_time) + ';' + activity.description
                file.write(line)
                file.write('\n')
            file.close()
        except Exception as error_message:
            raise ActivityTextFileRepositoryException(error_message)


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

                ids_of_persons_involved = line[1].split()
                ids_of_persons_involved = [int(person_id) for person_id in ids_of_persons_involved]

                date_attributes = line[2].split('-')
                year = int(date_attributes[0])
                month = int(date_attributes[1])
                day = int(date_attributes[2])
                date_of_activity = date(year, month, day)

                start_time_attributes = line[3].split(':')
                start_hour = int(start_time_attributes[0])
                start_minute = int(start_time_attributes[1])
                start_time = time(start_hour, start_minute)

                end_time_attributes = line[4].split(':')
                end_hour = int(end_time_attributes[0])
                end_minute = int(end_time_attributes[1])
                end_time = time(end_hour, end_minute)

                description = line[5].split('\n')
                super().add_activity(Activity(unique_id, ids_of_persons_involved, date_of_activity, start_time, end_time, description))

        except IOError as error_message:
            raise ActivityTextFileRepositoryException(error_message)