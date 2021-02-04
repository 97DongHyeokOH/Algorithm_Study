t = int(input())

for _ in range(t):
    n = int(input())
    arr1 = list(map(str, input()))
    arr2 = list(map(str, input()))

    b_w = 0
    w_b = 0

    for idx in range(n):
        if(arr1[idx] != arr2[idx]):
            if(arr1[idx] == 'W'):
                w_b += 1
            else:
                b_w += 1
    
    result = max(w_b, b_w)

    print(result)
