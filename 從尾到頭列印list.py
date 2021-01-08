# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 15:31:51 2021

@author: a8520
"""


# 是否能改變原始list?
# 後進先出 -> stack

class Node():
    def __init__(self, val, next_ = None):
        self.val = val
        self.next= next_
    def hasNext(self):
        if (self.next) == None:
            return False
        else:
            return True
        
node5 = Node(5)
node4 = Node(3, node5)
node3 = Node(11, node4)
node2 = Node(2, node3)
node1 = Node(1, node2)

def reversePrint(node):
    stack = []
    cur = node
    while cur.hasNext():
        stack.append(cur)
        cur = cur.next
    stack.append(cur)
    while stack:
        cur_node = stack.pop()
        print(cur_node.val)
# reversePrint(node1)

