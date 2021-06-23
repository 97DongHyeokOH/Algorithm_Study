# 문제: 방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다.
# 또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.
# 세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라.
# 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

# 입력: 첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000) 둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데, a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다.
# (1 ≤ c ≤ 1,000) 다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. (v1 ≠ v2, v1 ≠ N, v2 ≠ 1)

# 출력: 첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다.

import sys
import heapq
from types import MethodType

n, e = map(int, sys.stdin.readline().split())

# 그래프를 나타내는 my_map을 dictionary로 표현
my_map = dict()

for i in range(n):
    my_map[str(i)] = dict()

# 입력을 받아 my_map에 저장
for i in range(e):
    n1, n2, w = map(int, sys.stdin.readline().split())

    # 방향성이 없는 그래프이기 때문에 한쪽에 가중치가 저장되어있으면 반대쪽도 저장되어 있다.
    if(str(n1-1) in my_map[str(n2-1)]):
        my_map[str(n1-1)][str(n2-1)] = min(my_map[str(n1-1)][str(n2-1)], w)
        my_map[str(n2-1)][str(n1-1)] = min(my_map[str(n2-1)][str(n1-1)], w)
    else:
        my_map[str(n1-1)][str(n2-1)] = w
        my_map[str(n2-1)][str(n1-1)] = w

# 꼭 지나야되는 2개의 노드
node1, node2 = map(int, sys.stdin.readline().split())

# 내가 생각한 방법은 4가지의 단계를 거쳐야 된다고 생각이 되었다.
# 1. 시작노드에서 node1, node2까지의 각각의 최단거리를 구한다.
# 2. node1, node2 사이의 최단거리를 구한다.
# 3. node1, node2에서 도착노드까지 각각의 최단거리를 구한다.
# 4. node1을 먼저 가는 방법과 node2를 먼저 가는 방법중 최단거리를 구한다.

# 1. 1번 노드에서 출발해서 각 노드까지의 최단거리를 저장해주는 list 초기화
dist1 = [sys.maxsize]*n
dist1[0] = 0

# 우선순위 큐를 이용
queue = []
heapq.heappush(queue, [dist1[0], 0])

# 1번 실행
while(queue):
    cur_dist, cur_node = heapq.heappop(queue)

    if(dist1[cur_node] < cur_dist):
        continue

    for adj, weight in my_map[str(cur_node)].items():
        distance = cur_dist + weight

        if(distance < dist1[int(adj)]):
            dist1[int(adj)] = distance
            heapq.heappush(queue, [distance, int(adj)])

# 2. node1, node2 사이의 최단거리
dist2 = [sys.maxsize]*n
dist2[node1-1] = 0

# 우선순위 큐를 이용
queue = []
heapq.heappush(queue, [dist2[node1-1], node1-1])

# 1번 실행
while(queue):
    cur_dist, cur_node = heapq.heappop(queue)

    if(dist2[cur_node] < cur_dist):
        continue

    for adj, weight in my_map[str(cur_node)].items():
        distance = cur_dist + weight

        if(distance < dist2[int(adj)]):
            dist2[int(adj)] = distance
            heapq.heappush(queue, [distance, int(adj)])

# 3. node1, node2에서 마지막 노드까지의 최단거리
dist3 = [sys.maxsize]*n
dist3[n-1] = 0

# 우선순위 큐를 이용
queue = []
heapq.heappush(queue, [dist3[n-1], n-1])

# 1번 실행
while(queue):
    cur_dist, cur_node = heapq.heappop(queue)

    if(dist3[cur_node] < cur_dist):
        continue

    for adj, weight in my_map[str(cur_node)].items():
        distance = cur_dist + weight

        if(distance < dist3[int(adj)]):
            dist3[int(adj)] = distance
            heapq.heappush(queue, [distance, int(adj)])

# 4. node1을 먼저 가는것이 빠른지 node2를 먼저 가는것이 빠른지 판단
result = min(dist1[node1-1]+dist2[node2-1]+dist3[node2-1],
             dist1[node2-1]+dist2[node2-1]+dist3[node1-1])

if(result < sys.maxsize):
    print(result)
else:
    print(-1)
