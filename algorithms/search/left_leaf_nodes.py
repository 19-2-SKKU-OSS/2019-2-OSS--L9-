'''
Given a tree, one of the nodes will be removed. 
Then, this program will find the number of leaf nodes in the remaining tree.
'''

import sys
sys.stdin = open("input.txt", 'r')

def preorder(node):
    global cnt
    if node.child == []:
        cnt += 1
    for child in node.child:
        preorder(tree[child])

class Node:
    def __init__(self):
        self.child = []
    def setChild(self, node):
        self.child.append(node)
    def removeChild(self, node):
        self.child.remove(node)

N = int(input())
tree = [Node() for _ in range(N)]
cnt = 0
parent = list(map(int, input().split()))
for i in range(N):
    if parent[i] != -1:
        tree[parent[i]].setChild(i)
if N != 1:
    i = int(input())
    if parent[i] == -1:
        cnt = 0
    else:
        tree[parent[i]].removeChild(i)
        preorder(tree[parent.index(-1)])
print(cnt)
