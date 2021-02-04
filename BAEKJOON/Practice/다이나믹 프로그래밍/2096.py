import sys

def min_num(c):
    if(c == 0):
        return min(dp[0][0], dp[1][0])
    elif(c == 1):
        return min(dp[0][0], dp[1][0], dp[2][0])
    else:
        return min(dp[1][0], dp[2][0])
    
def max_num(c):
    if(c == 0):
        return max(dp[0][1], dp[1][1])
    elif(c == 1):
        return max(dp[0][1], dp[1][1], dp[2][1])
    else:
        return max(dp[1][1], dp[2][1])

n = int(sys.stdin.readline())

dp = [[0,0] for _ in range(3)]

for _ in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    temp = [[0,0] for _ in range(3)]
    for i in range(3):
        temp[i][0] = arr[i] + min_num(i)
        temp[i][1] = arr[i] + max_num(i)
    dp = temp.copy()
        
a = min(dp[0][0], dp[1][0], dp[2][0])
b = max(dp[0][1], dp[1][1], dp[2][1])

print(b,a)