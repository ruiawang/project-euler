"""
We can solve this using brute force and calculating the set of digits in each multiple of i and see if they are the same
"""
import itertools

def solve():
    for i in itertools.count(1):
        s = set([c for c in str(i)])
        if all(set([c for c in str(j*i)]) == s for j in range(1,7)):
            return i

if __name__ == "__main__":
    print(solve())