import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

class Node:
    def __init__(self, val, l, r):
        self.value = val
        self.left = l
        self.right = r



def finorder(node):
    global res
    if node.left != -1:
        finorder(tree[node.left])
        res += 1
    if node.value == finish:
        print(res)
        exit(0)
    res += 1
    if node.right != -1:
        finorder(tree[node.right])
        res += 1
        
def findLast(node):
    global finish
    if node.left != -1:
        findLast(tree[node.left])
    finish = node.value
    if node.right != -1:
        findLast(tree[node.right])

    

N = int(input())
tree = {}
res = 0
finish = -int(1e9)

for _ in range(N):
    a, b, c = map(int, input().split())
    tree[a] = Node(a, b, c)


findLast(tree[1])
finorder(tree[1])