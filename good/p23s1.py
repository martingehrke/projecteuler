#!/usr/bin/env python2.7

def divisors(n):
        n = abs(int(n))

	D = [1]
	if n % 2 == 0 and n != 2:
		D.append(2)

        for x in range(3, int(n/2)+1):
                if n % x == 0:
                        D.append(x)

        return D


def abundant(n):
	DIV = divisors(n)
	SUM = sum(DIV)
	if SUM > n:
		return True

	return False

LIMIT = 22000

ABD = filter(abundant, range(1,LIMIT))
ALL_POSSIBLE = []

for I in ABD:
	for J in ABD:
		SUM = I+J
		if I+J <= LIMIT:
			ALL_POSSIBLE.append(I+J)

print sum(set(range(1,LIMIT)) - set(ALL_POSSIBLE))
	
