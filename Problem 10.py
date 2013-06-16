"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

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

def add(a, b):
    return a + b

def prob10(n):
    return reduce(add, prime_sieve(n))

print prob10(2000000)