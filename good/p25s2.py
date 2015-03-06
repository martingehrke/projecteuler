def fib():
        x,y = 0,1
        while True:
            yield x
            x,y = y, x+y


def thousand_digits(seq):
        for index, number in enumerate(seq):
                if len(str(number)) >= 1000 :
                        return index

print thousand_digits(fib())
