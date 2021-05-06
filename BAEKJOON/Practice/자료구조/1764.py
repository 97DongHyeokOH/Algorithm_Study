import sys

n, m = map(int, sys.stdin.readline().split())

s1 = set()
result = []

for i in range(n):
    name = input()
    s1.add(name)

for i in range(m):
    name = input()
    if name in s1:
        result.append(name)

result.sort()
print(len(result))
for i in result:
    print(i)
