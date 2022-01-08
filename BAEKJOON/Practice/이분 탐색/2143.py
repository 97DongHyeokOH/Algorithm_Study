import sys

input = sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a_dict = dict()
b_dict = dict()
result = 0
a_sum = [0]*(n+1)
b_sum = [0]*(m+1)

for i in range(n):
    a_sum[i+1] = a_sum[i] + a[i]

for i in range(m):
    b_sum[i+1] = b_sum[i] + b[i]

for i in range(n):
    for j in range(i, n):
        num = a_sum[j+1] - a_sum[i]
        if(num in a_dict):
            a_dict[num] += 1
        else:
            a_dict[num] = 1

for i in range(m):
    for j in range(i, m):
        num = b_sum[j+1] - b_sum[i]
        if(num in b_dict):
            b_dict[num] += 1
        else:
            b_dict[num] = 1

for num, cnt in a_dict.items():
    if(t-num in b_dict):
        result += (cnt*b_dict[t-num])

print(result)
