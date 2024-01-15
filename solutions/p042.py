"""
We can use a property about triangular numbers to quickly determine if a number is triangular. Since triangular numbers n are always such that n = m*(m+1)/2 for some number m, we can rearrange to yield m^2 + m - 2n = 0, which yields solution m = (-1 + sqrt(1 - 4*(-2)*1))/2 = (-1 + sqrt(8n + 1))/2 by the quadratic formula, which will only yield integers whenever 8n + 1 is a perfect square.
Thus we can apply this equivalence to the value sum of a word and check, and then iterate through the file and count the number of such words.
"""
import math

WORD_MAP = {c:i+1 for i, c in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}

def triangular_word(word: str) -> bool:
    """Returns if given word's value sum is triangular"""
    n = sum(WORD_MAP[c] for c in word)
    return math.isqrt(8 * n + 1) ** 2 == 8 * n + 1

def solve():
    with open('0042_words.txt', 'r') as f:
        s = f.readline()[1:-1]
        words = s.split('","')
    
    return sum(1 for word in words if triangular_word(word))
if __name__ == "__main__":
    print(solve())