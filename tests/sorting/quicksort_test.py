import unittest

from algo.sorting.sorting import sort
from algo.sorting.quicksort import quicksort
from algo.utils.test_utils import ExtendedTestCase


class QuickSort(ExtendedTestCase):

    def test_two_elements_list(self):
        numbers = [9, 8]
        sorted_numbers = sort(numbers, algo="quicksort")
        self.assertEquals(
            [8, 9],
            sorted_numbers
        )

    def test_descendant_list(self):
        numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        sorted_numbers = sort(numbers, algo="quicksort")
        self.assertEquals(
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            sorted_numbers
        )
    def test_shuffled_list_of_ten_elements(self):
        numbers = [0, 9, 8, 2, 7, 5, 1, 3, 6, 4]
        sorted_numbers = sort(numbers, algo="quicksort")
        self.assertEquals(
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            sorted_numbers
        )

    def test_top_two_from_a_shuffled_list_of_ten_elements(self):
        numbers = [0, 9, 8, 2, 7, 5, 1, 3, 6, 4]
        quicksort(numbers, top_n=2)
        self.assertEquals(
            [0, 1, 2, 6, 3, 5, 4, 7, 8, 9],
            numbers
        )

    def test_top_five_from_a_shuffled_list_of_a_hundread_elements(self):
        numbers = [
            59, 7, 52, 50, 80, 40, 79, 10, 47, 72, 56, 91, 30, 83, 63,
            20, 98, 90, 93, 2, 34, 23, 31, 81, 89, 8, 62, 77, 41, 1, 12, 87, 
            88, 48, 11, 64, 21, 49, 53, 75, 18, 35, 84, 95, 25, 44, 92, 68, 
            73, 60, 6, 51, 76, 36, 24, 33, 85, 78, 57, 28, 97, 17, 58, 96, 19, 
            65, 26, 66, 14, 94, 3, 55, 46, 37, 45, 13, 39, 15, 43, 99, 29, 74, 
            86, 82, 4, 5, 69, 61, 27, 42, 32, 70, 54, 22, 67, 0, 38, 71, 16, 9
        ]
        quicksort(numbers, top_n=2)
        expected = [
            0, 1, 52, 50, 9, 40, 16, 10, 47, 38, 56, 7, 30, 22, 54, 20, 32,
            42, 27, 2, 34, 23, 31, 5, 4, 8, 29, 43, 41, 59, 12, 15, 39, 48,
            11, 13, 21, 49, 53, 45, 18, 35, 37, 46, 25, 44, 55, 3, 14, 26,
            6, 51, 19, 36, 24, 33, 58, 17, 57, 28, 97, 78, 85, 96, 76, 65,
            60, 66, 73, 94, 68, 92, 95, 84, 75, 64, 88, 87, 77, 99, 62, 74,
            86, 82, 89, 81, 69, 61, 93, 90, 98, 70, 63, 83, 67, 91, 72, 71,
            79, 80
        ]
        self.assertEquals(
            expected,
            numbers
        )
