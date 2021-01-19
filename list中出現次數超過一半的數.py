# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 21:00:17 2021

@author: a8520
"""


class Solution:
    
    def more_than_half_num(self, nums):
        # time complexity: O(n) -> traverse for 2n
        # space complexity: O(n) count_dictionary
        pass
    
    def more_then_half_num_2(self, nums):
        # quicksort變體
        # time complexity: O(N)
        # 會改變原先array
        if self.check_invalid_array(nums):
            return 0      
        mid = len(nums) // 2
        start = 0
        end = len(nums) - 1
        index = self.partition(nums, start, end)
        while index != mid:
            if index > mid:
                end = index - 1
                index = self.partition(nums, start, end)
            else:
                start = index + 1
                index = self.partition(nums, start, end)
        
        result = nums[mid]
        if not self.check_more_than_half(nums, result):
            return 0
        return result
    
    def partition(self, nums, start, end):
        import random
        rand_pivot = random.randint(start, end)
        l = start
        r = end
        pivot = nums[rand_pivot]
        nums[pivot] = nums[l]
        nums[l] = pivot
        l += 1
        while l < r:
            if nums[l] > pivot:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                r -= 1
            elif nums[l] == pivot:
                l += 1
            else:
                l += 1
        temp = nums[l-1]
        nums[l-1] = nums[0]
        nums[0] = temp
        
        return l-1
    
    def check_invalid_array(self, nums):
        if not nums:
            return True
        return False
    
    def check_more_than_half(self, nums, number):
        times = 0
        for i in range(len(nums)):
            if nums[i] == number:
                times += 1
        
        if times * 2 <= len(nums):
            return False
        return True
    
    def more_than_half_3(self, nums):
        if self.check_invalid_array(nums):
            return 0
        result = nums[0]
        times = 1
        for i in range(len(nums)):
            if times == 0:
                result = nums[i]
                times = 1
            elif nums[i] == result:
                times += 1
            else:
                times -= 1
        if not self.check_more_than_half(nums, result):
            result = 0
        return result
        
        
sol = Solution()
test = [1,2,3,2,2,2,5,4,2]
print(sol.more_then_half_num_2(test))
print(test)


test = [1,2,3,2,2,2,5,4,2]
print(sol.more_than_half_3(test))
print(test)             
        
        
        
        