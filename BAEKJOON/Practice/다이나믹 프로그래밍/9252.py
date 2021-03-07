import sys

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()

dp = ['']*len(s1)
result = ''

for c in s2:
    temp = ''
    for idx in range(len(s1)):
        if(c == s1[idx] and len(dp[idx]) < len(temp)+1):
            dp[idx] = temp + c
            if(len(result) < len(dp[idx])):
                result = dp[idx]
        else:
            if(len(temp) < len(dp[idx])):
                temp = dp[idx]

print(len(result))
print(result)
