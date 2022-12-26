import sys

input = sys.stdin.readline

n, m, b = map(int, input().split())

# 땅의 높이
height = [list(map(int, input().split())) for _ in range(n)]
# 모든 땅의 높이 합
height_sum = sum([sum(height[i]) for i in range(n)])

ans_time = float('inf')
ans_height = 0

# 높이는 0~256까지 가능. 모든 경우를 확인한다.
for h in range(257):
    # 모든 땅의 높이의 합 + 여분 벽돌의 수가 해당 높이로 땅을 세울 수 없다면 for문을 빠져나간다.
    if height_sum + b < h * n * m:
        break

    take_time = 0

    for y in range(n):
        for x in range(m):
            # 해당 땅의 높이 h보다 현재 좌표의 높이가 낮다면 벽돌을 올려주는 시간을 더해준다.
            if height[y][x] < h:
                take_time += h - height[y][x]
            # 반대로 벽돌을 인벤토리에 넣는 시간을 더해준다.
            else:
                take_time += 2 * (height[y][x] - h)

    # 현재 높이를 세우는데 걸리는 시간이 이전까지의 정답시간보다 작거나 같으면 높이와 시간을 업데이트해준다.
    if take_time <= ans_time:
        ans_height = h
        ans_time = take_time

print(ans_time, ans_height)
