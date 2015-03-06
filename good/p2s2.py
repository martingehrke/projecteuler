N0=0; N1=1; SUM=0
while N1 < 4000000:
        if N1 % 2 == 0: SUM += N1
        N1 += N0
        N0  = N1-N0
        
print SUM
