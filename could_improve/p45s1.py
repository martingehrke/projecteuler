def Tn(t):
        return (t*(t+1))/2

def Pn(p):
        return (p*(3*p-1))/2

def Hn(h):
        return h*(2*h-1)

MAX=100000

for t in range(MAX):
        TN = Tn(t)
        for p in range(MAX):
                PN = Pn(p)
                if PN == TN:
                        for h in range(MAX):
                                HN = Hn(h)
                                if HN == PN: print t,p,h
