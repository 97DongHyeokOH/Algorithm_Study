import sys
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [[0, 0] for _ in range(n+1)]

visit = [False]*(n+1)


def dfs(cur):
    visit[cur] = True
    dp[cur][0] = 1
    dp[cur][1] = 0
    for i in tree[cur]:
        if(not visit[i]):
            dfs(i)
            dp[cur][0] += dp[i][1]
            dp[cur][1] += max(dp[i][0], dp[i][1])


dfs(1)
print(n-max(dp[1]))
