# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 08:59:59 2021

@author: a8520
"""


# 輸入兩個序列，第一個為Stack Append的序列，判斷第二個序列是否
# 可能是第一個stack pop的序列

# 1, 2, 3, 4, 5
# 4, 3, 5, 1, 2

class Solution():
    def is_pop_order(self, nums1, nums2):
        # 1. pop數列第一個數字前append的數字pop時排序必為append的反向順序。
        if not nums1 or not nums2:
            return False
        if len(nums1) != len(nums2):
            return False
        
        stack = list()
        stack_reverse = list()
        for num in nums1:
            stack.append(num)
        while stack:
            stack_reverse.append(stack.pop())
        
        # stack.append(stack_reverse.pop())
        for i in range(len(nums2)):
            found = False
            cur_proc = nums2[i]
            if stack and stack[-1] == cur_proc:
                found = True
                stack.pop()
            else:
                while stack_reverse:
                    if stack_reverse[-1] == cur_proc:
                        stack_reverse.pop()
                        found = True
                        break
                    else:
                        stack.append(stack_reverse.pop())
            if found == False:
                return False
        return True
    def is_pop_order_ans(self, nums1, nums2):
        
        ans = False
        
        if nums1 and nums2 and len(nums1) == len(nums2) and len(nums1) > 0:
            i = 0
            j = 0
            stack = list()
            while j < len(nums2):
                while len(stack) == 0 or stack[-1] != nums2[j]:
                    if i == len(nums1):
                        break
                    stack.append(nums1[i])
                    i += 1
                
                if stack[-1] != nums2[j]:
                    break
                
                stack.pop()
                j += 1
            if len(stack) == 0 and j == len(nums2) :
                ans = True
        return ans
            

sol = Solution()
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 4, 3, 5, 2]

print(sol.is_pop_order(nums1, nums2))

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 4, 3, 5, 2]

print(sol.is_pop_order_ans(nums1, nums2))
        