import sys

n = int(sys.stdin.readline())

# 건물의 정보를 저장해주는 list -> [건물 건설 시간, .....(미리 건설되어야 하는 건물)]
inform = [0]
# result[i] -> 건물을 완성하는데 걸리는 최소 시간
result = [-1]*(n+1)
result[0] = 0

# -1을 제외한 정보들을 inform에 저장해 준다.
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))

    temp = temp[:-1]
    inform.append(temp)

    # 미리 건설해야되는 건물이 없는경우 바로 result에 넣어준다.
    if(len(temp) == 1):
        result[i+1] = temp[0]

# 모든 건물을 완성시킬때 까지 while문 반복
while(-1 in result):
    # result를 복사해 임의의 list를 만들어 줌
    temp = result.copy()

    for i in range(1, n+1):
        # 이미 건물을 완성하는 시간이 저장되어 있다면 continue
        if(temp[i] != -1):
            continue

        # 건물 건설 시간을 -1로 초기화
        k = -1

        # inform[i][1:]은 i번째 건물을 완성하기 위해 미리 완성되어야 하는 건물의 번호를 의미하고,
        # 그 건물들을 건설하는 시간이 결정이 되었다면 i번째 건물의 완성에 대한 최소시간도 구할 수 있다.
        for j in inform[i][1:]:
            # 만약 미리 건설되어야 하는 건물이 완성되지 않은 경우
            if(temp[j] == -1):
                k = -1
                break
            k = max(k, temp[j])

        # 미리 완성되어야하는 건물들의 시간이 결정된 경우
        if(k != -1):
            result[i] = inform[i][0] + k

for i in range(1, n+1):
    print(result[i])
