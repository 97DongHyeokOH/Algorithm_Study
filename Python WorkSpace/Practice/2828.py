n, m = map(int , input().split())

j = int(input())

cur = [1, m]
result = 0

for _ in range(j):
    i = int(input())

    if(i < cur[0]):
        k = cur[0] - i
        result += k
        cur[0] -= k
        cur[1] -= k
    elif(cur[1] < i):
        k = i - cur[1]
        result += k
        cur[0] += k
        cur[1] += k

print(result)