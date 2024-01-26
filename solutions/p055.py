"""
We can implement and check if a number is lychrel based on the conditions listed. We don't need to worry about negative numbers since negative numbers are never palindromic (and can't be reversed). Then we can brute force and check for each number in the range.
"""
def is_palindrome(n):
    """returns if n is palindrome"""
    return str(n)[::-1]==str(n)

def is_lychrel(n):
    """returns if n is lychrel"""
    for _ in range(50):
        rev = int(str(n)[::-1])
        if is_palindrome(n + rev):
            return False
        n += rev
    return True

def solve():
    return sum(1 for i in range(10000) if is_lychrel(i))

if __name__ == "__main__":
    print(solve())