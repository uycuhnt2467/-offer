# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 08:56:25 2021

@author: a8520
"""


# 53.在排序數列中找尋數字
# 例: {1, 2, 3, 3, 3, 3, 4, 5} 求3為4，因為3出現4次。

class Solution:
    def get_num_of_k_in_array(self, nums, k):
        if not nums or not k:
            return 0
        # 單次二分查詢
        # time complexity = N (仍要向前、向後找每個數字)
        i = 0
        j = len(nums)    
        
        while i < j:
            mid = i + (j - i)//2
            if nums[mid] == k:
                i = mid
                break
            elif nums[mid] < k:
                i = mid + 1
            else:
                j = mid
        
        if nums[mid] != k:
            return 0
        
        count = 0
        start = i - 1
        while start > 0:
            if nums[start] == k:
                count += 1
                start -= 1
            else:
                break
            
        end = i + 1
        while end < len(nums):
            if nums[end] == k:
                count += 1
                end += 1
            else:
                break
        count += 1
        return count
    
    def get_num_of_k_in_array_2(self, nums, k):
        # 利用兩次二分搜索
        # time complexity = logN
        start = self.get_first_k(nums, k)
        end = self.get_last_k(nums, k)
        if start == -1 or end == -1:
            return -1
        return end - start + 1
    
    def get_first_k(self, nums, k):
        i = 0
        j = len(nums)    
        
        while i < j:
            mid = i + (j - i)//2
            cond = self.check_first(nums, mid, k)
            if cond == 0:
                i = mid
                return i
            elif cond == -1:
                i = mid + 1
            else:
                j = mid
        
        return -1
    
    def check_first(self, nums, mid, k):
        if nums[mid] == k and mid > 0 and nums[mid - 1] != k:
            return 0
        elif nums[mid] == k and mid == 0:
            return 0
        elif nums[mid] == k and mid > 0 and nums[mid - 1] == k:
            return 1
        elif nums[mid] < k:
            return -1
        elif nums[mid] > k:
            return 1
        
    def get_last_k(self, nums, k):
        
        i = 0
        j = len(nums)    
        
        while i < j:
            mid = i + (j - i)//2
            cond = self.check_last(nums, mid, k)
           
            if cond == 0:
                i = mid
                return i
            elif cond == -1:
                i = mid + 1
            else:   
                j = mid
        return -1
    
    def check_last(self, nums, mid, k):
        if nums[mid] == k and mid < len(nums) - 1 and nums[mid + 1] != k:
            return 0
        elif nums[mid] == k and mid == len(nums) - 1:
            return 0
        elif nums[mid] == k and mid < len(nums) - 1 and nums[mid + 1] == k:
            return -1
        elif nums[mid] < k:
            return -1
        elif nums[mid] > k :
            return 1
        

sol = Solution()
test = [1, 2, 3, 3, 3, 3, 3, 4]
# test= [1,3]
# print(sol.get_num_of_k_in_array(test, 4))
print(sol.get_num_of_k_in_array_2(test, 3))