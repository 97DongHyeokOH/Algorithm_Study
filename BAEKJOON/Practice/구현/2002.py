import sys

input = sys.stdin.readline

n = int(input())

start = [input().rstrip() for _ in range(n)]
end = [input().rstrip() for _ in range(n)]

# 추월한 차의 수
cnt = 0
# 빠져나온 차량의 리스트 인덱스
idx = 0
# 이미 빠져나온 차량
passed = set()

# 시작된 차량이 나오기 전까지 몇 대의 차가 나오는지 판단해 cnt에 더해준다.
# 이미 지나간 차라면 다음 차로 넘어간다
for num in start:
    if num in passed:
        continue

    while(num != end[idx]):
        passed.add(end[idx])
        cnt += 1
        idx += 1

    idx += 1


print(cnt)
