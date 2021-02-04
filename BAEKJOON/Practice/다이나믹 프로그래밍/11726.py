import operator as op
from functools import reduce

def nCr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

n = int(input())

result = 0

for i in range(n//2+1):
    if(n % 2 == 1):
        b = i*2 + 1
    else:
        b = i*2
    a = (n+b) // 2
    result += (nCr(a,b))
    result %= 10007

print(result)