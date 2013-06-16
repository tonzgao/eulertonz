"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def prob9():
    for e in range(1, 1000):
        a = e
        for f in range(1, 1000):
            b = f
            c = 1000 - b - a
            if b > c or a > c:
                continue
            if c*c == b*b + a*a:
                return a*b*c, a, b, c

print prob9()