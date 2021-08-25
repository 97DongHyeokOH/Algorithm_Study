import sys

n, m, k = map(int, sys.stdin.readline().split())

# arr[i][j] -> 'a'가 i개, 'z'가 j개일때, 사전에 수록되어있는 문자열의 개수
arr = [[1]*(m+1) for _ in range(n+1)]
result = ''

for i in range(1, n+1):
    for j in range(1, m+1):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]

# 만약 사전에 수록될 수 있는 문자열의 개수가 k보다 작은 경우
if(arr[n][m] < k):
    print(-1)
else:
    while(1):
        if(n == 0 or m == 0):
            result += 'a'*n
            result += 'z'*m
            break

        temp = arr[n-1][m]

        if(k <= temp):
            result += 'a'
            n -= 1
        else:
            result += 'z'
            m -= 1
            k -= temp
    print(result)
