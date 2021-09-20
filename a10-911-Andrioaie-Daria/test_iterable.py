import unittest

from iterable_data_structure import Iterable


class TestIterable(unittest.TestCase):
    def setUp(self):
        self._my_collection = Iterable()

        self._my_collection.append(4)
        self._my_collection.append(1)
        self._my_collection.append(5)

    def test_get_item(self):
        index_of_item = 0
        item1 = self._my_collection.__getitem__(index_of_item)
        self.assertEqual(item1, self._my_collection._data[index_of_item])

    def test_set_item(self):
        index_of_item = 1
        new_value = 'this is an updated item'

        self._my_collection.__setitem__(index_of_item, new_value)
        updated_item = self._my_collection.__getitem__(index_of_item)

        self.assertEqual(updated_item, 'this is an updated item')

    def test_delete_item(self):
        index_of_item_to_be_removed = 1
        self._my_collection.__delitem__(index_of_item_to_be_removed)
        self.assertEqual(2, len(self._my_collection))

    def test_iterator(self):
        for item in self._my_collection:
            pass

    def test_insert(self):
        insertion_index = 2
        new_item = -2
        self._my_collection.insert(insertion_index, new_item)

        item_on_position_2 = self._my_collection.__getitem__(2)
        item_on_position_3 = self._my_collection.__getitem__(3)

        self.assertEqual(item_on_position_2, -2)
        self.assertEqual(item_on_position_3, 5)

        self._my_collection.__delitem__(3)
        self._my_collection.__delitem__(2)
        self._my_collection.__delitem__(1)
        self._my_collection.__delitem__(0)

        insertion_index = 0
        new_item = 1
        self._my_collection.insert(insertion_index, new_item)
        self.assertEqual(len(self._my_collection), 1)

        try:
            self._my_collection.insert(-1, 11)
        except ValueError:
            pass

    def test_filter_data(self):

        filtered_list = self._my_collection.filter_data(lambda item: item > 2)
        self.assertEqual(len(filtered_list), 2)

        filtered_list = self._my_collection.filter_data(lambda item: item < 0)
        self.assertEqual(len(filtered_list), 0)

    def test_sort_data(self):
        self._my_collection.sort_data(lambda a, b: a <= b)
        self.assertEqual(self._my_collection._data, [1, 4, 5])

        self._my_collection.append(-3)
        self._my_collection.append(2)
        self._my_collection.append(-8)

        self._my_collection.sort_data(lambda a, b: a >= b)
        self.assertEqual(self._my_collection._data, [5, 4, 2, 1, -3, -8])

        self._my_collection.sort_data(lambda a, b: a <= b)
        self.assertEqual(self._my_collection._data, [-8, -3, 1, 2, 4, 5])

    def test_swap(self):
        try:
            index_of_element1 = -1
            index_of_element2 = 2
            self._my_collection.swap(index_of_element1, index_of_element2)
        except ValueError:
            pass

        try:
            index_of_element1 = 2
            index_of_element2 = 7
            self._my_collection.swap(index_of_element1, index_of_element2)
        except ValueError:
            pass

        index_of_element1 = 2
        index_of_element2 = 2
        self._my_collection.swap(index_of_element1, index_of_element2)

        index_of_element1 = 1
        index_of_element2 = 2
        self._my_collection.swap(index_of_element1, index_of_element2)
        self.assertEqual(self._my_collection._data, [4, 5, 1])
