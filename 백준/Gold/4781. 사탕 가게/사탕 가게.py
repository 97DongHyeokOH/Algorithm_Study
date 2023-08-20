import sys

input = sys.stdin.readline
    
while 1:
    n, m = map(float, input().split())
    
    if not n and not m:
        break
    
    # 소수점 2자리로 돈을 입력 받기 때문에 100을 곱해서 dp를 만들어 준다
    # 왜 +1을 더 해주냐면, python에서 float -> int변환 시에 소수점 아래자리수는 버림되기 때문 -> 실제 0.29라고 해도 int(0.29 *100)은 28.999... 이렇게 될 수 있기 때문    max_money = int(m*100 + 1)
    max_money = round(m*100)
    
    dp = [0]*(max_money + 1)
    
    for _ in range(int(n)):
        c, p = map(float, input().split())
        money = round(p*100)
        
        for i in range(max_money):
            # 현재 돈이 0원 초과인 경우, 현재 돈으로 만들 수 있는 경우의 수가 있고, p를 더했을 경우에 최대 돈을 안넘어 간다면 dp를 업데이트
            if (i and not dp[i]) or i + money > max_money :
                continue
            
            dp[i + money] = max(dp[i + money], dp[i] + int(c))
    
    print(max(dp))