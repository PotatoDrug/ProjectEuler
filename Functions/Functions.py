#!/usr/bin/python

# Carmichael numbers
carmichael = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 126217, 162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153]

# Fermat's Little Theorem
def isPrime(x):
	prime = True
	if (x in carmichael):
		return False
	for i in range(2,10):
		if ((i**x - i) % x != 0):
			prime = False
			break
	return prime

# Sieve of Eratosthenes
def sieve(limit):
    not_prime = []
    prime = []
    for i in xrange(2, limit):
        if i not in not_prime:
            prime.append(i)
            for j in xrange(i*i, limit, i):
                not_prime.append(j)
    return prime

def sieve(limit):
	sieve = [True] * limit
	def mark(sieve, x):
		for i in xrange(x+x, len(sieve), x):
			sieve[i] = False

	for x in xrange(2, int(len(sieve) ** 0.5) + 1):
		if sieve[x]:
			mark(sieve, x)

	return sum(i for i in xrange(2, len(sieve)) if sieve[i])
