import sys
import math

input = sys.stdin.readline

g1, s1, b1 = map(int, input().split())
g2, s2, b2 = map(int, input().split())

cnt = 0

cnt += max(0, g2 - g1)
s1 -= max(0, g2 - g1) * 11
g1 += max(0, g2 - g1)

cnt += max(0, math.ceil((b2 - b1) / 9))
s1 -= max(0, math.ceil((b2 - b1) / 9))
b1 += max(0, math.ceil((b2 - b1) / 9)) * 9

while s1 < s2:
    cnt += 1
    
    if g1 > g2:
        g1 -= 1
        s1 += 9
    elif b1 - 11 >= b2:
        b1 -= 11
        s1 += 1
    else:
        cnt = -1
        break

print(cnt)