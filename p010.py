"""
We can use the sieve of eratosthenes to filter for all the primes
less than 2000000 and simply sum them
"""

def solve():
    n = 2000000
    primes = [True for _ in range(n+1)]
    primes[0] = primes[1] = False
    # sieve of eratosthenes
    for i in range(2, n + 1):
        if primes[i]:
            for j in range(i**2, n + 1, i):
                primes[j] = False

    return sum([i for i, is_prime in enumerate(primes) if is_prime == True])

if __name__ == "__main__":
    print(solve())