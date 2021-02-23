from queue import PriorityQueue


def solution(food_times, k):
    if(sum(food_times) <= k):
        return -1

    result = 0

    q = PriorityQueue()
    for idx in range(len(food_times)):
        q.put((food_times[idx], idx+1))

    val = 0
    prev = 0
    length = len(food_times)

    while(val + ((q.queue[0][0] - prev) * length) <= k):
        now = q.get()[0]
        val += (now - prev) * length
        length -= 1
        prev = now

    result = sorted(q.queue, key=lambda x: x[1])

    return result[(k-val) % len(q.queue)][1]
