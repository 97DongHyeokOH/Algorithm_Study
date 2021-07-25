# 문제: 봄캠프를 마친 김진영 조교는 여러 도시를 돌며 여행을 다닐 계획이다. 그런데 김 조교는, '느림의 미학'을 중요시하는 사람이라 항상 최단경로로만 이동하는 것은 별로 좋아하지 않는다. 하지만 너무 시간이 오래 걸리는 경로도 그리 매력적인 것만은 아니어서, 적당한 타협안인 'k번째 최단경로'를 구하길 원한다. 그를 돕기 위한 프로그램을 작성해 보자.

# 입력: 첫째 줄에 n, m, k가 주어진다. (1 ≤ n ≤ 1000, 0 ≤ m ≤ 2000000, 1 ≤ k ≤ 100) n과 m은 각각 김 조교가 여행을 고려하고 있는 도시들의 개수와, 도시 간에 존재하는 도로의 수이다.
# 이어지는 m개의 줄에는 각각 도로의 정보를 제공하는 세 개의 정수 a, b, c가 포함되어 있다. 이것은 a번 도시에서 b번 도시로 갈 때는 c의 시간이 걸린다는 의미이다. (1 ≤ a, b ≤ n. 1 ≤ c ≤ 1000)
# 도시의 번호는 1번부터 n번까지 연속하여 붙어 있으며, 1번 도시는 시작도시이다.

# 출력: n개의 줄을 출력한다. i번째 줄에 1번 도시에서 i번 도시로 가는 k번째 최단경로의 소요시간을 출력한다.
# 경로의 소요시간은 경로 위에 있는 도로들을 따라 이동하는데 필요한 시간들의 합이다. i번 도시에서 i번 도시로 가는 최단경로는 0이지만, 일반적인 k번째 최단경로는 0이 아닐 수 있음에 유의한다. 또, k번째 최단경로가 존재하지 않으면 -1을 출력한다. 최단경로에 같은 정점이 여러 번 포함되어도 된다.

import sys
import heapq

n, m, k = map(int, sys.stdin.readline().split())

# 그래프를 입력 받음
my_graph = dict()

for i in range(1, n+1):
    my_graph[str(i)] = dict()

for _ in range(m):
    f, t, w = map(int, sys.stdin.readline().split())

    my_graph[str(f)][str(t)] = w

# 결과값을 저장하기 위한 list
# result[i]는 1번 노드로 가는 최단경로를 k개 저장해줌
result = [[sys.maxsize]*k for _ in range(n+1)]
result[1][0] = 0
# heapq이용
queue = [[0, 1]]

# 다익스트라 알고리즘 이용
while(queue):
    cur_dist, cur_node = heapq.heappop(queue)

    for adj, weight in my_graph[str(cur_node)].items():
        distance = cur_dist+weight

        if(distance < result[int(adj)][k-1]):
            result[int(adj)][k-1] = distance
            result[int(adj)].sort()
            heapq.heappush(queue, [distance, int(adj)])

# result[i][k-1]이 sys.maxsize값이라면 k번째의 최단경로가 존재하지 않는다는 것을 의미
for i in range(1, n+1):
    if(result[i][k-1] == sys.maxsize):
        print(-1)
    else:
        print(result[i][k-1])
