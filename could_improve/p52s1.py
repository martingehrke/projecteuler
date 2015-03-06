import operator

def prod(lst): return reduce(operator.mul,lst)

def sum_of_digits(N):
        return sum(map(int,list(str(N))))

def prod_of_digits(N):
        return prod(map(int,list(str(N))))

def fil(i):
        A = sum_of_digits(i)
        P = prod_of_digits(i)
        print A,P
        for j in range(2,7):
                print j, i*j, sum_of_digits(i*j), prod_of_digits(i*j)
                if not A == sum_of_digits(i*j): return False
                if not P == prod_of_digits(i*j): return False

        return True
                        
print fil(4050)       
#print filter(fil,range(1,999999))                        
