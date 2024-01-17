"""
We can use dynamic programming to count the number of ways to make up a value of n,  with the base case that dp[0] = 1 (there is 1 way to make 0).
For each valid coin value c, if we start at that coin value and iterate up to the max as n, we can sum dp[n - c] for dp[n], since for a higher value of c, for example 20, there is no way to make any sums beneath 20 by using c.
"""
def solve():
    coins = [1,2,5,10,20,50,100,200]
    total = 200
    dp = [0]*(total+1)
    dp[0] = 1
    for c in coins:
        for n in range(c, total+1):
            dp[n] += dp[n-c]
    return dp[total]

if __name__ == "__main__":
    print(solve())