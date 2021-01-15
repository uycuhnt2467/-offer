# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 09:21:03 2021

@author: a8520
"""


# 給定一個序列，確認該序列是否為二元搜索樹後序traverse的結果。
# 例如: 5, 7, 6, 9, 11, 10, 8 => True
#       7, 4, 6, 5 => False



        
class Solution:
    def check_postorder_sequence(self, nums):        
        if not nums:
            return False
        root = nums[-1]
        i = 0
        while i < len(nums)-1:
            if root > nums[i]:
                i += 1
            else:
                break
        j = i
        while j < len(nums)-1:
            if root < nums[j]:
                j += 1
            else:
                return False
        
        check_left = True
        if i != 0:
            check_left = self.check_postorder_sequence(nums[:i])
            
        check_right = True
        if j != i:
            check_right = self.check_postorder_sequence(nums[i:j])
        
        return check_left and check_right

sol = Solution()
nums = [5, 7, 6, 9, 11, 10, 8]
nums = [7, 4, 6, 5]
nums = []
print(sol.check_postorder_sequence(nums))