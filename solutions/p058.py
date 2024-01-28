"""
We can implement a function to check if a number n is prime (inefficient, but computing is fast)
From then on, we note that for each square of length n, as described in the problem, the number n^2 will always the bottom left corner,
and the number (n-1)^2 will always be the number positioned immediately to the right of the upper left corner.
Thus we can derive that our numbers of interest are:
Upper Left = (n-1)^2 + 1 = n^2 - 2n + 2
Bottom Left = (n-1)^2 + n = n^2 - n + 1
Upper Right = (n-1)^2 - (n - 2) = n^2 - 3n + 3
Thus, when we iterate through n the size of the square, we only need to count each of these numbers and check their primality, and keep track.
Additionally, since there are always 2n - 1 total numbers on the two diagonals,
we can check the ratio of the prime count against this, and exit when we first dip under 0.10 (10%). And as we add on a layer, we increment n by 2.
"""
import math
import itertools

def is_prime(n):
    """Checks if number is prime"""
    return all(n % i != 0 for i in range(2, math.isqrt(n)))

def solve():
    primes = 0
    for n in itertools.count(3,2):
        ul = n**2 - 2*n + 2
        bl = n**2 - n + 1
        ur = n**2 - 3*n + 3
        primes += sum(1 for x in [ul, bl, ur] if is_prime(x))
        if primes/(2*n - 1) < 0.10:
            return n

if __name__ == "__main__":
    print(solve())