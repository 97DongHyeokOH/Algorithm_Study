import sys


def binary_search(n):
    start = 0
    end = len(card)-1

    while(start <= end):
        mid = (start + end) // 2

        if(card[mid] == n):
            return '1'
        elif(card[mid] < n):
            start = mid + 1
        else:
            end = mid - 1

    return '0'


n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
card_list = list(map(int, sys.stdin.readline().split()))
result = []

card.sort()
for i in card_list:
    result.append(binary_search(i))

print(' '.join(result))
