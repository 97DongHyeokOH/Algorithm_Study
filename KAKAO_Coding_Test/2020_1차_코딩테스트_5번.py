def solution(n, build_frame):
    answer = [[]]
    # [a,b,c,d] -> a,b: 기둥/보 설치 o, c,d: 기둥/보 삭제 -> 가능하면 1 안되면 0
    arr = [[[0]*4 for _ in range(n)] for _ in range(n)]
    return answer


def pos(build, arr):
    x, y, a, b = build
    if(b):
        if(a):
            if(not y and (arr[y-1][x][0] or (not x and arr[y][x-1][1]) and arr[y][x+1][1])):
                arr[y][x][1] = 1
        else:
            if(y == 0 or arr[y-1][x][0] or (not x and arr[y][x-1][1]) or arr[y][x][1]):
                arr[y][x][0] = 1
    else:
        if(a):
            if((x and arr[y][x-1][0] and arr[y][x+1][0]) or arr[y][x+1][0]):
                arr[y][x][1] = 0
        else:
            if((y and arr[y+1][x][0]))


def pos(build, arr):
    x, y, a, b = build

    if(arr[y][x][0]):
        if()


solution(3, 100)
