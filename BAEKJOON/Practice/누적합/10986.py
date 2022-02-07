import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

# 배열의 누적합을 저장하는 list
sum = [0]*(n+1)
# temp[i] -> sum배열에서 m으로 나눴을 때 나머지값이 i가 되는 숫자의 수
temp = [0]*m
# 결과값
result = 0
temp[0] = 1

for i in range(n):
    sum[i+1] = sum[i] + arr[i]
    temp[sum[i+1] % m] += 1

# 숫자들중 2개의 조합 수를 구해서 다 더해주면 결과값이 나온다.
for i in temp:
    if(i):
        result += (i * (i-1) // 2)

print(result)
