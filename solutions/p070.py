"""
We can implement the totient function and check for permutations, while maintaining the minimum.
We can cache the smallest prime factor of n to aid in the speed of the computation.
This code is pretty slow, and I think the implementation of totient can be improved.
"""

import math
import functools

@functools.cache
def smallest_factor(n: int) -> int:
    """Finds the smallest factor of n (necessarily prime)"""
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            return i

    return n # n itself is a prime number

def prime_factors(n: int) -> list:
    """Returns the distinct prime factors of n"""
    s = set()
    p = smallest_factor(n)
    s.add(p)
    while p < n:
        n //= p
        p = smallest_factor(n)
        s.add(p)
    return list(s)

def phi(n: int) -> int:
    """
    Implementation of Totient function using formulation
    phi(n) = n * \prod_{p|n, p prime} (1-1/p)
    """
    if n == 1:
        return 1
    phi = n
    for p in prime_factors(n):
        phi *= 1 - 1/p
    return int(phi)

def is_permutation(a: int, b: int) -> bool:
    """Checks if two numbers are permutations of each other"""
    return sorted(str(a)) == sorted(str(b))

def solve():
    m = float("inf")
    N = 0
    for n in range(2, 10**7):
        p = phi(n)
        if is_permutation(n, p) and n/p < m:
            m = n/p
            N = n
    return N
if __name__ == "__main__":
    print(solve())
