# 문제1
# 하노이 탑(Tower of Hanoi)은 퍼즐의 일종입니다.
# 세 개의 기둥과 이 기동에 꽂을 수 있는 크기가 다양한 원판들이 있고,
# 퍼즐을 시작하기 전에는 한 기둥에 원판들이 작은 것이 위에 있도록 순서대로 쌓여 있습니다.
# 게임의 목적은 다음 두 가지 조건을 만족시키면서,
# 한 기둥에 꽂힌 원판들을 그 순서 그대로 다른 기둥으로 옮겨서 다시 쌓는 것입니다.

# 한 번에 하나의 원판만 옮길 수 있습니다.
# 큰 원판이 작은 원판 위에 있어서는 안됩니다.
# 하노이 탑의 세 개의 기둥을 왼쪽 부터 1번, 2번, 3번이라고 하겠습니다.
# 1번에는 n개의 원판이 있고 이 n개의 원판을 3번 원판으로 최소 횟수로 옮기려고 합니다.

# 1번 기둥에 있는 원판의 개수 n이 매개변수로 주어질 때,
# n개의 원판을 3번 원판으로 최소로 옮기는 방법을 return하는 solution를 완성해주세요.

# 제한사항
# n은 15이하의 자연수 입니다.

def solution(n):
    return hanoi(1, 2, 3, n)


def hanoi(f, b, t, n):  # from, by, to, n-th plate
    result = []
    if(n == 1):
        return [[f, t]]
    else:
        result += hanoi(f, t, b, n-1)
        result += [[f, t]]
        result += hanoi(b, f, t, n-1)

    return result

# 문제2
# 문제 설명
# 회사원 Demi는 가끔은 야근을 하는데요, 야근을 하면 야근 피로도가 쌓입니다.
# 야근 피로도는 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값입니다.
# Demi는 N시간 동안 야근 피로도를 최소화하도록 일할 겁니다.
# Demi가 1시간 동안 작업량 1만큼을 처리할 수 있다고 할 때,
# 퇴근까지 남은 N 시간과 각 일에 대한 작업량 works에 대해
# 야근 피로도를 최소화한 값을 리턴하는 함수 solution을 완성해주세요.

# 제한 사항
# works는 길이 1 이상, 20,000 이하인 배열입니다.
# works의 원소는 50000 이하인 자연수입니다.
# n은 1,000,000 이하인 자연수입니다.

# import heapq as hq

# def solution(n, works):
#     heap = []
#     for work in works:
#         hq.heappush(heap, (-work, work))

#     while(heap and n):
#         work = hq.heappop(heap)[1]
#         work -= 1
#         n -= 1
#         if(work > 0):
#             hq.heappush(heap, (-work, work))

#     if(heap):
#         result = 0
#         for i in heap:
#             result += i[1]**2
#         return result

#     return 0
