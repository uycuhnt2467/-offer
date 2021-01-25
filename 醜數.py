# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 21:35:17 2021

@author: a8520
"""


# 49. 醜數
# 若數的因子只包含2, 3, 5，則該數為醜數，而1為第一個醜數，求第1500個醜數

class Solution:
    
    def get_ugly_number(self, num):
        # brutal
        i = 0
        cur_num = 1
        while i < num:
            # print(i)
            while self.check_valid(cur_num) != True:
                cur_num += 1
            # print(cur_num)
            i += 1
            cur_num += 1
        return cur_num - 1
    
    def check_valid(self, num):
        while num % 2 == 0:
            num /= 2
        
        while num % 3 == 0:
            num /= 3
        
        while num % 5 == 0:
            num /= 5
        
        if num == 1:
            return True
        else:
            return False
    
    def get_ugly_number_2(self, num):
        # dp求值
        # 醜數為前面某醜數 * 2/3/5 
        
        cur_num = [1]
        i = 1
        mult_2_index = 0
        mult_3_index = 0
        mult_5_index = 0
        
        while i < num:
            min_next = min(cur_num[mult_2_index] * 2, cur_num[mult_3_index] * 3, cur_num[mult_5_index] * 5 )
            
            if min_next == cur_num[mult_2_index] * 2:
                mult_2_index += 1
            elif min_next == cur_num[mult_3_index] * 3:
                mult_3_index += 1
            elif min_next == cur_num[mult_5_index] * 5:
                mult_5_index += 1
            
            if min_next > cur_num[-1]:
                cur_num.append(min_next)
                i += 1
        return cur_num[-1]
    

sol = Solution()
test = 1500
# print(sol.get_ugly_number(test))
print(sol.get_ugly_number_2(test))