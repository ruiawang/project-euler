"""
We can solve this with brute-force iteration, by simply (without loss of generality) assuming a < b < c.
but we can also do this purely mathematically,
using a clever result about the generation of Pythagorean triples by Euclid.
Namely, for a triple a, b, c, if we define a = m^2 - n^2, b = 2mn, then with c = m^2 + n^2
we yield a Pythagorean triple a, b, c. Thus, the problem is about finding m, n such that
we yield a + b + c = 1000. We see that for such m, n: a + b + c = m^2 - n^2 + 2mn + m^2 + n^2
= 2m^2 + 2mn = 2m * (m + n) = 1000 = 2 * 500. Since we require that m, n be natural numbers,
our task changes to be finding the numbers m, n such that m * (m + n) = 500. We can factor
500 = 20 * 25 = 20 * (20 + 5). Thus having m = 20, n = 5; with this selection a = 375, b = 200,
and thus c = 425. Thus the product is 375 * 200 * 425.
"""
def solve():
    # a, b, c = 375, 200, 425

    # brute force solution
    perimeter = 1000
    for a in range(1, perimeter + 1):
        for b in range(a + 1, perimeter + 1):
            c = perimeter - a - b
            if a**2 + b**2 == c**2:
                return a*b*c
    
    return a*b*c

if __name__ == "__main__":
    print(solve())