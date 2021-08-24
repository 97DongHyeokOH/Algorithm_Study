import sys

# i번째 작업을 완료하기위한 최소시간을 구해줌


def solution(i):
    # 만약 이미 구해져 있다면 바로 return
    if(dp[i]):
        return dp[i]
    # 결과 값
    result = 0

    # 앞에 완료해야되는 작업이 없다면 바로 결과값에 널어 줌
    if(arr[i-1][1] == 0):
        result = arr[i-1][0]
    else:
        # 완료해야되는 작업들중 가장 오래 걸리는 작업에 자신의 작업시간을 더해 줌
        for idx in arr[i-1][2:]:
            result = max(result, solution(idx)+arr[i-1][0])

    return result


n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# i번째 작업을 완료하는데 걸리는 최소시간
dp = [0]*(n+1)

for i in range(1, n+1):
    # i번째 작업에 대한 결과값이 구해져있지 않다면 solution함수 실행
    if(not dp[i]):
        dp[i] = solution(i)

print(max(dp))
