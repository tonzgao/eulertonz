"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def prob1():
    v = 0
    multiples = set()
    while v  < 997:
        v += 3
        multiples.add(v)
    v = 0
    while v < 995:
        v += 5
        multiples.add(v)
    return sum(list(multiples))

print prob1()