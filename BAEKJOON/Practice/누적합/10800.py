import sys

input = sys.stdin.readline

n = int(input())

balls = [list(map(int, input().split())) + [i] for i in range(n)]

# 입력받은 배열을 공의 크기를 기준으로 오름차순 정렬
balls.sort(key=lambda x: x[1])

# 해당 색 공의 무게 합
color = [0]*(n+1)
# 결과값을 저장하는 list
result = [0]*n
# 현재까지 누적 합
cur = 0
j = 0

for i in range(n):
    while(balls[j][1] < balls[i][1]):
        cur += balls[j][1]
        color[balls[j][0]] += balls[j][1]
        j += 1

    result[balls[i][2]] = cur - color[balls[i][0]]

for i in result:
    print(i)
