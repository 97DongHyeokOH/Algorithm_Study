import sys

input = sys.stdin.readline

n = int(input())
# 소수인지 판별하는 list
prime_num = [True]*(n+1)
prime_num[1] = False
# 결과 값
cnt = 0

# 에라토스테네스의 체로 소수를 판별
for i in range(2, int(n**0.5)+1):
    if(prime_num[i]):
        for j in range(i+i, n+1, i):
            prime_num[j] = False

# 소수를 저장하는 list
prime = [i for i in range(2, n+1) if prime_num[i]]

# start~end인덱스까지의 합과 end 값
num = 0
end = 0

# 두 포인터로 연속된 ㅣ소수의 합으로 나타낼 수 있는 경우의 수를 찾는다.
for start in range(len(prime)):
    while(num < n and end < len(prime)):
        num += prime[end]
        end += 1

    if(num == n):
        cnt += 1

    num -= prime[start]

print(cnt)
