t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    p = [0]*(n+1)
    book = []
    cnt = 0

    for _ in range(m):
        a, b = map(int, input().split())

        book.append((b,a))
    
    book.sort()

    for b, a in book:
        for idx in range(a, b+1):
            if(p[idx] != 1001):
                cnt += 1
                p[idx] = 1001
                break
    
    print(cnt)