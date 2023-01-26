import heapq


def solution(n, k, enemy):
    answer = 0

    min_heap = []

    for i in enemy:
        if len(min_heap) < k:
            heapq.heappush(min_heap, i)
        else:
            if min_heap[0] < i:
                cur = heapq.heappop(min_heap)
                heapq.heappush(min_heap, i)
            else:
                cur = i

            if n < cur:
                break
            else:
                n -= cur

        answer += 1

    return answer


print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
