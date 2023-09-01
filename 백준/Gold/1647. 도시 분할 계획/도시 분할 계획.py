import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())
graph = defaultdict(lambda: defaultdict(int))

for _ in range(m):
    n1, n2, c = map(int, input().split())
    graph[n1][n2] = c
    graph[n2][n1] = c

visit = [False]*(n+1)

queue = [(0, 1)]
costs = []

while queue:
    cur_cost, cur_node = heapq.heappop(queue)
    
    if visit[cur_node]:
        continue
    
    visit[cur_node] = True
    costs.append(cur_cost)
    
    for node, cost in graph[cur_node].items():
        if not visit[node]:
            heapq.heappush(queue, (cost, node))

print(sum(costs) - max(costs))