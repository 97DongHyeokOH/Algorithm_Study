import sys

input = sys.stdin.readline

n, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dp = [0]*(t+1)

for study_time, score in arr:
    for time in range(t, study_time-1, -1):
        if time - study_time == 0 or dp[time - study_time]:
            dp[time] = max(dp[time], dp[time - study_time] + score)

print(max(dp))