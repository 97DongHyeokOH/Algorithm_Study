import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def dfs(i, d):
    depth[i] = d
    visit[i] = True

    for node in graph[i]:
        if not visit[node]:
            ancestors[node][0] = i
            dfs(node, d+1)


def set_parent():
    dfs(1, 0)
    for i in range(1, 21):
        for j in range(1, n+1):
            ancestors[j][i] = ancestors[ancestors[j][i-1]][i-1]


def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a

    for i in range(20, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = ancestors[b][i]

    if a == b:
        return a

    for i in range(20, -1, -1):
        if ancestors[a][i] != ancestors[b][i]:
            a = ancestors[a][i]
            b = ancestors[b][i]

    return ancestors[a][0]


n = int(input())
graph = defaultdict(list)
depth = [0]*(n+1)
visit = [False]*(n+1)
ancestors = [[0] * 21 for _ in range(n+1)]

for _ in range(n-1):
    parent, child = map(int, input().split())

    graph[parent].append(child)
    graph[child].append(parent)

set_parent()

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))