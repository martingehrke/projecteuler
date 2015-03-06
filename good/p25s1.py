N0=0;N1=1;
iter=1
while 1:
        iter += 1
        N1 += N0
        N0 = N1-N0
        if len(str(N1)) >= 1000: break

print iter

