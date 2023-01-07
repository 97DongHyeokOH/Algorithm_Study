import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
recommand = list(map(int, input().split()))
result = []

for r in recommand:
    done = False
    for i in range(len(result)):
        if result[i][2] == r:
            result[i][0] += 1
            done = True
            break

    if done:
        result.sort(key=lambda x: (-x[0], x[1]))
        continue

    if len(result) < n:
        result.append([1, 0, r])
    else:
        result[-1] = [1, 0, r]

    for i in range(len(result)):
        result[i][1] += 1

    result.sort(key=lambda x: (-x[0], x[1]))

final_result = []

for a, b, c in result:
    final_result.append(c)

print(*sorted(final_result))
