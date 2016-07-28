def euclid(m,n):
    while n != 0:
        r = m % n
        m = n
        n = r
    return m


gcd = euclid(60, 24)

print gcd
