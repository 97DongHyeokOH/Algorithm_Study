import sys

input = sys.stdin.readline

length, width, height = map(int, input().split())

n = int(input())

cube = [list(map(int, input().split())) for _ in range(n)]
cube.sort(reverse=True)

ans = 0
ans, cur_total = 0, 0
total = length * width * height

for c_idx, c_cnt in cube:
    cur_total *= 8 
    c_len = 2**c_idx
    
    cube_cnt = (length // c_len) * (width // c_len) * (height // c_len) - cur_total
    cube_cnt = min(c_cnt, cube_cnt)
    
    ans += cube_cnt
    cur_total += cube_cnt

if cur_total == total:
    print(ans)
else:
    print(-1)