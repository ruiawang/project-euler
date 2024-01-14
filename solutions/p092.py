"""
We can implement recursively define the chain by taking advantage of knowing the only 2 stopping cases, and return 1 if the stop is 89 and 0 if the stop is 1. Additionally, we cache these functional evaluations to speed up the computation.

We can then just iterate through each number in the specified range. I chose to do it in reverse order because this way the savings on computation time due to the caching becomes a bit more intuitive.
"""
import functools

@functools.cache
def chain(n):
    if n == 1:
        return 0
    if n == 89:
        return 1
    return chain(sum(int(x)**2 for x in str(n)))

def solve():
    return sum(chain(n) for n in range(10**7-1, 0, -1))

if __name__ == "__main__":
    print(solve())