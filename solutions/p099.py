"""
We can use natural log and Python's (near) arbitrary-precision math
and iterate through the file
"""
import math
def solve():
    lines = []
    with open('0099_base_exp.txt', 'r') as f:
        for line in f:
            lines.append([int(n) for n in line.split(',')])
    idx, m = 0, 0
    for i, line in enumerate(lines):
        base, pow = line
        val = pow*math.log(base)
        if val >= m:
            idx = i
            m = val
    return idx + 1

if __name__ == "__main__":
    print(solve())