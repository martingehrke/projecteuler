def getseqlen(N):
        SLEN = 0
        while N > 1:
                SLEN += 1
                if N %2==0:
                        N=N/2
                else:
                        N = (3*N)+1

        return SLEN-1

MAX=0;NM=0
for N in range(2,1000000):
        SLEN = getseqlen(N)
        if SLEN > MAX: MAX=SLEN; NM=N


print MAX, NM
