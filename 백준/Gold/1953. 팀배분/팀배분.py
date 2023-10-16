import sys

input = sys.stdin.readline

def solution(person, is_blueteam):
    if is_blueteam:
        blue_team.append(person)
    else:
        read_team.append(person)
    for hate in hater[person]:
        if hate in candidate:
            candidate.remove(hate)
            solution(hate, not is_blueteam)

n = int(input())

blue_team = []
read_team = []
hater = [[]] + [list(map(int, input().split()))[1:] for _ in range(n)]
candidate = [i for i in range(1, n + 1)]

while candidate:
    c = candidate.pop()
    solution(c, True)   
    
blue_team.sort()
read_team.sort()
print(len(blue_team))
print(*blue_team)
print(len(read_team))
print(*read_team)