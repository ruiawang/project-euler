"""
We can simply iterate through each perimeter value
and find all pythagorean triplets and maintain the maximum value
"""
def find_triplets(p):
    """
    Finds the number of pythagorean triples that satisfy a sum value p
    """
    result = 0
    for a in range(1, p + 1):
        for b in range(a, (p - a) // 2 + 1):
            c = p - a - b
            if a**2 + b**2 == c**2:
                result += 1

    return result

def solve():
    return max(range(1, 1001), key = find_triplets)

if __name__ == "__main__":
    print(solve())