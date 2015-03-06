import math
SUMSQ = 0

for i in range(1,101):
        SUMSQ += i**2

SQSUM = sum(range(1,101))**2

print abs(SUMSQ-SQSUM)

        
