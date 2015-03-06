N=100; MAX=0
for a in range(N):
        for b in range(N):
                S = sum(map(int,list(str(a**b))))
                if S > MAX: MAX=S
print MAX
