import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insertValue(self.root, data)
        return self.root is not None

    def insertValue(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.value:
                node.left = self.insertValue(node.left, data)
            else:
                node.right = self.insertValue(node.right, data)
        return node
        
    def postOrder(self, node):
        
        if node.left != None: self.postOrder(node.left)
        if node.right != None: self.postOrder(node.right)
        print(node.value)

bint = BinaryTree()

while True:
    n = input().rstrip()
    if n.isdigit():
        bint.insert(int(n))
    else:
        break

bint.postOrder(bint.root)