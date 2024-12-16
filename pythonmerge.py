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
    merged_dict = dict1.copy()  # Start with a copy of the first dictionary
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict
