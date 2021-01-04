n = int(input())

arr = []
result = 0

for _ in range(n):
    tip = int(input())
    arr.append(tip)

arr.sort(reverse=True)

for idx in range(n):
    temp = arr[idx] - idx

    if(temp < 0):
        temp = 0

    result += temp

print(result)