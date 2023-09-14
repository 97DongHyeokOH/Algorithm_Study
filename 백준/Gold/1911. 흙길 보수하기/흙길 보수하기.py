import sys

input = sys.stdin.readline

n, l = map(int, input().split())

puddles = [list(map(int, input().split())) for _ in range(n)]

puddles.sort()
next_start = 0
cnt = 0

for start, end in puddles:
    start = max(start, next_start)
    cur = end - start
    
    cnt += cur // l
    next_start = start + (cur // l) * l
    
    if cur % l:
        cnt += 1
        next_start += l
        
print(cnt)