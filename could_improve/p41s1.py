#!/usr/bin/python2.7

import itertools, sys

def isprime(n):
	# make sure n is a positive integer
	n = abs(int(n))
	# 0 and 1 are not primes
	if n < 2:
		return False
	# 2 is the only even prime number
	if n == 2:
		return True
	# all other even numbers are not primes
	if not n & 1:
		return False
	# range starts with 3 and only needs to go up the squareroot of n
	# for all odd numbers
	for x in range(3, int(n**0.5)+1, 2):
		if n % x == 0:
			return False

	return True

for i in range(2,13):
	NDIGIT = range(1,i)
	NDIGIT.reverse()

	TOTAL = itertools.permutations(NDIGIT)

	for i in  TOTAL:
		NUM = int(''.join(map(str,i)))
		if isprime(NUM):
			print i

