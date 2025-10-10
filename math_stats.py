import statistics
from typing import Union, List

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """
    Add two numbers.

    Parameters:
    a (Number): The first number.
    b (Number): The second number.

    Returns:
    Number: The sum of the two numbers.

    Raises:
    TypeError: If either of the inputs is not a number.

    Example:
    >>> add(2, 3)
    5
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers.")
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """
    Subtract the second number from the first.

    Parameters:
    a (Number): The first number.
    b (Number): The second number.

    Returns:
    Number: The result of the subtraction.

    Raises:
    TypeError: If either of the inputs is not a number.

    Example:
    >>> subtract(5, 3)
    2
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers.")
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """
    Multiply two numbers.

    Parameters:
    a (Number): The first number.
    b (Number): The second number.

    Returns:
    Number: The product of the two numbers.

    Raises:
    TypeError: If either of the inputs is not a number.

    Example:
    >>> multiply(2, 3)
    6
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers.")
    return a * b


def divide(a: Number, b: Number) -> Number:
    """
    Divide the first number by the second.

    Parameters:
    a (Number): The first number.
    b (Number): The second number.

    Returns:
    Number: The result of the division.

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


def mean(data: List[Number]) -> float:
    """
    Calculate the mean of a list of numbers.

    Parameters:
    data (List[Number]): The list of numbers.

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


def median(data: List[Number]) -> float:
    """
    Calculate the median of a list of numbers.

    Parameters:
    data (List[Number]): The list of numbers.

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


def mode(data: List[Number]) -> Number:
    """
    Calculate the mode of a list of numbers.

    Parameters:
    data (List[Number]): The list of numbers.

    Returns:
    Number: The mode of the numbers.

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


def variance(data: List[Number]) -> float:
    """
    Calculate the variance of a list of numbers.

    Parameters:
    data (List[Number]): The list of numbers.

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


def standard_deviation(data: List[Number]) -> float:
    """
    Calculate the standard deviation of a list of numbers.

    Parameters:
    data (List[Number]): The list of numbers.

    Returns:
    float: The standard deviation of the numbers.

    Raises:
    TypeError: If the input is not a list or if the list contains non-number elements.
    ValueError: If the list is empty.

    Example:
    >>> standard_deviation([1, 2, 3, 4, 5])
    1.5811388300841898
    """
    if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("Input must be a list of numbers.")
    if not data:
        raise ValueError("The list must not be empty.")
    return statistics.stdev(data)


def harmonic_mean(data: List[Number]) -> float:
    """
    Calculate the harmonic mean of a list of numbers.

    Parameters:
    data (List[Number]): The list of numbers.

    Returns:
    float: The harmonic mean of the numbers.

    Raises:
    TypeError: If the input is not a list or if the list contains non-number elements.
    ValueError: If the list is empty.

    Example:
    >>> harmonic_mean([1, 2, 3, 4, 5])
    2.18978102189781
    """
    if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("Input must be a list of numbers.")
    if not data:
        raise ValueError("The list must not be empty.")
    return statistics.harmonic_mean(data)


def geometric_mean(data: List[Number]) -> float:
    """
    Calculate the geometric mean of a list of numbers.

    Parameters:
    data (List[Number]): The list of numbers.

    Returns:
    float: The geometric mean of the numbers.

    Raises:
    TypeError: If the input is not a list or if the list contains non-number elements.
    ValueError: If the list is empty.

    Example:
    >>> geometric_mean([1, 2, 3, 4, 5])
    2.6051710846973517
    """
    if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("Input must be a list of numbers.")
    if not data:
        raise ValueError("The list must not be empty.")
    return statistics.geometric_mean(data)


if __name__ == "__main__":
    import doctest
    doctest.testmod()