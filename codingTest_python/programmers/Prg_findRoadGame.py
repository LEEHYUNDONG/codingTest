import sys
sys.setrecursionlimit(10**6)
class Node:
    def __init__(self, x, y, item):
        self.key = item
        self.x = x
        self.y = y
        self.left = None
        self.right = None

class binaryTree:
    def __init__(self):
        self.root = None
    
    def insertNode(self, node, new_node):
        if node == None:
            node = new_node
            return node
        else:
            if new_node.x < node.x:
                node.left = self.insertNode(node.left, new_node)
            else:
                node.right = self.insertNode(node.right, new_node)
            return node
        
    def preorder(self, node):
        global tmp
        if node == None:
            return
        tmp.append(node.key)
        self.preorder(node.left)
        self.preorder(node.right)
        
    
    def postorder(self, node):
        global tmp
        if node == None:
            return 
        self.postorder(node.left)
        self.postorder(node.right)
        tmp.append(node.key)
        

tmp = []

def solution(nodeinfo):
    global tmp
    answer = []
    
    for i in range(len(nodeinfo)):     
        nodeinfo[i].extend([i+1])
        
    nodeinfo.sort(key = lambda x : x[1], reverse=True)
    
    BT = binaryTree()
    
    for i in nodeinfo:
        n = Node(i[0], i[1], i[2])
        if BT.root == None:
            BT.root = n
        else:
            BT.insertNode(BT.root, n)
    
    tmp = []
    BT.preorder(BT.root)
    answer.append(tmp)
    tmp = []
    BT.postorder(BT.root)
    answer.append(tmp)
    
    return answer