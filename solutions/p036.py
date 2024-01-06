"""
We can iterate through each number and check its palindromicity. We don't need to worry about negative numbers since automatically their binary representations are not palindromes.
"""
def palindrome(n):
    """Checks if number and its binary representation are both palindromes"""
    s = str(n)
    b = bin(n)[2:]
    return s == s[::-1] and b == b[::-1]

def solve():
    return sum(i for i in range(10**6) if palindrome(i))

if __name__ == "__main__":
    print(solve())