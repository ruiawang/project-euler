"""
We can solve this problem with purely mathematical intuition.
For any n-digit nth power x ** n, we evidently see that the base of the power x must be less than 10, as being an n-digit number implies that x**n < 10**n.
However, we can also supplement this with a lower bound, as the smallest n-digit number is 10**(n-1). 
Thus we have that 10**(n-1) <= x**n < 10**n.
Since x < 10, 10**(n-1) grows faster than x ** n, and thus
for each choice of x from 1 to 9, we see that 10**(n-1) <= x**n can be rearranged
into an inequality describing the maximum n until which the power x**n
will be less than 10^(n-1), and thus an n-1 digit number, failing the condition.
By taking a logarithm on both sides,  n-1 <= n log_10(x) yielding n <= 1/(1-log_10(x)). Similarly, if using ln the bound becomes:
n <= ln(10)/(ln(10)-ln(x)) which is equivalent to our expression.
All integer numbers k under this maximum will yield a k digit number for the kth power of x. 
From here we just sum up this bound for the possible bases 1 to 9.
"""
import math
def solve():
    return sum(int(1/(1-math.log(i, 10))) for i in range(1,10))

if __name__ == "__main__":
    print(solve())