import sys
import copy

input = sys.stdin.readline

n, m = map(int, input().split())


def pos(y, x):
    if 0 <= y < n and 0 <= x < m:
        return True
    return False


def get_score(y, x):
    ans = 0

    for i in range(5):
        cur = copy.deepcopy(tetris[i])
        for j in range(4):
            temp = 0

            if j:
                cur = [(-cur_x, cur_y) for cur_y, cur_x in cur]

            for k in range(4):
                temp_y, temp_x = y+cur[k][0], x+cur[k][1]

                if not pos(temp_y, temp_x):
                    temp = -float('inf')
                    break

                temp += paper[temp_y][temp_x]

            ans = max(ans, temp)

    for i in range(5):
        cur = copy.deepcopy(tetris_reverse[i])
        for j in range(4):
            temp = 0

            if j:
                cur = [(-cur_x, cur_y) for cur_y, cur_x in cur]

            for k in range(4):
                temp_y, temp_x = y+cur[k][0], x+cur[k][1]

                if not pos(temp_y, temp_x):
                    temp = -float('inf')
                    break

                temp += paper[temp_y][temp_x]

            ans = max(ans, temp)

    return ans


paper = [list(map(int, input().split())) for _ in range(n)]

tetris = [[(0, 0), (0, 1), (0, 2), (0, 3)], [(0, 0), (0, 1), (1, 0), (1, 1)], [
    (0, 0), (1, 0), (2, 0), (2, 1)], [(0, 0), (1, 0), (1, 1), (2, 1)], [(0, 0), (0, 1), (1, 1), (0, 2)]]
tetris_reverse = [[(i, -j) for i, j in tetris[idx]] for idx in range(5)]
score = 0

for i in range(n):
    for j in range(m):
        score = max(score, get_score(i, j))

print(score)
