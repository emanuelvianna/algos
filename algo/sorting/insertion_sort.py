def _insertion_sort_for_top_n(numbers, top_n):
    """
    Sorts "in situ" a list of numbers in ascendant order using
    the Insertion Sort method for only the top `n` numbers.

        >>> array = [5, 1, 8, 9, 2]
        >>> _insertion_sort_for_top_n(array, top_n=1)
        >>> array
        [1, 2, 5, 8, 9]

    In an analogy of a card player, the `top_n` parameters means
    the maximum number of cards that a player can hold in its hands.

    Parameters
    ----------
    i: int
        Index of current element (card) evaluated by Insertin Sort.
    top_n: int or None
        Defines the number of elements that should be sorted.
        For top_n=1, it will only put the smallest element in the beginning.
    """
    for i in xrange(1, len(numbers)):
        number = numbers[i]
        if i < top_n:
            j = i - 1
        else:
            j = top_n - 1
            if number < numbers[j]:
                numbers[i] = numbers[j]
        while j >= 0 and number < numbers[j]:
            if (j + 1) < top_n:
                numbers[j + 1] = numbers[j]
            j -= 1
        if (j + 1) < top_n:
            numbers[j + 1] = number


def _insertion_sort_algo(numbers):
    """
    Sorts "in situ" a list of numbers in ascendant order using
    the Insertion Sort method for the entire list.

        >>> array = [5, 1, 8, 9, 2]
        >>> _insertion_sort_algo(array)
        >>> array
        [1, 2, 5, 8, 9]

    Parameters
    ----------
    numbers: list
        List of numbers to be sorted.
    """
    for i in xrange(1, len(numbers)):
        number = numbers[i]
        j = i - 1
        while j >= 0 and number < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = number


def insertion_sort(numbers, top_n=None):
    """
    Sorts "in-situ" a list of numbers in ascendant order using 
    the Insertion Sort method.

        >>> array = [5, 1, 8, 9, 2]
        >>> insertion_sort(array)
        >>> array
        [1, 2, 5, 8, 9]

    It also supports the sorting of the first `n` numbers.

        >>> array = [5, 1, 8, 9, 2]
        >>> insertion_sort(array, top_n=1)
        >>> array
        [1, 2, 5, 8, 9]

    Parameters
    ----------
    numbers: list
        List of numbers to be sorted.
    top_n: int or None
        Defines the number of elements that should be sorted.
        For top_n=1, it will only put the smallest element in the beginning.
    """
    if top_n is not None:
        _insertion_sort_for_top_n(numbers, top_n)
    else:
        _insertion_sort_algo(numbers)
