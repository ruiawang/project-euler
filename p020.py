"""
We can simply calculate 100! using python math and sum the digits
"""
import math

def solve():
    return sum(int(x) for x in str(math.factorial(100)))

if __name__ == "__main__":
    print(solve())