import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline


def dfs(i):
    visit[i] = True
    route.append(i)
    temp = num[i]

    if(visit[temp]):
        if(temp in route):
            for k in route[route.index(temp):]:
                result[k] = 0
        return
    else:
        dfs(temp)


t = int(input())

for _ in range(t):
    n = int(input())
    num = [0] + list(map(int, input().split()))
    visit = [False]*(n+1)
    result = [1]*(n+1)
    visit[0] = True
    result[0] = 0

    for i in range(1, n+1):
        if(not visit[i]):
            route = []
            dfs(i)

    print(sum(result))
