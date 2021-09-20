from UI.console import ConsoleUI
from UI.graphical import GraphicalUI

from Repository.person_repository import PersonRepository
from Repository.person_text_file_repository import PersonTextFileRepository
from Repository.persons_binary_file_repository import PersonsBinaryFileRepository

from Repository.activity_repository import ActivityRepository
from Repository.activity_text_file_repository import ActivityTextFileRepository
from Repository.activity_binary_file_repository import ActivityBinaryFileRepository

from Domain.activity_entity import ActivityValidator
from Domain.person_entity import PersonValidator

from Service.person_service import PersonService
from Service.activity_service import ActivityService
from Service.undo_service import UndoService

from jproperties import Properties


class PropertiesConfiguration:
    def __init__(self):
        self._configurations = Properties()
        self._file_name = 'settings.properties'

        settings_file = open(self._file_name, 'rb')
        self._configurations.load(settings_file)

        try:
            self._repository_type = self._configurations.get("repository").data
            self._persons_repository_file_name = self._configurations.get('persons').data
            self._activities_repository_file_name = self._configurations.get('activities').data
            self._UI_type = self._configurations.get("user_interface").data
        except KeyError as ke:
            print(ke)
            exit(0)

    def start_with_binary_repository(self):
        persons_repository = PersonsBinaryFileRepository(self._persons_repository_file_name)

        persons_repository.initialise_persons()
        persons_repository._save_to_binary_file()

        activities_repository = ActivityBinaryFileRepository(self._activities_repository_file_name)

        activities_repository.initialise_10_activities()
        activities_repository._save_to_binary_file()

        return persons_repository, activities_repository

    def start_in_memory_repository(self):
        persons_repository = PersonRepository()
        activity_repository = ActivityRepository()

        persons_repository.initialise_persons()
        activity_repository.initialise_10_activities()

        return persons_repository, activity_repository

    def start_with_text_file_repository(self):
        persons_repository = PersonTextFileRepository(self._persons_repository_file_name)

        persons_repository.initialise_persons()
        persons_repository._save_to_text_file()

        activities_repository = ActivityTextFileRepository(self._activities_repository_file_name)
        activities_repository.initialise_10_activities()
        activities_repository._save_to_text_file()

        return persons_repository, activities_repository

    def start_program(self):
        if self._repository_type == 'binary_files' and self._persons_repository_file_name == 'persons.pickle' and self._activities_repository_file_name == 'activities.pickle':
            persons_repository, activities_repository = self.start_with_binary_repository()
        if self._repository_type == 'inmemory' and self._persons_repository_file_name == "" and self._activities_repository_file_name == "":
            persons_repository, activities_repository = self.start_in_memory_repository()
        if self._repository_type == 'text_files' and self._persons_repository_file_name == 'persons.txt' and self._activities_repository_file_name == 'activities.txt':
            persons_repository, activities_repository = self.start_with_text_file_repository()

        person_validator = PersonValidator()
        activity_validator = ActivityValidator()

        undo_service = UndoService()
        persons_service = PersonService(persons_repository, person_validator, undo_service)
        activity_service = ActivityService(activities_repository, persons_repository, activity_validator, undo_service)

        if self._UI_type == 'GUI':
            start_command = GraphicalUI(undo_service, persons_service, activity_service)
            start_command.start()

        if self._UI_type == 'console':
            start_command = ConsoleUI(undo_service, persons_service, activity_service)
            start_command.start()
