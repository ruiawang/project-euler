"""
This can be solved manually with some elementary counting.

Since we are given 2520 which is divisible by all the numbers from 1 to 10.
We see that 2520 = 2**3 * 3**2 * 5 * 7. To cover 1 to 20 we simply need to
additionally include the primes from 11 to 20, so 11, 13, 17, 19, as well
as any of the missing pre-existing prime powers. The composite numbers of 
11 to 20 are not all covered:
12 = 2**2 * 3, 14 = 2 * 7, 15 = 3 * 5, 18 = 2 * 3**2 
but 16 = 2**4, which is not included.
Thus we need to include an extra 2.
Thus our final answer will be 2520 * 11 * 13 * 17 * 19 * 2
whih will yield 232792560 at the end of some tedious arithmetic

We can also utilize math.lcm()
"""
# import math

def solve():
    return 2520 * 11 * 13 * 17 * 19 * 2

if __name__ == "__main__":
    print(solve())
    # print(math.lcm(*range(1,21)))