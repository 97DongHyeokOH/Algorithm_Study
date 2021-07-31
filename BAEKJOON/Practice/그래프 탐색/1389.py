import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
result = [[0]*(n+1) for _ in range(n+1)]
# 유저간의 친구 관계를 저장하기 위한 dictionary
# friends['i'] = set() -> 유져 i의 친구는 set()으로 저장을 해준다.(중복 방지)
friends = dict()
# 결과값을 추출하기 위해 중간에서 임의로 값을 저장해주는 변수
temp = sys.maxsize
# 결과값
ans = 0

for i in range(1, n+1):
    friends[str(i)] = set()

# 두 유저간의 친구 관계를 friends에 저장해준다.
for _ in range(m):
    f1, f2 = map(int, sys.stdin.readline().split())
    friends[str(f1)].add(f2)
    friends[str(f2)].add(f1)

# 1번 유저부터 케빈 베이컨의 수를 구해준다.
for i in range(1, n+1):
    # 우선순위 큐(heapq) 생성
    queue = []
    # visit[idx] -> idx번 유저와 연결이 되었는 확인
    visit = [False]*(n+1)
    visit[i] = True

    # i번째 유저와 바로 연결되어있는 유저를 queue에 저장
    for friend in friends[str(i)]:
        # 이전에 연결된 유저가 아닌경우에는 1로 설정(1단계)
        if(not result[i][friend]):
            result[i][friend] = 1
            result[friend][i] = 1
        heapq.heappush(queue, [result[i][friend], str(friend)])
        visit[friend] = True

    # stage(단계)를 기준으로 우선순위 큐를 돌아주면서 각 유저까지의 단계를 계산
    while(queue):
        # stage -> 단계, person -> 유저
        stage, person = heapq.heappop(queue)

        # 만약 모든 유저에 대해서 계산이 완료되었다면 while문 종료
        if(not False in visit):
            break

        # person 유저와 연결되어있는 유저들 중에서 아직 연결되지 않은 유저들을 queue에 넣어 줌
        for node in friends[person]:
            if(not visit[node]):
                heapq.heappush(queue, [stage+1, str(node)])
                visit[node] = True
                result[i][node] = stage+1
                result[node][i] = stage+1

    # i번째 유저의 케빈 베이컨의 수와 이전 값들중 작은 값을 가진 유저를 ans에 저장
    if(sum(result[i]) < temp):
        temp = sum(result[i])
        ans = i

print(ans)
