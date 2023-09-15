import sys

input = sys.stdin.readline

n, k = map(int, input().split())

history = [[0]*(n+1) for _ in range(n+1)]

for _ in range(k):
    front_inc, back_inc = map(int, input().split())
    
    history[front_inc][back_inc] = 1

s = int(input())

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if history[i][k] and history[k][j]:
                history[i][j] = 1

for _ in range(s):
    i1, i2 = map(int, input().split())
    
    if history[i1][i2]:
        print(-1)
    elif history[i2][i1]:
        print(1)
    else:
        print(0)