import sys
from collections import deque, defaultdict

input = sys.stdin.readline

# 입력 값을 받아줌
n = int(input())
m = int(input())
# temp[i][j] -> i번 노드가 j의 상태로 무게 비교가 된 노드들을 list에 저장한다
# j: 0 -> i번 노드보다 무게가 작은 경우, j: 1 -> i번 노드보다 무게가 큰 경우
temp = defaultdict(lambda: defaultdict(list))

for _ in range(m):
    a, b = map(int, input().split())

    temp[a][0].append(b)
    temp[b][1].append(a)

# 각 노드별로 무게 비교가 가능한 노드들을 bfs를 통해 찾아낸다.
# 시작할 때는 자기 자신을 제외하고 n-1개의 노드들은 비교가 안된다고 cnt에 저장하고, 비교 가능한 노드가 나올때 마다 cnt값을 1씩 줄여줌.
for i in range(1,n+1):
    queue = deque([(i,0), (i,1)])
    visit = [False]*(n+1)
    visit[i] = True
    cnt = n-1

    while(queue):
        node, k = queue.popleft()

        for next_node in temp[node][k]:
            if(not visit[next_node]):
                cnt -= 1
                visit[next_node] = True
                queue.append((next_node, k))
    
    print(cnt)