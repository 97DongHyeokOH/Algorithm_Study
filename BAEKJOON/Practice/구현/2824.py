import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

max_num = 1000000000

a_num = defaultdict(int)
b_num = defaultdict(int)

for num in a:
    for i in range(2, int(num**0.5)+1):
        while num % i == 0:
            num //= i
            a_num[i] += 1
    a_num[num] += 1

for num in b:
    for i in range(2, int(num**0.5)+1):
        while num % i == 0:
            num //= i
            b_num[i] += 1
    b_num[num] += 1

result = 1

for k, v in a_num.items():
    if b_num[k]:
        result *= (k ** min(a_num[k], b_num[k]))

if len(str(result)) > 9:
    print(str(result)[-9:])
else:
    print(result)
