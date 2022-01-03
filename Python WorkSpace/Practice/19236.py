import sys
import copy

input = sys.stdin.readline

# 배열을 벗어나지 않는지 판단


def pos(y, x):
    if(0 <= y < 4 and 0 <= x < 8):
        return True
    return False

# 물고기들이 움직이는 함수


def move(arr, shark):
    # idx-1번 물고기가 위치한 좌표 [-1,-1]이면 존재하지 않음을 의미
    loc = [[-1, -1] for _ in range(16)]

    # 움직이기 전 물고기의 위치를 배열에 넣어 줌
    for i in range(4):
        for j in range(0, 8, 2):
            if(arr[i][j] != -1):
                loc[arr[i][j]-1] = [i, j]

    # 1번 물고기부터 차례대로 이동
    for idx in range(16):
        y, x = loc[idx]
        # 물고기가 존재하는 경우에 움직여 준다
        if(y != -1 and x != -1):
            # 물고기가 가르키는 방향
            d = arr[y][x+1] - 1
            # 물고기가 움직일 수 있는지 판단(모든 방향으로 이동할 수 있는지 해본다)
            for i in range(8):
                nd = (d + i) % 8
                ny = y + direction[nd][0]
                nx = x + direction[nd][1]
                # 물고기가 움직일 수 있고 그 위치가 상어가 있는 위치가 아니라면
                if(pos(ny, nx) and not(ny == shark[0] and nx == shark[1])):
                    # 움직이는 칸이 빈칸인 경우
                    if(arr[ny][nx] != -1):
                        nidx = arr[ny][nx]-1
                        loc[idx], loc[nidx] = loc[nidx], loc[idx]
                    # 움직이는 칸에 다른 물고기가 있다면
                    else:
                        loc[idx] = [ny, nx]
                    arr[ny][nx], arr[y][x] = arr[y][x], arr[ny][nx]
                    arr[ny][nx+1], arr[y][x+1] = nd+1, arr[ny][nx+1]
                    break

    return arr

# 메인 함수(재귀)


def solution(arr, shark, cnt):
    global result
    # 상어가 있는 위치를 -1로 바꿔 준다.
    y, x, d = shark
    arr[y][x], arr[y][x+1] = -1, -1
    # 물고기를 움직여 주고 result값 최신화
    arr = move(arr, shark)
    result = max(result, cnt)
    # 상어가 가르키는 방향으로 몇칸을 이동할 지
    i = 1

    # while문을 통해서 상어가 더는 못 움직이는 경우까지 모든 경우를 탐색해 줌
    while(1):
        ny = y + (direction[d][0])*i
        nx = x + (direction[d][1])*i

        # 더는 이동하지 못하면 while문을 빠져나옴
        if(not pos(ny, nx)):
            break

        # 해당 위치가 빈칸이 아닌경우 (빈칸이면 상어가 위치하지 못 함)
        if(arr[ny][nx] != -1):
            next_shark = (ny, nx, arr[ny][nx+1]-1)
            arr_copy = copy.deepcopy(arr)
            solution(arr_copy, next_shark, cnt+arr[ny][nx])

        i += 1


# 초기 물고기들의 위치를 받아주는 배열
fishes = [list(map(int, input().split())) for _ in range(4)]

# 물고기가 가르키는 방향을 dictionary로 표현(편의를 위해 fishes배열의 direction을 dictionary에서는 direction-1로 표현)
direction = {0: (-1, 0), 1: (-1, -2), 2: (0, -2), 3: (1, -2),
             4: (1, 0), 5: (1, 2), 6: (0, 2), 7: (-1, 2)}
# 처음 상어는 (0,0)의 물고기를 잡아 먹는다.
result = fishes[0][0]-1
shark = (0, 0, fishes[0][1]-1)
fishes_copy = copy.deepcopy(fishes)

solution(fishes_copy, shark, fishes[0][0])

print(result)
