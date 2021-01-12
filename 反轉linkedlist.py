# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 09:18:57 2021

@author: a8520
"""

class Node:
    def __init__(self, val=None, next_=None):
        self.val = val
        self.next_ = next_


class Solution:
    def reverseNode(self, node):
        if not node:
            return None
        
        i = node
        if i.next_ != None:
            j = i.next_
            i.next_ = None
        else:
            return i
        k = j.next_
        while k != None:
            j.next_ = i
            i = j
            j = k
            k = k.next_
        j.next_ = i
        return j
            
            
        
        

node1 = Node(1, None)
node2 = Node(2, node1)
node3 = Node(3, node2)
node4 = Node(4, node3)
node5 = Node(5, node4)
node6 = Node(6, node5)
node7 = Node(7, node6)
node8 = Node(8, node7)

sol = Solution()
print(sol.reverseNode(node1).val)
            
            