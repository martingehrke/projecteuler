
def isinseq(N):
        M = N
        S = sum(map(int,list(str(N))))
        I=2
        if S == 1: return False
        while S**I <= N:
                if S**I == N:
                        print N, S, I, S**I
                        return True
                I+=1

        return False

I = 0
while I < 999999999:
        if isinseq(I):
                pass
        I += 1
