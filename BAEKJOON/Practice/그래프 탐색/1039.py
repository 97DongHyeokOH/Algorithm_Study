import sys
import copy

input = sys.stdin.readline

n, k = map(int, input().split())

# 연산을 k번 못하는 경우
if((len(str(n)) == 2 and n % 10 == 0) or len(str(n)) == 1):
    print(-1)
    exit(0)

# 너비우선탐색을 통해 문제를 푼다
queue = [n]

# k번 연산
while(k):
    # 중복되는 값은 예외
    visit = set()
    # k번 마다 임시 값을 저장
    temp_reuslt = 0
    # k번 마다 임시 큐를 저장
    temp_queue = []

    # k번 바꿔서 만들수 있는 수가 queue에 저장되어 있다.
    while(queue):
        temp = queue.pop(0)
        temp_list = list(str(temp))

        # temp라는 수에서 모든 경우의 교환을 진행한다.
        for i in range(len(str(n))-1):
            for j in range(i+1, len(str(n))):
                # 앞이 0으로 시작하는 수인 경우
                if(i == 0 and temp_list[j] == '0'):
                    continue
                temp_list[i], temp_list[j] = temp_list[j], temp_list[i]
                num = int(''.join(temp_list))
                temp_list[i], temp_list[j] = temp_list[j], temp_list[i]

                if(not num in visit):
                    temp_reuslt = max(temp_reuslt, num)
                    visit.add(num)
                    temp_queue.append(num)

    result = temp_reuslt
    queue = copy.deepcopy(temp_queue)
    k -= 1

print(result)
