from collections import defaultdict
from typing import Dict

def merge_dictionaries(dict1: Dict[str, int], dict2: Dict[str, int]) -> Dict[str, int]:
    """
    Merges two dictionaries summing the values of common keys.

    Args:
        dict1 (Dict[str, int]): The first input dictionary.
        dict2 (Dict[str, int]): The second input dictionary.

    Returns:
        Dict[str, int]: A new dictionary containing all keys from both input dictionaries.
                        The values of common keys are summed.
    """
    merged_dict = defaultdict(int)
    for key, value in dict1.items():
        merged_dict[key] += value
    for key, value in dict2.items():
        merged_dict[key] += value
    return dict(merged_dict)