"""
We can examine every pandigital number and check if the arrangement satisfies the property.
"""
import itertools

CHECKS = [2, 3, 5, 7, 11, 13, 17]
def divisibility_condition(n):
    return all((n[i+1]*100 + n[i+2]*10 + n[i+3]) % p == 0 for i, p in enumerate(CHECKS))

def solve():
    return sum(int(''.join(map(str, p))) for p in itertools.permutations(range(10)) if divisibility_condition(p))

if __name__ == "__main__":
    print(solve())