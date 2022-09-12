import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline


def count_S(comb):
    cnt = 0

    for y, x in comb:
        if classroom[y][x] == 'S':
            cnt += 1

    if cnt >= 4:
        return True
    else:
        return False


def check_connect(comb):
    visit = [False]*7
    dq = deque([comb[0]])
    visit[0] = True

    while dq:
        y, x = dq.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if [ny, nx] in comb:
                idx = comb.index([ny, nx])
                if not visit[idx]:
                    dq.append([ny, nx])
                    visit[idx] = True

    if False in visit:
        return False
    else:
        return True


classroom = [list(input().rstrip()) for _ in range(5)]
position = [[i, j] for i in range(5) for j in range(5)]

cnt = 0

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

for comb in list(combinations(position, 7)):
    if count_S(comb) and check_connect(comb):
        cnt += 1

print(cnt)
