# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 14:31:36 2021

@author: a8520
"""


class Solution():
    def partition(self, nums, start, end):
            if start == end:
                return
            pivot = nums[start]
            less = start
            large = end
            i = start + 1
            
            while i < end:
                if nums[i] < pivot:
                    nums[less] = nums[i]
                    less += 1
                    i += 1
                elif nums[i] > pivot:
                    temp = nums[large]
                    nums[large] = nums[i]
                    nums[i] = temp
                    large -= 1
                else:
                    i += 1
            return less, large
    def quicksort(self, nums, start, end):        
        if start < end:
            less, large = self.partition(nums, start, end)
            self.quicksort(nums, start, less)
            self.quicksort(nums, large, end)
        
        
            
        
        
        