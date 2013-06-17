"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
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

print prime_sieve(420000)[10000]