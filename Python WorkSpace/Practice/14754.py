import sys

n,m = map(int, sys.stdin.readline().split())

arr = []
side = [0]*n
front = [0]*m

result = 0

for _ in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    arr.append(l)

for i in range(n):
    for j in range(m):
        if(side[i] == arr[i][j]):
            result += arr[i][j]
        
        if(front[j] == arr[i][j]):
            result += arr[i][j]

        side[i] = max(side[i], arr[i][j])
        front[j] = max(front[j], arr[i][j])

for i in range(n):
    for j in range(m):
        if(side[i] != arr[i][j] and front[j] != arr[i][j]):
            result += arr[i][j]

print(result)