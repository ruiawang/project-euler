"""
We can use a modular power and sum.
"""
def solve():
    mod = 10**10
    return sum(pow(x, x, mod) for x in range(1,1001)) % mod

if __name__ == "__main__":
    print(solve())