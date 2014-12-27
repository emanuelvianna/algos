from algo.utils.list_utils import swap


def partition(numbers, left, right):
    """
    Rearrange, `in-situ`, the array of numbers to ensure that all 
    elements before a choose value, called `pivot`, will be smaller 
    than it, as well as, all values located after the pivot will be 
    greater than it.

    Parameters
    ----------
    numbers: list
        List of numbers to be sorted.
    left: int
        Index of the initial position of left side of the pivot.
    right: int
        Index of the initial position of right side of the pivot.

    Returns
    -------
    The positions i and j that the indexes from left and right 
    side crosses.
    """
    i, j = left, right
    pivot_index = (i + j) // 2
    pivot = numbers[pivot_index]
    while True:
        while numbers[i] < pivot:
            i += 1
        while numbers[j] > pivot:
            j -= 1
        if i <= j:
            swap(numbers, i, j)
            i += 1
            j -= 1
        if i > j:
            break
    return i, j


def quicksort_recursive_for_top_n(numbers, top_n, left, right):
    """
    Repeat recursively the partition of the array of numbers
    from `left` to `right` until sort the first `n` numbers.

        >>> array = [5, 1, 8, 9, 2]
        >>> quicksort_recursive_for_top_n(array, top_n=1, left=0,
        ...                               right=len(array) - 1)
        >>> array
        [1, 2, 8, 9, 5]

    Parameters
    ----------
    numbers: list
        List of numbers to be sorted.
    top_n: int or None
        Defines the number of elements that should be sorted.
        For top=1, it will only put the smallest element in the beginning.
    left: int
        Index of the initial position of the left side of the partition.
    right: int
        Index of the initial position of the right side of the partition.
    """
    i, j = partition(numbers, left, right)
    if (j - left) >= (top_n - 1):
        if left < j:
            quicksort_recursive_for_top_n(numbers, top_n, left, j)
    else:
        if left < j:
            quicksort_recursive_for_top_n(numbers, top_n, left, j)
        if i < right:
            quicksort_recursive_for_top_n(numbers, top_n, i, right)


def quicksort_recursive_algo(numbers, left, right):
    """
    Repeat recursively the partition of the array of numbers
    from `left` to `right` until get a sorted array of numbers.

        >>> array = [5, 1, 8, 9, 2]
        >>> quicksort(array)
        >>> array
        [1, 2, 5, 8, 9]

    Parameters
    ----------
    numbers: list
        List of numbers to be sorted.
    left: int
        Index of the initial position of the left side of the partition.
    right: int
        Index of the initial position of the right side of the partition.
    """
    i, j = partition(numbers, left, right)
    if left < j:
        quicksort_recursive_algo(numbers, left, j)
    if i < right:
        quicksort_recursive_algo(numbers, i, right)


def quicksort(numbers, top_n=None):
    """
    Sorts a list of numbers in ascendant order using the Quicksort method.

        >>> array = [5, 1, 8, 9, 2]
        >>> quicksort(array)
        >>> array
        [1, 2, 5, 8, 9]

    It also supports the sorting of the first `n` numbers.

        >>> array = [5, 1, 8, 9, 2]
        >>> quicksort(array, top_n=1)
        >>> array
        [1, 2, 8, 9, 5]

    This function starts the process calling the recursive quicksort with 
    the initial parameters `left` and `right`.

    Parameters
    ----------
    numbers: list
        List of numbers to be sorted.
    top_n: int or None
        Defines the number of elements that should be sorted.
        For top=1, it will only put the smallest element in the beginning.
    """
    if top_n is not None:
        quicksort_recursive_for_top_n(
            numbers,
            top_n,
            left=0,
            right=len(numbers) - 1,
        )
    else:
        quicksort_recursive_algo(
            numbers,
            left=0,
            right=len(numbers) - 1
        )
