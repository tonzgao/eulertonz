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

# print prime_sieve(600851475143)
# Buffer overflow

#print prime_sieve(420000)
# decently fast

def prob3(n, potential_factors):
    for e in range(0, len(potential_factors)):
        if n % potential_factors[-1 - e] == 0:
            return potential_factors[-1 - e]
    return -1

print prob3(600851475143, prime_sieve(4200000))


