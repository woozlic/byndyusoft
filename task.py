from typing import List
def sum_two_mins(arr: List[float]) -> float:
    """
    Function that returns sum of two minimal numbers in array

    Args:
        arr: Array of float or int

    Returns:
        Sum of two minimal numbers in array

    Raises:
        
    """
    if (len(arr) < 2):
        raise ValueError("Array should contain at least 2 numbers")
    first = float("inf")
    second = float("inf")
    for num in arr:
        if not type(num) in (int, float):
            raise TypeError("Only float or int numbers are allowed")
        if num < first:
            second = first
            first = num
        elif num < second and num != first:
            second = num
    if second == float("inf"):
        raise ValueError("Array contains only one smallest element")
            
    return first + second

