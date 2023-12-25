"""
We can solve this problem by understanding the combinatorial nature of lattice walk problems.
Notably, to go from (0,0) to (a,b), the total number of different ways to do this is the a+b choose a.
"""
import math

def solve():
    A = B = 20
    return math.comb(A + B, A)

if __name__ == "__main__":
    print(solve())