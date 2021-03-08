import sys
from collections import deque as dq


def solution(n, s, a, b, fares):
    maps = [[0]*n for _ in range(n)]
    distance = [[0, 0] for _ in range(n)]
    distance[0][0] = 1

    for i in fares:
        maps[i[0]-1][i[1]-1] = i[2]
        maps[i[1]-1][i[0]-1] = i[2]

    def search(f, t):
        dis = sys.maxsize
        result = []

        q = dq([[[f], 0]])

        while(q):
            l, d = q.popleft()

            point = l[len(l)-1]

            if(point == t):
                if(dis > d):
                    result = l
                    dis = d
                    continue

            for idx in range(n):
                temp = l.copy()
                temp_d = d
                if(maps[point][idx] and idx not in l):
                    temp.append(idx)
                    temp_d += maps[point][idx]
                    q.append([temp, temp_d])

        return result, dis

    for i in range(n):
        if(not distance[i][0]):
            l, d = search(i, a-1)

            distance[i][0] = d

            for j in range(1, len(l)):
                d -= maps[l[j]][l[j-1]]
                distance[l[j]][0] = d

        if(not distance[i][1]):
            l, d = search(i, b-1)

            distance[i][1] = d

            for j in range(1, len(l)):
                d -= maps[l[j]][l[j-1]]
                distance[l[j]][1] = d

    q = dq([[s-1, 0]])
    answer = sys.maxsize

    while(q):
        l, d = q.popleft()

        answer = min(answer, d + distance[l][0] + distance[l][1])

        for i in range(n):
            temp_d = d
            if(maps[l][i] and distance[l][0] + distance[l][1] > maps[l][i] + distance[i][0] + distance[i][1]):
                temp_d = d + maps[l][i]
                temp = i
                q.append([temp, temp_d])

    return answer


n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [
    5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

print(solution(n, s, a, b, fares))
