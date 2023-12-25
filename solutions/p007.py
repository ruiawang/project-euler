"""
We can solve this problem by implementing a prime checker and iterating through
numbers and incrementing the counter.
However, we can solve this with some intuitions about primes from number theory:
namely that the nth prime is bounded by the following relation for n >= 6

n * (ln(n) + ln(ln(n)) - 1) < p_n < n * (ln(n) + ln(ln(n)))

With that in mind, we can use n = 10001 and use that upper bound
and run the sieve of eratosthenes to filter and find the primes.
"""
import math

def solve():
    n = 10001
    bound = math.ceil(n * (math.log(n) + math.log(math.log(n))))
    # sieve of eratosthenes
    primes = [True for _ in range(bound+1)]
    primes[0] = primes[1] = False
    for i in range(2, bound + 1):
        if primes[i]:
            for j in range(i**2, bound + 1, i):
                primes[j] = False
    
    primes = [i for i, is_prime in enumerate(primes) if is_prime == True]
    return primes[n - 1]

if __name__ == "__main__":
    print(solve())