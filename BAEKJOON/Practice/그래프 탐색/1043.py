import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, m = map(int, input().split())

# 진신을 아는 사람들 번호
avoid_people = set(list(map(int, input().split()))[1:])
# 각 파티별 오는 사람들 번호
parties = [list(map(int, input().split()))[1:] for _ in range(m)]
# graph[i]는 i번 사람이 파티에서 만나는 모든 사람을 저장하는 집합
graph = defaultdict(set)
# 과장된 이야기를 할 수 있는 파티 개수
cnt = m

# 먼저 모든 파티를 돌면서 각 사람마다 파티에서 만나는 사람을 각 집합에 저장한다.
for party in parties:
    for i in range(len(party)-1):
        for j in range(i+1, len(party)):
            graph[party[i]].add(party[j])
            graph[party[j]].add(party[i])

# visit 인덱스 번호 사람이 한 명이라도 있는 파티에서는 과장된 말을 하면 안됨
visit = [False]*(n+1)

# 진실을 아는 사람들과 같은 파티에 참가하는 사람들이 있는 파티에서도 과장된 말을 하면 안됨
for person in avoid_people:
    dq = deque([person])
    visit[person] = True

    while dq:
        cur = dq.popleft()

        for i in graph[cur]:
            if not visit[i]:
                dq.append(i)
                visit[i] = True

# 파티에 visit 인덱스 값이 True인 사람이 한 명이라도 있으면 과장된 말을 못하니 결과 값에서 1을 빼줌
for party in parties:
    for person in party:
        if visit[person]:
            cnt -= 1
            break

print(cnt)
