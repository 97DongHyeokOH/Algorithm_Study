import sys

# 재귀 최대치 제한해제
sys.setrecursionlimit(100000000)

# 문제를 해결하기 위한 함수
# solution(start)는 start 인덱스부터 시작한 문자열이 입력된 문자들로 이어서 만들수 있는지 판단해줌
# 만드는 것이 가능하다면 1을 출력


def solution(start):
    if(start == len(s)):
        print(1)
        exit()

    for i in temp[start]:
        if(not visit[i]):
            visit[i] = True
            solution(i)


input = sys.stdin.readline

s = input().rstrip()
n = int(input())
words = {input().rstrip() for _ in range(n)}
visit = [False]*(len(s)+1)
# temp는 temp의 key를 시작 인덱스, value의 list에 들어있는 값들을 도착 인덱스로
# s[key:value+1]의 문자열이 입력된 문자열에 존재한다는 의미이다.
temp = dict()

for i in range(len(s)):
    temp[i] = []

for i in range(len(s)):
    for j in range(i, len(s)):
        # s[i:j+1] 문자열이 words에 있다면 temp[i]에 j+1를 append해줌
        if(s[i:j+1] in words):
            temp[i].append(j+1)

for i in temp[0]:
    # 이미 i번째 인덱스에서 시작한 적이 있다면 실행 x
    if(not visit[i]):
        visit[i] = True
        solution(i)

# 입력한 문자들을 이어붙혀서 s를 못만드는 경우 0을 print
print(0)
