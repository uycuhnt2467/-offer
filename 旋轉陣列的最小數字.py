# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 15:04:56 2021

@author: a8520
"""

# [3,4,5,1,2] -> [1,2,3,4,5] =>  ans = 1

# 1 2 3 4 5
# 3 5 1
# 3 5 7 1 2

class Solution():
    def findSol(self, nums):
        
        if not nums:
            return -1
        def processAllSame(nums, start, end):
            result = nums[start]
            for i in range(start, end):
                if result > nums[i]:
                    result = nums[i]
            return result
        
        start = 0
        end = len(nums) - 1
        
        while start < end:
            if end - start == 1:
                mid = end
                break
            
            mid = start + (end - start) // 2
            
            if nums[start] == nums[mid] and nums[mid] == nums[end]:
                return processAllSame(nums, start, end)
                
            
            if nums[start] <= nums[mid]:
                start = mid
            elif nums[mid] <= nums[end] :
                end = mid
            
        return nums[mid]
            
sol = Solution()


# test = [3, 5, 7, 1, 2]
# test = [1, 2, 2, 4, 5]
test = [1,1,1,1,1,1]
print(sol.findSol(test))











                