# 문제: 정수 집합 S가 주어졌을때, 다음 조건을 만족하는 구간 [A, B]를 좋은 구간이라고 한다.
# A와 B는 양의 정수이고, A < B를 만족한다.
# A ≤ x ≤ B를 만족하는 모든 정수 x가 집합 S에 속하지 않는다.
# 집합 S와 n이 주어졌을 때, n을 포함하는 좋은 구간의 개수를 구해보자.

# 입력: 첫째 줄에 집합 S의 크기 L이 주어진다. 둘째 줄에는 집합에 포함된 정수가 주어진다. 셋째 줄에는 n이 주어진다.

# 출력: 첫째 줄에 n을 포함하는 좋은 구간의 개수를 출력한다.

import sys

l = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline())

# 배열을 오름차순 정렬
arr.sort()

# A <= X <= B 를 만족시키기 위한 A를 start라고 두고 B를 end로 둔다.
start = 1
end = 1000

# 결과값 저장
result = 0

# 배열을 돌면서 start, end를 찾아 낸다.
for i in arr:
    if(i > n):
        end = i-1
        break
    else:
        start = i+1

# start 와 end 사이에 n이 있다면 갯수를 구해줌, 없다면 0을 출력
if(start <= n <= end):
    for i in range(start, n):
        result += (end - n + 1)

    print(result + (end-n))
else:
    print(0)
