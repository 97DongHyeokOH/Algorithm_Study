# 문제: 가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램을 작성하시오.

# 입력: 첫째 줄에 정점의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄부터 N개 줄에는 그래프의 인접 행렬이 주어진다. i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻이고, 0인 경우는 없다는 뜻이다. i번째 줄의 i번째 숫자는 항상 0이다.

# 출력: 총 N개의 줄에 걸쳐서 문제의 정답을 인접행렬 형식으로 출력한다. 정점 i에서 j로 가는 경로가 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력해야 한다.

import sys

# 시작 node를 출발해 갈수 있는 경로를 찾는다


def sol(start):
    visit = [False]*n
    queue = [start]

    while(queue):
        node = queue.pop(0)

        for i in graph[str(node)].keys():
            if(not visit[int(i)]):
                queue.append(int(i))
                visit[int(i)] = True

    return visit


n = int(sys.stdin.readline())

# 그래프를 저장해주는 dictionary
graph = dict()

# 결과값을 출력하기 위한 list
result = [['0']*n for _ in range(n)]

for i in range(n):
    graph[str(i)] = dict()

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 길이 연결되어있는 부분을 graph에 넣어준다
for i in range(n):
    for j in range(n):
        if(arr[i][j]):
            graph[str(i)][str(j)] = True

# n번째 노드를 출발점으로 생각해 경로가 있는지를 판단
for i in range(n):
    v = sol(i)

    for j in range(n):
        if(v[j]):
            result[i][j] = '1'

# 결과 값을 출력
for i in range(n):
    print(' '.join(result[i]))
