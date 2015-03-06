import operator
def prod(lst):
    return reduce(operator.mul, lst)

print sum(map(int, list(str(prod(range(1,101))))))
