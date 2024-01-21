"""
We can use Python's (near)-arbitrary precision math and using mod at each step

(28433*(2**7830457) + 1) % 10**10
=28433*(2**7830457 % 10**10) + 1) % 10**10
"""
def solve():
    M = 10**10 # 10 digits only
    return (28433*pow(2, 7830457, M) + 1) % M

if __name__ == "__main__":
    print(solve())