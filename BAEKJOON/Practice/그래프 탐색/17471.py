import sys
from collections import defaultdict, deque
from itertools import combinations

# 1. 모든 조합을 통해서 2개의 팀으로 나눈 뒤에 2개의 팀이 연결 되어있는지 확인을 한다.
# 2. 2개의 팀이 연결이 되어 있다면 인구수 차이를 확인한 뒤 result에 업데이트 해준다.

def connect_check(comb):
    visit = [False]*len(comb)
    dq = deque([comb[0]])
    visit[0] = True

    while dq:
        cur_node = dq.popleft()
        
        for node in graph[cur_node]:
            if node in comb:
                idx = comb.index(node)
                if not visit[idx]:
                    visit[idx] = True
                    dq.append(node)
    
    if False in visit:
        return False
    else:
        return True

def people_sum(comb):
    people = 0

    for i in comb:
        people += people_num[i]

    return people

input = sys.stdin.readline

n = int(input())

people_num = [0] + list(map(int, input().split()))
graph = defaultdict(list)
result = float('inf')
temp = [i for i in range(1,n+1)]

for i in range(1,n+1):
    for j in list(map(int, input().split()))[1:]:
        graph[i].append(j)

for i in range(1, n//2 + 1):
    for comb in list(combinations(temp, i)):
        comb = list(comb)
        comb2 = list(set(temp) - set(comb))

        if connect_check(comb) and connect_check(comb2):
            result = min(result, abs(people_sum(comb) - people_sum(comb2)))

if result == float('inf'):
    print(-1)
else:
    print(result)