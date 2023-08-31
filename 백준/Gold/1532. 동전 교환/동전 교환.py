import sys
import math

input = sys.stdin.readline

g1, s1, b1 = map(int, input().split())
g2, s2, b2 = map(int, input().split())

cnt = 0

# 금화 최소 개수를 맞춰줌
cnt += max(0, g2 - g1)
s1 -= max(0, g2 - g1) * 11
g1 += max(0, g2 - g1)

# 동화 최소 개수를 맞춰줌
cnt += max(0, math.ceil((b2 - b1) / 9))
s1 -= max(0, math.ceil((b2 - b1) / 9))
b1 += max(0, math.ceil((b2 - b1) / 9)) * 9

# 이제 은화 최소 개수를 맞추는데 금화 또는 동화가 부족하면 -1을 출력
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