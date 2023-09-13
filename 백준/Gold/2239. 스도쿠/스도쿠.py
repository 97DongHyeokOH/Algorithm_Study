import sys

input = sys.stdin.readline

def solution(y, x):
    if y == 9:
        for i in range(9):
            print(''.join(map(str, sudoku[i])))
        exit()
    
    if sudoku[y][x]:
        solution(y + (x+1) // 9, (x+1) % 9)
        return
        
    for i in range(1, 10):
        able = True
        for j in range(9):
            if sudoku[j][x] == i or sudoku[y][j] == i or sudoku[3 * (y // 3) + j//3][3 * (x // 3) + j%3] == i:
                able = False
                break
                
        if able:
            sudoku[y][x] = i
            solution(y + (x+1) // 9, (x+1) % 9)
            sudoku[y][x] = 0

sudoku = [list(map(int, input().rstrip())) for _ in range(9)]

solution(0, 0)