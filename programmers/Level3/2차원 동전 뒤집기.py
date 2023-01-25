import sys
sys.setrecursionlimit(10**8)


def solution(beginning, target):
    answer = 1000000
    y = len(beginning)
    x = len(beginning[0])

    def dfs(i, cnt):
        nonlocal answer

        if beginning == target:
            answer = min(answer, cnt)

        if i == y+x or cnt >= answer:
            return

        dfs(i+1, cnt)

        if i < y:
            for j in range(x):
                beginning[i][j] = (beginning[i][j] + 1) % 2

            dfs(i+1, cnt+1)

            for j in range(x):
                beginning[i][j] = (beginning[i][j] + 1) % 2
        else:
            for j in range(y):
                beginning[j][i-y] = (beginning[j][i-y] + 1) % 2

            dfs(i+1, cnt+1)

            for j in range(y):
                beginning[j][i-y] = (beginning[j][i-y] + 1) % 2

    dfs(0, 0)

    if answer == 1000000:
        return -1

    return answer
