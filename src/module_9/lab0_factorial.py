'''Alternative, more robust version
    def factorial(n: int) -> int:
        """Recursive function that calculates the factorial of an integer.
        Args:
            n: Non-negative integer for which the factorial will be calculated.

        Returns:
            The value of n factorial.

        Raises:
            ValueError: if n is negative.
            TypeError: if n is not an integer.
        """
        if not isinstance(n, int):
            raise TypeError("Factorials of non-integer numbers are undefined.")
        if n < 0:
            raise ValueError("Factorials of negative numbers are undefined.")
        if n <= 1:
            return 1
        return n * factorial(n - 1)
'''

def factorial(n: int) -> int:
    """Recursive function that calculates the factorial of an integer.
    Args:
        n: Number for which the factorial will be calculated.
    
    Returns:
        The value of n factorial.
    """
    if n == 1:
        return 1
    return n * factorial(n - 1)


result = factorial(3)