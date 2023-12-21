"""
We can simply use python's arbitrary-precision numbers
"""
def solve():
    return sum(int(c) for c in str(2**1000))

if __name__ == "__main__":
    print(solve())