def is_prime(n):
    """
    Check if a number is prime.
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if not isinstance(n, int) or n is None:
        return False

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

print(is_prime(3))