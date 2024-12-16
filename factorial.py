def calculate_factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the given number.

    Raises:
    ValueError: If the input is a negative integer.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)

# Example usage
print(calculate_factorial(5))  # Output: 120
print(calculate_factorial(0))  # Output: 1
print(calculate_factorial(-1)) # Output: ValueError: Input must be a non-negative integer.