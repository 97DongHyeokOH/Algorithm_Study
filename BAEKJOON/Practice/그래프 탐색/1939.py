import sys
from collections import defaultdict, deque

input = sys.stdin.readline

# dfs를 이용해 푸니 시간초과
# -> 중량 제한으로 통과를 못한다는 것을 미루어 보고, 그 중량이 굉장히 크다는 것을 보아 중량을 이분탐색하면서 해당 중량에서 목적지로 갈 수 있으면 중량을 더 줄여보고, 
# 못 지나간다면 중량을 늘리는 방법인 이분탐색을 진행한다.
# 이분탐색 + bfs로 해결

n, m = map(int, input().split())

graph = defaultdict(lambda: defaultdict(int))
temp = set()

for _ in range(m):
    a, b, c = map(int, input().split())

    temp.add(c)

    if graph[a][b]:
        graph[a][b] = max(graph[a][b], c)
        graph[b][a] = max(graph[b][a], c)
    else:
        graph[a][b] = c
        graph[b][a] = c

f1, f2 = map(int, input().split())
weight_list = sorted(list(temp))
left,right = 1, 1000000000

while left <= right:
    mid = (left + right) // 2

    visit = [False]*(n+1)
    visit[f1] = True
    dq = deque([f1])

    while dq:
        cur = dq.popleft()

        for node, weight in graph[cur].items():
            if not visit[node] and weight >= mid:
                dq.append(node)
                visit[node] = True

    if visit[f2]:
        left = mid+1
    else:
        right = mid-1

print(right)