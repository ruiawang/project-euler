"""
We can map out the special cases and the number of letters
Afterwards we can formalize the rules of when to add "and", etc.
"""
def letters(n):
    """
    Finds the number of letters in the spelling of n
    """
    mapping = {90: 6, 80: 6, 70: 7, 60: 5, 50: 5, 40: 5, 30: 6, 20: 6, 19: 8, 18: 8, 17: 9, 16: 7, 15: 7, 14: 8, 13: 8, 12: 6, 11: 6, 10: 3, 9: 4, 8: 5, 7: 5, 6: 3, 5: 4, 4: 4, 3: 5, 2: 3, 1: 3}
    if n == 1000:
        return 11
    count = 0
    
    c = n // 100
    if c != 0:
        count += mapping[c] + 7
        if n % 100 != 0:
            count += 3
    n -= c * 100

    for key in mapping:
        if n >= key:
            count += mapping[key]
            n -= key
    return count

def solve():
    return sum(letters(n) for n in range(1,1001))

if __name__ == "__main__":
    print(solve())