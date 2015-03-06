def nthtriangle(n):
        return sum(range(1,n+1))

def divisors(n):
        D = 0
        for i in range(1,(n/2)+1):
                if n % i == 0:
                        D+=1
        

        return D+1
        

I=1
TN=0
ND=0
while ND < 500:
        TN += I
        ND = divisors(TN)
        #print I, TN, ND
        if ND > 100:
                print "%s : %s : %s " % (I, TN, ND)
        I+=1
