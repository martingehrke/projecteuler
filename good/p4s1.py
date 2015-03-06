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

P = 0
for i in range(100,1000):
        for j in range(100,1000):
                NUM = i*j
                if ispalindrome(NUM) and P<NUM:
                        P=NUM
                                
print P
