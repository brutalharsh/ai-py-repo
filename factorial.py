def calculate_factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer using an iterative approach.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the given number.

    Raises:
    ValueError: If the input is a negative integer.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage
print(calculate_factorial(5))  # Output: 120
print(calculate_factorial(0))  # Output: 1
try:
    calculate_factorial(-1)
except ValueError as e:
    print(e)  # Output: ValueError: Input must be a non-negative integer.
