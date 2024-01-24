"""
We can simply use python's near-arbitrary precision math and brute force
"""
def solve():
    return max(sum(int(c) for c in str(a**b)) for a in range(100) for b in range(100))

if __name__ == "__main__":
    print(solve())