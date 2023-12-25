"""
We can simply iterate and add.

There is also a way to solve this problem completely manually
but computation is a better choice, indeed it is much faster and simpler:

We can separately sum the multiples of 3 and the multiples of 5 and subtract the 
multiples of 15 since we will be overcounting them.
Thus we are adding 3 + 6 + ... + 999 = 3(1 + 2 + ... + 333),
5 + 10 + ... + 995 = 5(1 + 2 + ... 199)
together, and then subtracting 15 + ... 990 = 15(1 + 2 + ... + 66)

3(1 + 2 + ... + 333) = 3*333*334/2, 5(1 + 2 ... + 199) = 5*199*200/2,
and 15(1 + 2 + ... + 66) = 15*66*67/2.

After some (tedious) arithmetic you will have:
3*333*334/2 = 166833
5*199*200/2 = 99500
15*66*67/2 = 33165
166733 + 99500 - 33165 = 233168
"""

def solve():
    return sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)

if __name__ == "__main__":
    print(solve())