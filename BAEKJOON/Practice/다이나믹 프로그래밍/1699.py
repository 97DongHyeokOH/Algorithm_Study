n=int(input())
dp=[0]*(n+1)

a=[i**2 for i in range(1, 317)]

for i in range(1,n+1):
    s=[]
    
    for j in a:
        if i < j:
            break
        s.append(dp[i-j])
        
    dp[i] = min(s) + 1

print(dp[n])