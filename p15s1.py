#!/usr/bin/env python

#see pascale's triangle

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
 
rows, cols = 20, 20
print factorial(rows+cols) / (factorial(rows) * factorial(cols))

