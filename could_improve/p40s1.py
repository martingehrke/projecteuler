

IDF = []
for i in range(190000):
        IDF.append(i)

S = ''.join(map(str,IDF))

PROD = 1
for j in range(7):
        PROD *= int(S[10**j])

print PROD
