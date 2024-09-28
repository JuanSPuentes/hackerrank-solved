"""The Maximum Subarray
https://www.hackerrank.com/challenges/maxsubarray/problem"""

def maxSubarray(arr) -> list[int]:
    """
    Returns the maximum subarray sum and the maximum subsequence sum.

    Args:
        arr (list): List of integers.

    Returns:
        list: Maximum subarray sum and maximum subsequence sum.
    """
    max_element, current_subarray_sum, max_subsequence_sum, max_subarray_sum = arr[0], 0, 0, 0
    for i in arr:
        max_element = max(max_element, i)
        current_subarray_sum = max(0, current_subarray_sum + i)
        max_subsequence_sum = max(max_subsequence_sum, current_subarray_sum)
        max_subarray_sum += max(0, i)
    
    if max_element < 0:
        return [max_element, max_element]
    return [max_subsequence_sum, max_subarray_sum]

if __name__ == '__main__':
    arr = [-1, -2, -3, -4, -5, -6]
    result = maxSubarray(arr)
    print(result) # [-1, -1]