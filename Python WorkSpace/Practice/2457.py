n = int(input())

arr = []
dp = [(3,1)]

for _ in range(n):`
    start_month, start_day, end_month, end_day = map(int, input().split())

    arr.append([(start_month,start_day), (end_month,end_day)])

arr.sort()

for i in arr:
    start = i[0]
    end = i[1]

    for idx in range(len(dp)):
        if(start <= dp[idx]):
            if(idx == len(dp)-1):
                dp.append(end)
            elif(dp[idx+1] < end):
                dp[idx+1] = end
            break
    
    if(end > (11,30)):
        break

if(dp[len(dp)-1] <= (11,30)):
    dp = [0]

print(len(dp)-1)