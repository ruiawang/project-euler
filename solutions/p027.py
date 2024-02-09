"""
We can implement this with brute force, with a prime checker.
"""
import math, itertools, functools

@functools.cache
def is_prime(n):
    """Checks if number is prime"""
    if n < 0:
        return False
    return all(n % i != 0 for i in range(2, math.isqrt(n)))

def count_primes(ab):
    """
    Counts how many primes are yielded the configuration a, b for consecutive inputs n for n^2 + an + b.
    """
    for i in itertools.count():
        a, b = ab
        n = i*i + a*i + b
        if not is_prime(n):
            return i
        
def solve():
	ans = max(((a, b) for a in range(-999, 1000) for b in range(2, 1000)),
		key=count_primes)
	return ans[0] * ans[1]

if __name__ == "__main__":
     print(solve())