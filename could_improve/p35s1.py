from collections import deque

def isprime(n):
        n = abs(int(n))
        if n < 2: return False
        if n == 2: return True
        if not n & 1:  return False

        for x in range(3, int(n**0.5)+1, 2):
                if n % x == 0:
                        return False

        return True

def rotations(n):
        A = []
        S = str(n)
        D = deque(list(S))
        L = len(S)
        for i in range(L):
                D.rotate(1)
                A.append(int(''.join(list(D))))
        return A

def iscprime(n):
        if not isprime(n):
                return False
        for c in rotations(n):
                if not isprime(c): return False

        return True
        

print len(filter(iscprime,range(1,2000000)))
