import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
result = [-sys.maxsize]

for num in arr:
    if(result[-1] < num):
        result.append(num)
    else:
        left = 0
        right = len(result)

        while(left < right):
            mid = (left + right) // 2

            if(result[mid] < num):
                left = mid + 1
            else:
                right = mid

        result[right] = num

print(len(result)-1)
