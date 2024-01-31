"""
We can implement the sieve of eratosthenes to enumerate all 4-digit primes 
by eliciting a bound of 9999
Afterwards, we can iterate through each such prime, and then iterate through each possible step size and check for the conditions.
We explicitly filter out the example solution of 1487, 4817, 8147 too.
"""

def is_permutation(a, b):
    """
    Returns if two numbers a, b are permutations of each other
    """
    return sorted(str(a)) == sorted(str(b))

def solve():
    bound = 9999
    # sieve of eratosthenes
    primes = [True for _ in range(bound + 1)]
    primes[0] = primes[1] = False
    for i in range(2, bound + 1):
        if primes[i]:
            for j in range(i**2, bound + 1, i):
                primes[j] = False

    for n in range(1000, bound+1):
        if primes[n]:
            for d in range(1, bound+1):
                a = n + d
                b = a + d
                if a < bound+1 and is_permutation(a, n) and primes[a] \
                and b < bound+1 and is_permutation(b, n) and primes[b] \
                and (n != 1487 or a != 4817 or b != 8147):
                    return str(n) + str(a) + str(b)

if __name__ == "__main__":
    print(solve())