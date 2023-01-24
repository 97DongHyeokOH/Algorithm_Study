def solution(target):
    dp = [[float('inf'), float('inf')] for _ in range(target+1)]

    for i in range(1, target+1):
        if 1 <= i <= 20 or i == 50:
            dp[i] = min(dp[i], [1, -1])
        elif (i % 2 == 0 and i <= 40) or (i % 3 == 0 and i <= 60):
            dp[i] = min(dp[i], [1, 0])

        for j in range(1, 21):
            if i + j <= target:
                dp[i+j] = min(dp[i+j], [dp[i][0]+1, dp[i][1]-1])
            if i + 2*j <= target:
                dp[i+2*j] = min(dp[i+2*j], [dp[i][0]+1, dp[i][1]])
            if i + 3*j <= target:
                dp[i+3*j] = min(dp[i+3*j], [dp[i][0]+1, dp[i][1]])

        if i + 50 <= target:
            dp[i+50] = min(dp[i+50], [dp[i][0]+1, dp[i][1]-1])

    dp[target][1] = -dp[target][1]

    return dp[target]


print(solution(58))
