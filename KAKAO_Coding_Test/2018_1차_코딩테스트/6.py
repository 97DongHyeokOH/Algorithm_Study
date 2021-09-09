import copy


def solution(n, m, board):
    answer = 0

    dy = [0, 1, 1]
    dx = [1, 0, 1]

    for i in range(n):
        board[i] = list(board[i])

    while(1):
        temp = copy.deepcopy(board)
        block_remove = False

        for i in range(n-1):
            for j in range(m-1):
                can_remove = True
                if(board[i][j] != '0'):
                    for idx in range(3):
                        if(board[i][j] != board[i+dy[idx]][j + dx[idx]]):
                            can_remove = False
                            break

                    if(can_remove):
                        temp[i][j] = '0'
                        temp[i+1][j] = '0'
                        temp[i][j+1] = '0'
                        temp[i+1][j+1] = '0'
                        block_remove = True

        if(not block_remove):
            break

        board = [['0']*m for _ in range(n)]

        for j in range(m):
            next_idx = n-1
            for i in range(n-1, -1, -1):
                board[next_idx][j] = temp[i][j]
                if(temp[i][j] != '0'):
                    next_idx -= 1

    for i in range(n):
        for j in range(m):
            if(board[i][j] == '0'):
                answer += 1

    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
