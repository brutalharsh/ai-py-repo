import statistics
from typing import Union, List

Number = Union[int, float]

def validate_numbers(*args: Number):
    """
    Validate that all provided arguments are numbers.

    Parameters:
    *args (Number): The numbers to validate.

    Raises:
    TypeError: If any of the inputs is not a number.
    """
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise TypeError("All inputs must be numbers.")

def validate_list_of_numbers(data: List[Number]):
    """
    Validate that the input is a list of numbers.

    Parameters:
    data (List[Number]): The list to validate.

    Raises:
    TypeError: If the input is not a list or if the list contains non-number elements.
    ValueError: If the list is empty.
    """
    if not isinstance(data, list):
        raise TypeError("Input must be a list of numbers.")
    if not data:
        raise ValueError("The list must not be empty.")
    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements in the list must be numbers.")

def add(a: Number, b: Number) -> Number:
    """
    Add two numbers.
    """
    validate_numbers(a, b)
    return a + b

def subtract(a: Number, b: Number) -> Number:
    """
    Subtract the second number from the first.
    """
    validate_numbers(a, b)
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """
    Multiply two numbers.
    """
    validate_numbers(a, b)
    return a * b

def divide(a: Number, b: Number) -> Number:
    """
    Divide the first number by the second.
    """
    validate_numbers(a, b)
    if b == 0:
        raise ZeroDivisionError("The second input must not be zero.")
    return a / b

def mean(data: List[Number]) -> float:
    """
    Calculate the mean of a list of numbers.
    """
    validate_list_of_numbers(data)
    return statistics.mean(data)

def median(data: List[Number]) -> float:
    """
    Calculate the median of a list of numbers.
    """
    validate_list_of_numbers(data)
    return statistics.median(data)

def mode(data: List[Number]) -> Number:
    """
    Calculate the mode of a list of numbers.
    """
    validate_list_of_numbers(data)
    try:
        return statistics.mode(data)
    except statistics.StatisticsError:
        raise ValueError("No unique mode found in the list.")

def variance(data: List[Number]) -> float:
    """
    Calculate the variance of a list of numbers.
    """
    validate_list_of_numbers(data)
    return statistics.variance(data)

def standard_deviation(data: List[Number]) -> float:
    """
    Calculate the standard deviation of a list of numbers.
    """
    validate_list_of_numbers(data)
    return statistics.stdev(data)

def harmonic_mean(data: List[Number]) -> float:
    """
    Calculate the harmonic mean of a list of numbers.
    """
    validate_list_of_numbers(data)
    return statistics.harmonic_mean(data)

def geometric_mean(data: List[Number]) -> float:
    """
    Calculate the geometric mean of a list of numbers.
    """
    validate_list_of_numbers(data)
    return statistics.geometric_mean(data)

if __name__ == "__main__":
    import doctest
    doctest.testmod()