"""
Once we count all the primes under 100, we can increment our counter by iteratively select primes until our product reaches the limit. We can do dfs on the tree of primes to find all the ways to pathways that yield different numbers.
"""
def solve():
    n = 10**9
    m = 100
    # Sieve of Eratosthenes to find primes
    primes = [True for _ in range(m+1)]
    primes[0] = primes[1] = False
    for i in range(2, m + 1):
        if primes[i]:
            for j in range(i**2, m + 1, i):
                primes[j] = False
    
    primes = [i for i, is_prime in enumerate(primes) if is_prime == True]
    
    def dfs(idx, prod):
        if idx == len(primes): # if we've finished going through primes
            return 1 if prod <= n else 0
        else:
            res = 0
            while prod <= n:
                res += dfs(idx+1, prod) # dfs
                prod *= primes[idx] # increase current product
            return res
    
    return dfs(0,1)

if __name__ == "__main__":
    print(solve())