import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

num = [int(input()) for _ in range(n)]

cnt = sorted(Counter(num).most_common(), key=lambda x: (-x[1], x[0]))

if len(cnt) == 1:
    mode = cnt[0][0]
elif cnt[0][1] == cnt[1][1]:
    mode = cnt[1][0]
else:
    mode = cnt[0][0]

print(round(sum(num) / n))
print(sorted(num)[n//2])
print(mode)
print(max(num) - min(num))
