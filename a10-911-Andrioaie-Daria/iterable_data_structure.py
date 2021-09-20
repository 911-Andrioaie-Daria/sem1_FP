class Iterable:

    class Iterator:
        def __init__(self, iterable_data):
            self._iterable_data = iterable_data
            self._index = 0

        def __next__(self):
            if self._index == len(self._iterable_data._data):
                raise StopIteration()

            self._index = self._index + 1
            return self._iterable_data._data[self._index - 1]

    def __init__(self):
        self._data = []

    def __iter__(self):
        return self.Iterator(self)

    def __getitem__(self, index_of_item):
        return self._data[index_of_item]

    def __setitem__(self, key, new_value):
        self._data[key] = new_value

    def __delitem__(self, key):
        del self._data[key]

    def __len__(self):
        return len(self._data)

    def append(self, item):
        self._data.append(item)

    def insert(self, insertion_index, new_item):
        """
        Inserts a new item in the list of records
        :param insertion_index: the position where the new item must be inserted
        """
        if insertion_index > len(self) or insertion_index < 0:
            raise ValueError('The position of insertion must be within the length of the list')

        if len(self) == 0 and insertion_index == 0:
            self._data.append(new_item)

        else:
            self._data.append(self._data[len(self)-1])

            for i in range(len(self)-1, insertion_index, -1):
                self._data[i] = self._data[i-1]

            self.__setitem__(insertion_index, new_item)

    def swap(self, index_of_element_1, index_of_element_2):
        """
        Swaps two elements from the list
        """
        if index_of_element_1 < 0 or index_of_element_1 > len(self):
            raise ValueError('The positions must be within the length of the list')

        if index_of_element_2 < 0 or index_of_element_2 > len(self):
            raise ValueError('The positions must be within the length of the list')

        if index_of_element_1 == index_of_element_2:
            return

        copy_of_element1 = self.__getitem__(index_of_element_1)
        self.__setitem__(index_of_element_1, self.__getitem__(index_of_element_2))
        self.__setitem__(index_of_element_2, copy_of_element1)

    def sort_data(self, comparison_function):
        """
        GNOME sort
        The algorithm is similar to insertion sort, taking each element one by one and trying to find its position in
        already sorted array, except it does this by a series of swaps, like in bubble sort.
        The complexity is O(n^2) and in practice it was found to run a little bit slower than bubble sort.
        :param self: the list to be sorted
        :param comparison_function: used to determine the order between two elements.
        """
        i = 1
        j = 2
        while i < len(self):
            if comparison_function(self._data[i-1], self._data[i]):
                i = j
                j += 1
            else:
                # swap compared elements
                self.swap(i-1, i)
                i -= 1
                if i == 0:
                    i = 1

    def filter_data(self, acceptance_function):
        """
        The function will use 2 parameters:
        the list to be filtered, and an acceptance function that decided whether a given value passes the filter.
        :return:
        """
        filtered_list = []
        for item in self:
            if acceptance_function(item):
                filtered_list.append(item)

        return filtered_list
