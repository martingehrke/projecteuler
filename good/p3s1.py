def isprime(n):
        n = abs(int(n))
        if n < 2: return False
        if n == 2: return True
        if not n & 1:  return False

        for x in range(3, int(n**0.5)+1, 2):
                if n % x == 0:
                        return False

        return True

def isfactor(n):
        if 600851475143 % n == 0: return True
        return False

print max(filter(isfactor,(filter(isprime,range(1,2000000)))))
