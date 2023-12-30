"""
We can simply iterate through all numbers and check if they satisfy the sum
condition. Notably, we can bound the numbers between 4 digits and 6 digits
as anything 7 * 9^5 < 10^7 and thus even if we had 9999999 the number
exceeds its fifth power digit sum. Similarly for 3 and 2 digits.
"""

def solve():
    return sum(n for n in range(1000,1000000) if dig_fifth_sum(n) == n)

def dig_fifth_sum(n):
    return sum(int(x)**5 for x in str(n))

if __name__ == "__main__":
    print(solve())