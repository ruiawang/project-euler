"""
Note that the total number of rectangles in a larger rectangle 
can be approached purely combinatorically.
If we imagine a m * n rectangle, we can envision it as a a grid space,
that occupies m + 1 vertical lattice lines, and n + 1 horizontal lattice lines.
Since each smaller sub-rectangle uses a selection of 2 different horizontal lines and 2 different vertical lines,
the total way to choose these pairs of lines is m + 1 choose 2 times n + 1 choose 2. 
This is equal to m * (m + 1) * n * (n + 1)/4  which is asymptotically (mn/2)^2.

From this, we can brute force through tuples of dimensions and measure its deviation from the target amount. We don't actually need to control this search space, and can just set it to be a square of area closest to our target
as a guaranteed estimate, then we just find the minimum deviation tuple, and compute its area.
"""

import math

def count_rectangles(m, n):
    return math.comb(m+1, 2) * math.comb(n+1, 2)

def solve():
    target = 2*(10**6)
    max_side = math.isqrt(target) + 1
    search_space = [(m, n) for m in range(1, max_side) for n in range(1, max_side)]
    deviation = lambda mn: abs(count_rectangles(*mn) - target)
    m, n = min(search_space, key=deviation)
    return m * n

if __name__ == "__main__":
    print(solve())