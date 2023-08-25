import sys

input = sys.stdin.readline

n = int(input())

height = list(map(int, input().split()))

ans = [0]*n

for i in range(n):
    max_slope = -float('inf')
    cnt = 0
    for j in range(i+1, n):
        cur_slope = (height[j]-height[i]) / (j-i)
        if max_slope < cur_slope:
            cnt += 1
            max_slope = cur_slope
            ans[j] += 1
            
    ans[i] += cnt

print(max(ans))