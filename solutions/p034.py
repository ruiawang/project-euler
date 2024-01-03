"""
We can set the upper bound of our search space to be 10^7 since 
9! * 7 < 9999999, which is also true if we keep adding digits so any
number with more than 7 digits will far exceed the sum of its digit factorials

We cache the digit factorials for easy retrieval.
"""
import math

def solve():
    factorials = {i:math.factorial(i) for i in range(10)}
    return sum(i for i in range(10,10**7) if sum(factorials[int(x)] for x in str(i)) == i)

if __name__ == "__main__":
    print(solve())