import copy

from algo.utils.string_utils import is_number
from algo.sorting.selection_sort import selection_sort
from algo.sorting.insertion_sort import insertion_sort
from algo.sorting.shellsort import shellsort
from algo.sorting.quicksort import quicksort
from algo.sorting.heapsort import heapsort
from algo.sorting.counting_sort import counting_sort
from algo.sorting.radixsort import radixsort


def _validate_args(entries):
    """
    Ensure that the input parameters is a list of 
    integers. It this function does not raises any
    exception, it has successfully validated them.

    Parameters
    ----------
    entries: list
        Input parameters received by sort function.

    Raises
    ------
    TypeError: when `entries` is not a list.

        >>> sort({})
        Traceback (most recent call last):
          ..
          TypeError: `entries` should be a list

    ValueError: when on entry of the list is not an integer.

        >>> sort(['wat'])
        Traceback (most recent call last):
          ..
          ValueError: entry `wat` is not a number
    """
    if not isinstance(entries, list):
        raise TypeError("`entries` should be a list")
    for entry in entries:
        if not is_number(entry):
            raise ValueError("entry `%s` is not a number" % entry)


def sort(entries, algo="selection"):
    """
    Sorts a list of numbers using the Quicksort method.

        >>> sort([5, 1, 8, 9, 2])
        [1, 2, 5, 8, 9]

    Parameters
    ----------
    entries: list
        A list of numbers to be sorted.
    algo: string (default: 'selection')
        Name of the sorting algorithm to be used.

    Returns
    -------
    A sorted list of numbers.

    Raises
    ------
    TypeError: when `entries` is not a list.

        >>> sort({})
        Traceback (most recent call last):
          ..
          TypeError: `entries` should be a list

    ValueError: 

        When on entry of the list is not an integer.

            >>> sort(['wat'])
            Traceback (most recent call last):
              ..
              ValueError: entry `wat` is not a number

        When sorting algorithm was not found.

            >>> sort([1, 4, 3], algo='wat')
            Traceback (most recent call last):
              ..
              ValueError: algorithm `wat` was not found
    """
    _validate_args(entries)
    numbers = copy.copy(entries)
    if algo == "selection":
        selection_sort(numbers)
    elif algo == "insertion":
        insertion_sort(numbers)
    elif algo == "shellsort":
        shellsort(numbers)
    elif algo == "quicksort":
        quicksort(numbers)
    elif algo == "heapsort":
        heapsort(numbers)
    elif algo == "counting":
        counting_sort(numbers)
    elif algo == "radixsort":
        radixsort(numbers)
    else:
        raise ValueError("algorithm `%s` not found" % algo)
    return numbers
