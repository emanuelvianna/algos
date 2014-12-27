"Maximum size of a key (2^NUM_KEY_BITS)."
NUM_KEY_BITS = 32

"Number of key bits evaluated at each iteration."
NUM_ITERATION_BITS = 8

"Base number, each input number can vary from 0 to BASE."
BASE = 256


def _get_bits(number, iter_num, num_iteration_bits):
    """
    Get the i-th n less significative bits of number, where `i` is given by 
    the iteration number and `n` is number of bits evaluted in each iteration.

        >>> _get_bits(22, iter_num=0, num_iteration_bits=3)
        6

    Parameters
    ----------
    number: int
        Current number of the list.
    iter_num: int
        Number of current iteration (zero-indexed).

    Returns
    -------
    The i-th n less signifcative bits of current number.
    """
    return (number >> (iter_num * num_iteration_bits)) & ~(~0 << num_iteration_bits)


def _put_each_number_in_its_position(numbers, positions, iter_num, num_iteration_bits):
    """
    Iterates over the actual numbers, get its positions (treating duplicates)
    and put it on another list in its final possition. On the end copy the
    values from the sorted list to the initial list.

        >>> numbers = [6, 33, 17, 22, 1, 6]
        >>> map(bin, numbers)
        ['110', '100001', '10001', '10110', '1', '110']
        >>> map(lambda x: _get_bits(x, iter_num=0, num_iteration_bits=3), numbers)
        [6, 1, 1, 6, 1, 6]
        >>> positions = [0, 3, 3, 3, 3, 3, 6, 6]
        >>> _put_each_number_in_its_position(numbers, positions, iter_num=0,
        ...                                  num_iteration_bits=3)
        >>> numbers
        [33, 17, 1, 6, 22, 6]
        >>> map(bin, numbers)
        ['1', '10001', '100001', '110', '10110', '110']

    Parameters
    ----------
    numbers: list
        List of integers to be sorted (zero-indexed).
    position: list
        List of the final positions of each number (one-indexed).
    iter_num: int
        Number of current iteration (zero-indexed).
    num_iteration_bits: int
        Number of key bits evaluated at each iteration.
    """
    sorted_numbers = [None] * len(numbers)
    for number in reversed(numbers):
        bits = _get_bits(number, iter_num, num_iteration_bits)
        position = positions[bits] - 1
        sorted_numbers[position] = number
        positions[bits] -= 1
    numbers[:] = sorted_numbers[:]


def _compute_the_position_of_each_number(counter):
    """
    Iterates over the possible values of keys, defined by the range that
    goes from the minimum number value until the maximum one, and compute
    the final position (one-indexed) of each number, given by the sum of the
    ocurrences of each number smaller than it, i.e. the cumulative count.

        >>> counter = [0, 3, 0, 0, 0, 0, 3, 0]
        >>> _compute_the_position_of_each_number(counter)
        [0, 3, 3, 3, 3, 3, 6, 6]

    Parameters
    ----------
    counter: list
        List with the number frequency stored in the number index.

    Returns
    -------
    list:
        List of the positions of each number.
    """
    cumulative_counter = counter
    for i in xrange(1, len(counter)):
        cumulative_counter[i] = counter[i] + cumulative_counter[i - 1]
    return cumulative_counter


def _count_the_occurrences_of_each_number(numbers, iter_num, base, num_iteration_bits):
    """
    Iterates over the numbers and count the ocurrences of each number,
    storing the result counter in an array indexed by the number value.

        >>> numbers = [6, 33, 17, 22, 1, 6]
        >>> map(bin, numbers)
        ['110', '100001', '10001', '10110', '1', '110']
        >>> map(lambda x: _get_bits(x, iter_num=0, num_iteration_bits=3), numbers)
        [6, 1, 1, 6, 1, 6]
        >>> _count_the_occurrences_of_each_number(numbers, iter_num=0,
        ...                                       base=8, num_iteration_bits=3)
        [0, 3, 0, 0, 0, 0, 3, 0]

    Parameters
    ----------
    numbers: list
        List of numbers to be sorted.
    iter_num: int
        Number of current iteration (zero-indexed).
    base: int
        Base number, each input number can vary from 0 to BASE.
    num_iteration_bits: int
        Number of key bits evaluated at each iteration.

    Returns
    -------
    list:
        List with the number's frequency stored in the number index.
    """    
    counter = [0] * base
    for number in numbers:
        bits = _get_bits(number, iter_num, num_iteration_bits)
        counter[bits] += 1
    return counter


def _counting_sort(numbers, iter_num, base, num_iteration_bits):
    """
    Sorts "in-situ" a list of _integer_ numbers in ascending order using
    the method Couting Sort, adapted to sort only the i-th n less significative
    bits of the keys, where `i` varies according to the iteration nuber and `n`
    is the nuber of bits evaluated on each iteration, supplied on initialization.

        >>> numbers = [6, 33, 17, 22, 1, 6]
        >>> map(bin, numbers)
        ['110', '100001', '10001', '10110', '1', '110']
        >>> map(lambda x: _get_bits(x, iter_num=0, num_iteration_bits=3), numbers)
        [6, 1, 1, 6, 1, 6]
        >>> _counting_sort(numbers, iter_num=0, base=8, num_iteration_bits=3)
        >>> numbers
        [1, 17, 33, 6, 22, 6]

    Parameters
    ----------
    numbers: list
        List of integers to be sorted.
    iter_num: int
        Number of current iteration (zero-indexed).
    base: int
        Base number, each input number can vary from 0 to BASE.
    num_iteration_bits: int
        Number of key bits evaluated at each iteration.
    """
    counter = _count_the_occurrences_of_each_number(
        numbers, iter_num, base, num_iteration_bits)
    positions = _compute_the_position_of_each_number(counter)
    _put_each_number_in_its_position(numbers, positions, iter_num, num_iteration_bits)


def radixsort(numbers, base=BASE, num_key_bits=NUM_KEY_BITS,
              num_iteration_bits=NUM_ITERATION_BITS):
    """
    Sorts "in situ" a list of _integer_ numbers in ascending order using the 
    method Radixsort.

        >>> numbers = [6, 33, 17, 22, 1, 6]
        >>> radixsort(numbers, base=8, num_key_bits=6, num_iteration_bits=3)
        >>> numbers
        [1, 6, 6, 17, 22, 33]

    Parameters
    ----------
    numbers: list
        List of integers to be sorted.
    base: int
        Base number, each input number can vary from 0 to BASE.
    num_key_bits: int
        Maximum size of a key (2^NUM_KEY_BITS).
    num_iteration_bits: int
        Number of key bits evaluated at each iteration.
    """
    num_iterations = num_key_bits // num_iteration_bits
    for iter_num in xrange(num_iterations):
        _counting_sort(numbers, iter_num, base, num_iteration_bits)
