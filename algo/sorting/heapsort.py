import heapq

from algo.utils.list_utils import swap


def _min_heapify_at_a_range(numbers, left, right):
    """
    Build max-heap in a range of the array.

    Parameters
    ----------
    numbers: list
        List of numbers to be sorted.
    left: int
        Initial index.
    right: int
        Final index.
    """
    part = slice(left, right + 1)
    partial = numbers[part]
    heapq.heapify(partial)
    numbers[part] = partial


def _heapsort_for_top_n(numbers, top_n):
    """
    Sorts "in situ" a list of numbers in ascendant order using
    the Heapsort method for only the top `n` numbers.

        >>> array = [5, 1, 8, 9, 2]
        >>> insertion_sort(array, top_n=1)
        >>> array
        [1, 2, 8, 9, 5]

    Parameters
    ----------
    numbers: list
        List of numbers to be sorted.
    top_n: int or None
        Defines the number of elements that should be sorted.
        For top=1, it will only put the smallest element in the beginning.
    """
    left, right = 1, len(numbers) - 1
    heapq.heapify(numbers)
    while left < top_n:
        _min_heapify_at_a_range(numbers, left, right)
        left += 1


def _max_heapify_at_a_range(numbers, left, right):
    """
    Build max-heap in a range of the array.

    Parameters
    ----------
    numbers: list
        List of numbers to be sorted.
    left: int
        Initial index.
    right: int
        Final index.
    """
    part = slice(left, right + 1)
    partial = numbers[part]
    heapq._heapify_max(partial)
    numbers[part] = partial


def _heapsort_algo(numbers):
    """
    Sorts "in situ" a list of numbers in ascendant order using
    the Insertion Sort method for the entire list.

        >>> array = [5, 1, 8, 9, 2]
        >>> _heapsort_algo(array)
        >>> array
        [1, 2, 5, 8, 9]

    Parameters
    ----------
    numbers: list
        List of numbers to be sorted.
    """
    left, right = 0, len(numbers) - 1
    heapq._heapify_max(numbers)
    while right >= 1:
        number = numbers[0]
        swap(numbers, 0, right)
        right -= 1
        _max_heapify_at_a_range(numbers, left, right)


def heapsort(numbers, top_n=None):
    """
    Sorts "in-situ" a list of numbers in ascendant order 
    using the method Heapsort.

        >>> array = [5, 1, 8, 9, 2]
        >>> heapsort(array)
        >>> array
        [1, 2, 5, 8, 9]

    It also supports the sorting of the first `n` numbers.

        >>> array = [5, 1, 8, 9, 2]
        >>> heapsort(array, top_n=1)
        >>> array
        [1, 2, 8, 9, 5]

    Parameters
    ----------
    numbers: list
        List of numbers to be sorted.
    top_n: int or None
        Defines the number of elements that should be sorted.
        For top=1, it will only put the smallest element in the beginning.
    """
    if top_n is not None:
        _heapsort_for_top_n(numbers, top_n)
    else:
        _heapsort_algo(numbers)
