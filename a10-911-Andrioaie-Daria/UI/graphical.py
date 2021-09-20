from datetime import date, time
from tkinter import *
from tkinter import messagebox


class GraphicalUI:
    """
    Implement the graphic user interface for add/list students
    """

    def __init__(self, undo_service, persons_service, activities_service):
        self.tk = Tk()
        self._undo_service = undo_service
        self._persons_service = persons_service
        self._activity_service = activities_service

    def start(self):
        self.tk.title("My first GUI :)")

# ----------------------------------------- PERSONS BUTTONS ----------------------------------------------------------

        persons_buttons_frame = Frame(self.tk)
        persons_buttons_frame.pack()

        self.list_persons_button = Button(persons_buttons_frame, text="List", command=self.display_list_of_persons, width=10, borderwidth=3, relief= RAISED)
        self.list_persons_button.pack(side=LEFT, pady=20, padx=5)

        self.add_person_button = Button(persons_buttons_frame, text="Add person", command=self.add_person_to_list_ui)
        self.add_person_button.pack(side=LEFT, padx=5)

        self.remove_person_button = Button(persons_buttons_frame, text="Remove person", command=self.remove_person_ui)
        self.remove_person_button.pack(side=LEFT, padx=5)

        self.update_person_button = Button(persons_buttons_frame, text="Update person", command=self.update_person_ui)
        self.update_person_button.pack(side=LEFT, padx=5)

        self.search_persons_button = Button(persons_buttons_frame, text="Search persons", command=self.search_for_person_ui)
        self.search_persons_button.pack(side=LEFT, padx=5)


# ----------------------------------------- PERSONS ENTRIES ------------------------------------------------------------

        persons_entries_frame = Frame(self.tk)
        persons_entries_frame.pack()

        label = Label(persons_entries_frame, text="ID:", background="#34A2FE")
        label.pack(side=LEFT, pady=5)

        self.person_id_entry = Entry(persons_entries_frame, {}, width=7)
        self.person_id_entry.pack(side=LEFT, padx=5)

        label = Label(persons_entries_frame, text="Name:")
        label.pack(side=LEFT)

        self.name_entry = Entry(persons_entries_frame, {})
        self.name_entry.pack(side=LEFT, padx=5)

        label = Label(persons_entries_frame, text="Phone number:")
        label.pack(side=LEFT)

        self.phone_number_entry = Entry(persons_entries_frame, {})
        self.phone_number_entry.pack(side=LEFT, padx=5)

# ----------------------------------------- ACTIVITIES BUTTONS ---------------------------------------------------------

        activities_buttons_frame = Frame(self.tk)
        activities_buttons_frame.pack()

        self.add_activity_button = Button(activities_buttons_frame, text="Add activity", command=self.add_activity_ui)
        self.add_activity_button.pack(side=LEFT,pady=20, padx=5)

        self.remove_activity_button = Button(activities_buttons_frame, text="Remove activity", command=self.remove_activity_ui)
        self.remove_activity_button.pack(side=LEFT, padx=5)

        self.update_activity_button = Button(activities_buttons_frame, text="Update activity", command=self.update_activity_ui)
        self.update_activity_button.pack(side=LEFT, padx=5)

        self.list_activities_button = Button(activities_buttons_frame, text="List activities", command=self.display_activities_ui)
        self.list_activities_button.pack(side=LEFT, padx=5)

        self.search_activities_button = Button(activities_buttons_frame, text="Search activities", command=self.search_activities_ui)
        self.search_activities_button.pack(side=LEFT, padx=5)

        self.list_activities_in_a_given_day_button = Button(activities_buttons_frame, text="List activities in a given day",
                                                            command=self.list_activities_in_a_given_day_ui)
        self.list_activities_in_a_given_day_button.pack(side=LEFT, padx=5)

        self.list_busiest_days_button = Button(activities_buttons_frame, text="List busiest days",
                                                            command=self.list_busiest_days_ui)
        self.list_busiest_days_button.pack(side=LEFT, padx=5)

        self.list_activities_with_a_given_person_button = Button(activities_buttons_frame, text="List activities with a person",
                                                            command=self.list_activities_with_a_given_person_ui)
        self.list_activities_with_a_given_person_button.pack(side=LEFT, padx=5)

# ----------------------------------------- ACTIVITIES ENTRIES ---------------------------------------------------------

        activities_entries_frame = Frame(self.tk)
        activities_entries_frame.pack()

        label = Label(activities_entries_frame, text="ID:", background="#34A2FE")
        label.pack(side=LEFT)

        self.activity_id_entry = Entry(activities_entries_frame, {}, width=5)
        self.activity_id_entry.pack(side=LEFT, pady=10, padx=5)

        label = Label(activities_entries_frame, text="List of persons:")
        label.pack(side=LEFT)

        self.persons_entry = Entry(activities_entries_frame, {})
        self.persons_entry.pack(side=LEFT, padx=5)

        label = Label(activities_entries_frame, text="Year:")
        label.pack(side=LEFT)

        self.year_of_activity_entry = Entry(activities_entries_frame, {}, width=7)
        self.year_of_activity_entry.pack(side=LEFT, padx=5)

        label = Label(activities_entries_frame, text="Month:")
        label.pack(side=LEFT)

        self.month_of_activity_entry = Entry(activities_entries_frame, {}, width=5)
        self.month_of_activity_entry.pack(side=LEFT, padx=5)

        label = Label(activities_entries_frame, text="Day:")
        label.pack(side=LEFT)

        self.day_of_activity_entry = Entry(activities_entries_frame, {}, width=5)
        self.day_of_activity_entry.pack(side=LEFT, padx=5)

        label = Label(activities_entries_frame, text="Start hour:")
        label.pack(side=LEFT)

        self.start_hour_of_activity_entry = Entry(activities_entries_frame, {}, width=5)
        self.start_hour_of_activity_entry.pack(side=LEFT, padx=5)

        label = Label(activities_entries_frame, text="Start minute:")
        label.pack(side=LEFT)

        self.start_minute_of_activity_entry = Entry(activities_entries_frame, {}, width=5)
        self.start_minute_of_activity_entry.pack(side=LEFT, padx=5)

        label = Label(activities_entries_frame, text="End hour:")
        label.pack(side=LEFT)

        self.end_hour_of_activity_entry = Entry(activities_entries_frame, {}, width=5)
        self.end_hour_of_activity_entry.pack(side=LEFT, padx=5)

        label = Label(activities_entries_frame, text="End minute:")
        label.pack(side=LEFT)

        self.end_minute_of_activity_entry = Entry(activities_entries_frame, {}, width=5)
        self.end_minute_of_activity_entry.pack(side=LEFT, padx=5)

        label = Label(activities_entries_frame, text="Description:")
        label.pack(side=LEFT)

        self.description_of_activity_entry = Entry(activities_entries_frame, {})
        self.description_of_activity_entry.pack(side=LEFT, padx=5)

# ----------------------------------------- UNDO-REDO BUTTONS ----------------------------------------------------------

        undo_redo_frame = Frame(self.tk)
        undo_redo_frame.pack()

        self.undo_button = Button(undo_redo_frame, text="UNDO", command=self.undo_operation_ui)
        self.undo_button.pack(side=LEFT, pady=20, padx=10)

        self.redo_button = Button(undo_redo_frame, text="REDO", command=self.redo_operation_ui)
        self.redo_button.pack(side=LEFT, padx=10)

# ----------------------------------------- QUITTING -------------------------------------------------------------------

        quit_frame = Frame(self.tk)
        quit_frame.pack()

        self.quit_button = Button(quit_frame, text="QUIT", fg="red", command=quit_frame.quit, width=10,
                                  borderwidth=3, relief=SUNKEN)
        self.quit_button.pack(side=LEFT, pady = 10)

        self.tk.mainloop()

    def clear_all_entries(self):
        self.person_id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.phone_number_entry.delete(0, END)
        self.activity_id_entry.delete(0, END)
        self.persons_entry.delete(0, END)

        self.year_of_activity_entry.delete(0, END)
        self.month_of_activity_entry.delete(0, END)
        self.day_of_activity_entry.delete(0, END)

        self.start_hour_of_activity_entry.delete(0, END)
        self.start_minute_of_activity_entry.delete(0, END)

        self.end_hour_of_activity_entry.delete(0, END)
        self.end_minute_of_activity_entry.delete(0, END)

        self.description_of_activity_entry.delete(0, END)


    def display_list_of_persons(self):
        """
          Handler method for list button
          Show all the students
        """
        persons = self._persons_service.get_all_persons()
        txt = "ID".ljust(15) + "Name".ljust(25) + "Phone number\n"
        for person in persons:
            txt += str(person.unique_id).ljust(15) + person.name.ljust(25).rjust(15) + str(person.phone_number)
            txt += "\n"
        messagebox.showinfo("Search result", txt)

    def read_new_person_data(self):
        list_of_person_attributes = [
            self.name_entry.get(),
            self.phone_number_entry.get()
        ]
        self.clear_all_entries()

        return list_of_person_attributes

    def add_person_to_list_ui(self):
        """
        The method reads the data of a new friend and passes this to the service in order to perform the addition to the list.
        """

        try:
            new_person_data = self.read_new_person_data()
            self._persons_service.add_person(new_person_data)
            messagebox.showinfo(message='Successfully added new person.')
        except Exception as exception_message:
            messagebox.showerror("Error encountered", exception_message)

    def remove_person_ui(self):

        try:
            id_of_person_to_be_removed = int(self.person_id_entry.get())
            self._persons_service.remove_person(id_of_person_to_be_removed)
            messagebox.showinfo(message='Successfully removed person')
        except Exception as exception_message:
            messagebox.showerror("Error encountered", exception_message)

        self.clear_all_entries()

    def update_person_ui(self):
        try:
            id_of_person_to_be_updated = int(self.person_id_entry.get())
            new_attributes_of_person = self.read_new_person_data()
            self._persons_service.update_person(id_of_person_to_be_updated, new_attributes_of_person)
            messagebox.showinfo(message='Successfully updated person data.')
        except Exception as exception_message:
            messagebox.showerror("Error encountered", exception_message)

        self.clear_all_entries()


    def search_for_person_ui(self):
        search_key = ""
        if self.name_entry.get():
            search_key = self.name_entry.get()
        elif self.phone_number_entry.get():
            search_key = self.phone_number_entry.get()

        search_result = self._persons_service.search_person_by(search_key)

        if not search_result:
            messagebox.showinfo(message="No matches found")
        else:
            txt = "ID".ljust(5) + "Name".ljust(15) + "Address\n"
            for person in search_result:
                txt += str(person.unique_id) + person.name.ljust(15) + str(person.phone_number)
                txt += "\n"
            messagebox.showinfo("Search result", txt)

    def read_new_activity_data(self):
        """
        The function reads the attributes of a new activity as a list
        :return: the list of attributes
        """
        ids_of_persons_involved = self.persons_entry.get().split()

        ids_of_persons_involved = [int(person_id) for person_id in ids_of_persons_involved]
        new_activity_data = [ids_of_persons_involved,
                             date(int(self.year_of_activity_entry.get()), int(self.month_of_activity_entry.get()),
                                  int(self.day_of_activity_entry.get())),
                             time(int(self.start_hour_of_activity_entry.get()), int(self.start_minute_of_activity_entry.get())),
                             time(int(self.end_hour_of_activity_entry.get()), int(self.end_minute_of_activity_entry.get())),
                             self.description_of_activity_entry.get()]

        self.clear_all_entries()

        return new_activity_data

    def add_activity_ui(self):
        """
        The method reads all the required data of a new activity in the form of a list and passes this data to the
        service in order to perform the addition.
        """
        try:
            new_activity_attributes = self.read_new_activity_data()
            self._activity_service.add_new_activity(new_activity_attributes)
            messagebox.showinfo(message='Successfully added new activity.')
        except Exception as exception_message:
            messagebox.showwarning(message=exception_message)

    def remove_activity_ui(self):
        try:
            id_of_activity_to_be_removed = int(self.activity_id_entry.get())
            self._activity_service.remove_activity(id_of_activity_to_be_removed)
            messagebox.showinfo(message='Successfully removed activity')
        except Exception as exception_message:
            messagebox.showinfo("Error encountered", exception_message)

        self.clear_all_entries()

    def update_activity_ui(self):
        """
        The method reads the ID of an activity and a list containing the new data with which the activity will be updated
        and passes this id and data to the service in order perform the update.
        """
        try:
            id_of_activity_to_be_updated = int(self.activity_id_entry.get())

            new_activity_attributes = self.read_new_activity_data()

            self._activity_service.update_activity(id_of_activity_to_be_updated, new_activity_attributes)
            messagebox.showinfo(message='Successfully updated activity')

        except Exception as exception_message:
            messagebox.showinfo("Error encountered", exception_message)

        self.clear_all_entries()

    def display_activities_ui(self):
        """
        The method prints all the activities in the current list of activities.
        """
        text = ""
        list_of_activities = self._activity_service.get_all_activities()
        for activity in list_of_activities:
            text += str(activity)
            text += "\n"
            text += "\n"

        messagebox.showinfo("List of activities", text)

    def search_activities_ui(self):
        year_of_activity = self.year_of_activity_entry.get()
        month_of_activity = self.month_of_activity_entry.get()
        day_of_activity = self.day_of_activity_entry.get()

        search_hour = self.start_hour_of_activity_entry.get()
        search_minute = self.start_minute_of_activity_entry.get()

        description_of_activity = self.description_of_activity_entry.get()

        try:
            search_key = ""
            if year_of_activity != "" and month_of_activity != "" and day_of_activity != "":
                search_key = date(int(year_of_activity), int(month_of_activity), int(day_of_activity))
            elif search_hour != "" and search_minute != "":
                search_key = time(int(search_hour), int(search_minute))
            elif description_of_activity != "":
                search_key = description_of_activity

            search_result = self._activity_service.search_activities(search_key)

            if not search_result:
                messagebox.showinfo(message='No matches found')
            else:
                text = ""
                for activity in search_result:
                    text += str(activity)
                    text += "\n"

                messagebox.showinfo("Search result", text)

        except Exception as exception_message:
            messagebox.showerror("Error encountered", exception_message)



    def list_activities_in_a_given_day_ui(self):
        """
        The method prints the activities that take place in a day entered by the user, in the order of their start time.
        """

        try:
            # read date
            given_date = date(int(self.year_of_activity_entry.get()), int(self.month_of_activity_entry.get()),
                              int(self.day_of_activity_entry.get()))

            # call method from activity service that returns a list of activities
            resulted_activities = self._activity_service.get_all_activities_in_a_day(given_date)

            # print the activities in the returned list
            if not resulted_activities:
                messagebox.showinfo(message='There are no activities taking place in the given date.')
            else:
                text = ""
                for activity in resulted_activities:
                    text += str(activity)
                    text += "\n"

                messagebox.showinfo("Activities in a day", text)

        except Exception as exception_message:
            messagebox.showerror("Error encountered", exception_message)

        self.clear_all_entries()

    def list_busiest_days_ui(self):
        """
        The method calls the service which provides the list of upcoming dates with activities, sorted in descending
        order of the free time and prints this list
        """
        list_of_busiest_days = self._activity_service.get_the_busiest_days()
        text = ""
        for day in list_of_busiest_days:
            text += str(day)
            text += "\n"
        messagebox.showinfo("Busiest days", text)

    def list_activities_with_a_given_person_ui(self):
        """
        The methods reads the id of a person and list all upcoming activities to which the person will participate.
        """
        try:
            id_of_person = int(self.persons_entry.get())
            resulted_activities = self._activity_service.get_all_activities_with_a_person(id_of_person)

            if not resulted_activities:
                messagebox.showinfo(message='The person is not involved in any activity for now')
            else:
                text = ""
                for activity in resulted_activities:
                    text += str(activity)
                    text += "\n"

                messagebox.showinfo("Activities with a person", text)

        except Exception as exception_message:
            messagebox.showerror("Error encountered", exception_message)

        self.clear_all_entries()

    def undo_operation_ui(self):
        if self._undo_service.undo_operation():
            messagebox.showinfo(message='Undone successfully.')
        else:
            messagebox.showinfo(message='There are no more operations that can be undone.')

    def redo_operation_ui(self):
        if not self._undo_service.redo_operation():
            messagebox.showinfo(message='There are no operations that can be redone.')
        else:
            messagebox.showinfo(message='Redone successfully')

