import operator as op
from functools import reduce
import sys

def nCr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

t = int(input())

for _ in range(t):
    r,n = map(int, sys.stdin.readline().split())

    print(nCr(n,r))