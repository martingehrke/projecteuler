N0=0
N1=1
SUM=0
while N1 < 4000000:
        TEMP = N0 + N1
        N0 = N1
        N1 = TEMP 
        if TEMP % 2 == 0: SUM += TEMP

print SUM
