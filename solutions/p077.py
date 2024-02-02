"""
We can implement a function that checks if a number is prime.

Furthermore, we can then use dynamic programming to find the number of summations of these primes.
"""
import itertools
import math

PRIMES = [2]

def is_prime(x):
	"""
	Returns if a number is prime or not.
	"""
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, math.isqrt(x) + 1, 2):
			if x % i == 0:
				return False
		return True

def num_summations(n):
	"""
	Returns number of ways to have prime summations of a number n.
	"""
	for i in range(PRIMES[-1] + 1, n + 1): # add new primes since the last prime
		if is_prime(i):
			PRIMES.append(i)
	
	dp = [1] + [0] * n # dp table
	for p in PRIMES:
		for i in range(n + 1 - p):
			dp[i + p] += dp[i]
	return dp[n]

def solve():
	cond = lambda n: num_summations(n) > 5000
	return next(filter(cond, itertools.count(2)))

if __name__ == "__main__":
	print(solve())