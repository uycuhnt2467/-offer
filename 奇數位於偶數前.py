# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 12:42:36 2021

@author: a8520
"""


class Solution():
    def reorder(self, nums):
        start = 0
        back = len(nums) - 1
        
        while start < back:
            if nums[start] % 2 == 0:
                temp = nums[start]
                nums[start] = nums[back]
                nums[back] = temp
                back -= 1
            else:
                start += 1
        
        return nums
    

sol = Solution()
test = [2,4,5,1,6]
print(sol.reorder(test))