import sys

input = sys.stdin.readline

# i번째 톱니바퀴를 direction방향(1: 시계방향, -1: 반시계방향)으로 돌린경우 톱니바퀴를 돌려준다.


def solution(i, direction):
    left = status[i-1][6]
    left_d = direction
    right = status[i-1][2]
    right_d = direction

    move_next = [[False, 0] for _ in range(4)]

    move_next[i-1] = [True, direction]

    for cur in range(i-2, -1, -1):
        cur_right = status[cur][2]

        if left == cur_right:
            break

        move_next[cur] = [True, -left_d]
        left_d = -left_d
        left = status[cur][6]

    for cur in range(i, 4):
        cur_left = status[cur][6]

        if right == cur_left:
            break

        move_next[cur] = [True, -right_d]
        right_d = -right_d
        right = status[cur][2]

    for i, t in enumerate(move_next):
        is_move, d = t
        if is_move:
            move(i, d)

# i-1번째 톱니바퀴가 direction방향(1: 시계방향, -1: 반시계방향)으로 돌려준다.


def move(i, direction):
    if direction == 1:
        temp = status[i][-1]

        for idx in range(7, -1, -1):
            status[i][idx] = status[i][idx-1]

        status[i][0] = temp
    else:
        temp = status[i][0]

        for idx in range(7):
            status[i][idx] = status[i][idx+1]

        status[i][-1] = temp


status = [list(map(int, input().rstrip())) for _ in range(4)]

k = int(input())

for _ in range(k):
    n, d = map(int, input().split())

    solution(n, d)

print(sum([status[i][0] * (2**i) for i in range(4)]))
