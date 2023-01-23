def solution(k, d):
    c = 0
    for y in range(0, d, k):
        x = (d**2 - y**2)**0.5
        c += x//k
    return c + d//k + 1
