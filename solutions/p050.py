"""
After locating the primes under 1 million, we can iterate through them.
At each prime, we iterate through the subsequent/remaining primes in the list and update our answer when we achieve a higher consecutive chain of primes.
We can transfer our list of primes into an O(1) lookup data structure like a set to speedup computation.
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

    p = 0
    c = 0
    check = set(primes)
    for i in range(len(primes)):
        s = primes[i]
        cur = 1
        for j in range(i+1, len(primes)):
            s += primes[j]
            cur += 1
            if s >= bound:
                break
            if s in check and cur > c:
                p = s
                c = cur
    return p, c
print(solve())