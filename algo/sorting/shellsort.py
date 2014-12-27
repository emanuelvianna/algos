REDUCE_FACTOR = 3


def shellsort_algo(numbers, jump_size):
    """
    Sorts "in-situ" a list of numbers using the Shellsort algorithm.

    Parameters
    ----------
    numbers: list
        List of numbers to be sorted
    jump_size: int
        Size of the jump in the array used by the Shellsort algorithm.
    """
    while True:
        jump_size = jump_size // REDUCE_FACTOR
        for i in xrange(jump_size, len(numbers)):
            j = i
            number = numbers[i]
            while numbers[j - jump_size] > number:
                numbers[j] = numbers[j - jump_size]
                j -= jump_size
                if j < jump_size:
                    break
            numbers[j] = number
        if jump_size == 1:
            break


def _init_jump_size(size):
    """
    Estimate the initial value of the parameter `h`, here called `jump_size`,
    which defines the size of the jump in the input array at each iteration of
    the Shellsort algorithm. Knuth found experimentally an efficient way to 
    initialize this parameter through the given recursion:

    h(s) = 3h(s-1) + 1, s > 1
    h(s) = 1, s = 1

    The sequence of h is as follows: 1, 4, 13, 40, 121, 364, etc.

    Parameters
    ----------
    size: int
        Size of the array to be sorted.

    Returns
    -------
    The estimated parameter-h.
    """
    jump_size = 1
    while True:
        jump_size = 3 * jump_size + 1
        if jump_size >= size:
            break
    return jump_size


def shellsort(numbers):
    """
    Sorts `in situ` a list of numbers in ascending order using 
    the Shellsort method.

        >>> array = [5, 1, 8, 9, 2]
        >>> shellsort(array)
        >>> array
        [1, 2, 5, 8, 9]

    Parameters
    ----------
    numbers: list
        List of numbers to be sorted.
    """
    jump_size = _init_jump_size(size=len(numbers))
    return shellsort_algo(numbers, jump_size)
