import sys

input = sys.stdin.readline

h, w = map(int, input().split())

height = list(map(int, input().split()))

stack = []
temp = 0
result = 0
temp = []
total_temp = []
front_height = height[0]

for i in height:
    if not stack or stack[-1] >= i:
        if temp:
            highest = min(front_height, stack[-1])

            total_temp += temp

            for idx in range(len(total_temp)):
                if highest >= total_temp[idx]:
                    result += highest - total_temp[idx]
                    total_temp[idx] = highest

            if highest >= front_height:
                front_height = stack[-1]
                total_temp = []

            temp = []

        stack.append(i)
    else:
        while stack and stack[-1] < i:
            temp.append(stack.pop())

        stack.append(i)

if temp:
    highest = min(front_height, stack[-1])

    total_temp += temp

    for t in total_temp:
        result += max(highest - t, 0)

print(result)
