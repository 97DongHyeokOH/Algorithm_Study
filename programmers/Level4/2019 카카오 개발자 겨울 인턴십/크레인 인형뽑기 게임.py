from collections import deque as dq


def solution(board, moves):
    q = [dq([]) for _ in range(len(board))]
    stack = []
    result = 0

    for i in range(len(board[0])):
        for j in range(len(board)):
            if(board[j][i]):
                q[i].append(board[j][i])

    for i in moves:
        if(q[i-1]):
            num = q[i-1].popleft()
        else:
            continue

        if(stack and stack[len(stack)-1] == num):
            stack.pop()
            result += 2
        else:
            stack.append(num)

    return result
