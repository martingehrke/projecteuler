def Tn(t):
        return (t*(t+1))/2

def Pn(p):
        return (p*(3*p-1))/2

def Hn(h):
        return h*(2*h-1)

TN = map(Tn, range(10000))
PN = map(Pn, range(10000))
HN = map(Hn, range(10000))

print Tn(55385), Pn(31977), Hn(27693)
