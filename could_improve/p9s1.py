
R = 1000
for i in range(R):
        for j in range(R):
                for k in range(R):
                        if i < j < k and (i**2 + j**2) == k**2:
                                if i+j+k == 1000:
                                        print i,j,k,i*j*k
                                        break

