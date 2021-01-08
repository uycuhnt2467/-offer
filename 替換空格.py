# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 14:58:31 2021

@author: a8520
"""

# 和leetcode相似
# 雙指標操作: 
#  1. 先用o(N) 找尋需要延長的長度
#  2. 從尾端插入字符或數字以減少挪移次數
test = [1,2,4, "", 5, 6, "", 7, 9, "", 10]
# replace [""] to ["%", "2", "0"]
def ReplaceBlank(nums):
    replaceN = 0
    for i in range(len(nums)):
        if str(nums[i]) == "":
            replaceN += 1
    newList = [0] * (len(nums) + (replaceN * 2))
    
    first_ptr = len(nums) - 1
    second_ptr = len(newList) - 1
    
    while first_ptr >= 0:
        if str(nums[first_ptr]) == "":
            newList[second_ptr] = "0"
            second_ptr -= 1
            
            newList[second_ptr] = "2"
            second_ptr -= 1
            
            newList[second_ptr] = "%"
            second_ptr -= 1
            
            first_ptr -= 1
        else:
            newList[second_ptr] = nums[first_ptr]
            first_ptr -= 1
            second_ptr -= 1
    return newList
print(test)
print(ReplaceBlank(test))