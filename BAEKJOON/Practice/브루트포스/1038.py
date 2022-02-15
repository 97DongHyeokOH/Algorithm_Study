from operator import length_hint
import sys

input = sys.stdin.readline

# 감소하는 수를 만들어주는 함수


def solution(k, s, length):
    # 감소하는 수의 최대 길이는 10
    if(length > 10):
        return

    # 배열에 감소하는 수를 넣어준다
    arr.append(s)

    # 다음 감소하는 수를 만들어준다
    for i in range(k-1, -1, -1):
        solution(i, s+str(i), length+1)


n = int(input())
# 모든 감수하는 수를 저장하는 list
arr = []

for k in range(9, -1, -1):
    solution(k, str(k), 1)

# 배열을 정렬
arr.sort(key=lambda x: int(x))

# 0번째 부터 len(arr)번째까지 모두 있지만 그 수는 len(arr)+1이다
# 따라서 len(arr)-1 보다 n이 크게되면 -1을 출력해야 된다.
if(len(arr)-1 < n):
    print(-1)
else:
    print(arr[n])
