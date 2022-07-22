import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
# 해당 높이에 몇개의 화실이 존재하는지 저장해주는 dictionary
arrows = defaultdict(int)
# 필요한 화살의 수
cnt = 0

for i in arr:
    # 만약 현재 높이에 있는 화살이 있다면 그 화살의 높이를 1 낮춰준다.
    if arrows.get(i):
        arrows[i] -= 1
        arrows[i-1] += 1
    # 현재 높이에 화살이 없다면 화살을 쏘고 풍선을 맞췄기 때문에 높이를 1 낮춰준다.
    else:
        arrows[i-1] += 1
        cnt += 1

print(cnt)