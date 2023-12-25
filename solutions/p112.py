"""
We can brute-force iterate through.
"""
import itertools

def solve():
    count = 0
    for i in itertools.count(1):
        n = str(i)
        sort = "".join(sorted(n))
        if n != sort and n[::-1] != sort:
            count += 1

        if count / i == 0.99:
            return i


if __name__ == "__main__":
    print(solve())