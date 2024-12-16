import statistics
from typing import List, Dict, Any

def calculate_statistics(numbers: List[int]) -> Dict[str, Any]:
    """
    Calculate and return statistical measures for a list of integers.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    Dict[str, Any]: A dictionary containing the min, max, mean, median, and standard deviation.
    """
    if not numbers:
        raise ValueError("The list of numbers is empty.")

    stats = {
        "min": min(numbers),
        "max": max(numbers),
        "mean": statistics.mean(numbers),
        "median": statistics.median(numbers),
        "std_dev": statistics.stdev(numbers) if len(numbers) > 1 else float('nan')
    }

    return stats

if __name__ == "__main__":
    example_data = [3, 5, 7, 2, 8, 10]
    print(calculate_statistics(example_data))