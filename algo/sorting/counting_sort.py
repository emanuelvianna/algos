def _put_each_number_in_its_final_position(numbers, positions):
    """
    Iterates over the actual numbers, get its positions (treating duplicates)
    and put it on another list in its final possition. On the end copy the
    values from the sorted list to the initial list.

        >>> numbers = [0, 2, 0, 1, 4]
        >>> positions = [2, 3, 5, 5, 6]
        >>> _put_each_number_in_its_final_position(numbers, positions)
        >>> array
        [0, 0, 1, 2, 4]

    Parameters
    ----------
    numbers: list
        List of integers to be sorted (zero-indexed).
    position: list
        List of the final positions of each number (one-indexed).
    """
    sorted_numbers = [None] * len(numbers)
    for number in reversed(numbers):
        position = positions[number] - 1
        sorted_numbers[position] = number
        positions[number] -= 1
    numbers[:] = sorted_numbers[:]


def _compute_the_final_position_of_each_number(counter):
    """
    Iterates over the possible values of keys, defined by the range that
    goes from the minimum number value until the maximum one, and compute
    the final position (one-indexed) of each number, given by the sum of 
    the ocurrences of each number smaller than it.

        >>> counter = [0, 0, 1, 2, 4]
        >>> _compute_the_final_position_of_each_number(counter)
        [2, 3, 5, 5, 6]

    Parameters
    ----------
    counter: list
        List with the number frequency stored in the number index.

    Returns
    -------
    list:
        List of the final positions of each number.
    """
    positions = counter
    for i in xrange(1, len(counter)):
        positions[i] = counter[i] + counter[i - 1]
    return positions


def _count_the_occurrences_of_each_number(numbers):
    """
    Iterates over the numbers and count the ocurrences of each number,
    storing the result counter in an array indexed by the number value.

        >>> array = [0, 2, 0, 1, 4]
        >>> _count_the_occurrences_of_each_number(array)
        [2, 1, 1, 0, 1]

    Parameters
    ----------
    numbers: list
        List of numbers to be sorted.

    Returns
    -------
    list:
        List with the number frequency stored in the number index.
    """
    counter = [0] * (max(numbers) + 1)
    for number in numbers:
        counter[number] += 1
    return counter


def counting_sort(numbers):
    """
    Sorts, "in situ", a list of _integer_ numbers, in ascending order, using
    the Counting Sort method.

        >>> numbers = [0, 2, 0, 1, 4]
        >>> counting_sort(numbers)
        >>> numbers
        [0, 0, 1, 2, 4]

    This sorting method is preferrred by card players. It is based on the 
    distribution principle and thus, instead of comparing the keys, it groups 
    the keys with the same value and redistribute them in the correct order.

    Parameters
    ----------
    numbers: list
        List of integers to be sorted.
    """
    counter = _count_the_occurrences_of_each_number(numbers)
    positions = _compute_the_final_position_of_each_number(counter)
    _put_each_number_in_its_final_position(numbers, positions)
