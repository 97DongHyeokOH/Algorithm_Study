import sys

# 재귀 횟수 제한 늘려줌
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

# 깊이 우선 탐색


def dfs(i):
    visit[i] = True
    dp[i][0] = people[i]
    for v in tree[i]:
        if(not visit[v]):
            dfs(v)
            # i마을이 우수 마을에 포함 될 경우 주변 마을은 모두 우수 마을이면 안된다.
            dp[i][0] += dp[v][1]
            # i마을이 우수 마을이 아닐 경우 주변 마을에서 최대값을 끌고 와 준다.
            dp[i][1] += max(dp[v])


n = int(input())
# 각 마을 사람의 수
people = [0] + list(map(int, input().split()))
# 연결되어 있는 마을을 저장
tree = [[] for _ in range(n+1)]
# dp[i][0] -> i번째 마을 포함시 최대 인원 수, dp[i][1] -> i마을 포함 안할시 최대 인원 수
dp = [[0, 0] for _ in range(n+1)]
visit = [False]*(n+1)

for _ in range(n-1):
    u, v = map(int, input().split())

    tree[u].append(v)
    tree[v].append(u)

dfs(1)

print(max(dp[1]))
