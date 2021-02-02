import sys
from collections import deque as dq


def pos(floor):
    if(0 < floor <= f):
        return True
    return False


def bfs():
    q = dq([(s, 0)])
    visit[s] = True

    while(q):
        cur, cnt = q.popleft()

        if(cur == g):
            return cnt

        for i in range(2):
            n_floor = cur + move[i]

            if(pos(n_floor) and not visit[n_floor]):
                q.append((n_floor, cnt+1))
                visit[n_floor] = True

    return -1


f, s, g, u, d = map(int, sys.stdin.readline().split())

visit = [False]*(f+1)
move = [u, -d]

result = bfs()

if(result == -1):
    print('use the stairs')
else:
    print(result)
