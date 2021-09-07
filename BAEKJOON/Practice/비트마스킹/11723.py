import sys

input = sys.stdin.readline

n = int(input())
num = 0

for _ in range(n):
    temp = input().rstrip()

    opcode = temp.split()[0]

    if(opcode == 'add'):
        num |= 1 << int(temp.split()[1])
    elif(opcode == 'remove'):
        num &= ~(1 << int(temp.split()[1]))
    elif(opcode == 'check'):
        if(num & (1 << int(temp.split()[1]))):
            print(1)
        else:
            print(0)
    elif(opcode == 'toggle'):
        num ^= (1 << int(temp.split()[1]))
    elif(opcode == 'all'):
        num = (1 << 21)-1
    else:
        num = 0
