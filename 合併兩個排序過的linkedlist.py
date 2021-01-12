# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 12:01:17 2021

@author: a8520
"""

class Node:
    def __init__(self, val=None, next_=None):
        self.val = val
        self.next_ = next_


# 合併兩個排序好的linked list

class Solution:
    def merge(self, node1, node2):
        if not node1 and not node2:
            return None
        elif not node1:
            return node2
        elif not node2:
            return node1
        
        if node1.val > node2.val:
            start = node2
            i = node2
            j = node1
        else:
            start = node1
            i = node1
            j = node2
        
        temp = None
        while i.next_ != None and j.next_ != None:
            if i.next_.val < j.val:
                i = i.next_
            elif i.next_.val > j.val:
                temp = i.next_
                i.next_ = j
                i = i.next_
                j = j.next_
                i.next_ = temp
            else:
                # i.next_.val == j.val
                i = i.next_

        if i.next_ == None and j.next_ == None:
            i.next_ = j
            return start
        elif i.next_ == None:
            i.next_ = j
            return start
        else:
            # i.next_ != None but j.next_ = None
            while i.next_ != None:
                if i.next_.val <= j.val:
                    i = i.next_
                else:
                    temp = i.next_
                    i.next_ = j
                    i = i.next_
                    i.next_ = temp
                    j = j.next_
                    break
            if j != None:
                i.next_ = j
            return start
    def merge_recursive(self, node1, node2):
        if node1 == None:
            return node2
        elif node2 == None:
            return node1
        start = None
        if node1.val < node2.val:
            start = node1
            start.next_ = self.merge_recursive(node1.next_, node2)
        else:
            start = node2
            start.next_ = self.merge_recursive(node1, node2.next_)
        return start
    
    def printNode(self, node):
        while node != None:
            print(node.val)
            node = node.next_
    
    
node1 = Node(8, None)
node2 = Node(5, node1)
node3 = Node(4, node2)
node4 = Node(2, node3)

node5 = Node(9, None)
node6 = Node(5, node5)
node7 = Node(3, node6)
node8 = Node(1, node7)

sol = Solution()
ans = sol.merge(node8, node4)

print("--------------------------------------")

sol.printNode(ans)
node1 = Node(8, None)
node2 = Node(5, node1)
node3 = Node(4, node2)
node4 = Node(2, node3)

node5 = Node(9, None)
node6 = Node(5, node5)
node7 = Node(3, node6)
node8 = Node(1, node7)
ans2 = sol.merge_recursive(node8, node4)
sol.printNode(ans2)