import sys

input = sys.stdin.readline

c, n = map(int, input().split())

# dp[i] -> 호텔 고객 i명 늘이기 위해 투자해야 돈의 최솟값
# 문제는 고객의 수를 c명 정확히 맞춰서 투자하는 것이 아니라 최소 c명 이상 늘이기 위함인 것을 알아야 한다.
# 그렇기 때문에 한 번에 늘어날 수 있는 고객 수인 100만큼 dp 길이를 추가함
dp = [float('inf')]*(c+100)
dp[0] = 0

for _ in range(n):
    cost, people = map(int, input().split())
    
    # 각 입력을 받을 때마다 각 비용의 최솟값을 업데이트
    for cur in range(c):
        # 현재 사람에서 입력받은 사람만큼 고객을 늘이는 경우 최솟값을 업데이트
        dp[cur+people] = min(dp[cur+people], dp[cur]+cost)
    
print(min(dp[c:]))