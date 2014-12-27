import unittest

from algo.sorting.sorting import sort
from algo.utils.test_utils import ExtendedTestCase


class ShellSort(ExtendedTestCase):

    def test_two_elements_list(self):
        numbers = [9, 8]
        sorted_numbers = sort(numbers, algo="shellsort")
        self.assertEquals(
            [8, 9],
            sorted_numbers
        )

    def test_three_elements_list(self):
        numbers = [9, 8, 7]
        sorted_numbers = sort(numbers, algo="shellsort")
        self.assertEquals(
            [7, 8, 9],
            sorted_numbers
        )

    def test_descendant_list(self):
        numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        sorted_numbers = sort(numbers, algo="shellsort")
        self.assertEquals(
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            sorted_numbers
        )

    def test_shuffled_list_of_ten_elements(self):
        numbers = [0, 9, 8, 2, 7, 5, 1, 3, 6, 4]
        sorted_numbers = sort(numbers, algo="shellsort")
        self.assertEquals(
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            sorted_numbers
        )
