import sys


class Node:
    def __init__(self, data, left, right):
        self.left = left
        self.right = right
        self.data = data


class BinaryTree:
    def __init__(self, root):
        self.root = root


def preorder(node):
    print(node.data, end="")
    if node.left != ".":
        preorder(tree[node.left])
    if node.right != ".":
        preorder(tree[node.right])


def inorder(node):
    if node.left != ".":
        inorder(tree[node.left])
    print(node.data, end="")
    if node.right != ".":
        inorder(tree[node.right])


def postorder(node):
    if node.left != ".":
        postorder(tree[node.left])
    if node.right != ".":
        postorder(tree[node.right])
    print(node.data, end="")


n = int(sys.stdin.readline())
tree = {}

for _ in range(n):
    root, l, r = map(str, sys.stdin.readline().split())
    tree[root] = Node(data=root, left=l, right=r)

preorder(tree["A"])
print()
inorder(tree["A"])
print()
postorder(tree["A"])

