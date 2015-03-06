def divisors(n):
        D = []
        for i in range(1,(n/2)+1):
                if n % i == 0:
                        D.append(i)
        
        return sum(D)

AP = {}
for a in range(10000):
        Da = divisors(a)
        for b in range(10000):
                if not a==b and not AP.has_key(b):
                        if Da == b and divisors(b)==a:
                                AP[a]=1
                                AP[b]=1

print list(iter(AP))
print sum(iter(AP))
                        
                
       
 
