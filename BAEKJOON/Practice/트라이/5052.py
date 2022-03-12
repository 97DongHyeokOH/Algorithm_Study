import sys

input = sys.stdin.readline

# 트라이 자료구조 사용


class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = dict()


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, s):
        curNode = self.head

        for c in s:
            if(c not in curNode.children):
                curNode.children[c] = Node(c)
            curNode = curNode.children[c]

        curNode.data = s

    def search(self, s):
        curNode = self.head

        for c in s:
            if(curNode.data):
                return True
            elif(c in curNode.children):
                curNode = curNode.children[c]
            else:
                return False

        return False


t = int(input())

for _ in range(t):
    n = int(input())

    phone_num = [input().rstrip() for _ in range(n)]

    # 입력받은 번호의 길이로 오름차순 정렬
    phone_num.sort(key=lambda x: len(x))

    trie = Trie()
    result = 'YES'

    # 트라이를 탐색하면서 True값이 반환된다면 다른 번호의 접두어이다.
    for num in phone_num:
        if(trie.search(num)):
            result = 'NO'
            break

        trie.insert(num)

    print(result)
