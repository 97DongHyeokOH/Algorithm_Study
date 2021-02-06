# 내가 생각해서 풀어낸 코드
# 정확성은 25/25 이지만 효율성은 30/75이다.
# -> 시간복잡도를 최대한 줄이기 위한 방법을 찾던 도중 '트라이(Trie)' 자료구조에 대해 알게 되었다.
# def solution(words, queries):
#     answer = []

#     for querie in queries:
#         idx = querie.find('?')
#         num = querie.count('?')
#         l1 = len(querie)
#         cnt = 0

#         if(idx):
#             s1 = querie[:idx]
#         else:
#             s1 = querie[idx+num:]

#         for word in words:
#             l2 = len(word)

#             if(idx):
#                 s2 = word[:idx]
#             else:
#                 s2 = word[idx+num:]

#             if(l1 == l2 and s1 == s2):
#                 cnt += 1

#         answer.append(cnt)

#     return answer

# '트라이(Trie)'를 공부 한 뒤 코드
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.children_cnt = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur_node = self.head
        c_cnt = len(string)

        for char in string:
            if(char not in cur_node.children):
                cur_node.children[char] = Node(char)

            if(c_cnt not in cur_node.children_cnt):
                cur_node.children_cnt[c_cnt] = 1
            else:
                cur_node.children_cnt[c_cnt] += 1

            c_cnt -= 1

            cur_node = cur_node.children[char]

        cur_node.data = string

    def starts_with(self, prefix):
        cur_node = self.head
        subtrie = self.head
        cnt = 0

        for char in prefix:
            if(char in cur_node.children):
                cur_node = cur_node.children[char]
                subtrie = cur_node
            elif(char == '?'):
                cnt += 1
            else:
                return 0

        if(cnt in subtrie.children_cnt):
            return subtrie.children_cnt[cnt]
        else:
            return 0


def solution(words, queries):
    answer = []

    trie = Trie()
    trie_r = Trie()

    for word in words:
        trie.insert(word)
        trie_r.insert(word[::-1])

    for querie in queries:
        if(querie[0] == '?'):
            answer.append(trie_r.starts_with(querie[::-1]))
        else:
            answer.append(trie.starts_with(querie))

    return answer
