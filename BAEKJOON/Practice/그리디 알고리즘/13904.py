n = int(input())

arr = []
result = []

for _ in range(n):
    d, w = map(int, input().split())

    arr.append((d, w))

arr.sort(key=lambda x: (x[0], -x[1]))

for i in arr:
    if(len(result) < i[0]):
        result.append(i[1])
    else:
        score1 = result.pop()
        score2 = i[1]
        score = max(score1, score2)
        result.append(score)
    
    result.sort(reverse=True)

print(sum(result))