'''
We can iterate through every pair and count the amicable numbers
'''
import functools
import math

@functools.cache # cache
def sum_proper_divisors(n):
    '''
    Finds the sum of the proper divisors of n
    '''
    s = 1 # since is always a divisor
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            s += i + n // i
    if math.isqrt(n) ** 2 == n:
        s -= math.isqrt(n) # account for overcounting on perfect squares
    return s

def solve():
    ans = 0
    for i in range(1, 10000):
        for j in range(1, 10000):
            if sum_proper_divisors(i) == j and sum_proper_divisors(j) == i and i != j:
                ans += i
    return ans

if __name__ == "__main__":
    print(solve())