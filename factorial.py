To optimize and improve the given Python code for calculating a factorial, you can move from a recursive approach to an iterative approach. This change will improve performance and avoid potential recursion limit issues for large inputs. Here is the improved version of the code:

```python
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
```

### Improvements:
1. **Iterative Approach**: The function now uses an iterative approach instead of recursion. This is more efficient for calculating factorials, particularly for larger values of `n`.
2. **`range` Function**: The range starts from `2