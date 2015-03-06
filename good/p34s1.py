#!/usr/bin/env python2.4
import operator

def prod(lst):
        return reduce(operator.mul, lst)

def factorial(N):
        if N==0 or N==1: return 1
        return prod(range(1,N+1))

def digitfactorial(NUM):
        return sum(map(factorial,map(int,list(str(NUM)))))

def equal(N):
        if N == digitfactorial(N):
                return 1
        else: return 0

print sum(filter(equal,range(3,99999)))
