""" Recursive Digit Sum
    https://www.hackerrank.com/challenges/recursive-digit-sum/problem """

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k) -> int:
    """
    Calculates the recursive digit sum of a number.

    The super digit of a number is defined as the recursive sum of its digits until a single digit is obtained.
    When the number is repeated `k` times, the super digit is calculated for the concatenated number.

    Args:
        n (str): The initial number represented as a string.
        k (int): The number of times the initial number is repeated.

    Returns:
        int: The super digit of the concatenated number.
    """
    if len(n) == 1:
        return int(n)
    else:
        sum_digits = sum([int(i) for i in n]) * k
        return superDigit(str(sum_digits), 1)

if __name__ == '__main__':
    n = '148'
    k = 3
    result = superDigit(n, k)
    print(result)  # 3