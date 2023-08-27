import sys

input = sys.stdin.readline

def get_cost(i, cost):
    global ans
    
    if i == l:
        ans = min(ans, cost)
        return
    
    for idx in range(i, l):
        if dp[i][idx] < float('inf'):
            get_cost(idx+1, cost+dp[i][idx])

sentence = input().rstrip()

n = int(input())

words = [input().rstrip() for _ in range(n)]

l = len(sentence)

dp = [[float('inf')]*(l+1) for _ in range(l+1)]
dp[0][0] = 0

for i in range(l):
    if dp[i][0] == float('inf'):
        continue
    
    for word in words:
        l_w = len(word)
        
        if sorted(sentence[i:i+l_w]) == sorted(word):
            cnt = 0
            
            for idx in range(l_w):
                if sentence[i+idx] != word[idx]:
                    cnt += 1
            
            dp[i][i+l_w-1] = min(dp[i][i+l_w-1], dp[i][0] + cnt)
            dp[i+l_w][0] = min(dp[i+l_w][0], dp[i][i+l_w-1])

if dp[-1][0] == float('inf'):
    print(-1)
else:
    print(dp[-1][0])