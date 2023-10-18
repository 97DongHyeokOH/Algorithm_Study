import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, k = map(int, input().split())

# 이름의 길이를 저장
names_len = [len(input().rstrip()) for _ in range(n)]

# 이전 이름들의 길이를 차례대로 저장
prev_name = deque([names_len[0]])
# 이전 이름들 길이의 수를 저장
prev_name_cnt = defaultdict(int)
# 0 번째 이름은 앞의 이름이 없기 때문에 미리 저장
prev_name_cnt[names_len[0]] += 1
cnt = 0

for l in names_len[1:]:
    cnt += prev_name_cnt[l]
    
    # 만약 이전 이름이 k개가 이미 있다면 현재 이름을 저장하기 위해서는 1칸씩 밀어야 함
    if len(prev_name) == k:
        prev_name_cnt[prev_name.popleft()] -= 1
    prev_name_cnt[l] += 1
    prev_name.append(l)

print(cnt)