n,m,k = map(int, input().split())

result = ''

if(m+k-1 > n or n > m*k):
    print(-1)
    exit()

arr = [list(i for i in range(1, k+1))]

num = k+1
n -= k
m -= 1

while(n):
    a = n // m
    arr.append(list(i for i in range(num, num+a)))
    num += a
    n -= a
    m -= 1

for i in arr:
    i.reverse()

    for j in i:
        result += str(j) + ' '

print(result)