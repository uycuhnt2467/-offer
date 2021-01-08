# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 11:22:42 2021

@author: a8520
"""


array = [2, 3, 1, 0, 2, 5, 3]

def get_duplicate(nums):
    # 能更改array內容的方式
    if nums == None or len(nums) < 1:
        return False
    i = 0
    while i < len(nums):
        while nums[i] != i:
            if nums[i] == nums[nums[i]]:
                print(nums[i])
                return True
            
            temp = nums[nums[i]]
            nums[nums[i]] = nums[i]
            nums[i] = temp
        
        i += 1
    return False

print(get_duplicate(array))

array = [2, 3, 1, 0, 2, 5, 3]
def get_duplicate2(nums):
    # 不更改array內容的方式
    # additaional space complexity = o(N)
    if nums == None or len(nums) < 1:
        return False
    i = 0
    temp_nums = nums[:]
    while i < len(temp_nums):
        while temp_nums[i] != i:
            if temp_nums[i] == temp_nums[temp_nums[i]]:
                print(temp_nums[i])
                return True
            
            temp = temp_nums[temp_nums[i]]
            temp_nums[temp_nums[i]] = temp_nums[i]
            temp_nums[i] = temp
        
        i += 1
    return False

print(get_duplicate2(array))

array = [2, 3, 1, 0, 2, 5, 3]
def get_duplicate3(nums):
    # 不更改原始array
    # time complexity = o(NlogN)
    # space complexity = o(1)
    if nums == None or len(nums) < 1:
        return -1
    # binary search + count compute
    l = 1 # min num
    r = len(nums) - 1 # max num
    
    def count_num(start, end):
        count = 0
        for i in nums:
            if i >= start and i <= end:
                count += 1
        return count
    
    while l <= r:
        mid = l + (r-l)//2
        count = count_num(l, mid)    
        if l == r:
            if count > 1:
                return l
            else:
                break
        if count > (mid - l + 1):
            r = mid
        else:
            l = mid + 1
    return -1
print(get_duplicate3(array))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
