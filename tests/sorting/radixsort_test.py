import unittest

from algo.sorting import radixsort
from algo.sorting.sorting import sort
from algo.utils.test_utils import ExtendedTestCase


class RadixSort(ExtendedTestCase):

    def test_six_elements_list_with_repetition(self):
        numbers = [6, 33, 17, 22, 1, 6]
        bits_by_number = map(
            lambda x: radixsort._get_bits(x, iter_num=0, num_iteration_bits=3),
            numbers
        )
        self.assertEquals(
            [6, 1, 1, 6, 1, 6],
            bits_by_number
        )
        counter = radixsort._count_the_occurrences_of_each_number(
            numbers,
            iter_num=0,
            base=8,
            num_iteration_bits=3
        )
        self.assertEquals(
            [0, 3, 0, 0, 0, 0, 3, 0],
            counter
        )
        positions = radixsort._compute_the_position_of_each_number(counter)
        self.assertEquals(
            [0, 3, 3, 3, 3, 3, 6, 6],
            positions
        )
        radixsort._put_each_number_in_its_position(
            numbers,
            positions,
            iter_num=0,
            num_iteration_bits=3
        )
        self.assertEquals(
            [33, 17, 1, 6, 22, 6],
            numbers
        )
        numbers = [1, 17, 33, 6, 22, 6]
        bits_by_number = map(
            lambda x: radixsort._get_bits(x, iter_num=1, num_iteration_bits=3),
            numbers
        )
        self.assertEquals(
            [0, 2, 4, 0, 2, 0],
            bits_by_number
        )
        counter = radixsort._count_the_occurrences_of_each_number(
            numbers,
            iter_num=1,
            base=8,
            num_iteration_bits=3
        )
        self.assertEquals(
            [3, 0, 2, 0, 1, 0, 0, 0],
            counter
        )
        positions = radixsort._compute_the_position_of_each_number(counter)
        self.assertEquals(
            [3, 3, 5, 5, 6, 6, 6, 6],
            positions
        )
        radixsort._put_each_number_in_its_position(
            numbers,
            [3, 3, 5, 5, 6, 6, 6, 6],
            iter_num=1,
            num_iteration_bits=3
        )
        self.assertEquals(
            [1, 6, 6, 17, 22, 33],
            numbers
        )
        radixsort.radixsort(numbers, base=8, num_key_bits=6, num_iteration_bits=3)
        self.assertEquals(
            [1, 6, 6, 17, 22, 33],
            numbers
        )

    def test_two_elements_list(self):
        numbers = [1, 0]
        sorted_numbers = sort(numbers, algo="radixsort")
        self.assertEquals(
            [0, 1],
            sorted_numbers
        )

    def test_descendant_list(self):
        numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        sorted_numbers = sort(numbers, algo="radixsort")
        self.assertEquals(
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            sorted_numbers
        )
    def test_shuffled_list_of_ten_elements(self):
        numbers = [0, 9, 8, 2, 7, 5, 1, 3, 6, 4]
        sorted_numbers = sort(numbers, algo="radixsort")
        self.assertEquals(
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            sorted_numbers
        )
