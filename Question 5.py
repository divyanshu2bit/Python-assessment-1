# math_utils.py

def factorial(n):
    """Return n! for a non-negative integer n."""
    if not isinstance(n, int):
        raise TypeError("factorial() only accepts integers")
    if n < 0:
        raise ValueError("factorial() not defined for negative numbers")

    if n == 0 or n == 1:
        return 1
    # recursion
    return n * factorial(n - 1)


def is_prime(n):
    """Return True if n is prime, False if not. Raise error for invalid input."""
    if not isinstance(n, int):
        raise TypeError("is_prime() only accepts integers")
    if n <= 1:
        raise ValueError("is_prime() only defined for integers greater than 1")

    # 2 is prime
    if n == 2:
        return True

    # even numbers > 2 are not prime
    if n %
