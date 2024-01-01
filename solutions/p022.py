"""
We can simply iterate through the list of names after reading it in.
"""
def solve():
    with open('0022_names.txt', 'r') as f:
        names = f.readline()[1:-1].split('\",\"')
    names.sort()
    return sum((i+1)*sum(ord(c) - ord('A') + 1 for c in name) for i, name in enumerate(names))

if __name__ == "__main__":
    print(solve())