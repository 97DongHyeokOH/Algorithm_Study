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

# dp[i][j] -> i번째 단어부터 j번째 단어까지 해석하기 위한 최소 비용
dp = [[float('inf')]*(l+1) for _ in range(l+1)]
dp[0][0] = 0

for i in range(l):
    # 현재 단어로 시작하는 해석을 하기 위해서는 이전 단어들이 모두 해석이 가능해야함
    # 하지만 값이 업데이트되지 않았다는 것은 이전 단어들을 해석하지 못하는 경우
    if dp[i][0] == float('inf'):
        continue
    
    for word in words:
        l_w = len(word)
        
        if sorted(sentence[i:i+l_w]) == sorted(word):
            cnt = 0
            
            for idx in range(l_w):
                if sentence[i+idx] != word[idx]:
                    cnt += 1
            
            # 현재 해당하는 단어의 비용 최솟값을 갱신
            dp[i][i+l_w-1] = min(dp[i][i+l_w-1], dp[i][0] + cnt)
            # 다음 단어부터 해석이 가능하다고, 이전 단어까지 해석하는데 최소 비용을 저장
            dp[i+l_w][0] = min(dp[i+l_w][0], dp[i][i+l_w-1])

if dp[-1][0] == float('inf'):
    print(-1)
else:
    print(dp[-1][0])