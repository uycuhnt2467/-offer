# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 08:45:23 2021

@author: a8520
"""



class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def is_symmetrical(self, root):
        return self.is_symmetrical_helper(root, root)
    
    def is_symmetrical_helper(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        
        if root1 == None or root2 == None:
            return False
        
        if root1.val != root2.val:
            return False
        
        return self.is_symmetrical_helper(root1.left, root2.right) and \
            self.is_symmetrical_helper(root1.right, root2.left)
       
sol = Solution()        


c = TreeNode()
print(sol.is_symmetrical(c))

a = TreeNode(2,None, None)
print(sol.is_symmetrical(a))

a = TreeNode(1,None, None)
b = TreeNode(3,None, None)
c = TreeNode(2, a, b)
print(sol.is_symmetrical(c))

a = TreeNode(2,None, None)
b = TreeNode(2,None, None)
c = TreeNode(3, a, b)
print(sol.is_symmetrical(c))