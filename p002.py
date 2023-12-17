"""
We can simply iterate and add.
"""

def solve():
    ans = 0
    x, y = 1, 2
    while x <= 4000000:
        if x % 2 == 0:
            ans += x 
        x, y = y, y + x
    
    return ans

if __name__ == "__main__":
    print(solve())