
def fp(N):
        return int(N)**5

def filt(N):
        if N==1: return False
        if sum(map(fp,list(str(N))))==N:
                return True
        return False

print sum(filter(filt,range(1000000)))
