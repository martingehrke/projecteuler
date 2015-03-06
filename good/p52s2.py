#!/usr/bin/env python


def compare(N,M):
        if sorted(str(M)) == sorted(str(N)):
                #print sorted(str(M)), sorted(str(N))
                return 1
        else: return 0

def test(N):

        for i in range(1,6):
                if not compare( N, i * N ):
                        return 0

        return N

for j in range(99999999):
        if not test(j) == 0: print j

