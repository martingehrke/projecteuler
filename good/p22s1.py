#!/usr/bin/env python2.4

ALPHABET ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def LETTER(L):
        return ALPHABET.find(L)+1

def score(WORD, I):
        return sum(map(LETTER,list(WORD))) * I

INFILE = open('./input/p22.txt','r')

NAMES = sorted(INFILE.readlines()[0].strip().split(','))

SUM=0
for INDEX, NAME in enumerate(NAMES):
        SUM += score(NAME,INDEX+1)

print SUM

        
