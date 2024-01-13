"""
We can implement the totient function and find the maximum.
We can cache the smallest prime factor of n to aid in the speed of the computation.
"""

import math
import functools

@functools.cache
def smallest_factor(n):
    """Finds the smallest factor of n (necessarily prime)"""
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            return i

    return n # n itself is a prime number

def prime_factors(n):
    """Returns the distinct prime factors of n"""
    s = set()
    p = smallest_factor(n)
    s.add(p)
    while p < n:
        n //= p
        p = smallest_factor(n)
        s.add(p)
    return list(s)

def phi(n):
    """
    Implementation of Totient function using formulation
    phi(n) = n * \prod_{p|n} (1-1/p)
    """
    if n == 1:
        return 1
    phi = n
    for p in prime_factors(n):
        phi *= 1 - 1/p
    return int(phi)

def solve():
    i, m = 1, 1
    for n in range(1, 10**6 + 1):
        if n/phi(n) > m:
            i, m = n, n/phi(n)
    return i

if __name__ == "__main__":
    print(solve())
