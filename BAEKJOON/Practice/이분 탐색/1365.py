import sys

input = sys.stdin.readline

# 가장 긴 증가하는 부분 수열을 찾아 해결한다. (nlogn)
n = int(input())
arr = list(map(int, input().split()))
# result에 초기값 -inf를 넣어준 뒤에 upper bound를 통해 값을 채워 가장 긴 증가하는 부분 수열을 찾는다.
result = [-float("inf")]

# 입력 받은 배열을 순차적으로 돌면서 result에 값을 채워 나간다.
for i in arr:
    left, right = 0, len(result)

    # 만약 result의 마지막 값보다 현재 값(i)가 크다면 result 가장 뒤에 현재 값을 추가해준다.
    if(i > result[-1]):
        result.append(i)
        continue

    # 그렇지 않다면 이분 탐색을 통해 result안에 있는 값들 중에 현재 값보다 작은 수 중에 가장 큰 수 뒤에 위치하게 해준다.
    while(left < right):
        mid = (left + right) // 2

        if(result[mid] < i):
            left = mid + 1
        else:
            right = mid
    
    result[right] = i

# 가장 긴 증가하는 부분 수열의 길이는 len(result)-1 이다.
# 그럼 n개의 전깃줄에서 가장 긴 증가하는 부분 수열의 길이를 제외한 나머지 전깃줄을 잘라야되니 n - (len(result) - 1)이 정답이 된다.
print(n-len(result)+1)