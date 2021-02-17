# Union, Find 알고리즘을 사용했지만 효율성 테스트에서 시간초과가 남...

# def solution(k, room_number):
#     root = [[i, i] for i in range(k+1)]
#     result = []

#     def find(x):
#         if(root[x][0] == x):
#             return x
#         else:
#             return find(root[x][0])

#     def union(x, y):
#         x = find(x)
#         y = find(y)

#         root[y][0] = x
#         root[x][1] = root[y][1]

#     for i in room_number:
#         i -= 1
#         idx = find(i)
#         result.append(root[idx][1]+1)
#         union(idx, root[idx][1]+1)

#     return result

def solution(k, room_number):
    room = [[0, i+1] for i in range(k+2)]
    result = []

    for i in room_number:
        if(room[i][0]):
            idx = room[i][1]
            temp = [i]
            while(room[idx][0]):
                temp.append(idx)
                idx = room[idx][1]
            room[idx][0] = 1
            result.append(idx)
            for t in temp:
                room[t][1] = idx+1
        else:
            result.append(i)
            room[i][0] = 1
        # idx = room[i][1]
        # temp = []
        # while(room[idx][0]):
        #     temp.append(idx)
        #     if(idx == room[idx][1]):
        #         room[idx][1] = idx+1
        #         idx += 1
        #     else:
        #         idx = room[idx][1]
        # room[idx][0] = 1
        # result.append(idx)
        # if(idx == i):
        #     room[idx][1] += 1
        # else:
        #     for j in temp:
        #         room[j][1] = idx
        print(i)
        print(room)

    return result


print(solution(10, [1, 3, 4, 1, 3, 1]))
