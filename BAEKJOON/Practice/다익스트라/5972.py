import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())

paths = defaultdict(lambda: defaultdict(lambda: float('inf')))

for _ in range(m):
    node1, node2, k = map(int, input().split())

    paths[node1][node2] = min(paths[node1][node2], k)
    paths[node2][node1] = min(paths[node2][node1], k)

dist = [float('inf')]*(n+1)

queue = [(0, 1)]

while queue:
    cur_cnt, cur_node = heapq.heappop(queue)

    if cur_node == n:
        print(cur_cnt)
        exit(0)

    for next_node, k in paths[cur_node].items():
        next_cnt = cur_cnt + k

        if next_cnt < dist[next_node]:
            dist[next_node] = next_cnt
            heapq.heappush(queue, (next_cnt, next_node))
