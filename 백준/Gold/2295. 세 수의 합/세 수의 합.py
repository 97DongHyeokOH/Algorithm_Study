import sys

input = sys.stdin.readline

n = int(input())

num = sorted([int(input()) for _ in range(n)])

# x + y = k - z를 맞춰주면 된다
# x + y, k - z list를 각각 만들어서 일치하는 값 중에 k값이 가장 큰 값을 구하면 됨

xy, kz = set(), set()

for i in range(n):
    for j in range(n):
        xy.add(num[i] + num[j])
        kz.add((num[i], num[i] - num[j]))
        
kz = sorted(list(kz), reverse=True)

for k, i in kz:
    if i in xy:
        print(k)
        break