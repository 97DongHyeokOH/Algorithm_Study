import sys

input = sys.stdin.readline

k = int(input())

arr = [list(map(int, input().split())) for _ in range(6)]

temp1 = arr[::2]
temp2 = arr[1::2]

max_t1, max_t2 = 0, 0
max_t1_idx, max_t2_idx = -1, -1

for i in range(3):
    if max_t1 < temp1[i][1]:
        max_t1 = temp1[i][1]
        max_t1_idx = i
    if max_t2 < temp2[i][1]:
        max_t2 = temp2[i][1]
        max_t2_idx = i

result = max_t1 * max_t2 - abs(temp2[max_t1_idx][1] - temp2[(
    max_t1_idx-1) % 3][1]) * abs(temp1[max_t2_idx][1] - temp1[(max_t2_idx+1) % 3][1])


print(result * k)
