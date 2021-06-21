# 문제: 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.

# 입력: 첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1≤V≤20,000, 1≤E≤300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다.
# 둘째 줄에는 시작 정점의 번호 K(1≤K≤V)가 주어진다. 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다.
# 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다.
# 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

# 출력: 첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.

import sys
import heapq

a, b = map(int, sys.stdin.readline().split())

k = int(sys.stdin.readline())

arr = dict()  # 가중치를 저장해놓은 list
queue = []  # 우선순위 큐 생성

for i in range(a):
    arr[str(i)] = dict()

for i in range(b):  # 간선의 가중치를 입력받아 arr에 가중치 입력
    u, v, w = map(int, sys.stdin.readline().split())

    if(str(v-1) in arr[str(u-1)]):  # 같은 노드로 향하는 간선이 이미 인는 경우
        arr[str(u-1)][str(v-1)] = min(arr[str(u-1)][str(v-1)], w)
    else:                          # 같은 노드로 향하는 간선이 없는 경우
        arr[str(u-1)][str(v-1)] = w

# 시작 노드로부터 다른 노드 까지의 최단 거리 (sys.maxsize인 경우는 그 노드로 갈 수 없는 노드)
dist = [sys.maxsize]*a
dist[k-1] = 0

# heapq를 이용한 최단거리 찾기
heapq.heappush(queue, [dist[k-1], k-1])

while(queue):
    cur_dist, cur_node = heapq.heappop(queue)

    if(dist[cur_node] < cur_dist):
        continue

    for adj, w in arr[str(cur_node)].items():
        distance = cur_dist + w

        if(distance < dist[int(adj)]):
            dist[int(adj)] = distance
            heapq.heappush(queue, [distance, int(adj)])

for i in dist:
    if(i == sys.maxsize):
        print('INF')
    else:
        print(i)
