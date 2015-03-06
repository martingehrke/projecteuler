ULIMIT = 99999999

def div(N):
        for I in range(1,21):
                if not N % I == 0:
                        return False

        return True

I=1
while I <= 2432902008176640000:
        if div(I): print I
        I+=1
