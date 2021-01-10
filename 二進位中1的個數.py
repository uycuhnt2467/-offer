# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 22:10:06 2021

@author: a8520
"""


class Solution():
    def NumberOf1(self, n):
        # 無法處理負數
        count = 0
        while n:
            if n & 1:
                count += 1
            n = n >> 1
        return count
    
    def NumberOf1_2(self, n):
        count = 0
        flag = 1
        if n < 0:
            n = -n
        while flag <= n:
            if n & flag:
                count += 1
            flag = flag << 1
        return count
    def Numberof1_3(self, n: int) -> int:
        count = 0
        if n < 0:
            n = -n
    
        while n:
            count = count + 1
            n = (n - 1) & n
    
        return count
    
    
sol = Solution()
print(sol.NumberOf1(5))
print(sol.NumberOf1_2(5))
print(sol.Numberof1_3(5))