# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 15:44:50 2021

@author: a8520
"""


# preorder print = 1, 2, 4, 7, 3, 5, 6, 8
# inorder print = 4, 7, 2, 1, 5, 3, 8, 6

class BinaryTreeNode():
    def __init__(self, value=None, leftNode=None, rightNode=None):
        self.val = value
        self.left = leftNode
        self.right = rightNode


preorder_list = [1, 2, 4, 7, 3, 5, 6, 8]
inorder_list = [4, 7, 2, 1, 5, 3, 8, 6]


class Solution:
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        
        root_val = preorder[0]
        # split_index = inoder.indexOf(root_val)
        
        index = 0
        left_set = set()
        for i in inorder:
            if i == root_val:
                break
            left_set.add(i)
            index += 1
        left_inorder = inorder[:index]
        right_inorder = inorder[index+1:]
        
        # find preorder
        j = 1
        while j < len(preorder):
            if preorder[j] in left_set:
                j += 1
            else:
                break
        left_preorder = preorder[1:j]
        right_preorder = preorder[j:]
        node = BinaryTreeNode()
        node.val = root_val
        node.left = self.buildTree(left_preorder, left_inorder)
        node.right = self.buildTree(right_preorder, right_inorder)
        return node
sol = Solution()
a = sol.buildTree(preorder_list, inorder_list)


def preorderTraverse(node):
    if node != None:
        print(node.val)
    
    if node.left != None:
        preorderTraverse(node.left)
    if node.right != None:
        preorderTraverse(node.right)
        
def inorderTraverse(node):
    if node.left != None:
        inorderTraverse(node.left)
    if node != None:
        print(node.val)
    if node.right != None:
        inorderTraverse(node.right)
        
preorderTraverse(a)
print("-----------")
inorderTraverse(a)
                 