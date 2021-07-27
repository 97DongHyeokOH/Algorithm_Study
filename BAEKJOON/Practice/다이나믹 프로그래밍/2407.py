import sys
import operator as op
from functools import reduce


def combination(n, r):
    r = min(r, n-r)

    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator


n, m = map(int, sys.stdin.readline().split())

print(combination(100, 6))
