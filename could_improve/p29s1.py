
A = {}
for a in range(2,101):
        for b in range(2,101):
                C = a**b
                if not A.has_key(C):
                        A[C] = C

print len(A)                                
