"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""
import runtime

def prime_sieve(ceiling):
    not_prime = set()
    primes = []
    tceiling = ceiling + 1
    for i in range(2, tceiling):
        if i in not_prime:
            continue
        for j in range(i*2, tceiling, i):
            not_prime.add(j)
        primes.append(i)
    return primes

# def divisors(n):
#     divisors = set([])
#     cap = n
#     i = 1
#     while i <= cap:
#         if n % i == 0:
#             divisors.add(i)
#             divisors.add(n/i)
#         i += 1
#         cap = n/i + 1
#     return divisors

def triangles(start, end=None):
    triangle = sum(range(start))
    i = start
    while triangle < end or end == None:
        triangle = triangle + i
        yield triangle
        i += 1

def prob12(start):
    primes = prime_sieve(999999)
    t = triangles(start)
    triangle = t.next()
    print triangle
    while 1 <= 500:
        triangle = t.next()
        print triangle
    return triangle


prob12(100)


