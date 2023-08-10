import sys

input = sys.stdin.readline

class Node():
    def __init__(self, key):
        self.key = key
        self.children = {}
        
class Trie():
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, feeds):
        cur_node = self.head
        
        for feed in feeds:
            if feed not in cur_node.children:
                cur_node.children[feed] = Node(feed)
            cur_node = cur_node.children[feed]
            
def print_tree(i, parent):
    for child in sorted(parent.children):
        print('--'*i + child)
        print_tree(i+1, parent.children[child])

n = int(input())

tree = Trie()

for _ in range(n):
    temp = list(input().split())
    
    k, feeds = int(temp[0]), temp[1:]
    
    tree.insert(feeds)

print_tree(0, tree.head)