"""
We can start our t, p, h pointers at the numbers after the ones outlined in the problem and increment them based on which of T_t, P_p, and H_h are the smallest of each other until we reach equality, i.e the smallest and largest values are equal.
"""
import math

def solve():
    t = 286
    p = 166
    h = 144
    while True:
        T = t*(t+1)//2
        P = p*(3*p-1)//2
        H = h*(2*h-1)
        m = min(T,P,H)
        M = max(T,P,H)
        if m == M:
            return T
        if m == T:
            t += 1
        elif m == P:
            p += 1
        else:
            h += 1

if __name__ == "__main__":
    print(solve())