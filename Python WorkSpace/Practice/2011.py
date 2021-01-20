import sys

def pos_combine(idx):
    if(code[idx-1] == '0' or code[idx-1] > '2' or (code[idx-1] >= '2' and code[idx] > '6')):
        return False
    return True

code = list(sys.stdin.readline().rstrip())

if(not code or code[0] == '0'):
    print(0)
    exit()

dp = [[0,0] for _ in range(len(code))]

dp[0][0] = 1

for idx in range(1, len(code)):
    if(pos_combine(idx)):
        dp[idx][1] = dp[idx-1][0]
        dp[idx][1] %= 1000000
        if(code[idx] == '0'):
            continue
    elif(code[idx] == '0'):
        dp[idx][0] = 0
        dp[idx][1] = 0
        continue
    
    dp[idx][0] = dp[idx-1][0] + dp[idx-1][1]
    dp[idx][0] %= 1000000

result = sum(dp.pop()) % 1000000

print(result)