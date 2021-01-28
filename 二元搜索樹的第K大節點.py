# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 14:54:56 2021

@author: a8520
"""


# 54. 二元搜索樹的第K大節點

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left # smaller
        self.right = right # larger


class Solution:
    def get_the_K_node(self, node, k):
        found_node, result = self.get_the_K_node_helper(node, k)
        if result == 0:
            return found_node.val
        else:
            return None
        
    def get_the_K_node_helper(self, node, k):
        if not node:
            return None, k
        
        if node.left != None:
            temp, k = self.get_the_K_node_helper(node.left, k)
            if k == 0:
                return temp, 0
        
        k -= 1
        if k == 0:
            return node, 0
        
        if node.right != None:
            temp, k = self.get_the_K_node_helper(node.right, k)
            if k == 0:
                return temp, 0
        return node, k
            
a = Node(6)
b = Node(8)
c = Node(2)
d = Node(4)

e = Node(7, a, b)
f = Node(3, c, d)

g = Node(5, f, e)

sol = Solution()
print(sol.get_the_K_node(g, 7))
            
            
            
            
            
            
            
            
            
    