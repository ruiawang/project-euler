"""
We can memoize/cache the computed collatz lengths as we iterate through 1-999999.
"""
import functools

@functools.cache
def count_collatz_seq(n):
    """Computes length of collatz sequence starting at n"""
    if n == 1:
        return 1
    
    if n % 2 == 1:
        
        return 1 + count_collatz_seq(3*n + 1)
    else:
        return 1 + count_collatz_seq(n/2)

def solve():
    return max(range(1,1000000), key=count_collatz_seq)

if __name__ == "__main__":
    print(solve())