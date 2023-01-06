import sys
from collections import defaultdict, Counter

input = sys.stdin.readline


def pos(y, x):
    if 0 <= y < n and 0 <= x < n:
        return True
    return False


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n*n)]
seat_arr = [[0]*n for _ in range(n)]
seat = defaultdict(tuple)
result = 0

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

for cur_arr in arr:
    st_num, favorite_st_num = cur_arr[0], cur_arr[1:]
    temp = []

    for y in range(n):
        for x in range(n):
            if seat_arr[y][x] == 0:
                like = 0
                blank = 0
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]

                    if pos(ny, nx) and seat_arr[ny][nx] in favorite_st_num:
                        like += 1

                    if pos(ny, nx) and seat_arr[ny][nx] == 0:
                        blank += 1

                temp.append([like, blank, y, x])

    temp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))

    seat_arr[temp[0][2]][temp[0][3]] = st_num
    seat[st_num] = (temp[0][2], temp[0][3])

for cur_arr in arr:
    st_num, favorite_st_num = cur_arr[0], cur_arr[1:]
    y, x = seat[st_num]
    score = 0

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if pos(ny, nx) and seat_arr[ny][nx] in favorite_st_num:
            if score:
                score *= 10
            else:
                score += 1

    result += score

print(result)
