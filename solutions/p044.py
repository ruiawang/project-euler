"""
We can solve this with mathematical reasoning.
For an n x n square with n > 1, we have that:
the top right corner will be n^2,
the top left corner will be n^2-n+1
the bot left corner will be n^2-2n+2
the bot right corner will be n^2-3n+3
which altogether sums to 4n^2-6n+6=4n^2-6(n-1),
and then we can solve again for an n-2 x n-2 square.

We can also go further and find a closed form for this in terms of n.
It is known that the sum of the first k odd squares is k(2k+1)(2k-1)/3,
since the sum of the first k squares is k(k+1)(2k+1)/6,
and the sum of the first k even squares is 4*k(2k+1)(2k-1)/6=2k*(k+1)(2k-1)/3
from which we use the sum of the first 2k squares is 2k(2k+1)(4k+1)/6 and subtract.
n = 2k-1, expressed as the kth odd.

If we express the sum of all these corners of the n x n square we yield:
1 + 4*(3^2 +  5^2 + ... + n^2)- 6(3-1 + 5-1 + ... n-1)
=1 + 4*(1^2 + 3^2 + ... + n^2) - 4 - 6(n^2-1)/4
=1 + 4*((n+1)*(n+2)*n/6) - 3(n^2-1)/2 - 4, which after simplfiication yields:
=(4n^3 + 3n^2 + 8n - 9)/6
"""

def solve():
    s = 1
    m = 1001
    for n in range(m, 1, -2):
        s += 4*(n**2)-6*(n-1)
    return s
    # return (4*(m**3) + 3*(m**2) + 8*m - 9)/6
if __name__ == "__main__":
    print(solve())