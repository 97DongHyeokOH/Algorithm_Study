# 문제: N개의 숫자 구슬이 <그림 1>과 같이 막대에 꿰어져 일자로 놓여 있다. 이들 구슬은 막대에서 빼낼 수 없고, 바꿀 수 없다.
# 이 숫자 구슬을 M개의 그룹으로 나누었을 때 각각의 그룹의 합 중 최댓값이 최소가 되도록 하려 하다. 예를 들어 세 그룹으로 나눈다고 할 때 <그림 2>와 같이 그룹을 나누면 그룹의 합은 각각 11, 15, 18이 되어 그 중 최댓값은 18이 되고, <그림 3>과 같이 나누면 각 그룹의 합은 각각 17, 12, 15가 되어 그 중 최댓값은 17이 된다. 숫자 구슬의 배열이 위와 같을 때는 그룹의 합 중 최댓값이 17보다 작게 만들 수는 없다. 그룹에 포함된 숫자 구슬의 개수는 0보다 커야 한다.
# 각 그룹의 합 중 최댓값이 최소가 되도록 M개의 그룹으로 나누었을 때, 그 최댓값과 각 그룹을 구성하는 구슬의 개수를 찾아 출력하는 프로그램을 작성하시오.

# 입력: 첫째 줄에 구슬의 개수 N과 그룹의 수 M이 주어진다. 둘째 줄에는 각 구슬이 적혀진 숫자가 왼쪽부터 차례로 주어진다. N은 300 이하의 자연수, M은 N이하의 자연수이며, 구슬에 적혀진 숫자는 100 이하의 자연수이다.

# 출력: 각 그룹의 합 중 최댓값이 최소가 되도록 M개의 그룹으로 나누었을 때 그 최댓값을 첫째 줄에 출력하고, 둘째 줄에는 각 그룹을 구성하는 구슬의 개수를 왼쪽부터 순서대로 출력한다. 구슬의 개수를 출력할 때는 사이에 한 칸의 공백을 둔다. 만약 그룹의 합의 최댓값이 최소가 되도록 하는 경우가 둘 이상이라면 그 중 하나만을 출력한다.

import sys

n, m = map(int, sys.stdin.readline().split())

bead = list(map(int, sys.stdin.readline().split()))

# 이분탐색으로 문제 해결
left = min(bead)
right = 30000
result = -1
result_num = []

# 그룹의 합의 최댓값이 최소가 되는 값을 이분탐색으로 찾는다.
while(left <= right):
    mid = (left + right) // 2

    # 그룹의 합을 임의로 저장해주는 변수
    temp = 0
    # 각 그룹에 몇개의 구술이 들어가는지 임의로 저장해주는 변수
    num_cnt = 0
    # 각 그룹에 몇개의 구술이 들어갔는지 저장해주는 list
    num = []
    # 현재까지 몇개의 그룹으로 이루어졌는지 임의로 저장해주는 변수
    cnt = 0

    # mid값을 기준으로 m개의 그룹을 만들어 내는지 확인 해봄
    for i in range(len(bead)):
        if(mid < max(bead)):
            cnt = -1
            break

        # 만약에 현재 남아있는 구술의 수와 만들어야되는 그룹의 수가 같을때 실행
        if(len(bead) - i == m - len(num) and num_cnt == 0):
            while(m - len(num)):
                cnt += 1
                num.append('1')
            break

        temp += bead[i]
        num_cnt += 1

        # 마지막 구술이거나 다음 구술을 더하면 mid값을 초과할때 실행
        if(i == len(bead)-1 or temp + bead[i+1] > mid):
            num.append(str(num_cnt))
            cnt += 1
            temp = 0
            num_cnt = 0

    # 그룹의 수가 m개보다 많거나 구술에 적힌 숫자가 mid보다 큰 경우
    if(cnt > m or cnt == -1):
        left = mid + 1
    else:
        # 그룹의 수와 m이 일치하면 result값에 저장을 해준다.
        if(cnt == m):
            result = mid
            result_num = num
        right = mid - 1


print(result)
print(' '.join(result_num))
