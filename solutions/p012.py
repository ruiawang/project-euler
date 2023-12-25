"""
We can simply brute force the number of divisors for each triangular number.
"""
import itertools, math

def triangular(n):
    """Computes the nth triangular number"""
    return n*(n+1)//2

def count_divisors(n):
    """Counts the number of divisors of n"""
    count = sum(2 for i in range(1, math.isqrt(n) + 1) if n % i == 0)
    if math.isqrt(n) ** 2 == n:
        count -= 1
    return count

def solve():
    for i in itertools.count(1):
        if count_divisors(triangular(i)) > 500:
            return triangular(i)
        
if __name__ == "__main__":
    print(solve())