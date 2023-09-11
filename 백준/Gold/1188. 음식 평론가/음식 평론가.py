import sys

input = sys.stdin.readline

n, m = map(int, input().split())

ans = 0

while n and m:
    if n == m:
        break
    
    if n > m:
        n -= m
    else:
        m -= n
        ans += n
        
print(ans)