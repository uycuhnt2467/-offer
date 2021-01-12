# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 13:31:14 2021

@author: a8520
"""


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverseTree(self, root1, root2):
        if root1 == None:
            return False
        if root2 == None:
            return False
        
        
        return self.checkSubTree(root1, root2) or \
            self.checkSubTree(root1.left, root2) or \
                self.checkSubTree(root1.right, root2)
        
    def checkSubTree(self, root1, root2):
        if root1.val == root2.val:
            same = True
            if root2.left != None:
                same = self.checkSubTree(root1.left, root2.left)
            if root2.right != None:
                same = same and self.checkSubTree(root1.right, root2.right)
            return same
        else:
            return False
        
a = TreeNode(1,None, None)
b = TreeNode(2,None, None)
c = TreeNode(3,b, a)


d = TreeNode(1,None, None)
e = TreeNode(2,None, None)
f = TreeNode(3, e, d)

sol = Solution()
print(sol.traverseTree(f, c))

        