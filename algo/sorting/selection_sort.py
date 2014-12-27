from algo.utils.list_utils import swap


def selection_sort(numbers, top_n=None):
    """
    Sorts "in-situ" a list of numbers in ascendant order using
    the Selection Sort method.

        >>> array = [5, 1, 8, 9, 2]
        >>> selection_sort(array)
        >>> array
        [1, 2, 5, 8, 9]

    It also supports the sorting of the first `n` numbers.

        >>> array = [5, 1, 8, 9, 2]
        >>> insertion_sort(array, top_n=1)
        >>> array
        [1, 5, 8, 9, 2]

    Parameters
    ----------
    numbers: list
        List of numbers to be sorted.
    top_n: int or None
        Defines the number of elements that should be sorted.
        For top_n=1, it will only put the smallest element in the beginning.
    """
    if top_n is not None:
        num_iter = top_n
    else: 
        num_iter = len(numbers) - 1
    for i in xrange(num_iter):
        min_index = i
        for j in xrange(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        swap(numbers, i, min_index)
