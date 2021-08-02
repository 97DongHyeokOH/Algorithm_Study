import sys

n, t = map(int, sys.stdin.readline().split())

cities = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

INF = sys.maxsize
dp = [[INF]*n for _ in range(n)]
to_teleport = [INF]*n

for i in range(n):
    for j in range(n):
        if(i == j):
            dp[i][j] = 0
            continue

        dist = abs(cities[i][1] - cities[j][1]) + \
            abs(cities[i][2] - cities[j][2])

        if(cities[i][0]):
            to_teleport[i] = 0
        elif(cities[j][0]):
            to_teleport[i] = min(to_teleport[i], dist)

        if(cities[i][0] and cities[j][0]):
            dp[i][j] = min(dist, t)
        else:
            dp[i][j] = dist

for k in range(n):
    for i in range(n):
        for j in range(i, n):
            dp[i][j] = min(dp[i][j], to_teleport[i] + to_teleport[j] + t)

m = int(sys.stdin.readline())

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())

    if(a > b):
        print(dp[b-1][a-1])
    else:
        print(dp[a-1][b-1])
