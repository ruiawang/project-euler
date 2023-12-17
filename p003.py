"""
For the problem of n, we can utilize its prime factorization
and at each step, divide n out by its lowest prime factor.
By doing so repeatedly, we will end up with the largest prime factor of n.

Additionally, when we divide n out by its lowest prime factor at each step,
we only need to find its lowest factor, which will still be prime.
"""
import math

def smallest_factor(n):
    """Finds the smallest factor of n"""
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            return i

    return n # n itself is a prime number


def solve():
    n = 600851475143
    p = smallest_factor(n)
    while p < n:
        n //= p
        p = smallest_factor(n)

    return p

if __name__ == "__main__":
    print(solve())