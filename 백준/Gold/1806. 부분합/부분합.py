import sys

input = sys.stdin.readline

n, s = map(int, input().split())

arr = list(map(int, input().split()))

start, end = 0, 1
total_sum = [0]*(n+1)
total_sum[0] = arr[0]
ans = float('inf')

for i in range(1, n+1):
    total_sum[i] += total_sum[i-1] + arr[i-1]

while start < end:
    cur = total_sum[end] - total_sum[start]
    
    if cur >= s:
        ans = min(ans, end - start)
        start += 1
    elif end == n:
        start += 1
    else:
        end += 1
        
if ans == float('inf'):
    print(0)
else:
    print(ans)