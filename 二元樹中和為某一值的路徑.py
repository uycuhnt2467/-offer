# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 09:49:07 2021

@author: a8520
"""

# 輸入一顆二元樹和一個整數，列出所有從"根到葉"節點值總和和輸入的值相同的路徑。

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def find_path(self, root, expected_sum):
        # if not root:
        #     return []
        
        ans = list()        
        cur_list = list() # is a stack
        
        def dfs(node, cur_list, expected_sum):
            if not node:
                return
            cur_list.append(node.val)
            expected_sum -= node.val
            
            if not node.left and not node.right and expected_sum == 0:
                ans.append(cur_list[:])
                
            if node.left:
                dfs(node.left, cur_list, expected_sum)
            if node.right:
                dfs(node.right, cur_list, expected_sum)
            cur_list.pop()
            
        dfs(root, cur_list, expected_sum)
        return ans

e = TreeNode(7)
d = TreeNode(4)

c = TreeNode(12)
b = TreeNode(5, d, e)

a = TreeNode(10, b, c)
sol = Solution()
print(sol.find_path(a, 22))
print(sol.find_path(None, 22))