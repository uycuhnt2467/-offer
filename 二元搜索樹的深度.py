# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 09:50:32 2021

@author: a8520
"""


# 55. 二元搜索樹的深度

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left # smaller
        self.right = right # larger


class Solution:
    def get_deepth(self, node):
        return self.get_deepth_helper(node)
    
    def get_deepth_helper(self, node):
        if node == None:
            return 0
        else:
            return 1 + max(self.get_deepth_helper(node.left), self.get_deepth_helper(node.right))
    
    
a = Node(6)
b = Node(8)
c = Node(2)
d = Node(4)

e = Node(7, a, b)
f = Node(3, c, d)

g = Node(5, f, e)


sol = Solution()

print(sol.get_deepth(g))