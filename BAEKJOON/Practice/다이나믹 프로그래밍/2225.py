# 중복조합 문제
import operator as op
from functools import reduce

def nCr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

def nHr(n,r):
    return nCr(n+r-1, r) % 1000000000

n,k = map(int, input().split())

print(nHr(k,n))