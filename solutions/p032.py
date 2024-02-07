'''
We can implement a check for the pandigital products and brute force.
We can also deduce that the upper bound of such numbers has to be at most 4 digits, since if it were 5 digits, the two multiplicative factors would not be able to produce it, as 3 digits * 1 digit, or 2 digits * 2 digits at maximum,
would not be able to produce 5 digits.
'''
import math

def has_prod(n):
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            s = str(i) + str(n//i) + str(n)
            if ''.join(sorted(s)) == '123456789':
                return True
    return False

def solve():
    return sum(i for i in range(1, 10000) if has_prod(i))

if __name__ == "__main__":
    print(solve())