"""
We can use python math.comb to efficiently and quickly calculate combinations
Then just use brute force to iterate through the possible ranges and count
"""
import math

def solve():
    return sum(1 for n in range(1, 101) for r in range(n+1) if math.comb(n, r) > 10**6)

if __name__ == "__main__":
    print(solve())