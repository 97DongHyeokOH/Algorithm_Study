import sys
import heapq

n, m, k = map(int, sys.stdin.readline().split())

my_graph = dict()
recieve = [[] for _ in range(n+1)]

for i in range(1, n+1):
    my_graph[str(i)] = dict()

for _ in range(m):
    f, t, w = map(int, sys.stdin.readline().split())

    my_graph[str(f)][str(t)] = w
    recieve[t].append(f)

queue = [[0, 1]]
dist = [sys.maxsize]*(n+1)

while(queue):
    cur_dist, cur_node = queue.pop(0)

    if(dist[cur_node] < cur_dist):
        continue

    for adj, weight in my_graph[str(cur_node)].items():
        distance = cur_dist + weight

        if(distance < dist[int(adj)]):
            dist[int(adj)] = distance
            queue.append([distance, int(adj)])

for idx in range(1, n+1):
    if(dist[idx] == sys.maxsize):
        dist[idx] = 0

for i in range(1, n+1):
    result = []
    for node in recieve[i]:
        result.append(dist[node]+my_graph[str(node)][str(i)])

    result.sort()

    print(result)

    if(len(result) == 0):
        print(-1)
    else:
        idx = (k-1) % len(result)
        print(result[idx])
