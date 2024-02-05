"""
We can run this with brute force.
"""
def solve():
    MAX = 28124
    sum_divs = [0 for _ in range(MAX)]
    for i in range(1, MAX):
        for j in range(i*2, MAX, i):
            sum_divs[j] += i
    abundants = [i for i, n in enumerate(sum_divs) if n > i]

    possibles = [False for _ in range(MAX)]
    for i in abundants:
        for j in abundants:
            if i + j < MAX:
                possibles[i + j] = True
            else:
                break
    
    return sum(i for i, n in enumerate(possibles) if not n)

if __name__ == "__main__":
    print(solve())