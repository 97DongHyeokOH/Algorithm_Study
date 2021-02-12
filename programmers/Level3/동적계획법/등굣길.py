def solution(m, n, puddles):
    arr = [[0]*m for _ in range(n)]
    for x, y in puddles:
        arr[y-1][x-1] = -1

    arr[0][0] = 1

    for i in range(n):
        for j in range(m):
            if(arr[i][j] == -1):
                continue

            if(j+1 < m and arr[i][j+1] != -1):
                arr[i][j+1] = (arr[i][j+1] + arr[i][j]) % 1000000007

            if(i+1 < n and arr[i+1][j] != -1):
                arr[i+1][j] = (arr[i+1][j] + arr[i][j]) % 1000000007
                
    return arr[n-1][m-1]