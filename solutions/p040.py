"""
We can simply create this fraction and find the requisite product of digits.
"""
def solve():
    s = ''.join(str(i) for i in range(1,10**7 + 1))
    ans = 1
    for n in range(7):
        ans *= int(s[10**n - 1])
    return ans

if __name__ == "__main__":
    print(solve())