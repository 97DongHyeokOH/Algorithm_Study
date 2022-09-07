import sys
from collections import defaultdict, deque

input = sys.stdin.readline

# 테스트 케이스 수
t = int(input())

# 테스트 케이스만큼 반복
for _ in range(t):
    # n: 컴퓨터 수, d: 의존성 개수, c: 해킹당한 컴퓨터
    n, d, c = map(int, input().split())

    # 자신이 감염되면 몇번 컴퓨터가 몇초만에 감염되는지 저장하는 dictionary
    computer = defaultdict(lambda: defaultdict(int))

    # 의존성을 dictionary에 추가
    for _ in range(d):
        a, b, s = map(int, input().split())

        computer[b][a] = s

    # 감염된 컴퓨터 수
    cnt = 0
    # 마지막 컴퓨터가 감염되기까지 걸리는 시간
    max_time = 0

    # list에 각 컴퓨터가 감염되기까지 걸리는 시간을 저장하면서 dijkstra 알고리즘을 사용
    time = [float("inf")]*(n+1)
    # 처음 감염된 컴퓨터는 0으로 초기화
    time[c] = 0

    # Dijkstra's algorithm
    dq = deque([[c, 0]])

    while dq:
        cur_com, cur_time = dq.popleft()

        if time[cur_com] < cur_time:
            continue

        for com, add_time in computer[cur_com].items():
            new_time = cur_time + add_time

            if new_time < time[com]:
                time[com] = new_time
                dq.append([com, new_time])

    for virus_time in time[1:]:
        if virus_time != float('inf'):
            cnt += 1
            max_time = max(max_time, virus_time)

    print(cnt, max_time)
