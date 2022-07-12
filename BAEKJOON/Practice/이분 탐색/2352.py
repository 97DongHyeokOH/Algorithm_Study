import sys

input = sys.stdin.readline

# 이분탐색 + 가장 긴 증가하는 부분 수열(LIS)

n = int(input())
arr = list(map(int, input().split()))
result = [-float("inf")]

# 입력받은 배열을 모두 탐색
for i in arr:
    # 만약 result의 마지막 값보다 크다면 append
    if(result[-1] < i):
        result.append(i)
    # 만약 result의 마지막 값보다 작다면 upper bound를 이용해 현재 값보다 작은 값 중에 가장 큰 수 다음에 현재 값을 넣는다.
    else:
        left = 0
        right = len(result)-1

        while(left < right):
            mid = (left + right) // 2

            if(result[mid] < i):
                left = mid + 1
            else:
                right = mid
        
        result[right] = i
    
print(len(result)-1)