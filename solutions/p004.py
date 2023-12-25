"""
While not a clever solution, we can simply iterate
through the numbers and exhaust the palindromes.
"""

def solve():
    return max(x*y for x in range(100,1000) for y in range(100,1000) if str(x*y) == str(x*y)[::-1])

if __name__ == "__main__":
    print(solve())