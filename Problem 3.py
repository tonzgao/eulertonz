"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
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

print prime_sieve(600851475143)
#Buffer overflow