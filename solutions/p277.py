"""
We can use the string outputs of the Modified Collatz Sequence (MCS) to reverse engineer
our initial starting position. The last step in the output string given to us tells us
that our second-to-last step's output, N' is equivalent to 2 mod 3. Since we know the
functions for each step, we can track the modifications to our initial start n, in the 
form of the coefficients, a, b, c, where the output at some step k_i = (a*n+b)/c. From
there, if we can write our second-to-last output N' = (a*n+b)/c, we will have a linear
congruence, (a*n+b)/c = 2 mod 3, thus a*n+b = 2c mod 3c, thus a*n = 2c - b mod 3c.

We can see that just by tracking each step of the MCS that the a coefficient will always 
be a power of 2, and that the c coefficient will always be a power of 3, so gcd(a,c), 
and thus gcd(a, 3c) will always be 1, meaning we can take the modulo inverse a^{-1} % 3c,
and that there is a unique solution to our congruence. This yields us n = a^{-1}*(2c - b) 
mod 3c. After we compute this, we can simply find the smallest initial n with equivalent
result mod 3*c while being larger than 10**15.
"""
S = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
S_ = "UDDDUdddDDUDDddDdDddDDUDDdUUD" # remove the last 'd' because it is not needed for computation.

def next_coeffs(S_i, a, b, c):
    """
    for the MCS step applied S[i], with previous coefficients a,b,c, return the next
    coefficients
    """
    if S_i == 'D':
        return (a,b,3*c)
    elif S_i == 'U':
        return (4*a, 4*b+2*c, 3*c)
    else:
        return (2*a, 2*b - c, 3*c)  

def coefficients():
    """
    for initial position n, given it undergoes some modified collatz sequence S, 
    return the result of applying sequence S on n, in terms of coefficients a,b,c
    where k is the final resultant number, as k = (a*n+b)/c
    """
    i = 0
    a, b, c = 1, 0, 1
    while i < len(S_):
        r = next_coeffs(S_[i], a, b, c)
        a, b, c = r
        i += 1
    return (a,b,c)

def step(n):
    """
    for input n, compute letter of next step in MCS and the output number
    """
    r = n % 3
    if r == 0:
        return ('D', n // 3)
    elif r == 1:
        return ('U', (4*n + 2) // 3)
    else:
        return ('d', (2*n - 1) // 3)

def matches_S(n):
    """
    for initial input n, does its computed MCS match that of S
    """
    n_i = n
    for i in range(len(S)):
        s_i, n_j = step(n_i)
        if s_i != S[i]:
            return False
        n_i = n_j
    return True

if __name__ == '__main__':
    a,b,c = coefficients()
    M = 3*c
    inv_a = pow(a, -1, M)
    T = (2*c - b) % M
    n = (inv_a * T) % M
    ans = (10**15 // M + 1) * M + n
    print('ans:', ans)
    print('double check:', matches_S(ans))
