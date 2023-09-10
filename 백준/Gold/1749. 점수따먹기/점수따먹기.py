import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[0]*(m+1)] + [([0] + list(map(int, input().split()))) for _ in range(n)]

ans = -float('inf')

for i in range(1, n+1):
    row_sum = [0]*(m+1)
    for j in range(i, n+1):
        cur_row_sum = [0]*(m+1)
        for k in range(1, m+1):
            row_sum[k] += arr[j][k]
            cur_row_sum[k] = max(cur_row_sum[k-1] + row_sum[k], row_sum[k])
            ans = max(ans, cur_row_sum[k])
            
print(ans)