"""
We can implement the circular primes function and brute force check.
"""
def solve():
    bound = 999999
    # sieve of eratosthenes
    primes = [True for _ in range(bound+1)]
    primes[0] = primes[1] = False
    for i in range(2, bound + 1):
        if primes[i]:
            for j in range(i**2, bound + 1, i):
                primes[j] = False
    
    primes = [i for i, is_prime in enumerate(primes) if is_prime == True]
    lookup = set(primes)

    def circular_prime(n):
        """Checks if n is a circular prime"""
        s = str(n)
        return all(int(s[i:] + s[:i]) in lookup for i in range(len(s)))
    
    return sum(1 for p in primes if circular_prime(p))

if __name__ == "__main__":
    print(solve())