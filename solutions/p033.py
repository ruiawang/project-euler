"""
for n = n0*10 + n1, d = d0*10 + d1, note that it is impossible for the canceling digits to be both n0,d0 or n1,d1, as that would yield n=d.
Thus, we must only have cross digits maintaining the fraction, as in
if n1 == d0, then n0/d1 = n/d, and if n0 == d1, then n1/d0 = n/d.
Then we just brute force through the possible choices of n, d.
We will cross multiply to remove the fraction so as to avoid divide by 0 errors.

This problem is also simple enough to just use pencil and paper, given enough time, you can note that the four fractions are: 16/64, 19/95, 26/65, as well as the given 49/98.
"""
import math

def solve():
    n_ans, d_ans = 1, 1
    for d in range(10, 100):
        for n in range(10, d):
            n0 = n // 10
            n1 = n % 10
            d0 = d // 10
            d1 = d % 10
            if (n1 == d0 and n0*d == n*d1) or (n0 == d1 and n1*d == n*d0):
                n_ans *= n
                d_ans *= d
    return d_ans // math.gcd(n_ans, d_ans)

if __name__ == "__main__":
    print(solve())