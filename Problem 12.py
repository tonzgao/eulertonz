import math
import itertools

def prime_sieve(ceiling):
    not_prime = set()
    primes = []
    tceiling = ceiling + 1
    for i in xrange(2, tceiling):
        if i in not_prime:
            continue
        for j in xrange(i*2, tceiling, i):
            not_prime.add(j)
        primes.append(i)
    return primes

primes = prime_sieve(100000)

def triangles(start, end=None):
    triangle = sum(xrange(start))
    i = start
    while triangle < end or end == None:
        triangle = triangle + i
        yield triangle
        i += 1

def primefactors(n):
    pfactors = []
    for p in primes:
        if n == 1:
            return pfactors
        elif n in primes:
            pfactors.append(n)
            return pfactors
        elif n%p == 0:
            while n%p == 0:
                pfactors.append(p)
                n = n/p

def factors(n, pfactors):
    factors = set([1, n])
    pfactors = list(set(pfactors))
    stack = [n]
    done = set([])
    while stack:
        n = stack.pop()
        done.add(n)
        if n in primes or n == 1:
            continue
        else:
            for p in pfactors:
                if n%p == 0:
                    v = n/p
                    if v not in stack and v not in done:
                        factors.add(v)
                        stack.append(v)
    return len(factors)

def prob12(start):
    t = triangles(start)
    nfactors = 0
    count = start
    while nfactors <= 500:
        triangle = t.next()
        count += 1
        ps = primefactors(triangle)
        if len(ps) >= 9:
            nfactors = factors(triangle, primefactors(triangle))
            # print count, triangle, nfactors
    return triangle

print prob12(12375)

# def test():
#     ints = (i+1 for i in xrange(int(1e9)))
#     n = 0
#     while n < 600:
#         v = ints.next()
#         li = range(v)
#         n = sum([len(list(itertools.combinations(li, r))) for r in li])
#         print v, n
#
# print primefactors(73920)
# print primefactors(97020)
# print primefactors(749700)
# print primefactors(2031120)
# print primefactors(3483480)
# print primefactors(10767120)
# print primefactors(17907120)






