class BinaryTree:
    def __init__(self):
        self.tree = {}

    def add_node(self, root, left, right):
        self.tree[root] = [left, right]

    def preorder(self, node):
        if node == '.':
            return
        print(node, end='')
        self.preorder(self.tree[node][0])
        self.preorder(self.tree[node][1])

    def inorder(self, node):
        if node == '.':
            return
        self.inorder(self.tree[node][0])
        print(node, end='')
        self.inorder(self.tree[node][1])

    def postorder(self, node):
        if node == '.':
            return
        self.postorder(self.tree[node][0])
        self.postorder(self.tree[node][1])
        print(node, end='')


import sys
input = sys.stdin.readline

N = int(input().strip())
bt = BinaryTree()

for _ in range(N):
    root, left, right = input().strip().split()
    bt.add_node(root, left, right)

bt.preorder('A')
print()
bt.inorder('A')
print()
bt.postorder('A')
