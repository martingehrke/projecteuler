def odd(n):
        return n & 1

ODDS = sorted(filter(odd,range(1500000)))

SPIRAL=1
NEXT=1

SUM=0

COUNT=1

while COUNT < 2001:
        SUM += ODDS[NEXT]
        print NEXT, ODDS[NEXT], SPIRAL, COUNT
        SPIRAL=int((COUNT+4)/4)
        NEXT+=SPIRAL
        COUNT +=1

print SUM+1
        
