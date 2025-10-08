import statistics

def add(a, b):
    """
    Add two numbers.

    Parameters:
    a (float or int): The first number.
    b (float or int): The second number.

    Returns:
    float or int: The sum of the two numbers.

    Raises:
    TypeError: If either of the inputs is not a number.

    Example:
    >>> add(2, 3)
    5
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers.")
    return a + b


def subtract(a, b):
    """
    Subtract the second number from the first.

    Parameters:
    a (float or int): The first number.
    b (float or int): The second number.

    Returns:
    float or int: The result of the subtraction.

    Raises:
    TypeError: If either of the inputs is not a number.

    Example:
    >>> subtract(5, 3)
    2
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers.")
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.

    Parameters:
    a (float or int): The first number.
    b (float or int): The second number.

    Returns:
    float or int: The product of the two numbers.

    Raises:
    TypeError: If either of the inputs is not a number.

    Example:
    >>> multiply(2, 3)
    6
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers.")
    return a * b


def divide(a, b):
    """
    Divide the first number by the second.

    Parameters:
    a (float or int): The first number.
    b (float or int): The second number.

    Returns:
    float or int: The result of the division.

    Raises:
    TypeError: If either of the inputs is not a number.
    ZeroDivisionError: If the second input is zero.

    Example:
    >>> divide(6, 3)
    2.0
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers.")
    if b == 0:
        raise ZeroDivisionError("The second input must not be zero.")
    return a / b


def mean(data):
    """
    Calculate the mean of a list of numbers.

    Parameters:
    data (list of float or int): The list of numbers.

    Returns:
    float: The mean of the numbers.

    Raises:
    TypeError: If the input is not a list or if the list contains non-number elements.
    ValueError: If the list is empty.

    Example:
    >>> mean([1, 2, 3, 4, 5])
    3.0
    """
    if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("Input must be a list of numbers.")
    if not data:
        raise ValueError("The list must not be empty.")
    return statistics.mean(data)


def median(data):
    """
    Calculate the median of a list of numbers.

    Parameters:
    data (list of float or int): The list of numbers.

    Returns:
    float: The median of the numbers.

    Raises:
    TypeError: If the input is not a list or if the list contains non-number elements.
    ValueError: If the list is empty.

    Example:
    >>> median([1, 2, 3, 4, 5])
    3
    """
    if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("Input must be a list of numbers.")
    if not data:
        raise ValueError("The list must not be empty.")
    return statistics.median(data)


def mode(data):
    """
    Calculate the mode of a list of numbers.

    Parameters:
    data (list of float or int): The list of numbers.

    Returns:
    float or int: The mode of the numbers.

    Raises:
    TypeError: If the input is not a list or if the list contains non-number elements.
    ValueError: If the list is empty or if no unique mode is found.

    Example:
    >>> mode([1, 2, 2, 3, 4])
    2
    """
    if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("Input must be a list of numbers.")
    if not data:
        raise ValueError("The list must not be empty.")
    try:
        return statistics.mode(data)
    except statistics.StatisticsError as e:
        raise ValueError(str(e))


def variance(data):
    """
    Calculate the variance of a list of numbers.

    Parameters:
    data (list of float or int): The list of numbers.

    Returns:
    float: The variance of the numbers.

    Raises:
    TypeError: If the input is not a list or if the list contains non-number elements.
    ValueError: If the list is empty.

    Example:
    >>> variance([1, 2, 3, 4, 5])
    2.5
    """
    if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("Input must be a list of numbers.")
    if not data:
        raise ValueError("The list must not be empty.")
    return statistics.variance(data)

if __name__ == "__main__":
    import doctest
    doctest.testmod()