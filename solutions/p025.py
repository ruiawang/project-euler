"""
We can simply run through each fibonacci number until we reach one with string length 1000
"""
import itertools 
def solve():
    x, y = 1, 1
    for i in itertools.count(1):
        if len(str(x)) >= 1000:
            return i
        x, y = y, y + x

if __name__ == "__main__":
    print(solve())