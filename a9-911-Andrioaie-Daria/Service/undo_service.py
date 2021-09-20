class UndoService:
    def __init__(self):
        self._history_of_operations = []
        self._current_index = -1

    def record_operation(self, new_operation):
        self._history_of_operations = self._history_of_operations[0: self._current_index + 1]
        self._history_of_operations.append(new_operation)
        self._current_index += 1

    def undo_operation(self):
        if self._current_index == -1:
            return False

        operation_to_be_undone = self._history_of_operations[self._current_index]
        operation_to_be_undone.undo()

        self._current_index -= 1
        return True

    def redo_operation(self):
        if self._current_index == len(self._history_of_operations) - 1:
            return False

        self._current_index += 1
        operation_to_be_redone = self._history_of_operations[self._current_index]
        operation_to_be_redone.redo()

        return True


class Operation:
    def __init__(self, undo_function, redo_function):
        self._function_undo = undo_function
        self._function_redo = redo_function

    def undo(self):
        self._function_undo()

    def redo(self):
        self._function_redo()


class FunctionCall:
    def __init__(self, function_name, *function_parameters):
        self._function_name = function_name
        self._function_parameters = function_parameters

    def call(self):
        self._function_name(*self._function_parameters)

    def __call__(self):
        self.call()
