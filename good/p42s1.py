
def Tn(n):
        return .5*n*(n+1)


TN = map(Tn,range(100))

def lv(l):
        ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return ALPHA.index(l)+1

def filt(f):
        if sum(map(lv,list(f))) in TN:
                return True
        return False

INFILE = open('./input/p42.txt')

WORDS = INFILE.readlines()[0].strip().split(',')

print len(filter(filt,WORDS))


