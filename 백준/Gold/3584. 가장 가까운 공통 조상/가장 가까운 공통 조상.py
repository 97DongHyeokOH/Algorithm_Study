import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def set_depth(i, node):
    node_depth[node] = i
    
    for child_node in child[node]:
        set_depth(i+1, child_node)

def lca(node1, node2):
    while node_depth[node1] != node_depth[node2]:
        if node_depth[node1] > node_depth[node2]:
            node1 = parent[node1]
        else:
            node2 = parent[node2]
    
    while node1 != node2:
        node1 = parent[node1]
        node2 = parent[node2]

    return node1

t = int(input())

for _ in range(t):
    n = int(input())
    
    parent = defaultdict(int)
    child = defaultdict(list)
    node_depth = [0]*(n+1)
    
    for i in range(n-1):
        p, c = map(int, input().split())
        
        parent[c] = p
        child[p].append(c)
    
    root_node = (set(i for i in range(1, n+1)) - set(parent.keys())).pop()
    set_depth(1, root_node)
    
    n1, n2 = map(int, input().split())
    
    print(lca(n1, n2))