"""
This problem can be solved with the mathematical concept of the partition function p(n), where you partition a number n into piles that sum up to n. We can implement the partition function and simply count the value of p(100) (subtracted by 1 since p(n) includes the configuration of one pile: n).
The partition function p(n), proven by Euler's pentagonal number theorem, can be expressed in terms of the partition functions of n - g_k where g_k is the kth generalized pentagonal number.
Pentagonal numbers are calculated by p_n = n(3n-1)/2 and are generalized by taking negative numbers as well, with the sequence of generalized pentagonal numbers being this function on the sequence 0, 1, -1, 2, -2, etc. We can cache this in the implementation.
"""
import functools

def pentagonal(i):
    """Returns the generalized pentagonal number given by the value i"""
    return i*(3*i - 1)//2

@functools.cache
def partition(n):
    """
    Recursively computes the partition function of n"""
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    s = 0
    i = 1
    neg = 1
    while n - pentagonal(i) >= 0 or n - pentagonal(-i) >= 0:
        s += neg*(partition(n - pentagonal(i)) + partition(n - pentagonal(-i)))
        i += 1
        neg *= -1
    return s

def solve():
    return partition(100) - 1

if __name__ == "__main__":
    print(solve())