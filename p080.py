"""
We have to lift the number and take an integer square root because of floating point precision in python.
To do this we multiply each number by 100^100 to get 100 digits, since int(sqrt(x)*10^100) = int(sqrt(x*((10^2)^100))
which is equal to int(sqrt(x*100^100)).
"""

import math

def solve():
    return sum(sum(int(c) for c in str(math.isqrt(i*(100**100)))[:100]) for i in range(100) if math.isqrt(i) ** 2 != i)

if __name__ == "__main__":
    print(solve())