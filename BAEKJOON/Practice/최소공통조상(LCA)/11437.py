import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

# 각 노드의 깊이를 저장하는 함수


def dfs(i, d):
    depth[i] = d
    visit[i] = True

    for node in graph[i]:
        if not visit[node]:
            ancestors[node][0] = i
            dfs(node, d+1)

# ancestors[i][j] -> i번 노드의 2^j번 위의 조상
# 각 노드의 조상들을 초기화 해주는 함수


def set_parent():
    dfs(1, 0)
    for i in range(1, 21):
        for j in range(1, n+1):
            ancestors[j][i] = ancestors[ancestors[j][i-1]][i-1]

# 최소공통조상(LCA)를 찾아주는 메인 함수
# 깊이는 b가 더 깊게 만들어 준 상태로 함수를 돌린다.


def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a

    # 두 노드의 깊이 차이를 확인하고, 깊이를 같게 만들어준다.
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
