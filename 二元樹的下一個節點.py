# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 17:46:07 2021

@author: a8520
"""

# 給定一個二元樹和其中一個節點，找到中序traverse的下一個節點。

class Node():
    def __init__(self, val=None, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class Solution():
    def findNextNodeInOrder(node):
        if node.right != None:
            next_ = node.right
            while next_.left != None:
                next_ = next_.left
            return next_
        elif node.parent != None and node == node.parent.left:
            return node.parent
        elif node.parent != None and node == node.parent.right:
            next_ = node.parent
            while next_.parent != None and next_.parent.right == next_:
                next_ = next_.parent
            if next_.parent != None:
                return None
                
                    
                    
                
                
            
        