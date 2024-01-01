'''
We can utilize python itertools to list out the permutations for us and find the target.
'''

import itertools

def solve():
    s = '0123456789'
    i = 10**6
    return ''.join(list(itertools.permutations(s))[i - 1])

if __name__ == "__main__":
    print(solve())