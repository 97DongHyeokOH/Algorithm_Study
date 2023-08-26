import sys
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())

lamp = [input().rstrip() for _ in range(n)]

k = int(input())

cnt = defaultdict(int)
ans = 0

for l in lamp:
    cnt[l] += 1

sorted_cnt = sorted(cnt.items(), key=lambda x : x[1], reverse=True)

for l, c in sorted_cnt:
    change_light = k - l.count('0')
    if change_light >= 0 and change_light % 2 == 0:
        ans = c
        break

print(ans)