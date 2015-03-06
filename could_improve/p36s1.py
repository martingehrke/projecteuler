import operator
def prod(lst):
    return reduce(operator.mul, lst)

def ispalindrome(N):
        S = list(str(N))
        L = len(S)-1
        for D in range(len(S)):
                if not S[D] == S[L-D]:
                        return False

        return True

def tob2(N):
        digit = []
        while N != 0:
                rem = N % 2
                N = N/2
                digit.append(rem)
        digit.reverse()
        return ''.join(map(str,digit))

def both(N):
        if ispalindrome(N) and ispalindrome(tob2(N)):
                return True
        return False

BOTH = filter(both,range(1000000))
print sum(BOTH), BOTH
