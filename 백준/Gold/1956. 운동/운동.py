import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

v, e = map(int, input().split())

visit = [[False]*(v+1) for _ in range(v+1)]

cost = [[float('inf')]*(v+1) for _ in range(v+1)]
ans = float('inf')

for _ in range(e):
    s, e, c = map(int, input().split())
    cost[s][e] = c

# 플로이드-워셜로 모든 노드간 최단거리를 구함(i번 노드 -> i번 노드 값 중에서 최소값을 찾음)
for i in range(1, v+1):
    for j in range(1, v+1):
        for k in range(1, v+1):
            cost[i][k] = min(cost[i][k], cost[i][j] + cost[j][k])

for i in range(1, v+1):
    ans = min(ans, cost[i][i])

if ans == float('inf'):
    print(-1)
else:
    print(ans)