n = int(input())

arr = list(map(int, input().split()))
result = 0
h = 0

for i in arr:
    if(h <= i):
        h = i
        k = 0
    else:
        k += 1
        result = max(result, k)

print(result)