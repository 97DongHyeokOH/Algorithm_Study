import sys

input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

dp = [0]*len(s2)
result = 0

for i in range(len(s1)):
    for j in range(len(s2)-1, -1, -1):
        if s1[i] == s2[j]:
            if j:
                dp[j] = dp[j-1] + 1
                result = max(result, dp[j])
            else:
                dp[j] = 1
        else:
            dp[j] = 0

print(result)