# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 08:23:22 2021

@author: a8520
"""


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def reverseTree(self, root):
        if not root:
            return None
       
        temp = self.reverseTree(root.left)
        root.right = self.reverseTree(root.right)
        root.left = root.right
        root.right = temp
        return root
    
    def reverseTree_iterative(self, root):
        stack = list()
        stack.append(root)
        while stack:
            cur = stack.pop()
            temp = cur.left
            cur.left = cur.right
            cur.right = temp
            if cur.left != None:
                stack.append(cur.left)
            if cur.right != None:
                stack.append(cur.right)
        return root
    
    def inorderTraverse(self, root):
        if not root:
            return 
        if root.left:
            self.inorderTraverse(root.left)
        print(root.val)
        if root.right:
            self.inorderTraverse(root.right)

a = TreeNode(1,None, None)
b = TreeNode(3,None, None)
c = TreeNode(2, a, b)

sol = Solution()
sol.inorderTraverse(c)        
sol.reverseTree(c)
sol.inorderTraverse(c)

print("-----------")
a = TreeNode(1,None, None)
b = TreeNode(3,None, None)
c = TreeNode(2, a, b)

sol = Solution()
sol.inorderTraverse(c)        
sol.reverseTree_iterative(c)
sol.inorderTraverse(c)