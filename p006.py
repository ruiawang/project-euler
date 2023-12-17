"""
We can simply iterate and compute, but we can also solve this
completely manually with some results and identities about sums
The sum of the first n numbers is n(n+1)/2
The sum of the first n squares is n(n+1)(2n+1)/6
Thus the desired difference is:
(n(n+1)/2)**2 - n(n+1)(2n+1)/6
= 1/4 * (n**4 + 2n**3  + n**2) - 1/6 * (2n**3 + 3n**2 + n)
= n**4 / 4 + n**3 / 6 - n**2 / 4 - n / 6

which yields 232792560 after tedious arithmetic
"""

def solve():
    return 100**4 / 4 + 100**3 / 6 - 100**2 / 4 - 100 / 6

if __name__ == "__main__":
    print(solve())
    # print(sum(x for x in range(1, 101))**2 - sum(x**2 for x in range(1, 101)))