import sys

s = int(sys.stdin.readline())
# dp[i][j] -> 화면에 표시된 이모티콘 i개, 클립보드에 저장된 이모티콘 j개 일때 걸리는 시간의 최소값
dp = [[sys.maxsize]*(s+1) for _ in range(s+1)]
# 초기값 설정
dp[1][0] = 0
queue = [[1, 0]]

# bfs
while(queue):
    idx, clip = queue.pop(0)

    # 화면에 있는 이모티콘을 모두 복사해 클립보드에 저장
    if(dp[idx][idx] == sys.maxsize):
        dp[idx][idx] = dp[idx][clip] + 1
        queue.append([idx, idx])

    # 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
    if(idx + clip <= s and dp[idx+clip][clip] == sys.maxsize):
        dp[idx+clip][clip] = dp[idx][clip] + 1
        queue.append([idx+clip, clip])

    # 이모티콘 중 하나를 삭제한다.
    if(idx - 1 >= 0 and dp[idx-1][clip] == sys.maxsize):
        dp[idx-1][clip] = dp[idx][clip] + 1
        queue.append([idx-1, clip])

print(min(dp[s]))
